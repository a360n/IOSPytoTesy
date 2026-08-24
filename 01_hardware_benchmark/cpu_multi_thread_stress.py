#!/usr/bin/env python3
"""
⚡ اختبار إجهاد المعالج وتعدد الأنوية (CPU & Multi-Threading Stress Test)
يقوم هذا السكربت باختبار القوة الحسابية الخارقة لمعالج الآيفون (A-Series Pro / Neural Engine)
من خلال عمليات رياضية مكثفة، ضرب مصفوفات، واختبار تعدد الخيوط (Multi-Threading).
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
    """حساب الأعداد الأولية لاختبار الحساب النقطي الأحادي"""
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
    """حساب قيمة باي عبر محاكاة مونت كارلو"""
    import random
    inside = 0
    for _ in range(samples):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1.0:
            inside += 1
    return (4.0 * inside) / samples

def test_single_core():
    print_header("1. اختبار النواة الواحدة (Single-Core Stress Test)")
    
    # 1. اختبار الأعداد الأولية
    print("⏳ جاري حساب الأعداد الأولية حتى 150,000...")
    t0 = time.time()
    count = cpu_heavy_primes(150000)
    t1 = time.time()
    dt_primes = t1 - t0
    print(f"   ✅ تم العثور على {count:,} عدد أولي خلال {dt_primes:.3f} ثانية.")

    # 2. اختبار مونت كارلو
    print("⏳ جاري محاكاة مونت كارلو (2 مليون نقطة)...")
    t0 = time.time()
    pi_val = cpu_heavy_monte_carlo_pi(2000000)
    t1 = time.time()
    dt_mc = t1 - t0
    print(f"   ✅ قيمة Pi التقريبية: {pi_val:.6f} خلال {dt_mc:.3f} ثانية.")

    score = int(10000 / (dt_primes + dt_mc))
    print(f"🏆 نتيجة النواة الواحدة (Single-Core Score): {score:,} نقطة")
    return score

def test_matrix_multiplication():
    print_header("2. اختبار ضرب المصفوفات الحسابية (Matrix Multiplication)")
    try:
        import numpy as np
        print("⚡ باستخدام مكتبة NumPy مع تسريع المعمارية...")
        size = 1500
        print(f"⏳ توليد مصفوفتين عشوائيتين بحجم {size}x{size}...")
        A = np.random.rand(size, size).astype(np.float64)
        B = np.random.rand(size, size).astype(np.float64)

        t0 = time.time()
        C = np.dot(A, B)
        dt = time.time() - t0
        
        # 2 * N^3 operations
        gflops = (2.0 * (size ** 3)) / (dt * 1e9)
        print(f"   ✅ اكتمل ضرب مصفوفة {size}x{size} خلال {dt:.3f} ثانية!")
        print(f"   🚀 الأداء: {gflops:.2f} GFLOPS")
    except ImportError:
        print("⚠️ مكتبة NumPy غير متوفرة، سيتم تجاوز اختبار المصفوفات الضخمة.")

def worker_task(thread_id, iterations=80000):
    """مهمة فرعية تعمل في خيط مستقل"""
    primes = 0
    for num in range(2, iterations):
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            primes += 1
    return primes

def test_multi_threading():
    print_header("3. اختبار تعدد الخيوط والأنوية (Multi-Threading Stress Test)")
    num_cores = os.cpu_count() or 4
    num_threads = num_cores * 2
    print(f"⚙️ الأنوية المكتشفة: {num_cores} | تشغيل {num_threads} خيوط معالجة متوازية...")

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(worker_task, i, 80000) for i in range(num_threads)]
        results = [f.result() for f in futures]
    dt_multi = time.time() - t0

    print(f"   ✅ اكتملت جميع المهام المتوازية ({sum(results):,} عملية) خلال {dt_multi:.3f} ثانية.")
    multi_score = int((num_threads * 10000) / dt_multi)
    print(f"🏆 نتيجة تعدد الأنوية (Multi-Core Score): {multi_score:,} نقطة")
    return multi_score

if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("   📱 اختبار سرعة وقوة معالج الآيفون عبر Pyto")
    print("#" * 60)

    s_score = test_single_core()
    test_matrix_multiplication()
    m_score = test_multi_threading()

    print("\n" + "=" * 60)
    print(f"🏁 النتيجة الإجمالية المجمعة للأداء: {s_score + m_score:,} نقطة")
    print("=" * 60 + "\n")
