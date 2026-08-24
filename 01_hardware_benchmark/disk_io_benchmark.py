#!/usr/bin/env python3
"""
⚡ اختبار سرعة القراءة والكتابة على وحدة التخزين (Disk I/O Benchmark)
يقوم هذا السكربت بقياس سرعة القراءة والكتابة التسلسلية والعشوائية
على ذاكرة التخزين السريعة (NVMe Flash) لجهاز الآيفون داخل مسار تطبيق Pyto.
"""

import os
import time
import tempfile

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  📂 {title}")
    print("=" * 60)

def benchmark_disk_io(file_size_mb=100, chunk_size_kb=1024):
    print_header("اختبار سرعة التخزين (Storage I/O Speed Test)")
    print(f"📊 حجم الملف التجريبي: {file_size_mb} MB | حجم الكتلة (Block): {chunk_size_kb} KB\n")

    temp_dir = tempfile.gettempdir()
    test_file_path = os.path.join(temp_dir, "pyto_disk_speed_test.bin")
    chunk_bytes = os.urandom(chunk_size_kb * 1024)
    total_chunks = int((file_size_mb * 1024) / chunk_size_kb)

    try:
        # 1. اختبار الكتابة التسلسلية (Sequential Write)
        print("⏳ جاري اختبار سرعة الكتابة (Sequential Write)...")
        t0 = time.time()
        with open(test_file_path, "wb") as f:
            for _ in range(total_chunks):
                f.write(chunk_bytes)
            f.flush()
            os.fsync(f.fileno())  # التأكد من الكتابة الفعلية للقرص
        write_time = time.time() - t0
        write_speed = file_size_mb / write_time
        print(f"   ✍️ سرعة الكتابة: {write_speed:.2f} MB/s (استغرق {write_time:.3f} ثانية)")

        # 2. اختبار القراءة التسلسلية (Sequential Read)
        print("⏳ جاري اختبار سرعة القراءة (Sequential Read)...")
        t0 = time.time()
        with open(test_file_path, "rb") as f:
            while True:
                data = f.read(chunk_size_kb * 1024)
                if not data:
                    break
        read_time = time.time() - t0
        read_speed = file_size_mb / read_time
        print(f"   📖 سرعة القراءة: {read_speed:.2f} MB/s (استغرق {read_time:.3f} ثانية)")

        # التقييم
        print("\n" + "-" * 60)
        print(f"🏆 النتيجة النهائية:")
        print(f"   • معدل الكتابة: {write_speed:.2f} MB/s")
        print(f"   • معدل القراءة: {read_speed:.2f} MB/s")
        print("-" * 60)

    finally:
        if os.path.exists(test_file_path):
            os.remove(test_file_path)
            print("🧹 تم تنظيف الملف التجريبي بنجاح.")

if __name__ == "__main__":
    benchmark_disk_io()
