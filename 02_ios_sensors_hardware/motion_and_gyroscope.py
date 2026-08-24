#!/usr/bin/env python3
"""
📱 اختبار حساسات الحركة والجيروسكوب (Motion & Gyroscope Test)
يقوم هذا السكربت بالاتصال المباشر بحساسات التسارع، الجيروسكوب، والجاذبية في الآيفون،
وقراءة زوايا الميل (Roll, Pitch, Yaw) وتسارع حركة الجهاز بالزمن الحقيقي (Real-Time).
"""

import time
import math

def format_bar(value, min_val=-1.0, max_val=1.0, length=20):
    """توليد شريط بصري متحرك لقيمة الحساس"""
    norm = (value - min_val) / (max_val - min_val)
    norm = max(0.0, min(1.0, norm))
    pos = int(norm * length)
    bar = ["-"] * length
    if 0 <= pos < length:
        bar[pos] = "●"
    return "[" + "".join(bar) + "]"

def test_motion_sensors(duration_seconds=15):
    print("=" * 60)
    print("  🧭 اختبار حساسات الحركة والجيروسكوب (Motion Sensors)")
    print("=" * 60)

    try:
        import motion
    except ImportError:
        print("❌ مكتبة 'motion' غير متوفرة خارج بيئة تطبيق Pyto على نظام iOS.")
        print("💡 لتجربة هذا الكود، قم بتشغيله مباشرة داخل تطبيق Pyto على الآيفون.")
        return

    print("🚀 بدء تفعيل الحساسات (Motion Tracking)...")
    print(f"⏳ سيتم عرض القراءات الحية لمدة {duration_seconds} ثانية. حرك جهاز الآيفون الآن!\n")
    
    try:
        motion.start_updating()
        time.sleep(0.5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            # قراءة التوجيه وزوايا الميل
            attitude = motion.get_attitude() or (0, 0, 0)
            gravity = motion.get_gravity() or (0, 0, 0)
            user_acc = motion.get_user_acceleration() or (0, 0, 0)
            
            # تحويل الراديان إلى درجات
            pitch = math.degrees(attitude[0]) if len(attitude) > 0 else 0
            roll = math.degrees(attitude[1]) if len(attitude) > 1 else 0
            yaw = math.degrees(attitude[2]) if len(attitude) > 2 else 0

            gx, gy, gz = gravity[0] if len(gravity) > 0 else 0, gravity[1] if len(gravity) > 1 else 0, gravity[2] if len(gravity) > 2 else 0

            print("\033[H\033[J", end="")  # مسح الشاشة لتحديث حي
            print("=" * 60)
            print("  📱 قراءات الحساسات المباشرة (Live iPhone Sensors)")
            print("=" * 60)
            print(f"📐 زوايا الجهاز (Attitude Degrees):")
            print(f"   • Pitch (الميل للأمام/الخلف) : {pitch:>7.1f}° {format_bar(pitch, -90, 90)}")
            print(f"   • Roll  (الميل لليمين/اليسار) : {roll:>7.1f}° {format_bar(roll, -90, 90)}")
            print(f"   • Yaw   (البوصلة/الدوران)    : {yaw:>7.1f}° {format_bar(yaw, -180, 180)}")
            print("\n🌍 متجه الجاذبية (Gravity Vector G):")
            print(f"   • X: {gx:>6.2f} G  | Y: {gy:>6.2f} G  | Z: {gz:>6.2f} G")
            print(f"\n⚡ تسارع حركة المستخدم (User Acceleration):")
            print(f"   • X: {user_acc[0]:>6.2f} | Y: {user_acc[1]:>6.2f} | Z: {user_acc[2]:>6.2f}")
            print("\n" + "-" * 60)
            print("⏳ اضغط إيقاف أو انتظر انتهاء مدة الاختبار...")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n⏹️ تم إيقاف الاختبار يدوياً.")
    except Exception as e:
        print(f"\n⚠️ خطأ أثناء قراءة الحساسات: {e}")
    finally:
        try:
            motion.stop_updating()
        except Exception:
            pass
        print("\n✅ تم إيقاف تحديث الحساسات بنجاح.")

if __name__ == "__main__":
    test_motion_sensors()
