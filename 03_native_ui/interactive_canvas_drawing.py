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
    view.background_color = ui.COLOR_SYSTEM_BACKGROUND
    view.title = "🖌️ اللوحة التفاعلية"

    status_label = ui.Label("المس الأزرار لتغيير ألوان اللوحة")
    status_label.font = ui.Font.bold_system_font_of_size(16)
    status_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    status_label.size = (320, 30)
    status_label.center = (view.width / 2, 40)

    # صندوق المعاينة الرئيسي
    canvas_box = ui.View()
    canvas_box.size = (280, 220)
    canvas_box.center = (view.width / 2, 180)
    canvas_box.corner_radius = 16
    canvas_box.background_color = ui.COLOR_SYSTEM_INDIGO

    # أزرار اختيار الألوان
    colors = [
        ("أزرق", ui.COLOR_SYSTEM_BLUE),
        ("أخضر", ui.COLOR_SYSTEM_GREEN),
        ("برتقالي", ui.COLOR_SYSTEM_ORANGE),
        ("وردي", ui.COLOR_SYSTEM_PINK),
        ("بنفسجي", ui.COLOR_SYSTEM_PURPLE),
    ]

    button_container = ui.View()
    button_container.size = (320, 50)
    button_container.center = (view.width / 2, 330)

    btn_width = 55
    spacing = 8
    for i, (col_name, col_val) in enumerate(colors):
        btn = ui.Button(title="")
        btn.background_color = col_val
        btn.corner_radius = 12
        btn.size = (btn_width, 40)
        btn.frame = (i * (btn_width + spacing), 0, btn_width, 40)
        
        def make_handler(c_val, name):
            def handler(sender):
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
