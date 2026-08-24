#!/usr/bin/env python3
"""
🖌️ Interactive Palette & Touch Canvas
Tests dynamic color changing, haptic interactions, and layout sizing in UIKit.
"""

def show_interactive_canvas():
    try:
        import pyto_ui as ui
    except ImportError:
        print("❌ This test requires the Pyto app on iOS.")
        return

    def get_system_color(name, legacy_name=None):
        if hasattr(ui, 'SystemColors') and hasattr(ui.SystemColors, name):
            return getattr(ui.SystemColors, name)
        if legacy_name and hasattr(ui, legacy_name):
            return getattr(ui, legacy_name)
        if hasattr(ui, f"COLOR_{name}"):
            return getattr(ui, f"COLOR_{name}")
        return None

    view = ui.View()
    bg_col = get_system_color('SYSTEM_BACKGROUND', 'COLOR_SYSTEM_BACKGROUND')
    if bg_col is not None:
        view.background_color = bg_col
    view.title = "🖌️ Interactive Palette"

    status_label = ui.Label()
    status_label.text = "Tap buttons to change canvas color"
    try:
        title_font = ui.Font.bold_system_font_of_size(16)
        status_label.font = title_font
        if hasattr(ui, 'TextAlignment'):
            status_label.text_alignment = ui.TextAlignment.CENTER
        elif hasattr(ui, 'TEXT_ALIGNMENT_CENTER'):
            status_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    status_label.size = (320, 30)
    status_label.center = (view.width / 2, 40)

    # Preview Canvas Box
    canvas_box = ui.View()
    canvas_box.size = (280, 220)
    canvas_box.center = (view.width / 2, 180)
    canvas_box.corner_radius = 16
    indigo_col = get_system_color('SYSTEM_INDIGO', 'COLOR_SYSTEM_INDIGO') or get_system_color('SYSTEM_BLUE', 'COLOR_SYSTEM_BLUE')
    if indigo_col is not None:
        canvas_box.background_color = indigo_col

    # Color Options
    colors = [
        ("Blue", get_system_color('SYSTEM_BLUE', 'COLOR_SYSTEM_BLUE')),
        ("Green", get_system_color('SYSTEM_GREEN', 'COLOR_SYSTEM_GREEN')),
        ("Orange", get_system_color('SYSTEM_ORANGE', 'COLOR_SYSTEM_ORANGE')),
        ("Pink", get_system_color('SYSTEM_PINK', 'COLOR_SYSTEM_PINK')),
        ("Purple", get_system_color('SYSTEM_PURPLE', 'COLOR_SYSTEM_PURPLE')),
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
                status_label.text = f"Selected Color: {name}"
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

    mode = getattr(ui.PresentationMode, 'SHEET', None) if hasattr(ui, 'PresentationMode') else getattr(ui, 'PRESENTATION_MODE_SHEET', 0)
    if mode is not None:
        ui.show_view(view, mode=mode)
    else:
        ui.show_view(view)

if __name__ == "__main__":
    show_interactive_canvas()
