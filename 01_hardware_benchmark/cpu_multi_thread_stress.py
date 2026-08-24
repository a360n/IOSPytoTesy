#!/usr/bin/env python3
"""
⚡ CPU & Multi-Threading Stress Benchmark
Tests single-core and multi-core computational performance of the Apple Silicon chip
via intensive integer factorization, Monte Carlo simulations, NumPy matrix multiplications, and thread pools.
"""

import time
import math
import os
import sys
from concurrent.futures import ThreadPoolExecutor

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  🔥 {title}")
    print("=" * 60)

def cpu_heavy_primes(n=150000):
    """Calculates prime numbers to test single-core floating/integer arithmetic"""
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return len(primes)

def cpu_heavy_monte_carlo_pi(samples=2000000):
    """Calculates approximate Pi using 2M Monte Carlo random points"""
    import random
    inside = 0
    for _ in range(samples):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1.0:
            inside += 1
    return (4.0 * inside) / samples

def test_single_core():
    print_header("1. Single-Core Stress Test")
    
    # 1. Prime computation
    print("⏳ Calculating prime numbers up to 150,000...")
    t0 = time.time()
    count = cpu_heavy_primes(150000)
    t1 = time.time()
    dt_primes = t1 - t0
    print(f"   ✅ Found {count:,} primes in {dt_primes:.3f} seconds.")

    # 2. Monte Carlo
    print("⏳ Running Monte Carlo simulation (2,000,000 points)...")
    t0 = time.time()
    pi_val = cpu_heavy_monte_carlo_pi(2000000)
    t1 = time.time()
    dt_mc = t1 - t0
    print(f"   ✅ Pi approximation: {pi_val:.6f} in {dt_mc:.3f} seconds.")

    score = int(10000 / (dt_primes + dt_mc))
    print(f"🏆 Single-Core Score: {score:,} points")
    return score

def test_matrix_multiplication():
    print_header("2. Matrix Multiplication Benchmark (GFLOPS)")
    try:
        import numpy as np
        print("⚡ Using NumPy with hardware SIMD acceleration...")
        size = 1500
        print(f"⏳ Generating two random matrices of size {size}x{size}...")
        A = np.random.rand(size, size).astype(np.float64)
        B = np.random.rand(size, size).astype(np.float64)

        t0 = time.time()
        C = np.dot(A, B)
        dt = time.time() - t0
        
        # 2 * N^3 operations
        gflops = (2.0 * (size ** 3)) / (dt * 1e9)
        print(f"   ✅ Computed {size}x{size} dot product in {dt:.3f} seconds!")
        print(f"   🚀 Compute Throughput: {gflops:.2f} GFLOPS")
    except ImportError:
        print("⚠️ NumPy not installed. Skipping matrix benchmark.")

def worker_task(thread_id, iterations=80000):
    """Sub-task executing in a worker thread"""
    primes = 0
    for num in range(2, iterations):
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            primes += 1
    return primes

def test_multi_threading():
    print_header("3. Multi-Threading & Multi-Core Stress Test")
    num_cores = os.cpu_count() or 4
    num_threads = num_cores * 2
    print(f"⚙️ Detected Cores: {num_cores} | Spawning {num_threads} concurrent worker threads...")

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(worker_task, i, 80000) for i in range(num_threads)]
        results = [f.result() for f in futures]
    dt_multi = time.time() - t0

    print(f"   ✅ Completed all parallel tasks ({sum(results):,} operations) in {dt_multi:.3f} seconds.")
    multi_score = int((num_threads * 10000) / dt_multi)
    print(f"🏆 Multi-Core Score: {multi_score:,} points")
    return multi_score

if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("   📱 Apple Silicon iPhone CPU Benchmark via Pyto")
    print("#" * 60)

    s_score = test_single_core()
    test_matrix_multiplication()
    m_score = test_multi_threading()

    print("\n" + "=" * 60)
    print(f"🏁 Total Combined Performance Score: {s_score + m_score:,} points")
    print("=" * 60 + "\n")
