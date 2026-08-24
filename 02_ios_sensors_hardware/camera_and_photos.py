#!/usr/bin/env python3
"""
📸 Camera & Photo Library Integration
Inspects interfaces for capturing photos and accessing user media albums within Pyto.
"""

def test_photos_and_camera():
    print("=" * 60)
    print("  📸 Photo Library & Camera Interface")
    print("=" * 60)

    try:
        import photo_library
        print("✅ The 'photo_library' module is available in Pyto.")
        print("💡 Allows programmatic access to pick, edit, and export photos.")
        
        methods = [m for m in dir(photo_library) if not m.startswith('_')]
        print(f"🛠️ Available API functions: {', '.join(methods)}")
        
    except ImportError:
        try:
            import photos
            print("✅ The 'photos' module is available.")
        except ImportError:
            print("ℹ️ Photo library module is designed for iOS Pyto.")

    print("\n" + "=" * 60)
    print("✨ Photo library inspection completed!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_photos_and_camera()
