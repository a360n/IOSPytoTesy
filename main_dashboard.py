#!/usr/bin/env python3
"""
📱 Master Test Suite Dashboard (Pyto on iPhone 17 Pro Max)
Interactive launcher equipped with automatic garbage collection and background cleanup.
"""

import sys
import os
import time
import gc

MENU_ITEMS = [
    # 1. Hardware & Limits Benchmark
    ("1", "Device Diagnostics & Python Environment", "01_hardware_benchmark/device_info_diagnostics.py"),
    ("2", "CPU & Multi-Threading Stress Test (GFLOPS)", "01_hardware_benchmark/cpu_multi_thread_stress.py"),
    ("3", "RAM Allocation Limits & Stress Test", "01_hardware_benchmark/ram_limit_test.py"),
    ("4", "Storage NVMe Read & Write Speed (MB/s)", "01_hardware_benchmark/disk_io_benchmark.py"),

    # 2. iOS Hardware Sensors
    ("5", "Motion, Gyroscope & Attitude Tracking", "02_ios_sensors_hardware/motion_and_gyroscope.py"),
    ("6", "GPS Location, Speed & Reverse Geocoding", "02_ios_sensors_hardware/gps_and_geocoding.py"),
    ("7", "Taptic Engine Haptic Feedback & Audio", "02_ios_sensors_hardware/haptics_and_sound.py"),
    ("8", "Siri Speech Synthesis & TTS", "02_ios_sensors_hardware/speech_tts_arabic.py"),
    ("9", "Local Interactive Push Notifications", "02_ios_sensors_hardware/local_notifications.py"),
    ("10", "Photo Library & Camera Interface", "02_ios_sensors_hardware/camera_and_photos.py"),

    # 3. Native Graphical User Interfaces
    ("11", "Native iOS UIKit Interface Showcase", "03_native_ui/pyto_ui_showcase.py"),
    ("12", "Live Animated Inclinometer Leveler (60 FPS)", "03_native_ui/live_sensor_ui.py"),
    ("13", "Interactive Touch & Color Palette Canvas", "03_native_ui/interactive_canvas_drawing.py"),

    # 4. AI & Data Science
    ("14", "OpenCV Computer Vision & Image Pipeline", "04_ai_machine_learning/cv2_face_and_vision.py"),
    ("15", "On-Device Scikit-Learn Model Training", "04_ai_machine_learning/sklearn_ml_training.py"),
    ("16", "Scientific Computing & 1M-pt FFT (NumPy/SciPy)", "04_ai_machine_learning/numpy_scipy_math_engine.py"),
    ("17", "High-DPI Data Visualization Plots (Matplotlib)", "04_ai_machine_learning/data_visualization_plot.py"),

    # 5. Local Web Servers & Networking
    ("18", "iPhone Hosted Web Server & Control Center", "05_networking_servers/iphone_web_server.py"),
    ("19", "Network Latency Ping & Download Throughput", "05_networking_servers/network_speed_and_ping.py"),
    ("20", "Live REST API Fetch & JSON Parsing", "05_networking_servers/api_fetch_weather_sample.py"),

    # 6. Widgets & Automations
    ("21", "Custom Home & Lock Screen Widget", "06_widgets_and_shortcuts/custom_home_widget.py"),
    ("22", "Apple Shortcuts & Siri Automation", "06_widgets_and_shortcuts/shortcuts_integration.py"),
]

def clear_screen():
    print("\033[H\033[J", end="")

def cleanup_environment():
    """Flushes RAM and stops all active sensor streams to ensure stability across runs."""
    try:
        import motion
        motion.stop_updating()
    except Exception:
        pass

    try:
        import location
        location.stop_updating()
    except Exception:
        pass

    try:
        import matplotlib.pyplot as plt
        plt.close('all')
    except Exception:
        pass

    gc.collect()

def run_script(script_rel_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_full_path = os.path.join(base_dir, script_rel_path)
    
    if not os.path.exists(script_full_path):
        print(f"❌ File not found: {script_full_path}")
        return

    cleanup_environment()

    print("\n" + "=" * 65)
    print(f"🚀 Running: {script_rel_path}...")
    print("=" * 65 + "\n")
    
    try:
        with open(script_full_path, "r", encoding="utf-8") as f:
            code = compile(f.read(), script_full_path, 'exec')
            exec(code, {"__name__": "__main__", "__file__": script_full_path})
    except KeyboardInterrupt:
        print("\n⏹️ Execution interrupted by user.")
    except Exception as e:
        print(f"\n⚠️ Note during execution: {e}")
    finally:
        cleanup_environment()
        time.sleep(0.2)

def main():
    while True:
        clear_screen()
        print("=" * 65)
        print("  📱 iPhone 17 Pro Max Pyto Test Suite & Hardware Limits")
        print("=" * 65)
        print("  Select a test number to execute:")
        print("-" * 65)
        
        current_cat = ""
        for num, title, path in MENU_ITEMS:
            cat = path.split("/")[0].replace("_", " ").title()
            if cat != current_cat:
                current_cat = cat
                print(f"\n📁 [{current_cat}]")
            print(f"   [{num:>2}] {title}")

        print("\n   [ 0] 🚪 Exit")
        print("=" * 65)

        try:
            choice = input("👉 Enter option number and press Enter: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            break

        if choice == "0" or choice.lower() == "exit" or choice.lower() == "q":
            print("\n👋 Goodbye! Enjoy developing with Python on iOS.\n")
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
                input("\n⏎ Press Enter to return to main menu...")
            except (KeyboardInterrupt, EOFError):
                pass
        else:
            print("⚠️ Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
