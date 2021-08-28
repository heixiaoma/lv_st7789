"""
lv_example_spinner_1.py using st7789 driver on a T-Display
"""

import lvgl as lv
from ili9XXX import st7789

disp = st7789(width=135, height=240, rot=st7789.LANDSCAPE)

# Create a spinner
spinner = lv.spinner(lv.scr_act(), 1000, 60)
spinner.set_size(100, 100)
spinner.center()


