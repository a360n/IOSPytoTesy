# 📱 iPhone Pyto Test Suite & Hardware Limits (IOSPytoTesy)

A comprehensive, modular testing and benchmarking suite designed to push the **hardware and software limits of Python on iOS** (**iPhone 17 Pro Max**) using the **Pyto** IDE, unlocking the full power of Apple Silicon compute, CoreMotion sensors, Neural Engine, native UIKit interfaces, on-device AI, and system automations.

---

## 🚀 Quick Start Guide

### 1. Synchronize Updates to iPhone
Inside the **Pyto** app on your iPhone:
1. Open the existing root script: `pull_repo.py`.
2. Tap the **Play ▶️ (Run)** button.
3. The script will pull the latest release archive from GitHub and extract it into `./IOSPytoTesy/`.

### 2. Launch the Master Interactive Dashboard
1. Open the `IOSPytoTesy` folder in Pyto.
2. Run `main_dashboard.py`.
3. An interactive numerical menu `[1 - 22]` will appear. Type any test number and press **Enter**!

---

## 📂 Catalog of Modules & Benchmarks

### 1️⃣ Hardware Compute & Memory Benchmarks (`01_hardware_benchmark/`)
* **`device_info_diagnostics.py`**: Full inspection of CPU cores, architecture, memory state, and installed Pyto/C-extensions.
* **`cpu_multi_thread_stress.py`**: Single-core and multi-threaded integer/float compute stress test, measuring matrix dot-product throughput in **GFLOPS**.
* **`ram_limit_test.py`**: Safe incremental RAM allocation test to discover maximum per-app heap thresholds before Jetsam memory warnings.
* **`disk_io_benchmark.py`**: Sequential and random read/write throughput (MB/s) on NVMe storage.

### 2️⃣ iOS Hardware Sensors & Peripherals (`02_ios_sensors_hardware/`)
* **`motion_and_gyroscope.py`**: Real-time 60 Hz telemetry of device attitude (Pitch, Roll, Yaw), gravity vectors, and user acceleration.
* **`gps_and_geocoding.py`**: High-precision GPS latitude/longitude, altitude, speed, and Apple Maps reverse geocoding into street addresses.
* **`haptics_and_sound.py`**: Taptic Engine feedback vibrations (Light, Medium, Heavy, Success, Warning, Error, Selection) and audio alerts.
* **`speech_tts_arabic.py`**: Neural Siri Text-To-Speech engine synthesis with custom pitch, rate, and multilingual accents.
* **`local_notifications.py`**: Scheduled and immediate background push notifications with custom payloads.
* **`camera_and_photos.py`**: Programmatic access to photo library albums and camera capture.

### 3️⃣ Native iOS Graphical User Interfaces (`03_native_ui/`)
* **`pyto_ui_showcase.py`**: Native UIKit interface constructed entirely in Python (Buttons, Sliders, TextFields, Switches, SF Symbols).
* **`live_sensor_ui.py`**: Animated 60 FPS digital bubble inclinometer/leveler responding to iPhone orientation.
* **`interactive_canvas_drawing.py`**: Interactive touch palette with dynamic theme switching and haptic responses.

### 4️⃣ On-Device AI & Computer Vision (`04_ai_machine_learning/`)
* **`cv2_face_and_vision.py`**: OpenCV 1080p pipeline measuring frame latency for Canny edge detection, Gaussian filters, contours, and 2D Fourier transforms.
* **`sklearn_ml_training.py`**: On-device training of Random Forest (50 trees), Logistic Regression, and K-Means clustering across 15,000 samples.
* **`numpy_scipy_math_engine.py`**: High-dimensional linear algebra (1M-point FFT, Singular Value Decomposition SVD, Eigenvalue decomposition).
* **`data_visualization_plot.py`**: High-DPI scientific multi-plot generation (trigonometric waves, 2D Gaussian heatmaps, histograms) via Matplotlib.

### 5️⃣ Network Services & Local Hosting (`05_networking_servers/`)
* **`iphone_web_server.py`**: Embedded HTTP web server running on the iPhone, accessible from any Mac/PC on the local Wi-Fi.
* **`network_speed_and_ping.py`**: TCP socket connection latency (Ping) to global endpoints and HTTP download throughput.
* **`api_fetch_weather_sample.py`**: Asynchronous REST API integration and JSON deserialization.

### 6️⃣ Widgets & System Integrations (`06_widgets_and_shortcuts/`)
* **`custom_home_widget.py`**: Native Home Screen and Lock Screen widget displaying time, date, telemetry, and dynamic quotes.
* **`shortcuts_integration.py`**: Input parameter handling from Apple Shortcuts and voice automation via Siri.

---

## 🛡️ Stability & Memory Architecture
This suite implements an automatic **Garbage Collection and Sensor Teardown** architecture (`cleanup_environment()`) to ensure zero crashes, dangling threads, or memory leaks even when cycling through heavy tests in rapid succession.
