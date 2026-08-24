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
    try:
        view.background_color = ui.COLOR_SYSTEM_BACKGROUND
    except Exception:
        pass
    view.title = "🧭 ميزان الميل الرقمي التفاعلي"

    # عنوان الشاشة
    title_label = ui.Label()
    title_label.text = "حرك هاتفك لمشاهدة تفاعل الفقاعة"
    try:
        title_label.font = ui.Font.bold_system_font_of_size(18)
        title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    title_label.size = (320, 30)
    title_label.center = (view.width / 2, 40)

    # ملصق الزوايا
    angle_label = ui.Label()
    angle_label.text = "Pitch: 0.0° | Roll: 0.0°"
    try:
        angle_label.font = ui.Font.system_font_of_size(15)
        angle_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
        angle_label.text_color = ui.COLOR_SECONDARY_LABEL
    except Exception:
        pass
    angle_label.size = (320, 30)
    angle_label.center = (view.width / 2, 75)

    # حلقة الميزان الخارجية (الهدف)
    target_circle = ui.View()
    target_circle.size = (220, 220)
    target_circle.corner_radius = 110
    try:
        target_circle.background_color = ui.COLOR_SYSTEM_GRAY5
    except Exception:
        try:
            target_circle.background_color = ui.Color(0.85, 0.85, 0.9, 0.5)
        except Exception:
            pass
    target_circle.center = (view.width / 2, 280)

    # خطوط المحور (الهدف المتعامد في المركز)
    h_line = ui.View()
    h_line.size = (200, 2)
    h_line.center = (target_circle.width / 2, target_circle.height / 2)
    try:
        h_line.background_color = ui.COLOR_SYSTEM_GRAY3
    except Exception:
        pass
    target_circle.add_subview(h_line)

    v_line = ui.View()
    v_line.size = (2, 200)
    v_line.center = (target_circle.width / 2, target_circle.height / 2)
    try:
        v_line.background_color = ui.COLOR_SYSTEM_GRAY3
    except Exception:
        pass
    target_circle.add_subview(v_line)

    # فقاعة الميزان المتحركة
    bubble = ui.View()
    bubble.size = (54, 54)
    bubble.corner_radius = 27
    try:
        bubble.background_color = ui.COLOR_SYSTEM_BLUE
    except Exception:
        pass
    bubble.center = (target_circle.width / 2, target_circle.height / 2)
    target_circle.add_subview(bubble)

    view.add_subview(title_label)
    view.add_subview(angle_label)
    view.add_subview(target_circle)

    # متغير للتحكم بالحلقة عند إغلاق الشاشة
    is_running = True

    def sensor_loop():
        try:
            motion.start_updating()
        except Exception:
            return
        time.sleep(0.2)
        center_x = target_circle.width / 2
        center_y = target_circle.height / 2
        max_offset = 80

        while is_running:
            try:
                gravity = motion.get_gravity() or (0, 0, 0)
                gx = gravity[0]
                gy = gravity[1]

                # حساب إزاحة الفقاعة بناء على الجاذبية
                offset_x = -gx * max_offset * 1.6
                offset_y = gy * max_offset * 1.6

                # تقييد المسافة داخل الدائرة
                dist = math.hypot(offset_x, offset_y)
                if dist > max_offset:
                    offset_x = (offset_x / dist) * max_offset
                    offset_y = (offset_y / dist) * max_offset

                bubble.center = (center_x + offset_x, center_y + offset_y)

                # تغيير اللون للأخضر عند الوصول لنقطة الاتزان
                if dist < 8:
                    try:
                        bubble.background_color = ui.COLOR_SYSTEM_GREEN
                    except Exception:
                        pass
                else:
                    try:
                        bubble.background_color = ui.COLOR_SYSTEM_BLUE
                    except Exception:
                        pass

                pitch = gy * 90
                roll = -gx * 90
                angle_label.text = f"Pitch: {pitch:>4.1f}° | Roll: {roll:>4.1f}°"

                time.sleep(0.03)  # تحديث سلس 30 FPS
            except Exception:
                break

        try:
            motion.stop_updating()
        except Exception:
            pass

    # تشغيل خيط قراءة الحساسات
    sensor_thread = threading.Thread(target=sensor_loop, daemon=True)
    sensor_thread.start()

    ui.show_view(view, mode=ui.PRESENTATION_MODE_SHEET)

if __name__ == "__main__":
    run_live_sensor_ui()
