/*
Code for lidghtdream remotes.
- Input from 2 rotary encoders and 1 arcade button
- Send UDP packets with input values
- Receive UDP packets with commands
- Display feedback via LEDs

Set board to "Adafruit Feather HUZZAH ESP8266"

9/12: fixed IP address to match laptop
refactored color code to allow multiple "modes"
this was the hypno final
still kinda buggy (random crashes / network disconnects)

References: https://sdvx-diy.github.io/
https://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/udp-examples.html
GNU License: <https://www.gnu.org/licenses/>.
*/
#include "ESPRotary.h"
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Adafruit_NeoPixel.h>

// i.e. sensitivity. higher is less sensitive
#define CLICKS_PER_STEP 18

// what values are we sending home?
#define MIN_POS   -1
#define MAX_POS   128

const char* ssid     = "hypnodrome";
const char* password = "hypnodrome";
WiFiUDP Udp;
unsigned int localUdpPort = 4210;
char incomingPacket[256];

#define NEOPIXEL_RING_SIZE 24
#define NUM_LEDS 48

#define BRIGHTNESS 25

/* Encoder */
#define ENC_1_PIN_A 14
#define ENC_1_PIN_B 12

#define ENC_2_PIN_A 5
#define ENC_2_PIN_B 4

// neopixel LED data
#define LED_PIN 2

#define BUTTON_SWITCH_PIN 13
#define BUTTON_SWITCH_LED 15
#define DEBOUNCE 25

bool isButtonPressed = false;
int keyTimer = 0;
int udpTimer = 0;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);
// CRGB leds[NUM_LEDS];


// should we connect to wifi?
#define ONLINE true

byte remoteIP[] = {192, 168, 1, 5};
int remotePort = 7005;

#define ENC_MODE_NORMAL 0
int encMode = 0;

ESPRotary ra = ESPRotary(ENC_1_PIN_A, ENC_1_PIN_B, CLICKS_PER_STEP, MIN_POS, MAX_POS);
ESPRotary rb = ESPRotary(ENC_2_PIN_A, ENC_2_PIN_B, CLICKS_PER_STEP, MIN_POS, MAX_POS);

// encoder modes
const byte MODE_NORMAL = 0;
const byte MODE_INFINITE = 1;

// @TODO make dynamic later
byte ra_mode = MODE_NORMAL;
byte rb_mode = MODE_INFINITE;

// color ramp, 5 lights, rotates
const byte DRAW_NORMAL = 0;
// point to a certain direction. 5 lights but middle is focused.
const byte DRAW_DIRECTIONAL = 1;
// value corresponds to the number of LEDs drawn.
const byte DRAW_AMOUNT = 2;

byte ra_draw = DRAW_AMOUNT;
byte rb_draw = DRAW_DIRECTIONAL;

const byte ra_rotation = 6;
const byte rb_rotation = 17;

int ra_value = 0;
int rb_value = 0;

/* Startup Loop */
void setup() {
  //pinMode(0, OUTPUT);
  // pinMode(4,OUTPUT);

  // button pin
  pinMode(BUTTON_SWITCH_PIN, INPUT_PULLUP);
  pinMode(BUTTON_SWITCH_LED, OUTPUT);
  
  Serial.begin(115200);
  delay(50);
  Serial.println("\n\nSetup...");
  
  
  ra.setChangedHandler(rotatea);
  rb.setChangedHandler(rotateb);

  strip.begin();
  strip.setBrightness(BRIGHTNESS);
  // updateEncoderA(0);
  // updateEncoderB(0);
  strip.show();

  Serial.printf("MAC address = %s\n", WiFi.softAPmacAddress().c_str());
  if (!ONLINE) return;
  Serial.println("Connecting to wifi...");

  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  Udp.begin(localUdpPort);

}

/* Main Loop */
void loop() {
  // must call to get em to work
  ra.loop();
  rb.loop();
  checkButtonEvents();

  if (!ONLINE) return;
  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    Serial.print("found packet size...");
    readUdp(packetSize);
    Serial.println("done.");
  }
}

void checkButtonEvents() {
  if (digitalRead(BUTTON_SWITCH_PIN) == HIGH && isButtonPressed == false && (millis() - keyTimer) > DEBOUNCE) {
    // press
    Serial.println("pressing.");
    digitalWrite(BUTTON_SWITCH_LED, HIGH);
    isButtonPressed = true;
    sendUpdate("ra", ra_value);
    sendUpdate("rb", rb_value);
    sendUpdate("rc", 1);
    keyTimer = millis();
  } else if (digitalRead(BUTTON_SWITCH_PIN) == LOW && isButtonPressed == true && (millis() - keyTimer) > DEBOUNCE) {
    // release
    Serial.println("releasing.");
    digitalWrite(BUTTON_SWITCH_LED, LOW);
    isButtonPressed = false;
    sendUpdate("rc", 0);
    keyTimer = millis();
  }
}

void readUdp(int packetSize) {
  Serial.printf("Received %d bytes from %s, port %d\n", packetSize, Udp.remoteIP().toString().c_str(), Udp.remotePort());
  int len = Udp.read(incomingPacket, 255);
  if (len > 0)
  {
    incomingPacket[len] = '\0';
  }
  if (incomingPacket[0] == 'r') {
    // reset
    reset();
  } else if (incomingPacket[0] == 'm') {
    int m = int(incomingPacket[2]);
    Serial.printf("updating mode: %d\n", m);
    encMode = m;
  }
  Serial.printf("UDP packet contents: %s\n", incomingPacket);
}


