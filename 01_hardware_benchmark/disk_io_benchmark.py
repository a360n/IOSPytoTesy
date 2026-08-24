#!/usr/bin/env python3
"""
⚡ Storage I/O Read & Write Benchmark
Measures sequential read and write speeds (MB/s) on the iPhone NVMe flash storage
inside the Pyto sandbox container.
"""

import os
import time
import tempfile

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  📂 {title}")
    print("=" * 60)

def benchmark_disk_io(file_size_mb=100, chunk_size_kb=1024):
    print_header("Storage I/O Speed Test")
    print(f"📊 Test File Size: {file_size_mb} MB | Block Size: {chunk_size_kb} KB\n")

    temp_dir = tempfile.gettempdir()
    test_file_path = os.path.join(temp_dir, "pyto_disk_speed_test.bin")
    chunk_bytes = os.urandom(chunk_size_kb * 1024)
    total_chunks = int((file_size_mb * 1024) / chunk_size_kb)

    try:
        # 1. Sequential Write
        print("⏳ Testing Sequential Write speed...")
        t0 = time.time()
        with open(test_file_path, "wb") as f:
            for _ in range(total_chunks):
                f.write(chunk_bytes)
            f.flush()
            os.fsync(f.fileno())
        write_time = time.time() - t0
        write_speed = file_size_mb / write_time
        print(f"   ✍️ Write Speed : {write_speed:.2f} MB/s (Completed in {write_time:.3f} s)")

        # 2. Sequential Read
        print("⏳ Testing Sequential Read speed...")
        t0 = time.time()
        with open(test_file_path, "rb") as f:
            while True:
                data = f.read(chunk_size_kb * 1024)
                if not data:
                    break
        read_time = time.time() - t0
        read_speed = file_size_mb / read_time
        print(f"   📖 Read Speed  : {read_speed:.2f} MB/s (Completed in {read_time:.3f} s)")

        # Summary
        print("\n" + "-" * 60)
        print(f"🏆 Final Storage Benchmark Results:")
        print(f"   • Write Throughput : {write_speed:.2f} MB/s")
        print(f"   • Read Throughput  : {read_speed:.2f} MB/s")
        print("-" * 60)

    finally:
        if os.path.exists(test_file_path):
            os.remove(test_file_path)
            print("🧹 Cleaned up temporary test file.")

if __name__ == "__main__":
    benchmark_disk_io()
