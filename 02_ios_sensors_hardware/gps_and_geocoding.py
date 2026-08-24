#!/usr/bin/env python3
"""
📍 اختبار الموقع الجغرافي والـ GPS وعكس الإحداثيات (GPS & Geocoding)
يقوم هذا السكربت بالحصول على إحداثيات الـ GPS الدقيقة للآيفون (خط الطول، العرض، الارتفاع، السرعة)
وتحويلها إلى عنوان بشري فعلي (اسم الشارع، المدينة، الدولة) عبر تقنية Reverse Geocoding.
"""

import time

def test_gps_location():
    print("=" * 60)
    print("  📍 اختبار الـ GPS والموقع الجغرافي (GPS & Geocoding)")
    print("=" * 60)

    try:
        import location
    except ImportError:
        print("❌ مكتبة 'location' غير متوفرة خارج تطبيق Pyto على نظام iOS.")
        print("💡 لتجربة هذا الاختبار، قم بتشغيل السكربت من داخل تطبيق Pyto على الآيفون.")
        return

    print("🛰️ جاري طلب إذن وتفعيل رقاقة الـ GPS عالية الدقة...")
    
    try:
        location.start_updating()
        print("⏳ جاري استقبال إشارات الأقمار الصناعية (انتظر ثانيتين)...")
        time.sleep(2)

        loc = location.get_location()
        if not loc:
            print("⚠️ لم يتم استلام إحداثيات بعد، جاري المحاولة مرة أخرى...")
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
            print("🎯 بيانات الـ GPS المستلمة بنجاح:")
            print(f"   • خط العرض (Latitude)    : {lat:.6f}°")
            print(f"   • خط الطول (Longitude)   : {lon:.6f}°")
            print(f"   • الارتفاع (Altitude)     : {altitude:.1f} متر فوق مستوى البحر")
            print(f"   • دقة التحديد (Accuracy) : ±{h_acc:.1f} متر")
            print(f"   • السرعة الحالية (Speed) : {max(0, speed) * 3.6:.1f} كم/ساعة")
            print(f"   • الاتجاه (Heading)       : {course:.1f}°")
            print("-" * 60)

            # محاولة تحويل الإحداثيات إلى اسم المدينة والعنوان
            print("\n🗺️ جاري الاتصال بخدمة Apple Maps للتعرف على العنوان (Reverse Geocoding)...")
            try:
                places = location.reverse_geocode(loc)
                if places and len(places) > 0:
                    place = places[0]
                    print(f"   🏢 اسم المكان/الشارع: {place.get('name', 'غير محدد')}")
                    print(f"   🏙️ المدينة / الحي   : {place.get('locality', place.get('subLocality', 'غير محدد'))}")
                    print(f"   🏛️ المقاطعة / الولاية : {place.get('administrativeArea', 'غير محدد')}")
                    print(f"   🌍 الدولة            : {place.get('country', 'غير محدد')} ({place.get('isoCountryCode', '')})")
                else:
                    print("ℹ️ تم جلب الإحداثيات ولكن تعذر الحصول على تفاصيل العنوان النصي.")
            except Exception as ge:
                print(f"ℹ️ تعذر تحويل العنوان: {ge}")

            # رابط مباشر لخريطة آبل
            maps_url = f"https://maps.apple.com/?q={lat},{lon}"
            print(f"\n🔗 رابط خريطة آبل المباشر: {maps_url}")

        else:
            print("❌ تعذر التقاط الموقع. تأكد من تفعيل خدمات الموقع (Location Services) لتطبيق Pyto من إعدادات الآيفون.")

    except Exception as e:
        print(f"❌ حدث خطأ أثناء فحص الـ GPS: {e}")
    finally:
        try:
            location.stop_updating()
        except Exception:
            pass
        print("\n✅ تم إيقاف خدمة الـ GPS بنجاح.")

if __name__ == "__main__":
    test_gps_location()
