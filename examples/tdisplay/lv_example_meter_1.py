"""
lv_example_meter_1.py using st7789 driver on a T-Display
"""

import utime as time
import lvgl as lv
from ili9XXX import st7789

disp = st7789(width=135, height=240, rot=st7789.PORTRAIT)

def set_value(indic, v):
    meter.set_indicator_value(indic, v)

#
# A simple meter
#
meter = lv.meter(lv.scr_act())
meter.center()
meter.set_size(135, 135)

# Add a scale first
scale = meter.add_scale()
meter.set_scale_ticks(scale, 51, 2, 10, lv.palette_main(lv.PALETTE.GREY))
meter.set_scale_major_ticks(scale, 10, 4, 15, lv.color_black(), 10)

indic = lv.meter_indicator_t()

# Add a blue arc to the start
indic = meter.add_arc(scale, 3, lv.palette_main(lv.PALETTE.BLUE), 0)
meter.set_indicator_start_value(indic, 0)
meter.set_indicator_end_value(indic, 20)

# Make the tick lines blue at the start of the scale
indic = meter.add_scale_lines(scale, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.BLUE), False, 0)
meter.set_indicator_start_value(indic, 0)
meter.set_indicator_end_value(indic, 20)

# Add a red arc to the end
indic = meter.add_arc(scale, 3, lv.palette_main(lv.PALETTE.RED), 0)
meter.set_indicator_start_value(indic, 80)
meter.set_indicator_end_value(indic, 100)

# Make the tick lines red at the end of the scale
indic = meter.add_scale_lines(scale, lv.palette_main(lv.PALETTE.RED), lv.palette_main(lv.PALETTE.RED), False, 0)
meter.set_indicator_start_value(indic, 80)
meter.set_indicator_end_value(indic, 100)

# Add a needle line indicator
indic = meter.add_needle_line(scale, 4, lv.palette_main(lv.PALETTE.GREY), -10)

# Create an animation to set the value
a = lv.anim_t()
a.init()
a.set_var(indic)
a.set_values(0, 100)
a.set_time(2000)
a.set_repeat_delay(100)
a.set_playback_time(500)
a.set_playback_delay(100)
a.set_repeat_count(lv.ANIM_REPEAT.INFINITE)
a.set_custom_exec_cb(lambda a,val: set_value(indic,val))
lv.anim_t.start(a)

