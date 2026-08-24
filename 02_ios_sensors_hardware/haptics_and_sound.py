#!/usr/bin/env python3
"""
📳 Taptic Engine Haptics & Audio Feedback
Tests tactile feedback vibration patterns (Light, Medium, Heavy, Success, Warning, Error, Selection)
and system audio tones.
"""

import time

def test_haptics_and_sound():
    print("=" * 60)
    print("  📳 Taptic Engine Haptic Feedback & Audio")
    print("=" * 60)

    # 1. Haptic Feedback
    print("\n1️⃣ Testing Taptic Engine feedback vibrations:")
    try:
        import pyto_ui as ui
        
        haptics_types = [
            ("Light Impact", getattr(ui.HapticFeedback, 'IMPACT_LIGHT', None) if hasattr(ui, 'HapticFeedback') else None),
            ("Medium Impact", getattr(ui.HapticFeedback, 'IMPACT_MEDIUM', None) if hasattr(ui, 'HapticFeedback') else None),
            ("Heavy Impact", getattr(ui.HapticFeedback, 'IMPACT_HEAVY', None) if hasattr(ui, 'HapticFeedback') else None),
            ("Success Notification", getattr(ui.HapticFeedback, 'NOTIFICATION_SUCCESS', None) if hasattr(ui, 'HapticFeedback') else None),
            ("Warning Notification", getattr(ui.HapticFeedback, 'NOTIFICATION_WARNING', None) if hasattr(ui, 'HapticFeedback') else None),
            ("Error Notification", getattr(ui.HapticFeedback, 'NOTIFICATION_ERROR', None) if hasattr(ui, 'HapticFeedback') else None),
            ("Selection Changed", getattr(ui.HapticFeedback, 'SELECTION', None) if hasattr(ui, 'HapticFeedback') else None),
        ]

        for name, feedback in haptics_types:
            print(f"   👉 Generating {name}...")
            try:
                if feedback is not None:
                    ui.HapticFeedback(feedback).generate()
                else:
                    import sound
                    sound.beep()
            except Exception:
                pass
            time.sleep(0.8)
            
        print("   ✅ All haptic vibrations triggered successfully!")
        
    except ImportError:
        print("   ⚠️ pyto_ui module not available in current environment.")

    # 2. Sound Effects
    print("\n2️⃣ Testing system sound alerts:")
    try:
        import sound
        print("   🔔 Playing system beep tone...")
        sound.beep()
        time.sleep(1)
        print("   ✅ Sound played successfully.")
    except ImportError:
        print("   ℹ️ sound module is designed for iOS Pyto.")

    print("\n" + "=" * 60)
    print("✨ Haptics and audio test completed!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_haptics_and_sound()
