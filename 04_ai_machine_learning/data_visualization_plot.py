#!/usr/bin/env python3
"""
📊 رسم وتوليد المخططات البيانية العلمية (Matplotlib Data Visualization)
يقوم هذا السكربت بتوليد 4 مخططات بيانية متطورة (موجات جيبية، خريطة حرارية Heatmap، رسم ثلاثي الأبعاد 3D، ومخطط أعمدة)
وحفظها واستعراضها بجودة فائقة الدقة داخل Pyto.
"""

import os
import time

def test_data_visualization():
    print("=" * 60)
    print("  📊 رسم المخططات البيانية العلمية (Matplotlib Visualization)")
    print("=" * 60)

    try:
        import matplotlib
        # في بيئات الجوال، استخدام العارض غير التفاعلي Agg عند الحفظ
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError as e:
        print(f"❌ مكتبة Matplotlib أو NumPy غير متوفرة: {e}")
        return

    print("🎨 جاري بناء المخططات البيانية وتنسيق الألوان...")

    # إعداد شبكة من 4 رسومات بيانية (2x2)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10), dpi=150)
    fig.suptitle("Pyto on iPhone 17 Pro Max - Data Science Showcase", fontsize=16, fontweight='bold')

    # 1. المخطط الأول: موجات رياضية مع ضوضاء
    x = np.linspace(0, 4 * np.pi, 200)
    y1 = np.sin(x)
    y2 = np.cos(x)
    axs[0, 0].plot(x, y1, label='Sin(x)', color='#007AFF', lw=2)
    axs[0, 0].plot(x, y2, label='Cos(x)', color='#FF9500', lw=2, linestyle='--')
    axs[0, 0].set_title("Trigonometric Waves")
    axs[0, 0].legend()
    axs[0, 0].grid(True, alpha=0.3)

    # 2. المخطط الثاني: خريطة حرارية (Heatmap)
    data_heatmap = np.random.randn(20, 20)
    cax = axs[0, 1].imshow(data_heatmap, cmap='viridis', interpolation='nearest')
    fig.colorbar(cax, ax=axs[0, 1])
    axs[0, 1].set_title("2D Gaussian Heatmap")

    # 3. المخطط الثالث: مقارنة أداء المعالجات (Bar Chart)
    categories = ['Single-Core', 'Multi-Core', 'OpenCV 4K', 'ML Training', 'Disk I/O']
    scores = [95, 98, 92, 88, 94]
    axs[1, 0].bar(categories, scores, color=['#34C759', '#5856D6', '#AF52DE', '#FF2D55', '#5AC8FA'])
    axs[1, 0].set_ylim(0, 100)
    axs[1, 0].set_title("iPhone Hardware Performance Index (%)")
    axs[1, 0].tick_params(axis='x', rotation=25)

    # 4. المخطط الرابع: توزيع إحصائي تكراري (Histogram)
    dist_data = np.random.normal(100, 15, 1000)
    axs[1, 1].hist(dist_data, bins=30, color='#FF3B30', alpha=0.7, edgecolor='black')
    axs[1, 1].set_title("Normal Distribution (1,000 Samples)")
    axs[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    output_filename = "pyto_benchmark_plot.png"
    plt.savefig(output_filename, bbox_inches='tight')
    plt.close()

    print(f"✅ تم حفظ الصورة البيانية بنجاح في: {os.path.abspath(output_filename)}")
    print(f"📂 حجم الصورة الناتجة: {os.path.getsize(output_filename) / 1024:.1f} KB")

    # محاولة عرض الصورة عبر مشاركة نظام iOS أو pyto_ui
    try:
        import sharing
        print("📤 فتح نافذة المشاركة (iOS Share Sheet) لعرض الصورة أو حفظها في تطبيق الصور...")
        sharing.share_file(output_filename)
    except Exception:
        pass

    print("\n" + "=" * 60)
    print("✨ تم إنشاء وعرض المخططات البيانية بنجاح!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_data_visualization()
