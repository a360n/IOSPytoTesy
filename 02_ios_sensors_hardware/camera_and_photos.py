#!/usr/bin/env python3
"""
📸 اختبار مكتبة الصور والوسائط (Camera & Photo Library Test)
يقوم هذا السكربت بفحص إمكانيات الوصول لمكتبة صور الآيفون والتقاط الصور أو استعراضها.
"""

def test_photos_and_camera():
    print("=" * 60)
    print("  📸 اختبار مكتبة الصور والكاميرا (Photo Library)")
    print("=" * 60)

    try:
        import photo_library
        print("✅ مكتبة 'photo_library' متوفرة ومدعومة في Pyto.")
        print("💡 تتيح هذه المكتبة استعراض ألبومات الصور، اختيار الصور، وتحريرها برمجياً.")
        
        # محاولة فحص دوال المكتبة
        methods = [m for m in dir(photo_library) if not m.startswith('_')]
        print(f"🛠️ الدوال المتاحة في المكتبة: {', '.join(methods)}")
        
    except ImportError:
        try:
            import photos
            print("✅ مكتبة 'photos' متوفرة.")
        except ImportError:
            print("ℹ️ مكتبة الصور مخصصة للعمل على نظام iOS داخل تطبيق Pyto.")

    print("\n" + "=" * 60)
    print("✨ تم فحص واجهة مكتبة الصور بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_photos_and_camera()
