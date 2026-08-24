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
    view.title = "🧭 ميزان الميل الرقمي التفاعلي"

    # عنوان الشاشة
    title_label = ui.Label()
    title_label.text = "حرك هاتفك لمشاهدة تفاعل الفقاعة"
    try:
        title_label.font = ui.Font.bold_system_font_of_size(18)
        if hasattr(ui, 'TextAlignment'):
            title_label.text_alignment = ui.TextAlignment.CENTER
        elif hasattr(ui, 'TEXT_ALIGNMENT_CENTER'):
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
        sec_color = get_system_color('SECONDARY_LABEL', 'COLOR_SECONDARY_LABEL')
        if sec_color is not None:
            angle_label.text_color = sec_color
        if hasattr(ui, 'TextAlignment'):
            angle_label.text_alignment = ui.TextAlignment.CENTER
        elif hasattr(ui, 'TEXT_ALIGNMENT_CENTER'):
            angle_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    angle_label.size = (320, 30)
    angle_label.center = (view.width / 2, 75)

    # حلقة الميزان الخارجية (الهدف)
    target_circle = ui.View()
    target_circle.size = (220, 220)
    target_circle.corner_radius = 110
    gray5 = get_system_color('SYSTEM_GRAY5', 'COLOR_SYSTEM_GRAY5')
    if gray5 is not None:
        target_circle.background_color = gray5
    target_circle.center = (view.width / 2, 280)

    # خطوط المحور (الهدف المتعامد في المركز)
    gray3 = get_system_color('SYSTEM_GRAY3', 'COLOR_SYSTEM_GRAY3')
    h_line = ui.View()
    h_line.size = (200, 2)
    h_line.center = (target_circle.width / 2, target_circle.height / 2)
    if gray3 is not None:
        h_line.background_color = gray3
    target_circle.add_subview(h_line)

    v_line = ui.View()
    v_line.size = (2, 200)
    v_line.center = (target_circle.width / 2, target_circle.height / 2)
    if gray3 is not None:
        v_line.background_color = gray3
    target_circle.add_subview(v_line)

    # فقاعة الميزان المتحركة
    bubble = ui.View()
    bubble.size = (54, 54)
    bubble.corner_radius = 27
    blue_col = get_system_color('SYSTEM_BLUE', 'COLOR_SYSTEM_BLUE')
    green_col = get_system_color('SYSTEM_GREEN', 'COLOR_SYSTEM_GREEN')
    if blue_col is not None:
        bubble.background_color = blue_col
    bubble.center = (target_circle.width / 2, target_circle.height / 2)
    target_circle.add_subview(bubble)

    view.add_subview(title_label)
    view.add_subview(angle_label)
    view.add_subview(target_circle)

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

                dist = math.hypot(offset_x, offset_y)
                if dist > max_offset:
                    offset_x = (offset_x / dist) * max_offset
                    offset_y = (offset_y / dist) * max_offset

                bubble.center = (center_x + offset_x, center_y + offset_y)

                # تغيير اللون للأخضر عند الوصول لنقطة الاتزان
                if dist < 8:
                    if green_col is not None:
                        bubble.background_color = green_col
                else:
                    if blue_col is not None:
                        bubble.background_color = blue_col

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

    sensor_thread = threading.Thread(target=sensor_loop, daemon=True)
    sensor_thread.start()

    mode = getattr(ui.PresentationMode, 'SHEET', None) if hasattr(ui, 'PresentationMode') else getattr(ui, 'PRESENTATION_MODE_SHEET', 0)
    if mode is not None:
        ui.show_view(view, mode=mode)
    else:
        ui.show_view(view)

if __name__ == "__main__":
    run_live_sensor_ui()
