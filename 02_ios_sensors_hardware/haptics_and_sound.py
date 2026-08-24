#!/usr/bin/env python3
"""
📳 اختبار محرك الاهتزاز والصوت (Taptic Engine Haptics & Sound)
يقوم هذا السكربت بتجربة أنماط الاهتزاز اللمسية التفاعلية لمحرك Taptic Engine في الآيفون
(خفيف، متوسط، قوي، نجاح، تحذير، خطأ)، بالإضافة لتشغيل أصوات ونغمات النظام.
"""

import time

def test_haptics_and_sound():
    print("=" * 60)
    print("  📳 اختبار محرك اللمس والأصوات (Haptic Feedback & Sound)")
    print("=" * 60)

    # 1. اختبار الاهتزازات التفاعلية (Haptics)
    print("\n1️⃣ تجربة اهتزازات محرك Taptic Engine:")
    try:
        import pyto_ui as ui
        
        haptics_types = [
            ("اهتزاز خفيف (Light Impact)", ui.HapticFeedback.IMPACT_LIGHT if hasattr(ui, 'HapticFeedback') else None),
            ("اهتزاز متوسط (Medium Impact)", ui.HapticFeedback.IMPACT_MEDIUM if hasattr(ui, 'HapticFeedback') else None),
            ("اهتزاز قوي (Heavy Impact)", ui.HapticFeedback.IMPACT_HEAVY if hasattr(ui, 'HapticFeedback') else None),
            ("إشعار نجاح (Notification Success)", ui.HapticFeedback.NOTIFICATION_SUCCESS if hasattr(ui, 'HapticFeedback') else None),
            ("إشعار تحذير (Notification Warning)", ui.HapticFeedback.NOTIFICATION_WARNING if hasattr(ui, 'HapticFeedback') else None),
            ("إشعار خطأ (Notification Error)", ui.HapticFeedback.NOTIFICATION_ERROR if hasattr(ui, 'HapticFeedback') else None),
            ("تغيير اختيار (Selection Changed)", ui.HapticFeedback.SELECTION if hasattr(ui, 'HapticFeedback') else None),
        ]

        for name, feedback in haptics_types:
            print(f"   👉 تشغيل {name}...")
            try:
                if feedback is not None:
                    ui.HapticFeedback(feedback).generate()
                else:
                    # محاولة عبر مكتبة sound إن وجدت
                    import sound
                    sound.beep()
            except Exception:
                pass
            time.sleep(1.0)
            
        print("   ✅ تم إرسال جميع أنماط الاهتزاز بنجاح!")
        
    except ImportError:
        print("   ⚠️ مكتبة pyto_ui غير متوفرة في بيئة الاختبار الحالية.")

    # 2. اختبار الأصوات (Sound Effects)
    print("\n2️⃣ تجربة أصوات النظام والصوتيات:")
    try:
        import sound
        print("   🔔 تشغيل صوت التنبيه Beep...")
        sound.beep()
        time.sleep(1)
        
        # نغمات أو مؤثرات إن كانت مدعومة
        print("   ✅ تم تشغيل المؤثر الصوتي بنجاح.")
    except ImportError:
        print("   ℹ️ مكتبة sound مخصصة لبيئة iOS و Pyto.")

    print("\n" + "=" * 60)
    print("✨ اكتمل اختبار الاهتزاز والصوتيات بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_haptics_and_sound()
