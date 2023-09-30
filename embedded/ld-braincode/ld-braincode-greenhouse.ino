/*
Accept Artnet data and display it, through an OctoWS2811 / Teensy / Wiz850io

Install Teensyduino and set board to "Teensy 4.1"

9/12: fixed the 34=>35 conversion bug that I found at the campsite
added constellations but haven't tested or made fancy yet

from 7/23: updated the Artnet library to use NativeEthernet and NativeEthernetUdp
it "just works" after that. tried to use #define TEENSY41 to conditionally load
those specific libraries but that wasn't working for me, was still trying to load
the normal Ethernat library.
After warming up, this was getting 40 fps with 3 universes.


MIT License

Resources:
https://www.pjrc.com/teensy/td_libs_OctoWS2811.html
*/
// for the artnet library to load the right ethernet stuff.
// due to edits I made, it now loads NativeEthernet and NativeEthernetUDP
#include "Artnet.h"
#include <SPI.h>
#include <OctoWS2811.h>
#include "TeensyID.h"

// OctoWS2811 settings
const int BRIGHTNESS = 50;
const int ledsPerStrip = 581; // change for your setup // should be 581
const byte numStrips = 5;        // change for your setup
const int numLeds = ledsPerStrip * numStrips;
const int numberOfChannels = numLeds * 3; // Total number of channels you want to receive (1 led = 3 channels)
DMAMEM int displayMemory[ledsPerStrip * 6];
int drawingMemory[ledsPerStrip * 6];
const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(ledsPerStrip, displayMemory, drawingMemory, config);
// @TODO not sure I need this really.
// const bool hasReceivedArtnet = false;

// Artnet settings
Artnet artnet;
const int startUniverse = 0; // CHANGE FOR YOUR SETUP most software this is 1, some software send out artnet first universe as 0.

// Check if we got all universes
const int maxUniverses = 8; // @TODO update to more universes
bool universesReceived[maxUniverses];
int universesReceivedTotal[maxUniverses]; // for debugging lost universes
bool sendFrame = 1;
int previousDataLength = 0;

bool receiving = false;
bool isConnected = false;

bool isNetworkingRequired = true;

// Change ip and mac address for your setup
byte ip[] = {169, 254, 18, 0};
byte broadcast[] = {192, 168, 2, 255};
byte fakemac[] = {0x04, 0xE9, 0xE5, 0x00, 0x69, 0xEC};

long hues[256];

uint8_t serial[4];

// update 'ip' to make the IP consistent with the MAC address
void updateIp()
{
  teensySN(serial);
  Serial.printf("Serial number: %02X-%02X-%02X-%02X \n", serial[0], serial[1], serial[2], serial[3]);
  Serial.println("Version: 2023.8");
  uint8_t serials[5] = {
      //0xDA, // 00-10-16-DA orange
      0xFE, // replacing this for prototyping
      0x5E, // 00-0C-46-5E yellow
      0x5D, // 00-0C-46-5D green - motherbrain
      0x92, // 00-0C-46-92 blue
      0x70, // 00-0C-46-70 purple
  };
  // byte hardcoded_addresses[6] = {32, 33, 34, 35, 36};
  byte hardcoded_addresses[5] = {32, 33, 34, 35, 36};
  for (int i = 0; i < 5; i++)
  {
    if (serials[i] == serial[3])
    {
      Serial.println("Used serial to figure out which brain I am.");
      ip[3] = hardcoded_addresses[i];
      fakemac[5] = hardcoded_addresses[i];
    }
  }
}

void setup()
{
  delay(2000); // necessary for the serial number call
  Serial.println("started");

  Serial.begin(115200);

  leds.begin();
  Serial.printf("LED counter: %d pixels, %d LEDs \n", leds.numPixels(), numLeds);
  Serial.println();

  rainbowSetup();
  leds.show();

  // delay(5000);
  // for (int i = 0; i < 201; i += 25)
  // {
  //   whileNetworking(i);
  //   delay(500);
  // }
  // delay(1000);

  updateIp();

  Serial.println("Setting up Artnet via Ethernet cable...");
  Serial.print("Link status (should be 2): ");
  Serial.println(Ethernet.linkStatus());

  if (isNetworkingRequired) {
    artnet.begin(fakemac, ip);
    Serial.println("Set up Artnet.");
    Serial.print("Local ip: ");
    Serial.println(Ethernet.localIP());
  }
}

