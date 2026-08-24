#!/usr/bin/env python3
"""
⚡ Apple Shortcuts & Siri Automation Integration
Handles input parameters passed from the iOS Shortcuts app, processes them in Python,
and interfaces with the system clipboard and Siri triggers.
"""

import sys
import os

def run_shortcuts_integration():
    print("=" * 60)
    print("  ⚡ Apple Shortcuts & Siri Integration")
    print("=" * 60)

    # 1. Inspect command-line arguments passed via Shortcuts
    input_args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    print("📥 Input parameters received from Shortcuts:")
    if input_args:
        for i, arg in enumerate(input_args, 1):
            print(f"   • Argument {i}: {arg}")
    else:
        print("   ℹ️ No arguments passed via sys.argv (standalone execution).")

    # 2. Pasteboard / Clipboard check
    try:
        import pasteboard
        clip_text = pasteboard.string()
        print(f"\n📋 Current Clipboard Contents: \"{clip_text}\"")
    except ImportError:
        pass

    # 3. Shortcuts module check
    try:
        import shortcuts
        print("✅ The 'shortcuts' module is available for direct automation integration.")
    except ImportError:
        pass

    print("\n💡 How to integrate with Apple Shortcuts:")
    print("1. Open the 'Shortcuts' app on your iPhone and create a new Shortcut (+).")
    print("2. Add a 'Run Python Script' action and select the Pyto app.")
    print("3. Select this script file (shortcuts_integration.py) and pass input text/images.")
    print("4. Trigger it anytime via Siri voice command: 'Hey Siri, Run Pyto Script'!")
    
    print("\n" + "=" * 60)
    print("✨ Shortcuts integration check completed!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_shortcuts_integration()
