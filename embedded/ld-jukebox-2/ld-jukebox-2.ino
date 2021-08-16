#include "Seeed_MPR121_driver.h"
#include "FastLED.h"
#include <SoftwareSerial.h>

#define LED_STRAND_1_DATA_PIN 2
#define LED_STRAND_1_NUM_LEDS 50
#define LED_STRAND_2_DATA_PIN 3
#define LED_STRAND_2_NUM_LEDS 50

#define LED_TYPE WS2811
#define COLOR_ORDER GRB
#define NUM_LEDS 100 // i.e. total LEDs
#define BRIGHTNESS 55

int sections = 6;
// i.e. this section starts at LED [x] and ends at LED [x+1]
u16 sectionIndices[7] = {0, 10, 20, 30, 40, 50, 100};
bool sectionEnabled[6] = {false, false, false, false, false, false};

// ex. touch input 'i' will enable/disable section touchInputToSectionMap[i]
int touchInputToSectionMap[8] = {0, 1, 2, 3, -1, -1, -1, -1};

CRGB leds[NUM_LEDS];

Mpr121 mpr121;
u16 touch_status_flag[CHANNEL_NUM] = {0};

// SoftwareSerial ssa(2, 3); // RX, TX

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  // ssa.begin(9600);

  _setupTouchInput();
  delay(3000); // 3 second delay for recovery
  _setupLeds();
}

void loop()
{
  // put your main code here, to run repeatedly:
  _readTouchInput();

  _readSerial();

  pride2();
  FastLED.show();
}

void _setupLeds()
{
  // tell FastLED about the LED strip configuration
  // https://github.com/FastLED/FastLED/wiki/Multiple-Controller-Examples#one-array-many-strips
  FastLED.addLeds<LED_TYPE, LED_STRAND_1_DATA_PIN, COLOR_ORDER>(leds, 0, LED_STRAND_1_NUM_LEDS)
      .setCorrection(TypicalLEDStrip)
      .setDither(BRIGHTNESS < 255);

  FastLED.addLeds<LED_TYPE, LED_STRAND_2_DATA_PIN, COLOR_ORDER>(leds, LED_STRAND_1_NUM_LEDS, LED_STRAND_2_NUM_LEDS)
      .setCorrection(TypicalLEDStrip)
      .setDither(BRIGHTNESS < 255);

  // set master brightness control
  FastLED.setBrightness(BRIGHTNESS);
}

void _setupTouchInput()
{
  s32 ret = 0;

  if (mpr121.begin() < 0)
  {
    Serial.println("Can't detect device!!!!");
  }
  else
  {
    Serial.println("mpr121 init OK!");
  }
}
void _readTouchInput()
{
  u16 result = 0;
  u16 filtered_data_buf[CHANNEL_NUM] = {0};
  u8 baseline_buf[CHANNEL_NUM] = {0};

  result = mpr121.check_status_register();

  mpr121.get_filtered_reg_data(&result, filtered_data_buf);

  for (int i = 0; i < CHANNEL_NUM; i++)
  {
    if (result & (1 << i)) /*key i is pressed!!*/
    {
      if (0 == touch_status_flag[i])
      {
        touch_status_flag[i] = 1;
        Serial.print("key ");
        Serial.print(i);
        Serial.println("pressed");

        int section = touchInputToSectionMap[i];
        if (i >= 0)
          sectionEnabled[section] = true;
      }
    }
    else
    {
      if (1 == touch_status_flag[i])
      {
        touch_status_flag[i] = 0;
        Serial.print("key ");
        Serial.print(i);
        Serial.println("release");

        int section = touchInputToSectionMap[i];
        if (i >= 0)
          sectionEnabled[section] = false;
      }
    }
  }
}

// FORMAT:
// byte 51: main menu - turn on jukebox song menu lights
// byte 50: song selected - turn off
void _readSerial()
{
  while (Serial.available())
  {
    int rcvd = Serial.read();
    if (rcvd == 51)
    {
      sectionEnabled[5] = true;
    }
    else if (rcvd == 50)
    {
      sectionEnabled[5] = false;
    }
  }

  // ssa is data sent from ex. the triangle controller
  // we relay it to Serial so that TouchDesigner can read it
  //  while(ssa.available()) {
  //    char rcvd = ssa.read();
  //    Serial.print(rcvd);
  //  }
}

