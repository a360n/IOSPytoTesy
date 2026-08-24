#!/usr/bin/env python3
"""
💾 اختبار حدود استهلاك الذاكرة العشوائية (RAM Limit & Stress Test)
يقوم هذا السكربت بحجز كتل من الذاكرة بشكل تدريجي لمعرفة كمية الرام (RAM)
التي يسمح نظام iOS لتطبيق Pyto باستخدامها بأمان قبل الوصول لحدود Jetsam.
"""

import sys
import time
import gc

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  💾 {title}")
    print("=" * 60)

def test_ram_limits(step_mb=50, max_mb=1500):
    print_header("بدء اختبار قياس حدود الذاكرة (RAM Allocation Test)")
    print(f"⚙️ خطوة الحجز: {step_mb} MB لكل دفعة | الحد الأقصى الآمن: {max_mb} MB")
    print("⚠️ ملاحظة: نظام iOS يقوم بإنهاء التطبيقات تلقائياً إذا تجاوزت حداً معيناً، لذا تم ضبط حد الأمان.\n")

    chunks = []
    total_allocated_mb = 0

    try:
        while total_allocated_mb < max_mb:
            # حجز كتلة ذاكرة ممتلئة بالبيانات (bytearray)
            block = bytearray(step_mb * 1024 * 1024)
            block[0] = 1
            block[-1] = 1
            chunks.append(block)
            total_allocated_mb += step_mb
            
            gb_allocated = total_allocated_mb / 1024.0
            print(f"📈 تم حجز بنجاح: {total_allocated_mb:>5} MB  ({gb_allocated:.2f} GB) ...")
            time.sleep(0.04)

        print(f"\n🎉 مذهل! تم الوصول للحد الأقصى للاختبار بنجاح: {total_allocated_mb} MB ({total_allocated_mb/1024.0:.2f} GB) بدون أي مشاكل!")

    except MemoryError:
        print(f"\n🚨 وصل التطبيق إلى حد الذاكرة الأقصى (MemoryError) عند: {total_allocated_mb} MB ({total_allocated_mb/1024.0:.2f} GB)!")
    except Exception as e:
        print(f"\n⚠️ توقف الاختبار: {e} عند {total_allocated_mb} MB")
    finally:
        print("\n🧹 جاري تحرير الذاكرة وتفعيل Garbage Collector فوراً...")
        chunks.clear()
        gc.collect()
        time.sleep(0.5)
        print("✅ تم استرجاع وتنظيف الذاكرة بالكامل بنجاح!\n")

if __name__ == "__main__":
    test_ram_limits()
