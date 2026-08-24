#!/usr/bin/env python3
"""
🎨 Native iOS UIKit User Interface Showcase
Builds a complete native iOS graphical user interface entirely with Python!
Includes interactive buttons, sliders, text fields, switches, and SF Symbols.
"""

def show_native_ui():
    try:
        import pyto_ui as ui
    except ImportError:
        print("=" * 60)
        print("❌ 'pyto_ui' only runs inside the Pyto app on iOS.")
        print("💡 Run this script inside Pyto on your iPhone to view the UI.")
        print("=" * 60)
        return

    def get_system_color(name, legacy_name=None):
        if hasattr(ui, 'SystemColors') and hasattr(ui.SystemColors, name):
            return getattr(ui.SystemColors, name)
        if legacy_name and hasattr(ui, legacy_name):
            return getattr(ui, legacy_name)
        if hasattr(ui, f"COLOR_{name}"):
            return getattr(ui, f"COLOR_{name}")
        return getattr(ui, 'COLOR_WHITE', None)

    # Main Container View
    view = ui.View()
    bg_color = get_system_color('SYSTEM_BACKGROUND', 'COLOR_SYSTEM_BACKGROUND')
    if bg_color is not None:
        view.background_color = bg_color
    view.title = "📱 iOS UIKit Showcase"

    # Title Label
    title_label = ui.Label()
    title_label.text = "Python on iPhone 17 Pro Max"
    try:
        title_label.font = ui.Font.bold_system_font_of_size(20)
        if hasattr(ui, 'TextAlignment'):
            title_label.text_alignment = ui.TextAlignment.CENTER
        elif hasattr(ui, 'TEXT_ALIGNMENT_CENTER'):
            title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    title_label.size = (340, 40)
    title_label.center = (view.width / 2, 40)

    # Subtitle Label
    desc_label = ui.Label()
    desc_label.text = "Native UIKit interface created entirely with pure Python!"
    try:
        desc_label.font = ui.Font.system_font_of_size(14)
        sec_label_color = get_system_color('SECONDARY_LABEL', 'COLOR_SECONDARY_LABEL')
        if sec_label_color is not None:
            desc_label.text_color = sec_label_color
        if hasattr(ui, 'TextAlignment'):
            desc_label.text_alignment = ui.TextAlignment.CENTER
    except Exception:
        pass
    desc_label.size = (340, 30)
    desc_label.center = (view.width / 2, 75)

    # Text Input Field
    text_field = ui.TextField()
    try:
        text_field.placeholder = "Type your text here..."
        if hasattr(ui, 'TextFieldBorderStyle'):
            text_field.border_style = ui.TextFieldBorderStyle.ROUNDED_RECT
        elif hasattr(ui, 'TEXT_FIELD_BORDER_STYLE_ROUNDED_RECT'):
            text_field.border_style = ui.TEXT_FIELD_BORDER_STYLE_ROUNDED_RECT
    except Exception:
        pass
    text_field.size = (300, 44)
    text_field.center = (view.width / 2, 130)

    # Result Label
    result_label = ui.Label()
    result_label.text = "Result will appear here..."
    try:
        result_label.font = ui.Font.system_font_of_size(16)
        if hasattr(ui, 'TextAlignment'):
            result_label.text_alignment = ui.TextAlignment.CENTER
    except Exception:
        pass
    result_label.size = (300, 30)
    result_label.center = (view.width / 2, 180)

    # Action Handler
    def button_tapped(sender):
        text = getattr(text_field, 'text', '')
        if text and text.strip():
            result_label.text = f"✨ Hello: {text}!"
            green_col = get_system_color('SYSTEM_GREEN', 'COLOR_SYSTEM_GREEN')
            if green_col is not None:
                result_label.text_color = green_col
        else:
            result_label.text = "⚠️ Please enter some text first!"
            red_col = get_system_color('SYSTEM_RED', 'COLOR_SYSTEM_RED')
            if red_col is not None:
                result_label.text_color = red_col
        
        try:
            ui.HapticFeedback(ui.HapticFeedback.IMPACT_MEDIUM).generate()
        except Exception:
            pass

    # Primary Action Button
    btn = ui.Button()
    btn.title = "🚀 Execute Action"
    btn.size = (200, 50)
    btn.center = (view.width / 2, 240)
    blue_col = get_system_color('SYSTEM_BLUE', 'COLOR_SYSTEM_BLUE')
    if blue_col is not None:
        btn.background_color = blue_col
    white_col = get_system_color('WHITE', 'COLOR_WHITE')
    if white_col is not None:
        btn.title_color = white_col
    btn.corner_radius = 12
    btn.action = button_tapped

    # Slider
    slider_label = ui.Label()
    slider_label.text = "Slider Value: 50%"
    try:
        if hasattr(ui, 'TextAlignment'):
            slider_label.text_alignment = ui.TextAlignment.CENTER
    except Exception:
        pass
    slider_label.size = (300, 30)
    slider_label.center = (view.width / 2, 310)

    def slider_changed(sender):
        val = int(getattr(sender, 'value', 0.5) * 100)
        slider_label.text = f"Slider Value: {val}%"

    slider = ui.Slider()
    try:
        slider.value = 0.5
    except Exception:
        pass
    slider.size = (260, 30)
    slider.center = (view.width / 2, 350)
    slider.action = slider_changed

    # Switch
    def switch_changed(sender):
        is_active = getattr(sender, 'is_on', getattr(sender, 'value', False))
        try:
            if is_active:
                grp_bg = get_system_color('SYSTEM_GROUPED_BACKGROUND', 'COLOR_SYSTEM_GROUPED_BACKGROUND')
                if grp_bg is not None:
                    view.background_color = grp_bg
            else:
                std_bg = get_system_color('SYSTEM_BACKGROUND', 'COLOR_SYSTEM_BACKGROUND')
                if std_bg is not None:
                    view.background_color = std_bg
        except Exception:
            pass

    switch = ui.Switch()
    switch.center = (view.width / 2, 410)
    switch.action = switch_changed

    # Add Subviews
    view.add_subview(title_label)
    view.add_subview(desc_label)
    view.add_subview(text_field)
    view.add_subview(result_label)
    view.add_subview(btn)
    view.add_subview(slider_label)
    view.add_subview(slider)
    view.add_subview(switch)

    print("📱 Presenting native UIKit view on iPhone screen...")
    mode = getattr(ui.PresentationMode, 'SHEET', None) if hasattr(ui, 'PresentationMode') else getattr(ui, 'PRESENTATION_MODE_SHEET', 0)
    if mode is not None:
        ui.show_view(view, mode=mode)
    else:
        ui.show_view(view)

if __name__ == "__main__":
    show_native_ui()
