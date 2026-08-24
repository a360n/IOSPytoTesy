#!/usr/bin/env python3
"""
🔍 فحص وتشخيص النظام والبيئة البرمجية (Device Info & Diagnostics)
يقوم هذا السكربت بفحص مواصفات المعالج، الذاكرة، نظام iOS، وإصدار بايثون والمكتبات المثبتة في Pyto.
"""

import sys
import os
import platform
import time
import multiprocessing

def print_header(title):
    print("=" * 60)
    print(f"  📌 {title}")
    print("=" * 60)

def test_system_info():
    print_header("معلومات النظام والعتاد (System & Hardware)")
    print(f"📱 نظام التشغيل: {platform.system()} {platform.release()}")
    print(f"🏷️ إصدار المنصة (Platform): {platform.platform()}")
    print(f"⚙️ المعمارية (Architecture): {platform.machine()} ({sys.byteorder} endian)")
    print(f"🧠 عدد أنوية المعالج (CPU Cores): {os.cpu_count()} أصلية / خيوط")
    
    # محاولة فحص الذاكرة إن أمكن
    try:
        import psutil
        mem = psutil.virtual_memory()
        print(f"💾 إجمالي الرام (RAM): {mem.total / (1024**3):.2f} GB")
        print(f"📊 الرام المتاح حالياً: {mem.available / (1024**3):.2f} GB ({mem.percent}% مستخدم)")
    except ImportError:
        print("💾 مكتبة psutil غير مثبتة (يتم قياس الرام عبر اختبار الذاكرة المخصص)")

def test_python_environment():
    print_header("بيئة بايثون (Python Environment)")
    print(f"🐍 إصدار بايثون: {sys.version.split()[0]} ({sys.version})")
    print(f"📁 مسار التنفيذ: {sys.executable}")
    print(f"📍 المسار الحالي: {os.getcwd()}")
    print(f"🔤 الترميز الافتراضي: {sys.getdefaultencoding()}")

def test_pyto_modules():
    print_header("فحص مكتبات Pyto الخاصة بـ iOS")
    pyto_modules = [
        ("pyto_ui", "واجهات iOS الأصلية (UIKit UI)"),
        ("motion", "حساسات الحركة والجيروسكوب (Motion & Gyro)"),
        ("location", "الموقع الجغرافي والـ GPS (Location & GPS)"),
        ("sound", "الصوت والنغمات (Audio & Sound)"),
        ("speech", "تحويل النص لكلام سيري (Text-to-Speech)"),
        ("notifications", "الإشعارات المحلية (Local Notifications)"),
        ("widgets", "ويدجت الشاشة الرئيسية (Home Screen Widgets)"),
        ("photo_library", "مكتبة الصور والكاميرا (Photos & Camera)"),
        ("sharing", "مشاركة الملفات ونظام المشاركة (iOS Share Sheet)"),
        ("pasteboard", "الحافظة والنسخ/اللصق (Clipboard)"),
        ("background", "المهام في الخلفية (Background Tasks)"),
        ("shortcuts", "اختصارات سيري (Shortcuts)"),
        ("mainthread", "التحكم في خيط الواجهة الأساسي (Main Thread)"),
        ("pyto_core", "نواة تطبيق بايتو (Pyto Core)")
    ]

    for mod_name, desc in pyto_modules:
        try:
            __import__(mod_name)
            print(f"  ✅ {mod_name:<16} : مدعومة ({desc})")
        except ImportError:
            print(f"  ⚠️ {mod_name:<16} : غير متوفرة حالياً في هذه البيئة")

def test_datascience_modules():
    print_header("فحص مكتبات الذكاء الاصطناعي والعلوم (AI & Data Science)")
    ds_modules = [
        ("numpy", "العمليات الرياضية والمصفوفات"),
        ("scipy", "الحوسبة العلمية المتقدمة"),
        ("pandas", "معالجة وتحليل البيانات"),
        ("matplotlib", "رسم المخططات البيانية"),
        ("cv2", "مكتبة الرؤية الحاسوبية OpenCV"),
        ("PIL", "معالجة الصور Pillow"),
        ("sklearn", "تعلم الآلة Scikit-Learn"),
        ("requests", "طلبات الشبكة HTTP"),
        ("httpx", "طلبات الشبكة الحديثة Async"),
        ("sqlite3", "قواعد البيانات المحلية SQLite")
    ]

    for mod_name, desc in ds_modules:
        try:
            mod = __import__(mod_name)
            ver = getattr(mod, "__version__", "متوفرة")
            print(f"  ✅ {mod_name:<14} : إصدار {ver} ({desc})")
        except ImportError:
            print(f"  ❌ {mod_name:<14} : غير مثبتة ({desc})")

if __name__ == "__main__":
    print("\n🚀 بدء تشخيص شامل لجهاز الآيفون وتطبيق Pyto...\n")
    test_system_info()
    test_python_environment()
    test_pyto_modules()
    test_datascience_modules()
    print("\n✨ اكتمل الفحص التشخيصي بنجاح!\n")
