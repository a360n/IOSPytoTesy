#!/usr/bin/env python3
"""
📹 Continuous Rear/Front Camera Video Recorder (Manual Stop)
Records high-definition video from the iPhone Back Camera (or Front Camera) continuously.
The recording will NOT stop until you tap the Stop button or press Enter!
Safely finalizes and saves the MP4 video and opens the iOS Share Sheet.
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
    # Provide quick default or user input
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

    # Frame properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 1280
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 720
    fps = 30.0

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    prefix = "back_cam" if camera_index == 0 else "front_cam"
    output_filename = f"{prefix}_recording_{timestamp}.mp4"

    # Setup Video Writer with MP4 codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

    # Control flag
    is_recording = True

    def input_listener():
        """Allows stopping via Enter / return in console"""
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
    print(f"   • Resolution: {frame_width} x {frame_height} @ {fps:.0f} FPS")
    print(f"   • Output    : {output_filename}")
    print("=" * 60)
    print("👉 To STOP recording: Press ENTER in console or tap the STOP button (⏹️) in Pyto.")
    print("-" * 60 + "\n")

    start_time = time.time()
    frames_recorded = 0

    try:
        while is_recording:
            ret, frame = cap.read()
            if not ret or frame is None:
                # Brief retry to prevent random drop
                time.sleep(0.01)
                continue

            out.write(frame)
            frames_recorded += 1
            elapsed = time.time() - start_time
            
            # Format time display MM:SS.d
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
        
        # Cleanly release hardware and flush video buffers
        try:
            cap.release()
        except Exception:
            pass
        try:
            out.release()
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
            print(f"   • File Size      : {file_size_mb:.2f} MB")
            print(f"   • File Path      : {os.path.abspath(output_filename)}")
            print("-" * 60)

            # Present iOS Share Sheet to save or share video
            try:
                import sharing
                print("📤 Opening iOS Share Sheet to preview, save to Camera Roll, or AirDrop...")
                sharing.share_file(output_filename)
            except Exception as se:
                print(f"ℹ️ Share sheet note: {se}")
        else:
            print("⚠️ Video file not found.")

        print("\n✨ Ready!\n")

if __name__ == "__main__":
    record_continuous_video()
