#!/usr/bin/env python3
"""
📸 Native Camera Capture & Image Processing
Opens the native iOS Camera viewfinder directly from Python, allows you to capture a live photo,
and processes/displays image metadata (resolution, dimensions, color channels).
"""

import os
import time

def capture_live_camera():
    print("=" * 60)
    print("  📸 Native iOS Camera Capture")
    print("=" * 60)

    try:
        import photo_library
    except ImportError:
        try:
            import photos as photo_library
        except ImportError:
            print("❌ The 'photo_library' module is only available inside Pyto on iOS.")
            print("💡 Run this script inside the Pyto app on your iPhone.")
            return

    print("🚀 Launching native iOS Camera viewfinder...")
    print("📸 Please snap a photo or tap Cancel...")

    try:
        # Launch native camera viewfinder
        if hasattr(photo_library, 'take_photo'):
            captured_image = photo_library.take_photo()
        elif hasattr(photo_library, 'capture_image'):
            captured_image = photo_library.capture_image()
        else:
            print("⚠️ 'take_photo' method not found in photo_library.")
            return

        if captured_image is not None:
            print("\n" + "-" * 60)
            print("🎉 Photo captured successfully from iPhone camera!")
            
            # Analyze image properties if PIL is available
            try:
                from PIL import Image
                if isinstance(captured_image, Image.Image):
                    width, height = captured_image.size
                    mode = captured_image.mode
                    print(f"   • Resolution  : {width} x {height} pixels ({width*height/1e6:.1f} Megapixels)")
                    print(f"   • Color Format: {mode}")
                    
                    # Save to local file
                    output_path = "captured_camera_photo.jpg"
                    captured_image.save(output_path, quality=95)
                    print(f"   • Saved to    : {os.path.abspath(output_path)} ({os.path.getsize(output_path)/1024:.1f} KB)")
                    
                    # Open share sheet or preview
                    try:
                        import sharing
                        print("📤 Opening iOS Share Sheet to preview or save to Camera Roll...")
                        sharing.share_file(output_path)
                    except Exception:
                        pass
            except Exception as e:
                print(f"   ℹ️ Image received: {type(captured_image)} ({e})")
            print("-" * 60)
        else:
            print("ℹ️ Camera capture was cancelled by user.")

    except Exception as e:
        print(f"❌ Error during camera capture: {e}")

    print("\n✨ Camera capture test completed!\n")

if __name__ == "__main__":
    capture_live_camera()
