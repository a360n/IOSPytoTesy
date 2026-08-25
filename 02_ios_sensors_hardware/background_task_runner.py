#!/usr/bin/env python3
"""
⚡ iOS Background Tasks & Long-Running Services (Pyto Background API)
Demonstrates running continuous background tasks on iOS (e.g. computations, sensor telemetry, audio services)
even when switching apps or locking the screen.
"""

import time
import sys

def run_background_task(duration_seconds=20):
    print("=" * 60)
    print("  ⚡ iOS Long-Running Background Task")
    print("=" * 60)

    try:
        import background
    except ImportError:
        print("❌ 'background' module is only available in Pyto on iOS.")
        return

    print("🚀 Requesting iOS Background Execution Mode...")
    try:
        # Request long-running background capability
        background.start_background_task()
        print("✅ Background Mode Activated! (Pyto will remain running in background)")
        print(f"⏳ Now lock your phone or switch to any other app for {duration_seconds} seconds...\n")

        start_time = time.time()
        count = 0

        while (time.time() - start_time) < duration_seconds:
            count += 1
            elapsed = time.time() - start_time
            print(f"   ⏱️ Running in background... {elapsed:>4.1f}s / {duration_seconds}s (Heartbeat #{count})")
            
            # Send periodic haptic or notification when allowed
            time.sleep(2.0)

        print("\n✨ Background task finished its cycle successfully!")

    except Exception as e:
        print(f"⚠️ Error running background task: {e}")
    finally:
        try:
            background.stop_background_task()
            print("🛑 Background task execution token released.")
        except Exception:
            pass

if __name__ == "__main__":
    run_background_task()
