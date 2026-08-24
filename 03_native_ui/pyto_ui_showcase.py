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
    view.background_color = ui.COLOR_SYSTEM_BACKGROUND
    view.title = "📱 تجربة واجهات iOS"

    # عنوان رئيسي
    title_label = ui.Label("تجربة قدرات بايثون على الآيفون")
    title_label.font = ui.Font.bold_system_font_of_size(20)
    title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    title_label.size = (340, 40)
    title_label.center = (view.width / 2, 40)
    title_label.flex = [ui.FLEXIBLE_TOP_MARGIN, ui.FLEXIBLE_BOTTOM_MARGIN, ui.FLEXIBLE_LEFT_MARGIN, ui.FLEXIBLE_RIGHT_MARGIN]

    # نص وصفي
    desc_label = ui.Label("هذه واجهة أصلية (Native UIKit) تم بناؤها بالكامل بكود بايثون!")
    desc_label.font = ui.Font.system_font_of_size(14)
    desc_label.text_color = ui.COLOR_SECONDARY_LABEL
    desc_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    desc_label.size = (340, 30)
    desc_label.center = (view.width / 2, 75)

    # حقل إدخال نصي
    text_field = ui.TextField(placeholder="اكتب شيئاً هنا لتجربته...")
    text_field.size = (300, 44)
    text_field.center = (view.width / 2, 130)
    text_field.border_style = ui.TEXT_FIELD_BORDER_STYLE_ROUNDED_RECT

    # ملصق النتيجة
    result_label = ui.Label("النتيجة ستظهر هنا...")
    result_label.font = ui.Font.system_font_of_size(16)
    result_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    result_label.size = (300, 30)
    result_label.center = (view.width / 2, 180)

    # دالة تفاعل عند الضغط على الزر
    def button_tapped(sender):
        text = text_field.text
        if text.strip():
            result_label.text = f"✨ مرحباً: {text}!"
            result_label.text_color = ui.COLOR_SYSTEM_GREEN
        else:
            result_label.text = "⚠️ الرجاء كتابة نص أولاً!"
            result_label.text_color = ui.COLOR_SYSTEM_RED
        
        # اهتزاز تفاعلي عند النقر
        try:
            ui.HapticFeedback(ui.HapticFeedback.IMPACT_MEDIUM).generate()
        except Exception:
            pass

    # زر تفاعلي رئيسي
    btn = ui.Button(title="🚀 اضغط للتنفيذ")
    btn.size = (200, 50)
    btn.center = (view.width / 2, 240)
    btn.background_color = ui.COLOR_SYSTEM_BLUE
    btn.title_color = ui.COLOR_WHITE
    btn.corner_radius = 12
    btn.action = button_tapped

    # شريط تمرير (Slider)
    slider_label = ui.Label("قيمة المؤشر: 50%")
    slider_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    slider_label.size = (300, 30)
    slider_label.center = (view.width / 2, 310)

    def slider_changed(sender):
        val = int(sender.value * 100)
        slider_label.text = f"قيمة المؤشر: {val}%"

    slider = ui.Slider(value=0.5)
    slider.size = (260, 30)
    slider.center = (view.width / 2, 350)
    slider.action = slider_changed

    # مفتاح تبديل (Switch)
    def switch_changed(sender):
        if sender.is_on:
            view.background_color = ui.COLOR_SYSTEM_GROUPED_BACKGROUND
        else:
            view.background_color = ui.COLOR_SYSTEM_BACKGROUND

    switch = ui.Switch(is_on=False)
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

    # عرض الواجهة للمستخدم بنمط Sheet أو FullScreen
    print("📱 جاري عرض واجهة UIKit التفاعلية على شاشة الآيفون...")
    ui.show_view(view, mode=ui.PRESENTATION_MODE_SHEET)

if __name__ == "__main__":
    show_native_ui()
