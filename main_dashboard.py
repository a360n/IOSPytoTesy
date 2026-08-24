#!/usr/bin/env python3
"""
📱 لوحة التحكم الرئيسية لاختبارات Pyto على الآيفون (Master Test Suite Dashboard)
تتضمن نظام تنظيف تلقائي للذاكرة (Memory & Sensor Garbage Collector) لمنع أي كراش عند التشغيل السريع.
"""

import sys
import os
import time
import gc

MENU_ITEMS = [
    # 1. اختبارات العتاد والأداء
    ("1", "فحص وتشخيص عتاد الجهاز وبيئة بايثون", "01_hardware_benchmark/device_info_diagnostics.py"),
    ("2", "اختبار إجهاد وقوة المعالج وتعدد الأنوية (CPU Stress)", "01_hardware_benchmark/cpu_multi_thread_stress.py"),
    ("3", "اختبار أقصى حد للذاكرة العشوائية (RAM Limits)", "01_hardware_benchmark/ram_limit_test.py"),
    ("4", "اختبار سرعة قراءة وكتابة وحدة التخزين (Disk Speed)", "01_hardware_benchmark/disk_io_benchmark.py"),

    # 2. حساسات وميزات iOS
    ("5", "اختبار الجيروسكوب وزوايا الميل والتسارع (Motion)", "02_ios_sensors_hardware/motion_and_gyroscope.py"),
    ("6", "اختبار الـ GPS الدقيق وعكس العناوين (Location)", "02_ios_sensors_hardware/gps_and_geocoding.py"),
    ("7", "اختبار اهتزازات محرك اللمس والأصوات (Haptics & Sound)", "02_ios_sensors_hardware/haptics_and_sound.py"),
    ("8", "اختبار النطق الصوتي العربي والإنجليزي (Speech TTS)", "02_ios_sensors_hardware/speech_tts_arabic.py"),
    ("9", "اختبار الإشعارات المحلية التفاعلية (Notifications)", "02_ios_sensors_hardware/local_notifications.py"),
    ("10", "اختبار مكتبة الصور والكاميرا (Photos & Camera)", "02_ios_sensors_hardware/camera_and_photos.py"),

    # 3. واجهات المستخدم الرسومية
    ("11", "عرض واجهة مستخدم iOS أصلية بالكامل (Pyto UIKit)", "03_native_ui/pyto_ui_showcase.py"),
    ("12", "ميزان رقمي رسومي حي باستخدام الحساسات (Live Leveler)", "03_native_ui/live_sensor_ui.py"),
    ("13", "لوحة الرسم والألوان التفاعلية (Interactive Canvas)", "03_native_ui/interactive_canvas_drawing.py"),

    # 4. الذكاء الاصطناعي وعلوم البيانات
    ("14", "اختبار معالجة الصور عبر OpenCV (Computer Vision)", "04_ai_machine_learning/cv2_face_and_vision.py"),
    ("15", "تدريب نماذج تعلم الآلة On-Device (Scikit-Learn)", "04_ai_machine_learning/sklearn_ml_training.py"),
    ("16", "الحوسبة العلمية المتقدمة و FFT (NumPy/SciPy)", "04_ai_machine_learning/numpy_scipy_math_engine.py"),
    ("17", "توليد ورسم المخططات البيانية (Matplotlib Plots)", "04_ai_machine_learning/data_visualization_plot.py"),

    # 5. خوادم الويب والشبكات
    ("18", "تشغيل خادم ويب حي على الآيفون (Web Server)", "05_networking_servers/iphone_web_server.py"),
    ("19", "قياس سرعة وزمن استجابة الشبكة (Latency & Ping)", "05_networking_servers/network_speed_and_ping.py"),
    ("20", "جلب بيانات الطقس الحية عبر REST API (JSON Fetch)", "05_networking_servers/api_fetch_weather_sample.py"),

    # 6. الويدجت والاختصارات
    ("21", "معاينة ويدجت الشاشة الرئيسية (Home Widget)", "06_widgets_and_shortcuts/custom_home_widget.py"),
    ("22", "اختبار التكامل مع اختصارات سيري (Shortcuts)", "06_widgets_and_shortcuts/shortcuts_integration.py"),
]

def clear_screen():
    print("\033[H\033[J", end="")

def cleanup_environment():
    """تنظيف فوري للذاكرة وإيقاف أي حساسات أو رسومات معلقة في الخلفية لمنع الكراش"""
    # 1. إيقاف حساسات الحركة
    try:
        import motion
        motion.stop_updating()
    except Exception:
        pass

    # 2. إيقاف الـ GPS
    try:
        import location
        location.stop_updating()
    except Exception:
        pass

    # 3. إغلاق نوافذ Matplotlib البيانية
    try:
        import matplotlib.pyplot as plt
        plt.close('all')
    except Exception:
        pass

    # 4. تحرير الذاكرة العشوائية وتفريغ الكائنات غير المستخدمة
    gc.collect()

def run_script(script_rel_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_full_path = os.path.join(base_dir, script_rel_path)
    
    if not os.path.exists(script_full_path):
        print(f"❌ لم يتم العثور على الملف: {script_full_path}")
        return

    # تنظيف مسبق قبل التشغيل
    cleanup_environment()

    print("\n" + "=" * 65)
    print(f"🚀 جاري تشغيل: {script_rel_path}...")
    print("=" * 65 + "\n")
    
    try:
        with open(script_full_path, "r", encoding="utf-8") as f:
            code = compile(f.read(), script_full_path, 'exec')
            exec(code, {"__name__": "__main__", "__file__": script_full_path})
    except KeyboardInterrupt:
        print("\n⏹️ تم إيقاف التشغيل بواسطة المستخدم.")
    except Exception as e:
        print(f"\n⚠️ تنبيه أثناء تنفيذ السكربت: {e}")
    finally:
        # تنظيف لاحق بعد انتهاء التشغيل
        cleanup_environment()
        time.sleep(0.2)  # مهلة قصيرة لإعطاء نظام iOS فرصة لإغلاق الواجهات بسلاسة

def main():
    while True:
        clear_screen()
        print("=" * 65)
        print("  📱 مركز اختبار قدرات وحدود Pyto على iPhone 17 Pro Max")
        print("=" * 65)
        print("  اختر رقم الاختبار الذي ترغب بتشغيله:")
        print("-" * 65)
        
        current_cat = ""
        for num, title, path in MENU_ITEMS:
            cat = path.split("/")[0].replace("_", " ").title()
            if cat != current_cat:
                current_cat = cat
                print(f"\n📁 [{current_cat}]")
            print(f"   [{num:>2}] {title}")

        print("\n   [ 0] 🚪 خروج (Exit)")
        print("=" * 65)

        try:
            choice = input("👉 أدخل رقم الخيار واضغط Enter: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 وداعاً!")
            break

        if choice == "0" or choice.lower() == "exit" or choice.lower() == "q":
            print("\n👋 وداعاً! نتمنى لك تجربة ممتعة مع بايثون على الآيفون.\n")
            cleanup_environment()
            break

        selected = None
        for num, title, path in MENU_ITEMS:
            if choice == num:
                selected = path
                break

        if selected:
            run_script(selected)
            try:
                input("\n⏎ اضغط Enter للعودة إلى القائمة الرئيسية...")
            except (KeyboardInterrupt, EOFError):
                pass
        else:
            print("⚠️ خيار غير صحيح، الرجاء المحاولة مرة أخرى.")
            time.sleep(1)

if __name__ == "__main__":
    main()