// This function draws rainbows with an ever-changing,
// widely-varying set of parameters.
void pride2()
{
  static uint16_t sPseudotime = 0;
  static uint16_t sLastMillis = 0;
  static uint16_t sHue16 = 0;

  uint8_t sat8 = beatsin88(87, 220, 250);
  uint8_t brightdepth = beatsin88(341, 96, 224);
  uint16_t brightnessthetainc16 = beatsin88(203, (25 * 256), (40 * 256));
  uint8_t msmultiplier = beatsin88(147, 23, 60);

  uint16_t hue16 = sHue16; //gHue * 256;
  uint16_t hueinc16 = beatsin88(113, 1, 3000);

  uint16_t ms = millis();
  uint16_t deltams = ms - sLastMillis;
  sLastMillis = ms;
  sPseudotime += deltams * msmultiplier;
  sHue16 += deltams * beatsin88(400, 5, 9);
  uint16_t brightnesstheta16 = sPseudotime;

  // to color
  for (uint16_t i = 0; i < NUM_LEDS; i++)
  {
    hue16 += hueinc16;
    uint8_t hue8 = hue16 / 256;

    brightnesstheta16 += brightnessthetainc16;
    uint16_t b16 = sin16(brightnesstheta16) + 32768;

    uint16_t bri16 = (uint32_t)((uint32_t)b16 * (uint32_t)b16) / 65536;
    uint8_t bri8 = (uint32_t)(((uint32_t)bri16) * brightdepth) / 65536;
    bri8 += (255 - brightdepth);

    CRGB newcolor = CHSV(hue8, sat8, bri8);

    uint16_t pixelnumber = i;
    pixelnumber = (NUM_LEDS - 1) - pixelnumber;

    nblend(leds[i], newcolor, 64);
  }

  for (byte section = 0; section < sections; section++)
  {
    if (sectionEnabled[section] == false)
    {
      // to black
      for (uint16_t i = sectionIndices[section]; i < sectionIndices[section + 1]; i++)
      {
        leds[i] = CRGB::Black;
      }
      // continue;
    }
  }
}

//
//// This function draws rainbows with an ever-changing,
//// widely-varying set of parameters.
//void pride()
//{
//  static uint16_t sPseudotime = 0;
//  static uint16_t sLastMillis = 0;
//  static uint16_t sHue16 = 0;
//
//  uint8_t sat8 = beatsin88( 87, 220, 250);
//  uint8_t brightdepth = beatsin88( 341, 96, 224);
//  uint16_t brightnessthetainc16 = beatsin88( 203, (25 * 256), (40 * 256));
//  uint8_t msmultiplier = beatsin88(147, 23, 60);
//
//  uint16_t hue16 = sHue16;//gHue * 256;
//  uint16_t hueinc16 = beatsin88(113, 1, 3000);
//
//  uint16_t ms = millis();
//  uint16_t deltams = ms - sLastMillis ;
//  sLastMillis  = ms;
//  sPseudotime += deltams * msmultiplier;
//  sHue16 += deltams * beatsin88( 400, 5, 9);
//  uint16_t brightnesstheta16 = sPseudotime;
//
//  for ( uint16_t i = 0 ; i < NUM_LEDS; i++) {
//    hue16 += hueinc16;
//    uint8_t hue8 = hue16 / 256;
//
//    brightnesstheta16  += brightnessthetainc16;
//    uint16_t b16 = sin16( brightnesstheta16  ) + 32768;
//
//    uint16_t bri16 = (uint32_t)((uint32_t)b16 * (uint32_t)b16) / 65536;
//    uint8_t bri8 = (uint32_t)(((uint32_t)bri16) * brightdepth) / 65536;
//    bri8 += (255 - brightdepth);
//
//    CRGB newcolor = CHSV( hue8, sat8, bri8);
//
//    uint16_t pixelnumber = i;
//    pixelnumber = (NUM_LEDS - 1) - pixelnumber;
//
//    nblend( leds[pixelnumber], newcolor, 64);
//  }
//}