/*
 * 9/8 got a Leonardo. st board to Arduino AVR->Arduino Leonardo
 * 
 * 8/30 Ran into problems since ESP8266 doesn't have USB support.
 * Need a different board :/
 * 
This code is written for the SDVX DIY tutorial at https://sdvx-diy.github.io/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
#include <Keyboard.h>

/* Button Input Pins */
#define BTA_PIN 13
#define BTB_PIN 9
#define START_PIN 11

/* LED Output Pins */
#define BTA_LED 12
#define BTB_LED 6
#define START_LED 10

/* Software Debounce Interval */
#define DEBOUNCE 25

/* Button */
unsigned int buttonPin[3] = {BTA_PIN, BTB_PIN, START_PIN};
unsigned long keyTimer[3] = {0, 0, 0};
bool buttonState[3];
bool switchType[3] = {false, false, false};
char asciiKey[3] = {0xDA, 0xD9, 0x31}; //  0x6A, 0x6B, 0x6D, 0x63

/* Lighting */
unsigned int ledPin[3] = {BTA_LED, BTB_LED, START_LED};

/* Startup Loop */
void setup() {
  Keyboard.begin();
  
  pinMode(BTA_PIN, INPUT_PULLUP);
  pinMode(BTB_PIN, INPUT_PULLUP);
  pinMode(START_PIN, INPUT_PULLUP);
  
  pinMode(BTA_LED, OUTPUT);
  pinMode(BTB_LED, OUTPUT);
  pinMode(START_LED, OUTPUT);
  
  Serial.begin(9600);
}

/* Main Loop */
void loop() {
  checkAllKeyEvents();
}

void checkAllKeyEvents(){
  
  //Serial.print("somethin");
  for(int i = 0; i < sizeof(buttonPin) / 2; i++){
    if(switchType[i] == true){
      if(digitalRead(buttonPin[i]) == LOW && buttonState[i] == false){
        Serial.print("a button was pressed\n");
        // Keyboard.press(asciiKey[i]);
        digitalWrite(ledPin[i], HIGH);
        buttonState[i] = true;
        keyTimer[i] = millis();
      }
      else if(digitalRead(buttonPin[i]) == HIGH && buttonState[i] == true && millis() - keyTimer[i] > DEBOUNCE){
        Serial.print("a button was released\n");
        // Keyboard.release(asciiKey[i]);
        digitalWrite(ledPin[i], LOW);
        buttonState[i] = false;
      }
    }
    else{
      if(digitalRead(buttonPin[i]) == HIGH && buttonState[i] == false  && millis() - keyTimer[i] > DEBOUNCE){
        Serial.print("a button was pressed");
        Serial.println(i);
        Keyboard.press(asciiKey[i]);
        digitalWrite(ledPin[i], HIGH);
        buttonState[i] = true;
        keyTimer[i] = millis();
      }
      else if(digitalRead(buttonPin[i]) == LOW && buttonState[i] == true && millis() - keyTimer[i] > DEBOUNCE){
        Serial.print("a button was released: ");
        Serial.println(i);
        Keyboard.release(asciiKey[i]);
        digitalWrite(ledPin[i], LOW);
        buttonState[i] = false;
        keyTimer[i] = millis();
      }
    }
  }
}