void loop()
{
  if (isNetworkingRequired) {

    // we call the read function inside the loop
    uint16_t r = artnet.read();
    if (r == ART_DMX)
    {
      handleDmxFrame();
    }
  }

  if (!receiving)
  {
    demoRunner();
  }
}



// each frame contains one universe of data.
// - interpret the data
// - set the LEDs to the incoming data
// - if we've received data for each universe, call leds.show()
void handleDmxFrame()
{
  int uni = artnet.getUniverse();
  if (!receiving)
  {
    Serial.println("receiving.");
    receiving = true;
  }
  // Serial.println(uni);
  if (universesReceived[uni] > 0)
    return;

  universesReceived[uni] = 1;
  sendFrame = 1;

  int length = artnet.getLength();
  uint8_t *frame = artnet.getDmxFrame();
  universesReceivedTotal[uni] = universesReceivedTotal[uni] + 1;
  printFps();

  // LD timing: 15-17 microseconds to set pixels
  //uint32_t beginTime = micros();
  updateLeds();
  //uint32_t elapsedTime = micros() - beginTime;
  //Serial.printf("elapsed microseconds: %lu \n", elapsedTime);

  for (int i = 0; i < maxUniverses; i++)
  {
    if (universesReceived[i] == 0)
    {
      sendFrame = 0;
      break;
    }
  }
  if (sendFrame)
  {
    leds.show();
    memset(universesReceived, 0, maxUniverses);
  }
}

byte timeOffset = 0;


byte ledsPerLayer[] = {
  24 * 3,
  22 * 3,
  20 * 3 + 1,
  18 * 3 + 1,
  16 * 3 + 2, // was 3
  14 * 3 + 3, // was 2
  12 * 3 + 4,
  10 * 3 + 4,
  8 * 3 + 4,
  6 * 3 + 5,
  4 * 3 + 5,
  2 * 3 + 6,
  0 * 3 + 6
};

byte ledDataPerLayer[] = {
  24,
  22,
  20,
  18,
  16,
  15,
  13,
  11,
  9,
  7,
  5,
  4,
  2
};

byte blanksPerLayer[] = {
  5,
  7,
  5,
  6,
  6,
  4,
  5,
  6,
  5,
  5,
  6,
  5,
  5
};

uint8_t layers = 13;

int ledsPerUniverse = 581;

// uint8_t blended(uint8_t usage, uint8_t *frame, uint8_t frameIdx) {
//   uint8_t current_value = frame[frameIdx];
//   if (usage == 0) {
//     if (frameIdx >= 3) {
//       return 0.6667 * current_value + 0.3333 * frame[frameIdx - 3];
//     }
//   } else if (usage == 2) {
//     // not checking frames because we should have enough blank data at the end
//     return 0.6667 * current_value + 0.3333 * frame[frameIdx + 3];
//   }
//   return current_value;
// }

// call setPixel using frame data.
void updateLeds() {
  int length = artnet.getLength();
  uint8_t *frame = artnet.getDmxFrame();
  int uni = artnet.getUniverse();

  int start = uni * ledsPerStrip;
  int frameIdx = 0;
  uint8_t ledDataWidth = 3;

  int target = start;
  
  // iterate through each layer
  for (uint8_t i=0; i<13; i++) {
    uint8_t extension = ledsPerLayer[i] - 3*ledDataPerLayer[i];
    //Serial.printf("using extension %d for layer %d\n", extension, i);
    // if (uni == 0) {
    //   Serial.printf("layer %d; target %d; leds in layer %d; data per layer %d extension %d \n", i, target, ledsPerLayer[i], ledDataPerLayer[i], extension);
    // }

    uint8_t handledExtension = 0;

    // iterate through each color in this layer
    for (uint8_t j=0; j<ledDataPerLayer[i]; j++) {
      uint8_t width = 3;
      // extend the midpoint by however many filler pixels we need
      if (j == 12-i) {
        width = width + extension;
      }
      // set 3 (or more) pixels to the current color at frameIdx
      for (uint8_t k=0; k<width; k++) {
        leds.setPixel(
          target, 
          frame[frameIdx],
          frame[frameIdx+1],
          frame[frameIdx+2]
        );
        target++;
      }
      // move frameIdx to the next color
      frameIdx += 3;
    }
    
    // add blanks
    for (uint8_t j=0; j<blanksPerLayer[i]; j++) {
      leds.setPixel(target, 0,0,0);
      target++;
    }
    
  }
}

