#!/usr/bin/env python3
"""
🎨 استعراض واجهات مستخدم iOS الأصلية (Native Pyto UIKit Showcase)
يقوم هذا السكربت ببناء واجهة مستخدم رسومية أصلية لنظام iOS بالكامل باستخدام بايثون!
تتضمن: أزرار تفاعلية، أشرطة تمرير، حقول نصية، مفاتيح تبديل، وأيقونات SF Symbols.
"""

def show_native_ui():
    try:
        import pyto_ui as ui
    except ImportError:
        print("=" * 60)
        print("❌ مكتبة 'pyto_ui' تعمل فقط داخل تطبيق Pyto على الآيفون.")
        print("💡 لتجربة الواجهة الرسومية الأصلية، شغل هذا السكربت داخل Pyto على هاتفك.")
        print("=" * 60)
        return

    # إنشاء العرض الرئيسي للواجهة
    view = ui.View()
    try:
        view.background_color = ui.COLOR_SYSTEM_BACKGROUND
    except Exception:
        pass
    view.title = "📱 تجربة واجهات iOS"

    # عنوان رئيسي
    title_label = ui.Label()
    title_label.text = "تجربة قدرات بايثون على الآيفون"
    try:
        title_label.font = ui.Font.bold_system_font_of_size(20)
        title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    title_label.size = (340, 40)
    title_label.center = (view.width / 2, 40)

    # نص وصفي
    desc_label = ui.Label()
    desc_label.text = "واجهة أصلية (Native UIKit) مبنية بالكامل ببايثون!"
    try:
        desc_label.font = ui.Font.system_font_of_size(14)
        desc_label.text_color = ui.COLOR_SECONDARY_LABEL
        desc_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    desc_label.size = (340, 30)
    desc_label.center = (view.width / 2, 75)

    # حقل إدخال نصي
    text_field = ui.TextField()
    try:
        text_field.placeholder = "اكتب شيئاً هنا لتجربته..."
        text_field.border_style = ui.TEXT_FIELD_BORDER_STYLE_ROUNDED_RECT
    except Exception:
        pass
    text_field.size = (300, 44)
    text_field.center = (view.width / 2, 130)

    # ملصق النتيجة
    result_label = ui.Label()
    result_label.text = "النتيجة ستظهر هنا..."
    try:
        result_label.font = ui.Font.system_font_of_size(16)
        result_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    result_label.size = (300, 30)
    result_label.center = (view.width / 2, 180)

    # دالة تفاعل عند الضغط على الزر
    def button_tapped(sender):
        text = getattr(text_field, 'text', '')
        if text and text.strip():
            result_label.text = f"✨ مرحباً: {text}!"
            try:
                result_label.text_color = ui.COLOR_SYSTEM_GREEN
            except Exception:
                pass
        else:
            result_label.text = "⚠️ الرجاء كتابة نص أولاً!"
            try:
                result_label.text_color = ui.COLOR_SYSTEM_RED
            except Exception:
                pass
        
        # اهتزاز تفاعلي عند النقر
        try:
            ui.HapticFeedback(ui.HapticFeedback.IMPACT_MEDIUM).generate()
        except Exception:
            pass

    # زر تفاعلي رئيسي
    btn = ui.Button()
    btn.title = "🚀 اضغط للتنفيذ"
    btn.size = (200, 50)
    btn.center = (view.width / 2, 240)
    try:
        btn.background_color = ui.COLOR_SYSTEM_BLUE
        btn.title_color = ui.COLOR_WHITE
        btn.corner_radius = 12
    except Exception:
        pass
    btn.action = button_tapped

    # شريط تمرير (Slider)
    slider_label = ui.Label()
    slider_label.text = "قيمة المؤشر: 50%"
    try:
        slider_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    slider_label.size = (300, 30)
    slider_label.center = (view.width / 2, 310)

    def slider_changed(sender):
        val = int(getattr(sender, 'value', 0.5) * 100)
        slider_label.text = f"قيمة المؤشر: {val}%"

    slider = ui.Slider()
    try:
        slider.value = 0.5
    except Exception:
        pass
    slider.size = (260, 30)
    slider.center = (view.width / 2, 350)
    slider.action = slider_changed

    # مفتاح تبديل (Switch)
    def switch_changed(sender):
        is_active = getattr(sender, 'is_on', getattr(sender, 'value', False))
        try:
            if is_active:
                view.background_color = ui.COLOR_SYSTEM_GROUPED_BACKGROUND
            else:
                view.background_color = ui.COLOR_SYSTEM_BACKGROUND
        except Exception:
            pass

    switch = ui.Switch()
    switch.center = (view.width / 2, 410)
    switch.action = switch_changed

    # إضافة العناصر إلى الواجهة
    view.add_subview(title_label)
    view.add_subview(desc_label)
    view.add_subview(text_field)
    view.add_subview(result_label)
    view.add_subview(btn)
    view.add_subview(slider_label)
    view.add_subview(slider)
    view.add_subview(switch)

    # عرض الواجهة للمستخدم بنمط Sheet
    print("📱 جاري عرض واجهة UIKit التفاعلية على شاشة الآيفون...")
    ui.show_view(view, mode=ui.PRESENTATION_MODE_SHEET)

if __name__ == "__main__":
    show_native_ui()
