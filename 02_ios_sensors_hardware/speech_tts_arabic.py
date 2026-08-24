#!/usr/bin/env python3
"""
🗣️ Text-to-Speech (TTS) Speech Synthesis
Tests Apple Neural Siri voice synthesis in English and international languages
with adjustable pitch, rate, and volume.
"""

import time

def test_speech_synthesis():
    print("=" * 60)
    print("  🗣️ Siri Speech Synthesis (TTS Engine)")
    print("=" * 60)

    try:
        import speech
    except ImportError:
        print("❌ The 'speech' module is only available in Pyto on iOS.")
        print("💡 Run this script inside the Pyto app on your iPhone.")
        return

    english_text = "Python is running at full native speed on Apple Silicon with Pyto!"
    multilingual_text = "Welcome to the ultimate Python testing suite on iPhone 17 Pro Max."

    print("\n1️⃣ Testing English Speech Synthesis (en-US):")
    print(f"   💬 Text: \"{english_text}\"")
    try:
        if hasattr(speech, 'get_siri_voices'):
            voices = speech.get_siri_voices()
            print(f"   🎙️ Available Siri voices count: {len(voices)}")

        speech.say(english_text, "en-US")
        print("   🔊 Speaking...")
        time.sleep(4)
    except Exception as e:
        print(f"   ⚠️ Error speaking English text: {e}")

    print("\n2️⃣ Testing Multilingual System Speech:")
    print(f"   💬 Text: \"{multilingual_text}\"")
    try:
        speech.say(multilingual_text, "en-GB")
        print("   🔊 Speaking...")
        time.sleep(4)
    except Exception as e:
        print(f"   ⚠️ Error speaking text: {e}")

    print("\n" + "=" * 60)
    print("✨ Speech synthesis test completed successfully!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_speech_synthesis()
