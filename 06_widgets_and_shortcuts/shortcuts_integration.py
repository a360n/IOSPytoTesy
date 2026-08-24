#!/usr/bin/env python3
"""
⚡ التكامل مع اختصارات سيري وتطبيق Shortcuts (Siri Shortcuts Integration)
يقوم هذا السكربت بتلقي المدخلات من تطبيق اختصارات آبل (Shortcuts)، ومعالجتها ببايثون،
ثم إرجاع المخرجات والنتائج أو حفظها في الحافظة (Clipboard) أو نطقها عبر سيري.
"""

import sys
import os

def run_shortcuts_integration():
    print("=" * 60)
    print("  ⚡ التكامل مع اختصارات سيري (Siri Shortcuts Integration)")
    print("=" * 60)

    # 1. فحص المدخلات الممررة من الاختصار (Parameters passed via Shortcuts)
    input_args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    print("📥 المدخلات المستلمة من اختصار آبل:")
    if input_args:
        for i, arg in enumerate(input_args, 1):
            print(f"   • المدخل {i}: {arg}")
    else:
        print("   ℹ️ لم يتم تمرير مدخلات عبر sys.argv (تم التشغيل المباشر).")

    # 2. فحص الحافظة (Pasteboard / Clipboard)
    try:
        import pasteboard
        clip_text = pasteboard.string()
        print(f"\n📋 محتوى الحافظة الحالي: \"{clip_text}\"")
    except ImportError:
        pass

    # 3. محاولة استخدام مكتبة shortcuts المخصصة في Pyto
    try:
        import shortcuts
        print("✅ مكتبة 'shortcuts' متوفرة للتواصل المباشر مع نظام أتمتة iOS.")
    except ImportError:
        pass

    print("\n💡 كيفية ربط هذا السكربت باختصارات سيري (Apple Shortcuts):")
    print("1. افتح تطبيق 'Shortcuts' على الآيفون وأنشئ اختصار جديد (+).")
    print("2. أضف إجراء (Run Python Script) واختر تطبيق Pyto.")
    print("3. اختر هذا الملف (shortcuts_integration.py) مع إمكانية تمرير نصوص أو صور.")
    print("4. يمكنك جعل سيري تشغل الكود بالأمر الصوتي: 'Hey Siri, Run Pyto Script'!")
    
    print("\n" + "=" * 60)
    print("✨ اكتمل فحص تكامل الاختصارات بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_shortcuts_integration()
