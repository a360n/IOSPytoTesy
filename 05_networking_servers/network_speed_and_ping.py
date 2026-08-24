#!/usr/bin/env python3
"""
📶 Network Latency & Throughput Benchmark
Measures TCP socket latency (Ping) to major DNS and cloud servers (Cloudflare, Google, Apple, GitHub)
and measures sustained HTTP download speed.
"""

import time
import socket
import urllib.request

def test_ping(host="1.1.1.1", port=53, timeout=3):
    """Measures TCP connection latency in ms"""
    t0 = time.time()
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        s.close()
        return (time.time() - t0) * 1000
    except Exception:
        return None

def test_network_benchmarks():
    print("=" * 60)
    print("  📶 Network Latency & Download Speed Benchmark")
    print("=" * 60)

    servers = [
        ("Cloudflare DNS", "1.1.1.1", 53),
        ("Google DNS", "8.8.8.8", 53),
        ("Apple Services", "apple.com", 80),
        ("GitHub Services", "github.com", 443),
    ]

    print("\n1️⃣ Measuring TCP Latencies:")
    for name, host, port in servers:
        latency = test_ping(host, port)
        if latency is not None:
            print(f"   🟢 {name:<18} ({host:<12}): {latency:>6.2f} ms")
        else:
            print(f"   🔴 {name:<18} ({host:<12}): Connection failed / Timed out")

    print("\n2️⃣ Testing HTTP Download Throughput:")
    test_url = "https://speed.cloudflare.com/__down?bytes=5000000"  # 5 MB
    print(f"⏳ Downloading 5 MB test payload from Cloudflare CDN...")
    try:
        t0 = time.time()
        req = urllib.request.Request(test_url, headers={'User-Agent': 'PytoSpeedTest'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        dt = time.time() - t0
        size_mb = len(data) / (1024 * 1024)
        speed_mbps = (size_mb * 8) / dt

        print(f"   ✅ Download completed in {dt:.2f} seconds")
        print(f"   🚀 Estimated Download Speed: {speed_mbps:.2f} Mbps ({size_mb/dt:.2f} MB/s)")
    except Exception as e:
        print(f"   ⚠️ Could not complete speed test: {e}")

    print("\n" + "=" * 60)
    print("✨ Network benchmark completed!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_network_benchmarks()
