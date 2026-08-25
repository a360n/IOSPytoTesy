#!/usr/bin/env python3
"""
📹 Front Camera Video Recorder & iOS Privacy Architecture
Demonstrates video recording from the Front Facing camera, explains iOS background privacy limits,
and captures video/frames into MP4 files.
"""

import time
import os
import sys

def record_front_camera_video(duration_seconds=5, output_filename="front_camera_recording.mp4"):
    print("=" * 60)
    print("  📹 Front Camera Video Recording Engine")
    print("=" * 60)

    print("\n🔒 [Important iOS Security & Privacy Note]:")
    print("   • Apple iOS kernel strictly forbids any app from accessing the camera")
    print("     silently in the background while another app is active or screen is locked.")
    print("   • When an app transitions to the background, iOS automatically revokes")
    print("     AVCaptureSession camera access (Hardware Privacy Indicator / Green Dot).")
    print("   • Audio recording and GPS tracking CAN run in the background, but camera")
    print("     video capture requires an active foreground session on iOS.\n")
    print("-" * 60)

    # 1. Background Task Registration in Pyto
    try:
        import background
        print("⚡ Requesting iOS Background Task Execution token...")
        background.start_background_task()
        print("   ✅ Background task capability enabled in Pyto.")
    except ImportError:
        print("   ℹ️ 'background' module is specific to Pyto on iOS.")
    except Exception as e:
        print(f"   ℹ️ Background token: {e}")

    # 2. Front Camera Capture via OpenCV
    print(f"\n🎥 Initializing Front Camera (Device Index: 1) for {duration_seconds} seconds...")
    try:
        import cv2
        import numpy as np

        # Index 1 = Front Camera on iOS / Mobile devices, 0 = Back Camera
        cap = cv2.VideoCapture(1)

        if not cap.isOpened():
            print("⚠️ Front camera (Index 1) not opened, falling back to camera Index 0...")
            cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("❌ Camera device could not be opened directly via cv2.VideoCapture.")
            print("💡 Tip: Use 'launch_native_camera.py' or Pyto's photo_library for native UI capture.")
            return

        # Fetch actual camera resolution
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 1280
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 720
        fps = 30.0

        print(f"   • Sensor Resolution : {frame_width} x {frame_height}")
        print(f"   • Frame Rate        : {fps} FPS")

        # Setup MP4 Video Writer (H.264 / mp4v codec)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

        print(f"\n🔴 RECORDING IN PROGRESS ({duration_seconds} seconds)...")
        start_time = time.time()
        frames_recorded = 0

        while (time.time() - start_time) < duration_seconds:
            ret, frame = cap.read()
            if not ret or frame is None:
                break
            
            # Write frame to video stream
            out.write(frame)
            frames_recorded += 1
            elapsed = time.time() - start_time
            print(f"\r   ⏱️ Elapsed: {elapsed:>4.1f}s / {duration_seconds}s | Frames: {frames_recorded}", end="")
            time.sleep(1.0 / fps)

        print("\n\n⏹️ Recording completed successfully!")
        cap.release()
        out.release()

        if os.path.exists(output_filename) and os.path.getsize(output_filename) > 0:
            file_size_kb = os.path.getsize(output_filename) / 1024.0
            print("-" * 60)
            print("🎉 Video File Summary:")
            print(f"   • File Name   : {output_filename}")
            print(f"   • Total Frames: {frames_recorded}")
            print(f"   • File Size   : {file_size_kb:.1f} KB")
            print(f"   • Location    : {os.path.abspath(output_filename)}")
            print("-" * 60)

            # Share sheet preview
            try:
                import sharing
                print("📤 Opening iOS Share Sheet to preview or save to Camera Roll...")
                sharing.share_file(output_filename)
            except Exception:
                pass
        else:
            print("⚠️ Video file was empty or not generated.")

    except ImportError:
        print("❌ OpenCV (cv2) is required for frame-level video recording.")
    except Exception as e:
        print(f"❌ Error during video recording: {e}")

if __name__ == "__main__":
    record_front_camera_video()
