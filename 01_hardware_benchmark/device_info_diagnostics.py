#!/usr/bin/env python3
"""
🔍 System & Device Diagnostics (Hardware & Environment)
Inspects CPU specifications, architecture, memory, iOS platform info, and installed packages in Pyto.
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
    print_header("System & Hardware Information")
    print(f"📱 OS / Kernel       : {platform.system()} {platform.release()}")
    print(f"🏷️ Platform Platform : {platform.platform()}")
    print(f"⚙️ Architecture      : {platform.machine()} ({sys.byteorder} endian)")
    print(f"🧠 CPU Logical Cores : {os.cpu_count()}")
    
    try:
        import psutil
        mem = psutil.virtual_memory()
        print(f"💾 Total RAM         : {mem.total / (1024**3):.2f} GB")
        print(f"📊 Available RAM     : {mem.available / (1024**3):.2f} GB ({mem.percent}% used)")
    except ImportError:
        print("💾 psutil not installed (RAM capacity is measured via memory benchmark)")

def test_python_environment():
    print_header("Python Environment")
    print(f"🐍 Python Version    : {sys.version.split()[0]} ({sys.version})")
    print(f"📁 Executable Path   : {sys.executable}")
    print(f"📍 Current Directory : {os.getcwd()}")
    print(f"🔤 Default Encoding  : {sys.getdefaultencoding()}")

def test_pyto_modules():
    print_header("Pyto iOS Native APIs Check")
    pyto_modules = [
        ("pyto_ui", "Native UIKit Graphical User Interfaces"),
        ("motion", "Accelerometer & Gyroscope Sensors"),
        ("location", "GPS Coordinates & Geocoding"),
        ("sound", "System Audio & Tone Synthesis"),
        ("speech", "Apple Siri Text-to-Speech Engine"),
        ("notifications", "Local Interactive Push Notifications"),
        ("widgets", "iOS Home & Lock Screen Widgets"),
        ("photo_library", "Photo Library & Camera Integration"),
        ("sharing", "iOS Share Sheet & Document Export"),
        ("pasteboard", "System Clipboard Access"),
        ("background", "Background Tasks & Execution"),
        ("shortcuts", "Apple Shortcuts & Siri Automation"),
        ("mainthread", "UIKit Main Thread Dispatcher"),
        ("pyto_core", "Core Pyto Engine & Runtime"),
    ]

    for mod_name, desc in pyto_modules:
        try:
            __import__(mod_name)
            print(f"  ✅ {mod_name:<16} : Supported ({desc})")
        except ImportError:
            print(f"  ⚠️ {mod_name:<16} : Not available in current environment")

def test_datascience_modules():
    print_header("AI & Data Science Libraries Check")
    ds_modules = [
        ("numpy", "Numerical Array Computations"),
        ("scipy", "Scientific & Linear Algebra Routines"),
        ("pandas", "Data Structures & Analysis"),
        ("matplotlib", "Data Visualization & Plotting"),
        ("cv2", "OpenCV Computer Vision Engine"),
        ("PIL", "Pillow Image Processing"),
        ("sklearn", "Scikit-Learn Machine Learning Models"),
        ("requests", "Synchronous HTTP Networking"),
        ("httpx", "Modern Async HTTP Client"),
        ("sqlite3", "Local SQLite Database Engine"),
    ]

    for mod_name, desc in ds_modules:
        try:
            mod = __import__(mod_name)
            ver = getattr(mod, "__version__", "Available")
            print(f"  ✅ {mod_name:<14} : Version {ver} ({desc})")
        except ImportError:
            print(f"  ❌ {mod_name:<14} : Not installed ({desc})")

if __name__ == "__main__":
    print("\n🚀 Starting comprehensive iPhone & Pyto diagnostic scan...\n")
    test_system_info()
    test_python_environment()
    test_pyto_modules()
    test_datascience_modules()
    print("\n✨ Diagnostic scan completed successfully!\n")