// // call setPixel using frame data.
// void updateLeds() {
//   int length = artnet.getLength();
//   uint8_t *frame = artnet.getDmxFrame();
//   int uni = artnet.getUniverse();

//   int start = uni * ledsPerStrip;
//   int frameIdx = 0;
//   // how many times have we used this value? ex. 0 is the first, 2 is the third.
//   // this is for reusing pixel data i.e. one data maps to three LEDs
//   uint8_t usage = 0;
  
//   int layer = 0;
//   int pixel = 0;

//   for (int target = start; target < start + ledsPerUniverse; target++) {

//     // starting the next layer
//     if (pixel >= ledsPerLayer[layer] + blanksPerLayer[layer]) {
//       layer += 1;
//       pixel = 0;
//       usage = 0;
//       frameIdx += 3;
//     }

//     // entering black zone
//     if (pixel >= ledsPerLayer[layer]) {
//       // Serial.println("Finally got to black idx code.");
//       leds.setPixel(target, 0,0,0);
//       // for (int i=0; i<numStrips; i++) {
//       //   leds.setPixel(target+ledsPerStrip*i, 0,0,0);
//       // }
//       pixel++;
//       continue;
//     }

//     if (usage >= 3) {
//       // are there pixels left?
//       if (pixel <= ledsPerLayer[layer]-3) {
//         frameIdx += 3;
//         usage = 0;
//       }
//     }

//     // safety
//     if (frameIdx+2 > length) {
//       Serial.printf("WARN: was about to access more artnet data than I have. idx %d, length %d\n", frameIdx, length);
//       return;
//     }

//     leds.setPixel(
//       target, 
//       frame[frameIdx],
//       frame[frameIdx+1],
//       frame[frameIdx+2]
//     );

//     pixel++;
//     usage++;
//   }
// }

uint32_t lastTiming = 0;
void printFps() {
  int uni = artnet.getUniverse();
  for (int i=0; i<10; i++) {
    artnet.getUniverse();
  }
  if (uni == 0 && universesReceivedTotal[0] % 100 == 0) {

    // check timing, do fps
    uint32_t currentTiming = millis();
    if (lastTiming > 0)
    {
      float fps = 100000. / (currentTiming - lastTiming);
      Serial.printf("%2.2f fps.  ", fps);
    }
    lastTiming = currentTiming;

    // print how many frames we got from each universe
    for (int i = 0; i < maxUniverses; i++)
    {
      Serial.print(i);
      Serial.print(": ");
      //float pct = 100 * universesReceivedTotal[i] / universesReceivedTotal[0];
      float pct = universesReceivedTotal[i];
      Serial.print(pct, 2);
      Serial.print(" ");
    }
    Serial.print("\n");
  }
}  

void rainbowSetup()
{
  for (int i = 0; i < 256; i++)
  {
    hues[i] = setLedColorHSV(i, 255, BRIGHTNESS);
  }
}

byte demo = 0;


void demoRunner()
{
  rainbowLoop();

  leds.show();
  timeOffset++;
  delay(90);
}

// hue 0 = green
// hue 32 = yellow
// hue 64 = yellow/red
// hue 96 = purple
// hue 128 = bright purple
// hue 160 = blue
// hue 192 = light blue
void whichTriangleAmI()
{
  // int i = 7;
  for (int i=0; i<numStrips; i++) {
    for (int j=0; j<ledsPerStrip; j++) {
      //byte hue = ((i-4) * 64) % 256;
      if (i > 3) {
        leds.setPixel(j+ledsPerStrip*i, hues[(160 + timeOffset) % 256]);
      } else {
        leds.setPixel(j+ledsPerStrip*i, hues[(32 + timeOffset) % 256]);
      }
      
    }
    
  }


}

