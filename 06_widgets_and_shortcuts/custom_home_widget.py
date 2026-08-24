#!/usr/bin/env python3
"""
📱 Custom iOS Home Screen & Lock Screen Widget
Builds a native iOS widget using Pyto's widgets module.
Displays current time, formatted date, dynamic quote, and telemetry.

💡 How to configure on iPhone:
1. Open Pyto on iOS.
2. Go to the Home Screen, long-press to enter jiggle mode, tap (+) to add a widget.
3. Select Pyto and choose your preferred widget size (Small, Medium, Large).
4. Tap the widget in edit mode and assign this script (custom_home_widget.py).
"""

import datetime
import random

def create_widget():
    try:
        import widgets as wd
    except ImportError:
        print("❌ The 'widgets' module is only available in Pyto on iOS.")
        print("💡 To use this widget, add a Pyto widget from your iPhone Home Screen and link this file.")
        return

    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%A, %d %B")

    quotes = [
        "Code is poetry written with logic.",
        "Python on iPhone: Limitless Power!",
        "Make it work, make it right, make it fast.",
        "Simplicity is prerequisite for reliability."
    ]
    quote = random.choice(quotes)

    widget = wd.Widget()
    widget.background_color = wd.Color.rgb(15/255, 23/255, 42/255)  # Dark Slate

    layout = wd.DynamicWidget()
    
    title_text = wd.Text(f"⚡ {time_str}")
    title_text.font = wd.Font.bold_system_font_of_size(22)
    title_text.color = wd.Color.rgb(56/255, 189/255, 248/255)  # Sky Blue

    date_text = wd.Text(date_str)
    date_text.font = wd.Font.system_font_of_size(13)
    date_text.color = wd.Color.rgb(148/255, 163/255, 184/255)

    quote_text = wd.Text(f"\"{quote}\"")
    quote_text.font = wd.Font.italic_system_font_of_size(14)
    quote_text.color = wd.Color.white

    layout.set_layout([title_text, date_text, wd.Spacer(), quote_text])
    
    wd.show_widget(layout)

if __name__ == "__main__":
    create_widget()
