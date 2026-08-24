#!/usr/bin/env python3
"""
👁️ Computer Vision & Image Processing Benchmark (OpenCV Pipeline)
Tests hardware acceleration and latency of OpenCV cv2 operations on Apple Silicon
including Canny Edge Detection, Gaussian Blurring, Contour extraction, and 2D Discrete Fourier Transforms.
"""

import time
import os

def test_opencv_pipeline():
    print("=" * 60)
    print("  👁️ OpenCV Computer Vision Pipeline Benchmark")
    print("=" * 60)

    try:
        import cv2
        import numpy as np
    except ImportError as e:
        print(f"❌ OpenCV or NumPy module not found: {e}")
        return

    print(f"📦 Installed OpenCV Version: {cv2.__version__}")
    
    # Generate high-resolution 1080p frame
    width, height = 1920, 1080
    print(f"\n🖼️ Generating synthetic Full HD ({width}x{height}) frame...")
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    cv2.circle(img, (width//2, height//2), 300, (0, 165, 255), -1)
    cv2.rectangle(img, (200, 150), (width-200, height-150), (255, 0, 128), 6)
    cv2.putText(img, "Pyto on iPhone 17 Pro Max", (width//4, height//2), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)

    print("⚡ Running Computer Vision Pipeline steps:")

    # 1. Grayscale conversion
    t0 = time.time()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    t_gray = (time.time() - t0) * 1000
    print(f"   1. Grayscale Conversion      : {t_gray:.2f} ms")

    # 2. Gaussian Blur
    t0 = time.time()
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    t_blur = (time.time() - t0) * 1000
    print(f"   2. Gaussian Blur (15x15)     : {t_blur:.2f} ms")

    # 3. Canny Edge Detection
    t0 = time.time()
    edges = cv2.Canny(blurred, 50, 150)
    t_canny = (time.time() - t0) * 1000
    print(f"   3. Canny Edge Detection      : {t_canny:.2f} ms")

    # 4. Contour Extraction
    t0 = time.time()
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    t_contours = (time.time() - t0) * 1000
    print(f"   4. Contour Extraction        : {t_contours:.2f} ms ({len(contours)} contours found)")

    # 5. 2D Discrete Fourier Transform (DFT)
    t0 = time.time()
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    t_dft = (time.time() - t0) * 1000
    print(f"   5. 2D Fourier Transform (DFT): {t_dft:.2f} ms")

    total_time = t_gray + t_blur + t_canny + t_contours + t_dft
    fps_estimate = 1000.0 / total_time
    print("-" * 60)
    print(f"🏆 Total 1080p Pipeline Frame Latency: {total_time:.2f} ms")
    print(f"🚀 Estimated Video Processing Rate   : {fps_estimate:.1f} FPS")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_opencv_pipeline()
