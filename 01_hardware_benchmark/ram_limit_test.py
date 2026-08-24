#!/usr/bin/env python3
"""
💾 اختبار حدود استهلاك الذاكرة العشوائية (RAM Limit & Stress Test)
يقوم هذا السكربت بحجز كتل من الذاكرة بشكل تدريجي لمعرفة كمية الرام (RAM)
التي يسمح نظام iOS لتطبيق Pyto باستخدامها قبل أن يتم تقييدها أو إيقافها.
"""

import sys
import time
import gc

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  💾 {title}")
    print("=" * 60)

def test_ram_limits(step_mb=100, max_mb=6000):
    print_header("بدء اختبار قياس حدود الذاكرة (RAM Allocation Test)")
    print(f"⚙️ خطوة الحجز: {step_mb} MB لكل دفعة | الحد الأقصى للاختبار: {max_mb} MB")
    print("⚠️ ملاحظة: سيتم حجز البيانات تدريجياً وتحريرها تلقائياً بعد انتهاء الاختبار.\n")

    chunks = []
    total_allocated_mb = 0

    try:
        while total_allocated_mb < max_mb:
            # حجز كتلة ذاكرة ممتلئة بالبيانات (bytearray)
            block = bytearray(step_mb * 1024 * 1024)
            # ملء بعض الخانات لضمان حجز الذاكرة فعلياً (dirty memory)
            block[0] = 1
            block[-1] = 1
            chunks.append(block)
            total_allocated_mb += step_mb
            
            gb_allocated = total_allocated_mb / 1024.0
            print(f"📈 تم حجز بنجاح: {total_allocated_mb:>5} MB  ({gb_allocated:.2f} GB) ...")
            time.sleep(0.05)

        print(f"\n🎉 مذهل! تم الوصول للحد الأقصى للاختبار بنجاح: {total_allocated_mb} MB بدون أي انهيار!")

    except MemoryError:
        print(f"\n🚨 وصل التطبيق إلى حد الذاكرة الأقصى المسموح به (MemoryError) عند: {total_allocated_mb} MB ({total_allocated_mb/1024.0:.2f} GB)!")
    except Exception as e:
        print(f"\n⚠️ توقف الاختبار لسبب غير متوقع: {e} عند {total_allocated_mb} MB")
    finally:
        print("\n🧹 جاري تحرير الذاكرة وتفعيل Garbage Collector...")
        chunks.clear()
        gc.collect()
        time.sleep(1)
        print("✅ تم استرجاع الذاكرة بالكامل بنجاح!\n")

if __name__ == "__main__":
    test_ram_limits()