void rainbowLoop()
{
  int uni = 0;

  int start = uni * ledsPerStrip;
  int frameIdx = 0;
  int usage = 0;
  
  int layer = 0;
  int pixel = 0;

  for (int target = start; target < start + ledsPerStrip; target++) {

    // starting the next layer
    if (pixel >= ledsPerLayer[layer] + blanksPerLayer[layer]) {
      layer += 1;
      pixel = 0;
      usage = 0;
      frameIdx += 3;
    }

    // entering black zone
    if (pixel >= ledsPerLayer[layer]) {
      // Serial.println("Finally got to black idx code.");
      for (int i=0; i<numStrips; i++) {
        leds.setPixel(target+ledsPerStrip*i, 0,0,0);
      }
      
      pixel++;
      continue;
    }

    if (usage >= 3) {
      // are there pixels left?
      if (pixel <= ledsPerLayer[layer]-3) {
        frameIdx += 3;
        usage = 0;
      }
    }

    for (int i=0; i<numStrips; i++) {
      leds.setPixel(target+ledsPerStrip*i, hues[(timeOffset+target) % 256]);
    }
    pixel++;
    usage++;
  }


}

void rainbowLoop_old()
{
  int uni = 0;

  int start = uni * ledsPerStrip;
  int frameIdx = 0;
  int usage = 0;
  
  int layer = 0;
  int pixel = 0;



  for (int target = start; target < start + ledsPerStrip; target++) {

    // starting the next layer
    if (pixel >= ledsPerLayer[layer] + 6) {
      layer += 1;
      pixel = 0;
      usage = 0;
      frameIdx += 3;
    }

    // entering black zone
    if (pixel >= ledsPerLayer[layer]) {
      // Serial.println("Finally got to black idx code.");
      for (int i=0; i<numStrips; i++) {
        leds.setPixel(target+ledsPerStrip*i, 0,0,0);
      }
      
      pixel++;
      continue;
    }

    if (usage >= 3) {
      // are there pixels left?
      if (pixel <= ledsPerLayer[layer]-3) {
        frameIdx += 3;
        usage = 0;
      }
    }

    for (int i=0; i<numStrips; i++) {
      leds.setPixel(target+ledsPerStrip*i, hues[(timeOffset+target) % 256]);
    }
    pixel++;
    usage++;
  }


}

long setLedColorHSV(byte h, byte s, byte v)
{
  byte RedLight;
  byte GreenLight;
  byte BlueLight;
  // this is the algorithm to convert from RGB to HSV
  h = (h * 192) / 256;           // 0..191
  unsigned int i = h / 32;       // We want a value of 0 thru 5
  unsigned int f = (h % 32) * 8; // 'fractional' part of 'i' 0..248 in jumps

  unsigned int sInv = 255 - s; // 0 -> 0xff, 0xff -> 0
  unsigned int fInv = 255 - f; // 0 -> 0xff, 0xff -> 0
  byte pv = v * sInv / 256;    // pv will be in range 0 - 255
  byte qv = v * (256 - s * f / 256) / 256;
  byte tv = v * (256 - s * fInv / 256) / 256;

  switch (i)
  {
  case 0:
    RedLight = v;
    GreenLight = tv;
    BlueLight = pv;
    break;
  case 1:
    RedLight = qv;
    GreenLight = v;
    BlueLight = pv;
    break;
  case 2:
    RedLight = pv;
    GreenLight = v;
    BlueLight = tv;
    break;
  case 3:
    RedLight = pv;
    GreenLight = qv;
    BlueLight = v;
    break;
  case 4:
    RedLight = tv;
    GreenLight = pv;
    BlueLight = v;
    break;
  case 5:
    RedLight = v;
    GreenLight = pv;
    BlueLight = qv;
    break;
  }
  long rgb = 0;

  rgb += RedLight << 16;
  rgb += GreenLight << 8;
  rgb += BlueLight;
  return rgb;
}