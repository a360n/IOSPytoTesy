# 📱 iPhone Pyto Test Suite & Hardware Limits (IOSPytoTesy)

حزمة اختبارات شاملة ومتطورة مصممة خصيصاً لاختبار **أقصى حدود وقدرات تطبيق Pyto** على هواتف الآيفون الحديثة (**iPhone 17 Pro Max**)، واستغلال القوة الحسابية الخارقة لمعالجات آبل سيليكون (Apple Silicon) مع حساسات وميزات نظام iOS.

---

## 🚀 كيفية التحديث والتشغيل على الآيفون (Quick Start)

### 1. سحب آخر التحديثات إلى الآيفون
داخل تطبيق **Pyto** على هاتفك الآيفون:
1. افتح الملف الرئيسي الموجود مسبقاً: `pull_repo.py`.
2. اضغط على زر التشغيل ▶️ (Run).
3. سيقوم السكربت بتحميل آخر نسخة من المستودع تلقائياً واستخراجها في مجلد `IOSPytoTesy`.

### 2. تشغيل لوحة التحكم التفاعلية
- افتح مجلد `IOSPytoTesy` داخل Pyto.
- شغّل الملف `main_dashboard.py` لاختيار أي اختبار من القائمة التفاعلية مباشرة، أو يمكنك فتح أي ملف وتشغيله بشكل مستقل.

---

## 📂 فهرس ومحتويات حزمة الاختبارات

### 1️⃣ اختبارات العتاد والأداء (Hardware & Limits Benchmark)
* 📁 `01_hardware_benchmark/device_info_diagnostics.py`: فحص تفصيلي للعتاد، عدد الأنوية، المعمارية، وإصدارات بايثون ومكتبات Pyto.
* 📁 `01_hardware_benchmark/cpu_multi_thread_stress.py`: اختبار إجهاد المعالج بحساب الأعداد الأولية، ضرب مصفوفات ضخمة (GFLOPS)، وتعدد الخيوط المتوازية (Multi-Threading).
* 📁 `01_hardware_benchmark/ram_limit_test.py`: اختبار استهلاك وحجز الذاكرة العشوائية (RAM) لمعرفة الحد الأقصى قبل حدوث Memory Warning أو MemoryError مع تنظيف تلقائي.
* 📁 `01_hardware_benchmark/disk_io_benchmark.py`: قياس سرعات القراءة والكتابة التسلسلية (MB/s) على ذاكرة التخزين السريعة NVMe.

### 2️⃣ حساسات وميزات نظام iOS (iOS Sensors & Hardware)
* 📁 `02_ios_sensors_hardware/motion_and_gyroscope.py`: قراءة حية بالزمن الحقيقي لزوايا ميل الجهاز (Roll, Pitch, Yaw)، الجيروسكوب، والجاذبية.
* 📁 `02_ios_sensors_hardware/gps_and_geocoding.py`: استقبال إحداثيات الـ GPS عالية الدقة، السرعة، الارتفاع، وتحويلها لاسم شارع ومدينة عبر Apple Maps.
* 📁 `02_ios_sensors_hardware/haptics_and_sound.py`: تجربة جميع أنماط الاهتزاز اللمسية لمحرك Taptic Engine (خفيف، قوي، نجاح، خطأ، اختيار) والمؤثرات الصوتية.
* 📁 `02_ios_sensors_hardware/speech_tts_arabic.py`: تحويل النص إلى كلام صوتي طبيعي باللغة العربية الفصحى والإنجليزية باستخدام محرك سيري (Siri Voices).
* 📁 `02_ios_sensors_hardware/local_notifications.py`: جدولة وإرسال إشعارات محلية تفاعلية تظهر حتى عند قفل الهاتف.
* 📁 `02_ios_sensors_hardware/camera_and_photos.py`: فحص التكامل مع مكتبة الصور والكاميرا.

### 3️⃣ واجهات المستخدم الرسومية الأصلية (Native UIKit & Graphics)
* 📁 `03_native_ui/pyto_ui_showcase.py`: بناء واجهة مستخدم أصلية لنظام iOS (أزرار، شرائح تمرير، مدخلات، أيقونات، تبديل ألوان) بلغة بايثون بالكامل.
* 📁 `03_native_ui/live_sensor_ui.py`: ميزان مائي رقمي تفاعلي (Bubble Level) تتحرك فيه الفقاعة بنعومة 60 FPS عند إمالة الهاتف.
* 📁 `03_native_ui/interactive_canvas_drawing.py`: لوحة تفاعلية لاختيار وتجربة الألوان والتأثيرات اللمسية.

### 4️⃣ الذكاء الاصطناعي والحوسبة العلمية (AI & Data Science)
* 📁 `04_ai_machine_learning/cv2_face_and_vision.py`: معالجة صور عالية الدقة 4K عبر OpenCV (كشف الحواف Canny، فلاتر ضبابية، استخراج المنحنيات ومعدل الإطارات FPS).
* 📁 `04_ai_machine_learning/sklearn_ml_training.py`: تدريب نماذج تعلم الآلة (Random Forest, Logistic Regression, K-Means) محلياً بالكامل على الآيفون.
* 📁 `04_ai_machine_learning/numpy_scipy_math_engine.py`: الحوسبة الجبرية المتقدمة (FFT لأكثر من مليون نقطة، تفكيك المصفوفات SVD، وحساب القيم الذاتية).
* 📁 `04_ai_machine_learning/data_visualization_plot.py`: رسم وتصدير 4 مخططات بيانية متقدمة بجودة طباعة فائقة الدقة عبر Matplotlib.

### 5️⃣ خوادم الويب والشبكات (Local Servers & Networking)
* 📁 `05_networking_servers/iphone_web_server.py`: تحويل الآيفون إلى سيرفر ويب مصغر (Web Server) يمكنك تصفحه والتحكم به عبر المتصفح من الماك أو الكمبيوتر على نفس شبكة الواي فاي.
* 📁 `05_networking_servers/network_speed_and_ping.py`: قياس زمن الاستجابة (Ping) وسرعة التحميل الفعلي للشبكة.
* 📁 `05_networking_servers/api_fetch_weather_sample.py`: جلب بيانات الطقس الحية عبر واجهات REST API بصيغة JSON.

### 6️⃣ ويدجت الشاشة والاختصارات (Widgets & Shortcuts)
* 📁 `06_widgets_and_shortcuts/custom_home_widget.py`: تصميم ويدجت تفاعلي للشاشة الرئيسية وشاشة القفل يظهر الوقت، التاريخ، واقتباسات متجددة.
* 📁 `06_widgets_and_shortcuts/shortcuts_integration.py`: استقبال الأوامر والبيانات من تطبيق اختصارات آبل وأتمتتها بصوت سيري.

---

## 🛠️ متطلبات التشغيل
- تطبيق **Pyto** (متوفر على متجر App Store لنظام iOS).
- اتصال بالإنترنت عند تشغيل `pull_repo.py` لتحميل التحديثات.
- تفعيل أذونات (الموقع، الإشعارات، الكاميرا) عند طلبها أثناء اختبار ميزات النظام المعنية.
