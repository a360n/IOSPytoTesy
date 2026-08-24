#!/usr/bin/env python3
"""
📱 Motion & Gyroscope Sensors Monitor
Reads real-time device attitude (Pitch, Roll, Yaw), gravity vectors,
and user acceleration from iPhone hardware sensors.
"""

import time
import math

def format_bar(value, min_val=-1.0, max_val=1.0, length=20):
    """Generates visual ascii bar for sensor values"""
    norm = (value - min_val) / (max_val - min_val)
    norm = max(0.0, min(1.0, norm))
    pos = int(norm * length)
    bar = ["-"] * length
    if 0 <= pos < length:
        bar[pos] = "●"
    return "[" + "".join(bar) + "]"

def test_motion_sensors(duration_seconds=15):
    print("=" * 60)
    print("  🧭 Motion Sensors & Gyroscope Monitor")
    print("=" * 60)

    try:
        import motion
    except ImportError:
        print("❌ The 'motion' module is only available inside Pyto on iOS.")
        print("💡 Run this script inside the Pyto app on your iPhone.")
        return

    print("🚀 Initializing motion tracking...")
    print(f"⏳ Displaying live readings for {duration_seconds} seconds. Tilt your iPhone!\n")
    
    try:
        motion.start_updating()
        time.sleep(0.5)

        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            attitude = motion.get_attitude() or (0, 0, 0)
            gravity = motion.get_gravity() or (0, 0, 0)
            user_acc = motion.get_user_acceleration() or (0, 0, 0)
            
            pitch = math.degrees(attitude[0]) if len(attitude) > 0 else 0
            roll = math.degrees(attitude[1]) if len(attitude) > 1 else 0
            yaw = math.degrees(attitude[2]) if len(attitude) > 2 else 0

            gx = gravity[0] if len(gravity) > 0 else 0
            gy = gravity[1] if len(gravity) > 1 else 0
            gz = gravity[2] if len(gravity) > 2 else 0

            print("\033[H\033[J", end="")  # Clear screen for live stream
            print("=" * 60)
            print("  📱 Live iPhone Sensor Stream")
            print("=" * 60)
            print("📐 Device Attitude (Degrees):")
            print(f"   • Pitch (Front/Back) : {pitch:>7.1f}° {format_bar(pitch, -90, 90)}")
            print(f"   • Roll  (Left/Right) : {roll:>7.1f}° {format_bar(roll, -90, 90)}")
            print(f"   • Yaw   (Heading)    : {yaw:>7.1f}° {format_bar(yaw, -180, 180)}")
            print("\n🌍 Gravity Vector (G):")
            print(f"   • X: {gx:>6.2f} G  | Y: {gy:>6.2f} G  | Z: {gz:>6.2f} G")
            print("\n⚡ User Acceleration:")
            print(f"   • X: {user_acc[0]:>6.2f} | Y: {user_acc[1]:>6.2f} | Z: {user_acc[2]:>6.2f}")
            print("\n" + "-" * 60)
            print("⏳ Press stop or wait for timer to finish...")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n⏹️ Test stopped manually.")
    except Exception as e:
        print(f"\n⚠️ Sensor reading error: {e}")
    finally:
        try:
            motion.stop_updating()
        except Exception:
            pass
        print("\n✅ Motion tracking stopped cleanly.")

if __name__ == "__main__":
    test_motion_sensors()
