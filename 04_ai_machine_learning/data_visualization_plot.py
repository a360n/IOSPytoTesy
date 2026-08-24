#!/usr/bin/env python3
"""
📊 Scientific Data Visualization & Chart Generation (Matplotlib)
Generates 4 publication-quality charts (trigonometric waveforms, 2D heatmaps, 3D bar indices, histograms)
and saves/renders them at high DPI inside Pyto.
"""

import os
import time

def test_data_visualization():
    print("=" * 60)
    print("  📊 Scientific Data Visualization (Matplotlib)")
    print("=" * 60)

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError as e:
        print(f"❌ Matplotlib or NumPy module not found: {e}")
        return

    print("🎨 Rendering charts and formatting layouts...")

    fig, axs = plt.subplots(2, 2, figsize=(12, 10), dpi=150)
    fig.suptitle("Pyto on iPhone 17 Pro Max - Data Science Showcase", fontsize=16, fontweight='bold')

    # 1. Trigonometric Waveforms
    x = np.linspace(0, 4 * np.pi, 200)
    y1 = np.sin(x)
    y2 = np.cos(x)
    axs[0, 0].plot(x, y1, label='Sin(x)', color='#007AFF', lw=2)
    axs[0, 0].plot(x, y2, label='Cos(x)', color='#FF9500', lw=2, linestyle='--')
    axs[0, 0].set_title("Trigonometric Waves")
    axs[0, 0].legend()
    axs[0, 0].grid(True, alpha=0.3)

    # 2. 2D Gaussian Heatmap
    data_heatmap = np.random.randn(20, 20)
    cax = axs[0, 1].imshow(data_heatmap, cmap='viridis', interpolation='nearest')
    fig.colorbar(cax, ax=axs[0, 1])
    axs[0, 1].set_title("2D Gaussian Heatmap")

    # 3. Hardware Performance Index Bar Chart
    categories = ['Single-Core', 'Multi-Core', 'OpenCV 1080p', 'ML Training', 'Disk I/O']
    scores = [95, 98, 92, 88, 94]
    axs[1, 0].bar(categories, scores, color=['#34C759', '#5856D6', '#AF52DE', '#FF2D55', '#5AC8FA'])
    axs[1, 0].set_ylim(0, 100)
    axs[1, 0].set_title("iPhone Hardware Performance Index (%)")
    axs[1, 0].tick_params(axis='x', rotation=25)

    # 4. Normal Distribution Histogram
    dist_data = np.random.normal(100, 15, 1000)
    axs[1, 1].hist(dist_data, bins=30, color='#FF3B30', alpha=0.7, edgecolor='black')
    axs[1, 1].set_title("Normal Distribution (1,000 Samples)")
    axs[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    output_filename = "pyto_benchmark_plot.png"
    plt.savefig(output_filename, bbox_inches='tight')
    plt.close('all')

    print(f"✅ Plot image saved successfully to: {os.path.abspath(output_filename)}")
    print(f"📂 Output file size: {os.path.getsize(output_filename) / 1024:.1f} KB")

    try:
        import sharing
        print("📤 Opening iOS Share Sheet to preview or save image...")
        sharing.share_file(output_filename)
    except Exception:
        pass

    print("\n" + "=" * 60)
    print("✨ Data visualization completed!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_data_visualization()
