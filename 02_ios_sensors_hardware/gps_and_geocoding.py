#!/usr/bin/env python3
"""
📍 GPS Location & Reverse Geocoding
Queries the high-precision iPhone GPS receiver (latitude, longitude, altitude, accuracy, speed)
and converts coordinates into physical addresses via Apple Maps Reverse Geocoding.
"""

import time

def test_gps_location():
    print("=" * 60)
    print("  📍 GPS Location & Reverse Geocoding")
    print("=" * 60)

    try:
        import location
    except ImportError:
        print("❌ The 'location' module is only available in Pyto on iOS.")
        print("💡 Run this script inside the Pyto app on your iPhone.")
        return

    print("🛰️ Requesting GPS authorization and activating receiver...")
    
    try:
        location.start_updating()
        print("⏳ Acquiring satellite fix (waiting 2 seconds)...")
        time.sleep(2)

        loc = location.get_location()
        if not loc:
            print("⚠️ No fix yet, retrying...")
            time.sleep(2)
            loc = location.get_location()

        if loc:
            lat = loc.get("latitude", 0.0)
            lon = loc.get("longitude", 0.0)
            altitude = loc.get("altitude", 0.0)
            h_acc = loc.get("horizontal_accuracy", 0.0)
            v_acc = loc.get("vertical_accuracy", 0.0)
            speed = loc.get("speed", 0.0)
            course = loc.get("course", 0.0)

            print("\n" + "-" * 60)
            print("🎯 GPS Telemetry Received:")
            print(f"   • Latitude    : {lat:.6f}°")
            print(f"   • Longitude   : {lon:.6f}°")
            print(f"   • Altitude    : {altitude:.1f} m above sea level")
            print(f"   • Accuracy    : ±{h_acc:.1f} m")
            print(f"   • Speed       : {max(0, speed) * 3.6:.1f} km/h")
            print(f"   • Course      : {course:.1f}°")
            print("-" * 60)

            print("\n🗺️ Querying Apple Maps Reverse Geocoding...")
            try:
                places = location.reverse_geocode(loc)
                if places and len(places) > 0:
                    place = places[0]
                    print(f"   🏢 Name / Street : {place.get('name', 'N/A')}")
                    print(f"   🏙️ Locality      : {place.get('locality', place.get('subLocality', 'N/A'))}")
                    print(f"   🏛️ State / Region: {place.get('administrativeArea', 'N/A')}")
                    print(f"   🌍 Country       : {place.get('country', 'N/A')} ({place.get('isoCountryCode', '')})")
                else:
                    print("ℹ️ Coordinates acquired, but reverse geocoding returned no placemarks.")
            except Exception as ge:
                print(f"ℹ️ Geocoding note: {ge}")

            maps_url = f"https://maps.apple.com/?q={lat},{lon}"
            print(f"\n🔗 Apple Maps URL: {maps_url}")

        else:
            print("❌ Unable to acquire GPS fix. Ensure Location Services permission is granted to Pyto in iOS Settings.")

    except Exception as e:
        print(f"❌ Error during GPS lookup: {e}")
    finally:
        try:
            location.stop_updating()
        except Exception:
            pass
        print("\n✅ GPS service stopped cleanly.")

if __name__ == "__main__":
    test_gps_location()
