#include <Wire.h>
#include "Adafruit_MCP23017.h"

// 2021-02-08: Takes triangle inputs and relays them to Serial out.
// 
// [xx yy]
// xx: 0x11 for presses, 0x10 for releases
// yy: the triangle address 0-44 
// 
// Needs a little uncommenting to get all 5 panels working (2 work currently)
// Runs on an Arduino Leonardo with 5 Waveshare MCP23017 chips/breakouts

// Basic pin reading and pullup test for the MCP23017 I/O expander
// public domain!

// Connect pin #12 of the expander to Analog 5 (i2c clock)
// Connect pin #13 of the expander to Analog 4 (i2c data)
// Connect pins #15, 16 and 17 of the expander to ground (address selection)
// Connect pin #9 of the expander to 5V (power)
// Connect pin #10 of the expander to ground (common ground)
// Connect pin #18 through a ~10kohm resistor to 5V (reset pin, active low)

// Input #0 is on pin 21 so connect a button or switch from there to ground

Adafruit_MCP23017 mcpa;
Adafruit_MCP23017 mcpb;
Adafruit_MCP23017 mcpc;
Adafruit_MCP23017 mcpd;
Adafruit_MCP23017 mcpe;

byte mcpv[45];

void setup() {
  Serial.begin(9600);
  while (!Serial) {}
  
  mcpa.begin(5);      // use default address 0
  mcpb.begin(6);      // use default address 0
  //mcpc.begin(5);      // use default address 0
  //mcpd.begin(6);      // use default address 0
  //mcpe.begin(7);      // use default address 0



  for (byte i=0; i<9; i++) {
    mcpa.pinMode(i, INPUT);
    mcpa.pullUp(i, HIGH);
    mcpb.pinMode(i, INPUT);
    mcpb.pullUp(i, HIGH);
//    mcpc.pinMode(i, INPUT);
//    mcpc.pullUp(i, HIGH);
//    mcpd.pinMode(i, INPUT);
//    mcpd.pullUp(i, HIGH);
//    mcpe.pinMode(i, INPUT);
//    mcpe.pullUp(i, HIGH);
  }

  for (byte i=0; i<45; i++) {
    mcpv[i] = 1;
  }

  // pinMode(13, OUTPUT);  // use the p13 LED as debugging
}

void cycle(Adafruit_MCP23017 mcp, byte offset) {
  byte val;
  byte msg[2];

  for (int i=0; i<9; i++) {
      val = mcp.digitalRead(i);
      //Serial.print(val);
      byte d = 9*offset+i;
      if (val != mcpv[d]) {
        if (val) {
          msg[0] = 0x10;
        } else {
          msg[0] = 0x11;
        }
        msg[1] = d;
        Serial.write(msg, 2);
//        Serial.println(" msg:");
//        Serial.print(msg[0]);
//        Serial.println(msg[1]);
        mcpv[d] = val;
      }    
    }  
}

void loop() {
  // The LED will 'echo' the button
  // digitalWrite(13, mcp.digitalRead(0));
  // int stateButton = mcp.digitalRead(0);
  cycle(mcpa, 0);
  cycle(mcpb, 1);
}
