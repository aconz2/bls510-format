# BLS-510 Brushless DC Driver File Format

This is a WIP documentation of the file format used for the configuration of the [BLS-510 BLDC](https://www.omc-stepperonline.com/bldc-driver/digital-brushless-dc-motor-driver-dc18v-50v-with-a-hall-sensor.html).

I was having issues configuring the parameters `Rise time` and `Dec time`. In the provided GUI, I would change the setting, hit `Save to EEPROM` and the setting would just revert.

Using the `Save to File` as a start, the configuration is 64 bytes of data. I created 64 files with all zeros and a single 1 byte in each position (this is in `genfiles.py`). Then I ran the ahk script `loadfile.ahk` to load it and screenshot the window. From there I found `Rise time` is bytes 36 and 37 as little endian 16 bit numbers as deciseconds (ie. rise time is `value / 10`) and dec time is bytes 38 and 39.

Right now that's all I need changed that I can't change elsewhere so I'm not bothering to document the whole thing but might get around to it at some point. It shouldn't be too hard especially with the screenshotting tool.

The ahk script requires [this](https://github.com/mmikeww/AHKv2-Gdip/blob/master/Gdip_All.ahk) for the screenshots
