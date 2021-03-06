"""
lv_example_spinner_1.py using st7789 driver on a T-Display
"""

import lvgl as lv
from ili9XXX import st7789

import axp202c

# init power manager, set backlight
axp = axp202c.PMU()
axp.enablePower(axp202c.AXP202_LDO2)
axp.setLDO2Voltage(2800)

# init display
disp = st7789(
    mosi=19,
    clk=18,
    cs=5,
    dc=27,
    rst=-1,
    backlight=12,
    power=-1,
    width=240,
    height=240,
    rot=st7789.INVERSE_PORTRAIT,
    factor=4)

# Create a spinner
spinner = lv.spinner(lv.scr_act(), 1000, 60)
spinner.set_size(200, 200)
spinner.center()


