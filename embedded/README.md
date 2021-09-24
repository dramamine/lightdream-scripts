
## Contracts, Responsibilities, Messages



## 1. Arduino sends serial data via USB, which is read by TouchDesigner.

Serial data format:
```
char strBuf[8];
sprintf(strBuf, "%d %d", address, message);
Serial.println(strBuf);  
```

Received as space-delimited message.


### 1a. Triangle button interface
45 buttons, representing different sections of the dome. Plays animations specifically at those points.

address: 0-44
message: 1 for presses, 0 for releases

<!-- ### 1b. Circular touch interface.
3 touchpads.

address: 50-52
message: 1 for presses, 0 for releases
 -->


### 1b. Bees interface
1 motion sensor. When active, play bees animation.

address: 60
1 for motion, 0 for stillness

### 1c. Wedges / Bananas interface
10 touchpads.

address: 70-79
message: 1 for presses, 0 for releases

lights: 25 lights

### 1c. Colorwheel interface
6 touchpads.

address: 80-85
message: 1 for presses, 0 for releases



## 2. TouchDesigner sends serial data back to Arduino.

Serial data format:
Send a single byte via TouchDesigner.

## 2a. toggle between different rainbow sketches for the triangle patterns.

[0x60] - select 1st animation
[0x61] - select 2nd animation
... (space for future options)

## 2b. Inform when "song select" menu is active.
Using this to decide if we should light up the LEDs around the touchscreen.
[0x51] for song select active
[0x50] for song select inactive


### Add Seeeduino to Arduino IDE

Add this to Preferences -> Additional Boards
https://raw.githubusercontent.com/Seeed-Studio/Seeed_Platform/master/package_legacy_seeeduino_boards_index.json

More info here:
https://wiki.seeedstudio.com/Seeed_Arduino_Boards/

## 12-Key Touch-capacitive Sensor: MPR121 Library / Demo

https://wiki.seeedstudio.com/Grove-12_Key_Capacitive_I2C_Touch_Sensor_V2-MPR121/#play-with-arduino

Include Library from zip: https://github.com/linux-downey/Grove_touch_sensor_MPR121/archive/refs/heads/master.zip
