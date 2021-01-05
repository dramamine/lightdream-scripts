// https://github.com/FastLED/FastLED/blob/master/examples/Multiple/OctoWS2811Demo/OctoWS2811Demo.ino
#define USE_OCTOWS2811
#include <OctoWS2811.h>
#include <FastLED.h>

#define NUM_LEDS_PER_STRIP 40
#define NUM_STRIPS 6

#define BRIGHTNESS  200
#define FRAMES_PER_SECOND 60
CRGB leds[NUM_LEDS_PER_STRIP * NUM_STRIPS];

int NUM_LEDS = NUM_LEDS_PER_STRIP * NUM_STRIPS;

void setup()
{
  LEDS.addLeds<OCTOWS2811>(leds, NUM_LEDS_PER_STRIP);
  LEDS.setBrightness(32);
}

void loop() {
  // huechange_w_n_leds_indicator()
  cylon2();
}

void huechange_w_n_leds_indicator()
{
  static uint8_t hue = 0;
  for (int i = 0; i < NUM_STRIPS; i++)
  {
    for (int j = 0; j < NUM_LEDS_PER_STRIP; j++)
    {
      leds[(i * NUM_LEDS_PER_STRIP) + j] = CHSV((32 * i) + hue + j, 192, 255);
    }
  }

  // Set the first n leds on each strip to show which strip it is
  for (int i = 0; i < NUM_STRIPS; i++)
  {
    for (int j = 0; j <= i; j++)
    {
      leds[(i * NUM_LEDS_PER_STRIP) + j] = CRGB::Red;
    }
  }

  hue++;

  LEDS.show();
  LEDS.delay(10);
}

void fadeall()
{
  for (int i = 0; i < NUM_LEDS; i++)
  {
    leds[i].nscale8(250);
  }
}

void cylon()
{
  static uint8_t hue = 0;
  Serial.print("x");
  // First slide the led in one direction
  for (int i = 0; i < NUM_LEDS; i++)
  {
    // Set the i'th led to red
    leds[i] = CHSV(hue++, 255, 255);
    // Show the leds
    LEDS.show();
    // now that we've shown the leds, reset the i'th led to black
    // leds[i] = CRGB::Black;
    fadeall();
    // Wait a little bit before we loop around and do it again
    delay(10);
  }
  Serial.print("x");

  // Now go in the other direction.
  for (int i = (NUM_LEDS)-1; i >= 0; i--)
  {
    // Set the i'th led to red
    leds[i] = CHSV(hue++, 255, 255);
    // Show the leds
    LEDS.show();
    // now that we've shown the leds, reset the i'th led to black
    // leds[i] = CRGB::Black;
    fadeall();
    // Wait a little bit before we loop around and do it again
    delay(10);
  }
}

void cylon2()
{
  static uint8_t hue = 0;
  Serial.print("x");
  // First slide the led in one direction
  for (int i = 0; i < 10; i++)
  {
    hue+=2;
    // Set the i'th led to red
    for (int strip = 0; strip < NUM_STRIPS; strip++) {
      leds[strip*NUM_LEDS_PER_STRIP + i] = CHSV(hue, 255, 255);
      leds[strip*NUM_LEDS_PER_STRIP + 19 - i] = CHSV(hue, 255, 255);
      leds[strip*NUM_LEDS_PER_STRIP + 20 + i] = CHSV(hue, 255, 255);
      leds[strip*NUM_LEDS_PER_STRIP + 39 - i] = CHSV(hue, 255, 255);
    }

    // Show the leds
    LEDS.show();

    // Wait a little bit before we loop around and do it again
    delay(500);
  }
  // now that we've shown the leds, reset the i'th led to black
  // leds[i] = CRGB::Black;
  for (int i = 0; i < 200; i++) {

    fadeall();
    LEDS.show();
    delay(10);
  }

  Serial.print("x");

  // // Now go in the other direction.
  // for (int i = (NUM_LEDS)-1; i >= 0; i--)
  // {
  //   hue++;
  //   // Set the i'th led to red
  //   for (int strip = 0; strip < NUM_STRIPS; strip++)
  //   {
  //     leds[strip * NUM_LEDS_PER_STRIP + i] = CHSV(hue, 255, 255);
  //     leds[strip * NUM_LEDS_PER_STRIP + 19 - i] = CHSV(hue, 255, 255);
  //     leds[strip * NUM_LEDS_PER_STRIP + 20 + i] = CHSV(hue, 255, 255);
  //     leds[strip * NUM_LEDS_PER_STRIP + 39 - i] = CHSV(hue, 255, 255);
  //   }
  //   // Show the leds
  //   LEDS.show();
  //   // now that we've shown the leds, reset the i'th led to black
  //   // leds[i] = CRGB::Black;
  //   fadeall();
  //   // Wait a little bit before we loop around and do it again
  //   delay(10);
  // }
}