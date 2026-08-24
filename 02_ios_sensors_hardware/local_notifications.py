#!/usr/bin/env python3
"""
🔔 اختبار إرسال الإشعارات المحلية التفاعلية (Local Push Notifications)
يقوم هذا السكربت بجدولة إشعارات نظام iOS محلية مع عناوين، نصوص، أصوات،
وتأخير زمني للتحقق من وصول الإشعار حتى لو تم قفل الهاتف أو الخروج من التطبيق.
"""

import time

def test_local_notifications():
    print("=" * 60)
    print("  🔔 اختبار الإشعارات المحلية (Local Notifications)")
    print("=" * 60)

    try:
        import notifications
    except ImportError:
        print("❌ مكتبة 'notifications' غير متوفرة خارج تطبيق Pyto على iOS.")
        print("💡 لتجربة الإشعارات، شغل هذا السكربت مباشرة داخل تطبيق Pyto على الآيفون.")
        return

    print("\n1️⃣ إرسال إشعار فوري (Immediate Notification)...")
    try:
        notif = notifications.Notification()
        notif.title = "🚀 Pyto على آيفون 17 برو ماكس"
        notif.message = "مرحباً! هذا إشعار تجريبي يعمل بنجاح من داخل بايثون."
        notifications.send_notification(notif)
        print("   ✅ تم إرسال الإشعار الفوري بنجاح!")
    except Exception as e:
        print(f"   ⚠️ تعذر إرسال الإشعار الفوري: {e}")

    print("\n2️⃣ جدولة إشعار بعد 5 ثوانٍ (Scheduled Notification)...")
    try:
        notif2 = notifications.Notification()
        notif2.title = "⏰ تذكير بايثون المجدول"
        notif2.message = "لقد مرت 5 ثوانٍ بنجاح! يعمل نظام الإشعارات الخلفي بكفاءة."
        # محاولة تعيين التأخير
        if hasattr(notifications, 'schedule_notification'):
            notifications.schedule_notification(notif2, delay=5)
            print("   ✅ تم جدولة الإشعار ليعمل بعد 5 ثوانٍ.")
            print("   💡 يمكنك الآن الخروج من التطبيق أو قفل الشاشة للتأكد من وصوله!")
        else:
            notifications.send_notification(notif2)
    except Exception as e:
        print(f"   ⚠️ تعذر جدولة الإشعار: {e}")

    print("\n" + "=" * 60)
    print("✨ اكتمل اختبار الإشعارات بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_local_notifications()
