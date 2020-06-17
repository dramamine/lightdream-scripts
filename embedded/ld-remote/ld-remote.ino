/*
Code for lidghtdream remotes.
- Input from 2 rotary encoders and 1 arcade button
- Send UDP packets with input values
- Receive UDP packets with commands
- Display feedback via LEDs

Set board to "Adafruit Feather HUZZAH ESP8266"

References: https://sdvx-diy.github.io/
https://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/udp-examples.html
GNU License: <https://www.gnu.org/licenses/>.
*/
#include "ESPRotary.h"
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <FastLED.h>

#define CLICKS_PER_STEP 2
#define MIN_POS   0
#define MAX_POS   127

const char* ssid     = "hypnodrome";
const char* password = "hypnodrome";
WiFiUDP Udp;
unsigned int localUdpPort = 4210;
char incomingPacket[256];

bool isButtonPressed = false;

#define NEOPIXEL_RING_SIZE 16
#define NUM_LEDS 32

float ENCODER_TICK_SIZE = 128 / 16;

CRGBArray<NUM_LEDS> leds;

/* Encoder */
#define ENC_1_PIN_A 5
#define ENC_1_PIN_B 4
#define ENC_2_PIN_A 3
#define ENC_2_PIN_B 2
#define LED_PIN 1

byte remoteIP[] = {192, 168, 1, 4};
int remotePort = 7005;

#define ENC_MODE_NORMAL 0
int encMode = 0;

ESPRotary ra = ESPRotary(ENC_1_PIN_A, ENC_1_PIN_B, CLICKS_PER_STEP, MIN_POS, MAX_POS);
ESPRotary rb = ESPRotary(ENC_2_PIN_A, ENC_2_PIN_B, CLICKS_PER_STEP, MIN_POS, MAX_POS);

int ra_value = 0;
int rb_value = 0;

/* Startup Loop */
void setup() {
  // pinMode(0, OUTPUT);
  Serial.begin(115200);
  delay(50);
  Serial.println("\n\nSimple Counter");
  
  
  ra.setChangedHandler(rotatea);
  rb.setChangedHandler(rotateb);

  Serial.printf("MAC address = %s\n", WiFi.softAPmacAddress().c_str());
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

  // FastLED.addLeds<NEOPIXEL,LED_PIN>(leds, NUM_LEDS);
  
  //r.setLeftRotationHandler(showDirection);
  //r.setRightRotationHandler(showDirection);
}

/* Main Loop */
void loop() {
//  digitalWrite(0, HIGH);
//  delay(500);
//  digitalWrite(0, LOW);
//  delay(500);

  ra.loop();
  rb.loop();
  // Serial.println("enc left:" + encLeft.read());

  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    readUdp(packetSize);
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

// on rotary change for the first rotary
void rotatea(ESPRotary& r) {
   Serial.println(r.getPosition());
   if (ra_value == r.getPosition()) return;

  // consider sending update
  sendUpdate("ra", r.getPosition());
   
   int o = int(ra_value / ENCODER_TICK_SIZE);
   int n = int(r.getPosition() / ENCODER_TICK_SIZE);
   if (n != o) {
     updateEncoder(0, n, NEOPIXEL_RING_SIZE);
   }
   ra_value = r.getPosition();
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

// on rotary change for the second rotary
void rotateb(ESPRotary& r) {
   Serial.println(r.getPosition());
}


CRGB white = CRGB(255,255,255);
CRGB black = CRGB(0,0,0);

// update the neopixel display to reflect encoder values
void updateEncoder(int p, int val, int len) {
  for (int i = p; i < p + len; i++) {
    if (i < p + val + 1) {
      leds[i] = white;
    } else {
      leds[i] = black;
    }
  }
  FastLED.show();
}

// reset to position 0
void reset()
{
  ra_value = 0;
  ra.resetPosition();
  rb_value = 0;
  rb.resetPosition();

  updateEncoder(0, 0, NEOPIXEL_RING_SIZE);
  updateEncoder(NEOPIXEL_RING_SIZE, 0, NEOPIXEL_RING_SIZE);
  // FastLED.show();
}  
