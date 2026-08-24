#!/usr/bin/env python3
"""
🧠 اختبار تدريب نماذج الذكاء الاصطناعي على الآيفون (On-Device Machine Learning)
يقوم هذا السكربت بتدريب وتقييم نماذج تعلم الآلة (Random Forest, K-Means, Logistic Regression)
مباشرة وبشكل كامل على معالج الآيفون بدون الحاجة لأي إنترنت أو خوادم سحابية!
"""

import time

def test_machine_learning():
    print("=" * 60)
    print("  🧠 اختبار تدريب نماذج تعلم الآلة (Scikit-Learn ML Training)")
    print("=" * 60)

    try:
        from sklearn.datasets import make_classification, make_blobs
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.cluster import KMeans
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import accuracy_score
        import numpy as np
    except ImportError as e:
        print(f"❌ مكتبة scikit-learn غير متوفرة: {e}")
        print("💡 لتثبيتها في Pyto، افتح Pyto Settings -> PyPi وابحث عن scikit-learn.")
        return

    n_samples = 15000
    n_features = 20
    print(f"📊 توليد بيانات تدريب اصطناعية: {n_samples:,} عينة مع {n_features} ميزة...")

    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=12,
        n_redundant=4,
        random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 1. تدريب نموذج Logistic Regression
    print("\n1️⃣ تدريب نموذج الانحدار اللوجستي (Logistic Regression)...")
    t0 = time.time()
    lr = LogisticRegression(max_iter=500)
    lr.fit(X_train, y_train)
    t_lr_train = time.time() - t0
    y_pred_lr = lr.predict(X_test)
    acc_lr = accuracy_score(y_test, y_pred_lr)
    print(f"   ⏱️ وقت التدريب : {t_lr_train:.3f} ثانية")
    print(f"   🎯 دقة التنبؤ  : {acc_lr * 100:.2f}%")

    # 2. تدريب نموذج الغابة العشوائية (Random Forest - 50 Trees)
    print("\n2️⃣ تدريب نموذج الغابة العشوائية (Random Forest - 50 أشجار)...")
    t0 = time.time()
    rf = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    t_rf_train = time.time() - t0
    
    t0 = time.time()
    y_pred_rf = rf.predict(X_test)
    t_rf_infer = (time.time() - t0) * 1000
    acc_rf = accuracy_score(y_test, y_pred_rf)
    
    print(f"   ⏱️ وقت التدريب : {t_rf_train:.3f} ثانية")
    print(f"   ⚡ سرعة التنبؤ  : {t_rf_infer:.2f} ms لـ {len(X_test):,} عينة اختبار")
    print(f"   🎯 دقة التنبؤ  : {acc_rf * 100:.2f}%")

    # 3. التجميع العنقودي غير الخاضع للإشراف (K-Means Clustering)
    print("\n3️⃣ تدريب التجميع العنقودي (K-Means Clustering - 5 Clusters)...")
    X_cluster, _ = make_blobs(n_samples=10000, centers=5, n_features=10, random_state=42)
    t0 = time.time()
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    kmeans.fit(X_cluster)
    t_kmeans = time.time() - t0
    print(f"   ⏱️ وقت تجميع 10,000 نقطة: {t_kmeans:.3f} ثانية")

    print("\n" + "=" * 60)
    print("🏆 ملخص أداء معالج الآيفون في تدريب الذكاء الاصطناعي:")
    print(f"   • تم تدريب 3 نماذج على {n_samples + 10000:,} عينة بنجاح كامل.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_machine_learning()