int ra_timer = 0;
// on rotary change for the first rotary
void rotatea(ESPRotary& r) {
  Serial.print("rotating a...");
  rotator(r, ra_value, "ra", 0, ra_mode, ra_draw, ra_rotation, ra_timer);
  Serial.print("done.\n");
}

int rb_timer = 0;
// on rotary change for the second rotary
void rotateb(ESPRotary &r) {
  Serial.print("rotating b...");
  rotator(r, rb_value, "rb", NEOPIXEL_RING_SIZE, rb_mode, rb_draw, rb_rotation, rb_timer);
  Serial.print("done.\n");
}

void rotator(ESPRotary &r, int &prev, char updateText[], byte startPixel, byte encMode, byte drawMode, byte rotation, int &timer) {
  int next = r.getPosition();

  if (prev == next)
    return;

  if (encMode == MODE_INFINITE) {
    if (prev >= 64 && next == 128) {
      next = 0;
      r.resetPosition(next);
    } else if (prev <= 64 && next == -1) {
      next = 127;
      r.resetPosition(CLICKS_PER_STEP*next);
    }
  } else {
    if (next < 0) next = 0;
    if (next > 127) next = 127;
  }

  prev = next;

  if (drawMode == DRAW_AMOUNT) {
    drawAmount(startPixel, next, rotation);
  } else if (drawMode == DRAW_DIRECTIONAL) {
    drawDirectional(startPixel, next, rotation);
  } else {
    updateEncoder(startPixel, next, rotation);
  }
  strip.show();
  
  if (isButtonPressed && (millis() - timer) > DEBOUNCE) {
    sendUpdate(updateText, next);
    timer = millis();
  }
}

// update TouchDesigner with the new value here
void sendUpdate(char msgtype[], int val) {
  char response[10];
  sprintf(response, "%s|%d", msgtype, val);
  Serial.println(response);
  Udp.beginPacket(remoteIP, remotePort);
  Udp.write(response);
  Udp.endPacket();
}

// this is the original color encoder option
void updateEncoder(byte offsetForSecondRing, int val, byte rotation) {
  Serial.printf("upding with value %d\n", val);

  // offset: 0-20
  byte offset = byte(val*19/127);

  // this includes:
  // 'base color' (color when knob is at 0
  // 'offset multiplier' (how much to scale the color towards red)
  // 'offsetForSecondRing multiplier' (how much should the rings look different
  byte color = byte( 86 - 4*offset + 5*offsetForSecondRing );
  // Serial.printf("using offset %d\n", offset);

  for (byte i=0; i<NEOPIXEL_RING_SIZE; i++) {
    byte adjusted_i = (i + rotation) % NEOPIXEL_RING_SIZE;
    if (i >= offset && i < offset+5) {
      strip.setPixelColor(adjusted_i+offsetForSecondRing, Wheel(color-3*(i-offset)));
    } else {
      strip.setPixelColor(adjusted_i+offsetForSecondRing, 0);
    }
  }
}


void drawAmount(byte offsetForSecondRing, int val, byte rotation) {
  // Serial.printf("upding with value %d", val);

    // offset: 0-23
  byte offset = (byte((val-1)*24/127)) % NEOPIXEL_RING_SIZE;

  for (byte i=0; i<NEOPIXEL_RING_SIZE; i++) {    
    byte adjusted_i = (i + rotation) % NEOPIXEL_RING_SIZE;
    

    uint32_t rgb = 0;
    if (i <= offset) {
      // @todo could be dynamic
      rgb = Wheel( 200 + i*2);
    }
    
    strip.setPixelColor(adjusted_i+offsetForSecondRing, rgb);
  }

}

void drawDirectional(byte offsetForSecondRing, int val, byte rotation) {
  // Serial.printf("upding with value %d", val);

    // offset: 0-23
  byte offset = (byte(val*24/127) + rotation) % NEOPIXEL_RING_SIZE;
  // Serial.printf("offset %d\n", offset);

  // this includes:
  // 'base color' (color when knob is at 0
  // 'offset multiplier' (how much to scale the color towards red)
  uint16_t hue = 4*10922;

  for (byte i=0; i<NEOPIXEL_RING_SIZE; i++) {    
    byte adjusted_i = (i + rotation) % NEOPIXEL_RING_SIZE;

    byte diff = min( abs(offset - adjusted_i), min(abs(offset-24 - adjusted_i), abs(offset+24 - adjusted_i)));
    // uint32_t rgb = Wheel(color-3*(i-offset));
    uint32_t rgb;
    // byte sv final_rgb;
    // sv notes: 
    // 127: colorful
    // 207: v. white
    
    switch(diff) {
      case 2:
        rgb = strip.gamma32(strip.ColorHSV(hue, 64, 127));
        break;
      case 1:
        rgb = strip.gamma32(strip.ColorHSV(hue, 157, 205));
        break;
      case 0:
        rgb = strip.gamma32(strip.ColorHSV(hue, 187, 255));
        break;
      default:
        rgb = 0;
        break;
    }
    
    strip.setPixelColor(adjusted_i+offsetForSecondRing, rgb);
  }

}


// reset to position 0
void reset()
{
  ra_value = 0;
  ra.resetPosition();
  rb_value = 0;
  rb.resetPosition();
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}
