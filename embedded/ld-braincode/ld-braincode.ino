/*
Accept Artnet data and display it, through an OctoWS2811 / Teensy / Wiz850io

Install Teensyduino and set board to "Teensy 3.2"

MIT License

Resources:
https://www.pjrc.com/teensy/td_libs_OctoWS2811.html
*/
#include "TeensyID.h"
#include <Artnet.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <SPI.h>
#include <OctoWS2811.h>

// OctoWS2811 settings
const int ledsPerStrip = 34*5; // change for your setup
const byte numStrips = 6; // change for your setup
const int numLeds = ledsPerStrip * numStrips;
const int numberOfChannels = numLeds * 3; // Total number of channels you want to receive (1 led = 3 channels)
DMAMEM int displayMemory[ledsPerStrip*6];
int drawingMemory[ledsPerStrip*6];
const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(ledsPerStrip, displayMemory, drawingMemory, config);

// @TODO not sure I need this really.
// const bool hasReceivedArtnet = false;

// Artnet settings
Artnet artnet;
const int startUniverse = 0; // CHANGE FOR YOUR SETUP most software this is 1, some software send out artnet first universe as 0.

// Check if we got all universes
const int maxUniverses = 3;
bool universesReceived[maxUniverses];
int universesReceivedTotal[maxUniverses]; // for debugging lost universes
bool sendFrame = 1;
int previousDataLength = 0;

// Change ip and mac address for your setup
byte ip[] = {169, 254, 18, 0};
//byte ip[] = {192, 168, 1, 101};
byte broadcast[] = {192, 168, 2, 255};
byte fakemac[] = {0x04, 0xE9, 0xE5, 0x00, 0x69, 0xEC};

uint8_t serial[4];

// update 'ip' to make the IP consistent with the MAC address
void updateIp()
{
  teensySN(serial);
   Serial.printf("Serialnumber: %02X-%02X-%02X-%02X \n", serial[0], serial[1], serial[2], serial[3]);
   uint8_t serials[6] = {
    0xBA,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00
   };
   byte hardcoded_addresses[6] = {32, 33, 34, 35, 36, 37};
   for(int i=0; i<6; i++) {
     if (serials[i] == serial[3]) {
      Serial.println("got em");
       ip[3] = hardcoded_addresses[i];
       fakemac[5] = hardcoded_addresses[i];
     }
   }
}

void setup()
{
  delay(2000); // necessary for the serial number call
  
  Serial.begin(115200);
  updateIp();
  
  
  // artnet.setBroadcast(broadcast);
  artnet.begin(fakemac, ip);
  leds.begin();
  Serial.println("set up.");
  Serial.println(Ethernet.localIP());
  initTest();

  // this will be called for each packet received
  // artnet.setArtDmxCallback(onDmxFrame);
}

void loop()
{
  // we call the read function inside the loop
  uint16_t r = artnet.read();
  if (r == ART_DMX) {
    handleDmxFrame();
  }
}

unsigned long lastTiming = 0;

void handleDmxFrame() {
  int uni = artnet.getUniverse();
  if (universesReceived[uni] > 0) return;
  universesReceived[uni] = 1;
  sendFrame = 1;
  
  int length = artnet.getLength();
  uint8_t* frame = artnet.getDmxFrame();
  universesReceivedTotal[uni] = universesReceivedTotal[uni] + 1;
  if (uni == 0 && universesReceivedTotal[0] % 100 == 0) {

    // check timing, do fps
    unsigned long currentTiming = millis();
    if (lastTiming > 0) {
      unsigned long fps = 100000 / (currentTiming - lastTiming);
      Serial.print(fps);
      Serial.print(" fps.  ");        
    }
    lastTiming = currentTiming;

    // print how many frames we got from each universe
    for (int i = 0; i < maxUniverses; i++) {
      Serial.print(i);
      Serial.print(": ");
      //float pct = 100 * universesReceivedTotal[i] / universesReceivedTotal[0];
      float pct = universesReceivedTotal[i];
      Serial.print(pct, 2);
      Serial.print(" ");
    }
    Serial.print("\n");
  }

  for (int i = 0; i < length / 3; i++)
  {
    int led = (i-1) + i + uni * 170*2;
    
    if (led < numLeds) {
      leds.setPixel(led, frame[i * 3], frame[i * 3 + 1], frame[i * 3 + 2]);
      leds.setPixel(led+1, frame[i * 3], frame[i * 3 + 1], frame[i * 3 + 2]);
      //leds.setPixel(led, 0x050505);
    }
  }

  for (int i = 0 ; i < maxUniverses ; i++)
  {
    if (universesReceived[i] == 0)
    {
      sendFrame = 0;
      break;
    }
  }
  if (sendFrame) {
    leds.show();
    memset(universesReceived, 0, maxUniverses);
  }
  
}

