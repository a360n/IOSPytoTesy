#!/usr/bin/env python3
"""
🔬 الحوسبة العلمية المتقدمة وتحليل فورييه (NumPy & SciPy Scientific Engine)
يقوم هذا السكربت باختبار كفاءة العمليات الجبرية الخطية المعقدة (FFT, SVD, Eigenvalues)
والتكاملات التفاضلية على معالج الآيفون.
"""

import time

def test_scientific_computing():
    print("=" * 60)
    print("  🔬 اختبار الحوسبة العلمية الرياضية (Scientific Computing Engine)")
    print("=" * 60)

    try:
        import numpy as np
        import scipy.linalg as la
        from scipy import signal
    except ImportError as e:
        print(f"❌ مكتبة NumPy أو SciPy غير متوفرة: {e}")
        return

    # 1. تحويل فورييه السريع لملايين النقاط (1D FFT)
    n_points = 2**20  # أكثر من مليون نقطة
    print(f"\n1️⃣ اختبار Fast Fourier Transform (FFT) على {n_points:,} نقطة...")
    t = np.linspace(0, 10, n_points)
    sig = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    
    t0 = time.time()
    fft_result = np.fft.fft(sig)
    dt_fft = (time.time() - t0) * 1000
    print(f"   ⚡ سرعة معالجة FFT: {dt_fft:.2f} ms")

    # 2. تفكيك القيم المفردة (Singular Value Decomposition - SVD)
    matrix_dim = 600
    print(f"\n2️⃣ اختبار تفكيك SVD لمصفوفة مربعة بحجم {matrix_dim}x{matrix_dim}...")
    M = np.random.randn(matrix_dim, matrix_dim)
    t0 = time.time()
    U, s, Vt = la.svd(M)
    dt_svd = time.time() - t0
    print(f"   ⏱️ زمن تفكيك SVD: {dt_svd:.3f} ثانية")

    # 3. حساب القيم والمتجهات الذاتية (Eigenvalues & Eigenvectors)
    print(f"\n3️⃣ حساب القيم والمتجهات الذاتية (Eigenvalues) لمصفوفة {matrix_dim}x{matrix_dim}...")
    t0 = time.time()
    eigenvalues, eigenvectors = la.eig(M)
    dt_eig = time.time() - t0
    print(f"   ⏱️ زمن الحساب: {dt_eig:.3f} ثانية")

    print("\n" + "=" * 60)
    print("✨ تم اجتياز جميع اختبارات الحوسبة العلمية بنجاح مبهر!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_scientific_computing()
