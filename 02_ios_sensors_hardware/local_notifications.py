#!/usr/bin/env python3
"""
🔔 Local Push Notifications Benchmark
Schedules immediate and delayed interactive iOS local push notifications
with custom titles, messages, sounds, and payloads.
"""

import time

def test_local_notifications():
    print("=" * 60)
    print("  🔔 Local Push Notifications")
    print("=" * 60)

    try:
        import notifications
    except ImportError:
        print("❌ The 'notifications' module is only available in Pyto on iOS.")
        print("💡 Run this script inside the Pyto app on your iPhone.")
        return

    print("\n1️⃣ Sending immediate notification...")
    try:
        notif = notifications.Notification()
        notif.title = "🚀 Pyto on iPhone 17 Pro Max"
        notif.message = "Hello! Python is running successfully natively on iOS."
        notifications.send_notification(notif)
        print("   ✅ Immediate notification sent successfully!")
    except Exception as e:
        print(f"   ⚠️ Could not send immediate notification: {e}")

    print("\n2️⃣ Scheduling notification in 5 seconds...")
    try:
        notif2 = notifications.Notification()
        notif2.title = "⏰ Python Scheduled Reminder"
        notif2.message = "5 seconds have elapsed! Background notification received."
        if hasattr(notifications, 'schedule_notification'):
            notifications.schedule_notification(notif2, delay=5)
            print("   ✅ Notification scheduled for 5 seconds from now.")
            print("   💡 You can lock your screen or switch apps to test delivery!")
        else:
            notifications.send_notification(notif2)
    except Exception as e:
        print(f"   ⚠️ Could not schedule notification: {e}")

    print("\n" + "=" * 60)
    print("✨ Notifications test completed!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_local_notifications()