void onDmxFrame(uint16_t universe, uint16_t length, uint8_t sequence, uint8_t* data, IPAddress remoteIP)
{
//  Serial.println("got a dmx frame from universe:");
//  Serial.println(length);
  // Serial.println(sequence);
//  if (universe == 3) Serial.println("got universe 3");
//  if (universe == 4) Serial.println("got universe 4");
  sendFrame = 1;

  int uni = universe - startUniverse;

  // Store which universe has got in
  if ((uni) < maxUniverses)
  {
    universesReceived[uni] = 1;
    universesReceivedTotal[uni] = universesReceivedTotal[uni] + 1;
  }
  for (int i = 0 ; i < maxUniverses ; i++)
  {
    if (universesReceived[i] == 0)
    {
      sendFrame = 0;
      break;
    }
  }

  // read universe and put into the right part of the display buffer
  for (int i = 0; i < length / 3; i++)
  {
    int led = i + (universe - startUniverse) * (previousDataLength / 3);
    
    // if (led < numLeds*6)
    if (led < numLeds) {
      leds.setPixel(led, (uint8_t)data[i * 3], (uint8_t)data[i * 3 + 1], (uint8_t)data[i * 3 + 2]);
    }
  }

//  for (int i = 0; i < 510; i++) {
//    leds.setPixel(i, (uint8_t)data[i * 3], (uint8_t)data[i * 3 + 1], (uint8_t)data[i * 3 + 2]);
//  }
  previousDataLength = length;
  
  if (true)
  {
    if (universe == 0 && universesReceivedTotal[0] % 100 == 0) {
      for (int i = 0; i < maxUniverses; i++) {
        Serial.print(i);
        Serial.print(": ");
        //float pct = 100 * universesReceivedTotal[i] / universesReceivedTotal[0];
        float pct = universesReceivedTotal[i];
        Serial.print(pct, 2);
        Serial.print(" ");
      }
      Serial.print("\n");
    }
    
    // Serial.println("showing leds.");
    leds.show();
    // Reset universeReceived to 0
    memset(universesReceived, 0, maxUniverses);
  }
}

#define RED    0x160000
#define GREEN  0x001600
#define BLUE   0x000016
#define YELLOW 0x101400
#define PINK   0x120009
#define ORANGE 0x100400
#define WHITE  0x101010

const long colors[6] = {
  WHITE,
  0x0066FF, // blue
  0x00CC99, // seagreen
  0xFF33CC, // purple
  0x300B00, // orange
  0x202400 // yellow
};

void initTest()
{
  Serial.printf("running led test: %d pixels, %d LEDs \n", leds.numPixels(), numLeds);
  for (int i = 0 ; i < leds.numPixels() ; i++) {
    
    if (i % ledsPerStrip == 0) leds.setPixel(i, GREEN);
    else if (i % ledsPerStrip == ledsPerStrip-1) leds.setPixel(i, RED);
    else {
      int stripNumber = round(i/ledsPerStrip);
      leds.setPixel(i, colors[stripNumber]);
    }
  }

  leds.show();
}
