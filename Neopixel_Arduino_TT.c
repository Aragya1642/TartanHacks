// Define a simple delay time for each chord change, e.g., 2 seconds
int simpleDelayTime = 2000;

#define PIN        6
#define NUM_LEDS   12

#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

uint32_t colors[9] = {
  strip.Color(238, 130, 238), // Violet for C
  strip.Color(75, 0, 130),    // Indigo for G
  strip.Color(0, 0, 255),     // Blue for Am
  strip.Color(0, 255, 0),     // Green for F
  strip.Color(255, 255, 0),   // Yellow for Dm7
  strip.Color(255, 165, 0),   // Orange for Am7
  strip.Color(255,0,0),       //Red for B
  strip.Color(255,192,203), //Pink for E
  strip.Color(0, 0, 0)              // Off for N.C.
};
// Define an array for the chord sequence
int songChords[] = {
   0, // A - fret 1
  1, // B and B flat - fret 2
  2, // C and C flat - fret 3
  3, // D and D flat - fret 4
  4, // E - fret 5
  5, // F and F sharp - fret 6
  6, // G and G sharp - fret 7
  7, // N.C.
  7, // N.C.
  7, // N.C.
  7, // N.C.
  7  // N.C.
  // Repeat the pattern or add more as needed}
};

void setStripColor(uint32_t color) {
  for(int i = 0; i < NUM_LEDS; i++) {
    strip.setPixelColor(i, color);
  }
  strip.show();
}
//LIFE IS A HIGH WAY NOTES:
//Main Riff:


void loop() {
  for (int i = 0; i < sizeof(songChords) / sizeof(int); i++) {
    // Set the LED color based on the current chord
    setStripColor(colors[songChords[i]]);
    // Wait for the simple delay time before changing to the next chord
    delay(simpleDelayTime);
  }
  // Here is the typical chords
  setStripColor(colors[4]);
  delay(simpleDelayTime);
  setStripColor(colors[1]);
  delay(simpleDelayTime);
  setStripColor(colors[6]);
  delay(simpleDelayTime);
  setStripColor(colors[3]);
  delay(simpleDelayTime);
  setStripColor(colors[0]);
  delay(simpleDelayTime);
  setStripColor(colors[4]);
  delay(simpleDelayTime);
}