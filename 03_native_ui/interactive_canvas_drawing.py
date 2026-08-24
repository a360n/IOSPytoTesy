#!/usr/bin/env python3
"""
🖌️ لوحة تفاعلية واستعراض المؤثرات (Interactive UI & Canvas)
يقوم هذا السكربت بتجربة واجهة تفاعلية لتغيير الألوان، معاينة المؤثرات، وحساب الأبعاد الحقيقية لشاشة الآيفون.
"""

def show_interactive_canvas():
    try:
        import pyto_ui as ui
    except ImportError:
        print("❌ يتطلب تشغيل هذا السكربت داخل تطبيق Pyto على جهاز iOS.")
        return

    view = ui.View()
    try:
        view.background_color = ui.COLOR_SYSTEM_BACKGROUND
    except Exception:
        pass
    view.title = "🖌️ اللوحة التفاعلية"

    status_label = ui.Label()
    status_label.text = "المس الأزرار لتغيير ألوان اللوحة"
    try:
        status_label.font = ui.Font.bold_system_font_of_size(16)
        status_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    status_label.size = (320, 30)
    status_label.center = (view.width / 2, 40)

    # صندوق المعاينة الرئيسي
    canvas_box = ui.View()
    canvas_box.size = (280, 220)
    canvas_box.center = (view.width / 2, 180)
    canvas_box.corner_radius = 16
    try:
        canvas_box.background_color = ui.COLOR_SYSTEM_INDIGO
    except Exception:
        try:
            canvas_box.background_color = ui.COLOR_SYSTEM_BLUE
        except Exception:
            pass

    # أزرار اختيار الألوان
    colors = [
        ("أزرق", getattr(ui, 'COLOR_SYSTEM_BLUE', None)),
        ("أخضر", getattr(ui, 'COLOR_SYSTEM_GREEN', None)),
        ("برتقالي", getattr(ui, 'COLOR_SYSTEM_ORANGE', None)),
        ("وردي", getattr(ui, 'COLOR_SYSTEM_PINK', None)),
        ("بنفسجي", getattr(ui, 'COLOR_SYSTEM_PURPLE', None)),
    ]

    button_container = ui.View()
    button_container.size = (320, 50)
    button_container.center = (view.width / 2, 330)

    btn_width = 55
    spacing = 8
    for i, (col_name, col_val) in enumerate(colors):
        btn = ui.Button()
        btn.title = ""
        if col_val is not None:
            btn.background_color = col_val
        btn.corner_radius = 12
        btn.size = (btn_width, 40)
        btn.frame = (i * (btn_width + spacing), 0, btn_width, 40)
        
        def make_handler(c_val, name):
            def handler(sender):
                if c_val is not None:
                    canvas_box.background_color = c_val
                status_label.text = f"تم اختيار اللون: {name}"
                try:
                    ui.HapticFeedback(ui.HapticFeedback.SELECTION).generate()
                except Exception:
                    pass
            return handler

        btn.action = make_handler(col_val, col_name)
        button_container.add_subview(btn)

    view.add_subview(status_label)
    view.add_subview(canvas_box)
    view.add_subview(button_container)

    ui.show_view(view, mode=ui.PRESENTATION_MODE_SHEET)

if __name__ == "__main__":
    show_interactive_canvas()
