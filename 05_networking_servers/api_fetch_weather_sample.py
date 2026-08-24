#!/usr/bin/env python3
"""
🌤️ REST API Client & JSON Parsing (Open-Meteo Weather Service)
Fetches live telemetry and meteorology data from public REST APIs,
parses JSON structures, and measures API round-trip latency.
"""

import urllib.request
import json
import time

def fetch_live_weather(lat=40.7128, lon=-74.0060, city_name="New York"):
    print("=" * 60)
    print(f"  🌤️ Live REST API Weather Client ({city_name})")
    print("=" * 60)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m&timezone=auto"

    print(f"📡 Sending HTTP GET request to: {url}")
    
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PytoWeatherClient/1.0"})
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
        print(f"🌡️ Weather Telemetry for ({city_name}):")
        print(f"   • Temperature         : {temp} °C")
        print(f"   • Apparent / Feels    : {feels_like} °C")
        print(f"   • Relative Humidity   : {humidity} %")
        print(f"   • Wind Speed (10m)    : {wind} km/h")
        print(f"   • Precipitation       : {precip} mm")
        print(f"   • API Latency         : {latency:.2f} ms")
        print("-" * 60)

    except Exception as e:
        print(f"❌ Network or parsing error: {e}")

    print("\n✨ Data fetching completed successfully!\n")

if __name__ == "__main__":
    fetch_live_weather()
