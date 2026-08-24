#!/usr/bin/env python3
"""
🧭 ميزان رقمي رسومي حي باستخدام الحساسات (Live Animated Sensor UI)
يقوم هذا السكربت بدمج واجهات UIKit مع حساسات الجيروسكوب والتسارع (Motion)،
ليصنع ميزاناً مائياً رقمياً تفاعلياً (Bubble Level) تتحرك فيه الفقاعة على الشاشة وفق ميل الهاتف.
"""

import math
import threading
import time

def run_live_sensor_ui():
    try:
        import pyto_ui as ui
        import motion
    except ImportError:
        print("❌ يتطلب هذا الاختبار تشغيله داخل تطبيق Pyto على جهاز iOS.")
        return

    view = ui.View()
    view.background_color = ui.COLOR_SYSTEM_BACKGROUND
    view.title = "🧭 ميزان الميل الرقمي التفاعلي"

    title_label = ui.Label("حرك هاتفك لمشاهدة تفاعل الفقاعة")
    title_label.font = ui.Font.bold_system_font_of_size(18)
    title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    title_label.size = (320, 30)
    title_label.center = (view.width / 2, 40)

    angle_label = ui.Label("Pitch: 0.0° | Roll: 0.0°")
    angle_label.font = ui.Font.system_font_of_size(15)
    angle_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    angle_label.text_color = ui.COLOR_SECONDARY_LABEL
    angle_label.size = (320, 30)
    angle_label.center = (view.width / 2, 75)

    # حلقة الميزان الخارجية (الهدف)
    target_circle = ui.View()
    target_circle.size = (200, 200)
    target_circle.corner_radius = 100
    target_circle.background_color = ui.Color(red=0.9, green=0.9, blue=0.95, alpha=0.5)
    target_circle.center = (view.width / 2, 280)

    # فقاعة الميزان المتحركة
    bubble = ui.View()
    bubble.size = (50, 50)
    bubble.corner_radius = 25
    bubble.background_color = ui.COLOR_SYSTEM_BLUE
    bubble.center = (target_circle.width / 2, target_circle.height / 2)
    target_circle.add_subview(bubble)

    view.add_subview(title_label)
    view.add_subview(angle_label)
    view.add_subview(target_circle)

    # متغير للتحكم بإيقاف الحلقة عند إغلاق الشاشة
    is_running = True

    def sensor_loop():
        motion.start_updating()
        time.sleep(0.2)
        center_x = target_circle.width / 2
        center_y = target_circle.height / 2
        max_offset = 75

        while is_running:
            try:
                gravity = motion.get_gravity() or (0, 0, 0)
                gx = gravity[0]
                gy = gravity[1]

                # حساب إزاحة الفقاعة بناء على الجاذبية
                offset_x = -gx * max_offset * 1.5
                offset_y = gy * max_offset * 1.5

                # تقييد المسافة داخل الدائرة
                dist = math.hypot(offset_x, offset_y)
                if dist > max_offset:
                    offset_x = (offset_x / dist) * max_offset
                    offset_y = (offset_y / dist) * max_offset

                bubble.center = (center_x + offset_x, center_y + offset_y)

                # تغيير اللون للأخضر إذا كان متزناً في المنتصف بدقة
                if dist < 8:
                    bubble.background_color = ui.COLOR_SYSTEM_GREEN
                else:
                    bubble.background_color = ui.COLOR_SYSTEM_BLUE

                pitch = gy * 90
                roll = -gx * 90
                angle_label.text = f"Pitch: {pitch:.1f}° | Roll: {roll:.1f}°"

                time.sleep(0.03)  # تحديث بمعدل ~30 إطار في الثانية
            except Exception:
                break

        try:
            motion.stop_updating()
        except Exception:
            pass

    # تشغيل خيط قراءة الحساسات المتوازي
    sensor_thread = threading.Thread(target=sensor_loop, daemon=True)
    sensor_thread.start()

    ui.show_view(view, mode=ui.PRESENTATION_MODE_SHEET)

if __name__ == "__main__":
    run_live_sensor_ui()
