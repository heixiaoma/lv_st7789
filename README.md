# lv_st7789 Hybrid MicroPython LVGL driver for ST7789 Displays

This driver adds support for 320x240, 240x240 and 135x240 ST7789 displays with
rotations for the ESP32 to the LVGL MicroPython bindings.

## Install and Build

- Clone the https://github.com/lvgl/lv_micropython repo.
- Copy the espidf.c and ili9XXX.py files from the es32 directory in this repo into the lv_micropython/lib/lv_bindings/driver/esp32/ directory of your cloned lv_micropython repo.
- Follow the build instructions from the README.md of the https://github.com/lvgl/lv_micropython repo.

## Pre-compiled firmware.bin

See the firmware/tdisplay directory for a pre-compiled ESP32 GENERIC firmware.bin file you can flash to an ESP32 device using the esptool.py utility.

## Examples

See the examples/tdisplay directory for several LVGL MicroPython example programs configured for the ESP32 TTGO T-Display device.

## Parameters and defaults

```
    st7789(
        miso=-1, mosi=19, clk=18, cs=5, dc=16, rst=23, power=-1, power_on=0
        backlight=4, backlight_on=1, spihost=esp.HSPI_HOST, mhz=40, factor=4,
        hybrid=True, width=135, height=240, colormode=COLOR_MODE_BGR, rot=PORTRAIT,
        invert=True, double_buffer=False, half_duplex=True, asynchronous=False,
        initialize=True)
```

Arg | Description
--- | -----------
miso | Pin for SPI Data from display, -1 if not used as many st7789 displays do not have this pin
mosi | Pin for SPI Data to display (REQUIRED)
clk | Pin for SPI Clock (REQUIRED)
cs | Pin for display CS
dc | Pin for display DC (REQUIRED)
rst | Pin for display RESET
power | Pin for display Power ON, -1 if not used
power_on | Pin value for Power ON
backlight | Pin for display backlight control
backlight_on | Pin value for backlight on
spihost | ESP SPI Port
mhz | SPI baud rate in mhz
factor | Decrease frame buffer by factor
hybrid | Boolean, True to use C refresh routine, False for pure Python driver
width | Display width
height | Display height
colormode | Display colormode
rot | Display orientation, PORTRAIT, LANDSCAPE, INVERSE_PORTRAIT, INVERSE_LANDSCAPE
invert | Display invert colors setting
double_buffer | Boolean, True to use double buffering, False to use single buffer (saves memory)
half_duplex | Boolean, True to use half duplex SPI communications
asynchronous | Boolean, True to use asynchronous routines
initialize | Boolean, True to initialize display

