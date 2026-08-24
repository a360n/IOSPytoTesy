#!/usr/bin/env python3
"""
🌤️ جلب ومعالجة بيانات الطقس عبر واجهات REST API (HTTP Client & JSON Parsing)
يقوم هذا السكربت بإرسال طلبات HTTP غير متزامنة / متزامنة لجلب بيانات حية
عبر Open-Meteo API المجاني وتنسيقها بشكل جميل.
"""

import urllib.request
import json
import time

def fetch_live_weather(lat=24.7136, lon=46.6753, city_name="الرياض"):
    print("=" * 60)
    print(f"  🌤️ جلب حالة الطقس المباشرة لمدينة {city_name} (REST API)")
    print("=" * 60)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m&timezone=auto"

    print(f"📡 إرسال طلب HTTP GET إلى: {url}")
    
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PytoWeatherApp/1.0"})
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode("utf-8"))
        
        latency = (time.time() - t0) * 1000
        current = data.get("current", {})

        temp = current.get("temperature_2m", "--")
        feels_like = current.get("apparent_temperature", "--")
        humidity = current.get("relative_humidity_2m", "--")
        wind = current.get("wind_speed_10m", "--")
        precip = current.get("precipitation", "--")

        print("\n" + "-" * 60)
        print(f"🌡️ بيانات الطقس الحالية لـ ({city_name}):")
        print(f"   • درجة الحرارة الفعلية  : {temp} °C")
        print(f"   • الحرارة المحسوسة     : {feels_like} °C")
        print(f"   • نسبة الرطوبة          : {humidity} %")
        print(f"   • سرعة الرياح           : {wind} كم/ساعة")
        print(f"   • معدل هطول الأمطار     : {precip} مم")
        print(f"   • زمن استجابة الـ API    : {latency:.2f} ms")
        print("-" * 60)

    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاتصال بالخادم: {e}")

    print("\n✨ اكتمل جلب البيانات بنجاح!\n")

if __name__ == "__main__":
    fetch_live_weather()
