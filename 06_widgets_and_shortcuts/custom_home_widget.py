#!/usr/bin/env python3
"""
📱 ويدجت الشاشة الرئيسية المخصص (Custom iOS Home Screen Widget)
يقوم هذا السكربت ببناء ويدجت حقيقي لشاشة الآيفون الرئيسية وشاشة القفل باستخدام مكتبة widgets في Pyto.
يعرض الويدجت: التاريخ، الوقت، اقتباس يومي تحفيزي، وإحصائيات النظام.

💡 كيفية تثبيته على شاشة الآيفون:
1. افتح تطبيق Pyto على الآيفون.
2. توجه للشاشة الرئيسية واضغط مطولاً لإضافة ويدجت جديد (+).
3. اختر تطبيق Pyto ثم اختر حجم الويدجت (Small, Medium, Large).
4. اضغط على الويدجت واختر هذا الملف (custom_home_widget.py) ليعمل تلقائياً!
"""

import datetime
import random

def create_widget():
    try:
        import widgets as wd
    except ImportError:
        print("❌ مكتبة 'widgets' تعمل فقط داخل تطبيق Pyto على iOS.")
        print("💡 لتشغيل الويدجت، قم بإضافته من شاشة الآيفون الرئيسية واختيار هذا الملف.")
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

    # بناء واجهة الويدجت
    widget = wd.Widget()
    widget.background_color = wd.Color.rgb(15/255, 23/255, 42/255)  # Dark Navy Slate

    # إضافة حاوية رأسية للعناصر
    layout = wd.DynamicWidget()
    
    # عنوان ووقت
    title_text = wd.Text(f"⚡ {time_str}")
    title_text.font = wd.Font.bold_system_font_of_size(22)
    title_text.color = wd.Color.rgb(56/255, 189/255, 248/255)  # Sky Blue

    date_text = wd.Text(date_str)
    date_text.font = wd.Font.system_font_of_size(13)
    date_text.color = wd.Color.rgb(148/255, 163/255, 184/255)

    quote_text = wd.Text(f"\"{quote}\"")
    quote_text.font = wd.Font.italic_system_font_of_size(14)
    quote_text.color = wd.Color.white

    # إضافة العناصر
    layout.set_layout([title_text, date_text, wd.Spacer(), quote_text])
    
    # عرض الويدجت في Pyto للمعاينة
    wd.show_widget(layout)

if __name__ == "__main__":
    create_widget()
