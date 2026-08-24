#!/usr/bin/env python3
"""
👁️ اختبار الرؤية الحاسوبية ومعالجة الصور عبر OpenCV (Computer Vision Benchmark)
يقوم هذا السكربت باختبار كفاءة وسرعة معالجة الصور ومقاطع الفيديو عبر مكتبة cv2 (OpenCV)
على معالج الآيفون من خلال خوارزميات كشف الحواف (Canny & Sobel)، الفلاتر، واستخراج المعالم.
"""

import time
import os

def test_opencv_pipeline():
    print("=" * 60)
    print("  👁️ اختبار معالجة الصور والرؤية الحاسوبية (OpenCV Pipeline)")
    print("=" * 60)

    try:
        import cv2
        import numpy as np
    except ImportError as e:
        print(f"❌ مكتبة OpenCV أو NumPy غير متوفرة: {e}")
        return

    print(f"📦 إصدار OpenCV المثبت: {cv2.__version__}")
    
    # 1. إنشاء صورة اختبارية ملونة عالية الدقة بدقة 4K (3840x2160)
    width, height = 3840, 2160
    print(f"\n🖼️ توليد صورة اختبارية عالية الدقة 4K ({width}x{height})...")
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # رسم أشكال هندسية ودوائر ومستطيلات
    cv2.circle(img, (width//2, height//2), 600, (0, 165, 255), -1)
    cv2.rectangle(img, (400, 300), (width-400, height-300), (255, 0, 128), 10)
    cv2.putText(img, "Pyto on iPhone 17 Pro Max", (width//4, height//2), 
                cv2.FONT_HERSHEY_SIMPLEX, 3.0, (255, 255, 255), 8)

    print("⚡ بدء تشغيل خط معالجة الرؤية الحاسوبية (Vision Pipeline):")

    # أ. تحويل الصورة إلى تدرجات الرمادي (Grayscale)
    t0 = time.time()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    t_gray = (time.time() - t0) * 1000
    print(f"   1. تحويل Grayscale           : {t_gray:.2f} ms")

    # ب. فلتر التنعيم الضبابي (Gaussian Blur)
    t0 = time.time()
    blurred = cv2.GaussianBlur(gray, (25, 25), 0)
    t_blur = (time.time() - t0) * 1000
    print(f"   2. فلتر Gaussian Blur (25x25)  : {t_blur:.2f} ms")

    # ج. كشف الحواف الدقيق (Canny Edge Detection)
    t0 = time.time()
    edges = cv2.Canny(blurred, 50, 150)
    t_canny = (time.time() - t0) * 1000
    print(f"   3. كشف الحواف (Canny Edges)    : {t_canny:.2f} ms")

    # د. كشف المنحنيات والمحيطات (Find Contours)
    t0 = time.time()
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    t_contours = (time.time() - t0) * 1000
    print(f"   4. استخراج المحيطات (Contours) : {t_contours:.2f} ms (تم العثور على {len(contours)} محيط)")

    # هـ. تحويل فورييه ثنائي الأبعاد للصورة (2D FFT)
    t0 = time.time()
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    t_dft = (time.time() - t0) * 1000
    print(f"   5. تحويل فورييه البصري (DFT)   : {t_dft:.2f} ms")

    total_time = t_gray + t_blur + t_canny + t_contours + t_dft
    fps_estimate = 1000.0 / total_time
    print("-" * 60)
    print(f"🏆 إجمالي زمن معالجة إطار 4K كامل: {total_time:.2f} ms")
    print(f"🚀 معدل الإطارات التقديري (FPS): {fps_estimate:.1f} FPS لمعالجة صور 4K!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_opencv_pipeline()
