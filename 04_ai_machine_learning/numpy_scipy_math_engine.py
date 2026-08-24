#!/usr/bin/env python3
"""
🔬 Scientific Computing & Advanced Linear Algebra Engine (NumPy & SciPy)
Benchmarks high-dimensional Fast Fourier Transforms (FFT), Singular Value Decomposition (SVD),
and Eigenvalue spectral computations on Apple Silicon.
"""

import time

def test_scientific_computing():
    print("=" * 60)
    print("  🔬 Scientific Computing & Linear Algebra (NumPy & SciPy)")
    print("=" * 60)

    try:
        import numpy as np
        import scipy.linalg as la
        from scipy import signal
    except ImportError as e:
        print(f"❌ NumPy or SciPy module not found: {e}")
        return

    # 1. Fast Fourier Transform (1M points)
    n_points = 2**20  # ~1,048,576 points
    print(f"\n1️⃣ Running 1D Fast Fourier Transform (FFT) on {n_points:,} points...")
    t = np.linspace(0, 10, n_points)
    sig = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
    
    t0 = time.time()
    fft_result = np.fft.fft(sig)
    dt_fft = (time.time() - t0) * 1000
    print(f"   ⚡ FFT Execution Latency: {dt_fft:.2f} ms")

    # 2. Singular Value Decomposition (SVD)
    matrix_dim = 600
    print(f"\n2️⃣ Running SVD decomposition on {matrix_dim}x{matrix_dim} dense matrix...")
    M = np.random.randn(matrix_dim, matrix_dim)
    t0 = time.time()
    U, s, Vt = la.svd(M)
    dt_svd = time.time() - t0
    print(f"   ⏱️ SVD Execution Time  : {dt_svd:.3f} s")

    # 3. Eigenvalues & Eigenvectors
    print(f"\n3️⃣ Computing Eigenvalues & Eigenvectors for {matrix_dim}x{matrix_dim} matrix...")
    t0 = time.time()
    eigenvalues, eigenvectors = la.eig(M)
    dt_eig = time.time() - t0
    print(f"   ⏱️ Eigen Computation Time: {dt_eig:.3f} s")

    print("\n" + "=" * 60)
    print("✨ All scientific linear algebra benchmarks passed successfully!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_scientific_computing()
