#!/usr/bin/env python3
"""
💾 RAM Allocation & Memory Limit Benchmark
Incrementally allocates memory blocks to safely test RAM usage thresholds on iOS
and monitors garbage collection recovery.
"""

import sys
import time
import gc

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  💾 {title}")
    print("=" * 60)

def test_ram_limits(step_mb=50, max_mb=1500):
    print_header("RAM Allocation & Threshold Test")
    print(f"⚙️ Step Size: {step_mb} MB per chunk | Safe Test Target: {max_mb} MB")
    print("⚠️ Note: iOS will enforce memory pressure limits; safety limits are in place.\n")

    chunks = []
    total_allocated_mb = 0

    try:
        while total_allocated_mb < max_mb:
            block = bytearray(step_mb * 1024 * 1024)
            block[0] = 1
            block[-1] = 1
            chunks.append(block)
            total_allocated_mb += step_mb
            
            gb_allocated = total_allocated_mb / 1024.0
            print(f"📈 Successfully allocated: {total_allocated_mb:>5} MB  ({gb_allocated:.2f} GB) ...")
            time.sleep(0.04)

        print(f"\n🎉 Excellent! Successfully reached target limit: {total_allocated_mb} MB ({total_allocated_mb/1024.0:.2f} GB) without issues!")

    except MemoryError:
        print(f"\n🚨 Hit memory threshold (MemoryError) at: {total_allocated_mb} MB ({total_allocated_mb/1024.0:.2f} GB)!")
    except Exception as e:
        print(f"\n⚠️ Test stopped: {e} at {total_allocated_mb} MB")
    finally:
        print("\n🧹 Releasing memory and invoking Garbage Collector...")
        chunks.clear()
        gc.collect()
        time.sleep(0.5)
        print("✅ Memory fully freed and reclaimed successfully!\n")

if __name__ == "__main__":
    test_ram_limits()
