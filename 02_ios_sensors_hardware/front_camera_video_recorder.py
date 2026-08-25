#!/usr/bin/env python3
"""
📹 Continuous Rear/Front Camera Video Recorder (Manual Stop)
Records high-definition video from the iPhone Back Camera (or Front Camera) continuously.
The recording will NOT stop until you tap the Stop button or press Enter!
Safely finalizes and saves the MP4 video, saves to Photos App, and opens the iOS Share Sheet.
"""

import time
import os
import sys
import datetime
import threading

def record_continuous_video():
    print("=" * 60)
    print("  📹 Continuous iPhone Video Recorder (Manual Stop)")
    print("=" * 60)

    try:
        import cv2
        import numpy as np
    except ImportError as e:
        print(f"❌ OpenCV (cv2) is required: {e}")
        return

    # 1. Select Camera Lens
    print("Select camera lens to use:")
    print("   [1] 📷 Back / Rear Camera (Default)")
    print("   [2] 🤳 Front / Selfie Camera")
    
    lens_choice = "1"
    try:
        user_in = input("👉 Enter choice (1/2, default: 1): ").strip()
        if user_in in ["1", "2"]:
            lens_choice = user_in
    except Exception:
        lens_choice = "1"

    camera_index = 0 if lens_choice == "1" else 1
    camera_name = "Back / Rear Camera" if camera_index == 0 else "Front / Selfie Camera"

    print(f"\n🚀 Initializing {camera_name} (Index: {camera_index})...")
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        fallback_index = 1 if camera_index == 0 else 0
        print(f"⚠️ Could not open Index {camera_index}, trying Index {fallback_index}...")
        cap = cv2.VideoCapture(fallback_index)

    if not cap.isOpened():
        print("❌ Unable to connect to iPhone camera stream.")
        return

    # 2. Read first test frame to acquire verified hardware dimensions
    print("🔍 Reading initial camera frame to lock exact sensor resolution...")
    ret, first_frame = cap.read()
    if not ret or first_frame is None:
        print("❌ Failed to grab frame from camera.")
        cap.release()
        return

    actual_height, actual_width = first_frame.shape[:2]
    fps = 30.0

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    prefix = "back_cam" if camera_index == 0 else "front_cam"
    output_filename = f"{prefix}_recording_{timestamp}.mp4"

    # Setup Video Writer with MP4 FourCC
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_filename, fourcc, fps, (actual_width, actual_height))
    
    # Write initial frame
    out.write(first_frame)
    frames_recorded = 1

    # Control flag
    is_recording = True

    def input_listener():
        nonlocal is_recording
        try:
            input()
            is_recording = False
        except Exception:
            pass

    listener_thread = threading.Thread(target=input_listener, daemon=True)
    listener_thread.start()

    print("\n" + "=" * 60)
    print(f"🔴 RECORDING STARTED ON {camera_name.upper()}!")
    print(f"   • Exact Resolution: {actual_width} x {actual_height} @ {fps:.0f} FPS")
    print(f"   • Target File     : {output_filename}")
    print("=" * 60)
    print("👉 To STOP recording: Press ENTER in console or tap the STOP button (⏹️) in Pyto.")
    print("-" * 60 + "\n")

    start_time = time.time()

    try:
        while is_recording:
            ret, frame = cap.read()
            if not ret or frame is None:
                time.sleep(0.01)
                continue

            out.write(frame)
            frames_recorded += 1
            elapsed = time.time() - start_time
            
            mins = int(elapsed // 60)
            secs = int(elapsed % 60)
            tenths = int((elapsed * 10) % 10)
            print(f"\r🔴 RECORDING: {mins:02d}:{secs:02d}.{tenths} | Frames: {frames_recorded:>5} | Press ENTER to Stop...", end="", flush=True)

            time.sleep(1.0 / (fps * 1.1))

    except (KeyboardInterrupt, SystemExit):
        print("\n\n⏹️ Stop command received via Pyto interface!")
    except Exception as e:
        print(f"\n⚠️ Note during recording: {e}")
    finally:
        is_recording = False
        print("\n⏳ Finalizing video encoding and writing MP4 headers...")
        
        try:
            out.release()
        except Exception:
            pass
        try:
            cap.release()
        except Exception:
            pass

        total_elapsed = time.time() - start_time
        print("\n" + "=" * 60)
        print("🎉 Video Recording Finalized Successfully!")
        print("=" * 60)
        print(f"   • Total Duration : {total_elapsed:.1f} seconds ({int(total_elapsed//60):02d}:{int(total_elapsed%60):02d})")
        print(f"   • Total Frames   : {frames_recorded:,} frames")
        
        if os.path.exists(output_filename):
            file_size_mb = os.path.getsize(output_filename) / (1024.0 * 1024.0)
            file_size_kb = os.path.getsize(output_filename) / 1024.0
            print(f"   • File Size      : {file_size_mb:.2f} MB ({file_size_kb:.1f} KB)")
            print(f"   • Full File Path : {os.path.abspath(output_filename)}")
            print("-" * 60)

            # 1. Save directly to iOS Photos App (Camera Roll)
            try:
                import photo_library
                if hasattr(photo_library, 'save_video'):
                    photo_library.save_video(output_filename)
                    print("📸 Successfully saved a copy to iPhone Photos App (Camera Roll)!")
            except Exception as pe:
                try:
                    import photos
                    if hasattr(photos, 'save_video'):
                        photos.save_video(output_filename)
                        print("📸 Successfully saved to iPhone Photos App!")
                except Exception:
                    pass

            # 2. Present iOS Share Sheet / Quick Look
            try:
                import sharing
                print("📤 Opening iOS Share Sheet to AirDrop, Preview, or Save...")
                if hasattr(sharing, 'share'):
                    sharing.share([output_filename])
                elif hasattr(sharing, 'quick_look'):
                    sharing.quick_look(output_filename)
            except Exception as se:
                print(f"ℹ️ Note: {se}")
        else:
            print("⚠️ Video file not found.")

        print(f"\n📂 File location: In Files app -> On My iPhone (or iCloud Drive) -> Pyto -> IOSPytoTesy -> {output_filename}\n")

if __name__ == "__main__":
    record_continuous_video()
