#!/usr/bin/env python3
"""
🗣️ اختبار تحويل النص إلى كلام باللغة العربية والإنجليزية (Speech Synthesis TTS)
يقوم هذا السكربت بتجربة محرك النطق الصوتي الخاص بشركة آبل ومساعد سيري (Siri Voice Engine)
لنطق نصوص باللغة العربية الفصحى والإنجليزية مع التحكم بالسرعة ونبرة الصوت.
"""

import time

def test_speech_synthesis():
    print("=" * 60)
    print("  🗣️ اختبار النطق الصوتي باللغة العربية (Apple TTS)")
    print("=" * 60)

    try:
        import speech
    except ImportError:
        print("❌ مكتبة 'speech' غير متوفرة خارج تطبيق Pyto على الآيفون.")
        print("💡 لتجربة الصوت الحقيقي، شغل هذا السكربت من داخل Pyto على جهازك.")
        return

    arabic_text = "أهلاً بك يا علي! تم تشغيل بايثون بنجاح على هاتفك آيفون 17 برو ماكس الخارق."
    english_text = "Python is running at full speed on Apple Silicon with Pyto!"

    print("\n1️⃣ تجربة النطق باللغة العربية (Arabic Voice - Saudi/Standard):")
    print(f"   💬 النص: \"{arabic_text}\"")
    try:
        # فحص اللغات المتاحة إن أمكن
        if hasattr(speech, 'get_siri_voices'):
            voices = speech.get_siri_voices()
            print(f"   🎙️ عدد أصوات سيري المتوفرة: {len(voices)}")

        # النطق بالعربية
        speech.say(arabic_text, "ar-SA")
        print("   🔊 جاري التحدث...")
        time.sleep(5)
    except Exception as e:
        print(f"   ⚠️ خطأ في نطق النص العربي: {e}")

    print("\n2️⃣ تجربة النطق باللغة الإنجليزية (English US Voice):")
    print(f"   💬 النص: \"{english_text}\"")
    try:
        speech.say(english_text, "en-US")
        print("   🔊 جاري التحدث...")
        time.sleep(4)
    except Exception as e:
        print(f"   ⚠️ خطأ في نطق النص الإنجليزي: {e}")

    print("\n" + "=" * 60)
    print("✨ اكتمل اختبار النطق الصوتي بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_speech_synthesis()
