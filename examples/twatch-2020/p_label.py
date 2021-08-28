"""
p_label.py example using st7789 driver on a T-Display in Portrait mode
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

# Show line wrap, re-color, line align and text scrolling.
label1 = lv.label(lv.scr_act())
label1.set_long_mode(lv.label.LONG.WRAP);     # Break the long lines*/
label1.set_recolor(True)                      # Enable re-coloring by commands in the text
label1.set_text("#0000ff Re-color# #ff00ff words# #ff0000 of a# label, align the lines to the center"
                              " and  wrap long text automatically.")
label1.set_width(135)                         # Set smaller width to make the lines wrap
label1.set_style_text_align(lv.ALIGN.CENTER, 0)
label1.align(lv.ALIGN.CENTER, 0, -40)

label2 = lv.label(lv.scr_act())
label2.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR) # Circular scroll
label2.set_width(135)
label2.set_text("This is a circularly scrolling text.......")
label2.align(lv.ALIGN.CENTER, 0, 40)
