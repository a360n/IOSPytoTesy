#!/usr/bin/env python3
"""
📶 اختبار سرعة وزمن استجابة الشبكة (Network Latency & Download Benchmark)
يقوم هذا السكربت بقياس سرعة الاتصال بالإنترنت، وزمن استجابة الـ DNS و Ping
إلى سيرفرات كبرى (Apple, Cloudflare, Google).
"""

import time
import socket
import urllib.request

def test_ping(host="1.1.1.1", port=53, timeout=3):
    """قياس زمن الاستجابة لمقبس TCP (Socket Ping)"""
    t0 = time.time()
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        s.close()
        return (time.time() - t0) * 1000
    except Exception:
        return None

def test_network_benchmarks():
    print("=" * 60)
    print("  📶 اختبار زمن الاستجابة وسرعة الشبكة (Network Benchmarks)")
    print("=" * 60)

    # 1. اختبار زمن استجابة الـ Ping
    servers = [
        ("Cloudflare DNS", "1.1.1.1", 53),
        ("Google DNS", "8.8.8.8", 53),
        ("Apple Services", "apple.com", 80),
        ("GitHub Services", "github.com", 443),
    ]

    print("\n1️⃣ قياس أزمنة الاستجابة (TCP Latency):")
    for name, host, port in servers:
        latency = test_ping(host, port)
        if latency is not None:
            print(f"   🟢 {name:<18} ({host:<12}): {latency:>6.2f} ms")
        else:
            print(f"   🔴 {name:<18} ({host:<12}): فشل الاتصال / لا يوجد استجابة")

    # 2. اختبار سرعة تنزيل حزمة بيانات صغيرة
    print("\n2️⃣ اختبار سرعة التحميل الفعلي (HTTP Download Speed):")
    test_url = "https://speed.cloudflare.com/__down?bytes=5000000"  # 5 MB
    print(f"⏳ جاري تحميل ملف تجريبي بحجم 5 MB من Cloudflare...")
    try:
        t0 = time.time()
        req = urllib.request.Request(test_url, headers={'User-Agent': 'PytoSpeedTest'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        dt = time.time() - t0
        size_mb = len(data) / (1024 * 1024)
        speed_mbps = (size_mb * 8) / dt

        print(f"   ✅ تم التحميل بنجاح خلال {dt:.2f} ثانية")
        print(f"   🚀 سرعة التحميل التقديرية: {speed_mbps:.2f} Mbps ({size_mb/dt:.2f} MB/s)")
    except Exception as e:
        print(f"   ⚠️ تعذر قياس سرعة التحميل: {e}")

    print("\n" + "=" * 60)
    print("✨ اكتمل فحص الشبكة بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_network_benchmarks()
