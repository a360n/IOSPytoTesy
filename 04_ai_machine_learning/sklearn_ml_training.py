#!/usr/bin/env python3
"""
🧠 On-Device Machine Learning Benchmark (Scikit-Learn)
Trains and benchmarks Machine Learning models (Random Forest, Logistic Regression, K-Means Clustering)
entirely on the iPhone CPU without requiring external cloud servers or internet.
"""

import time

def test_machine_learning():
    print("=" * 60)
    print("  🧠 On-Device Machine Learning (Scikit-Learn Benchmark)")
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
        print(f"❌ scikit-learn not available: {e}")
        print("💡 To install in Pyto, go to Pyto Settings -> PyPi and install scikit-learn.")
        return

    n_samples = 15000
    n_features = 20
    print(f"📊 Generating synthetic training dataset: {n_samples:,} samples with {n_features} features...")

    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=12,
        n_redundant=4,
        random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 1. Logistic Regression
    print("\n1️⃣ Training Logistic Regression Model...")
    t0 = time.time()
    lr = LogisticRegression(max_iter=500)
    lr.fit(X_train, y_train)
    t_lr_train = time.time() - t0
    y_pred_lr = lr.predict(X_test)
    acc_lr = accuracy_score(y_test, y_pred_lr)
    print(f"   ⏱️ Training Time : {t_lr_train:.3f} s")
    print(f"   🎯 Accuracy      : {acc_lr * 100:.2f}%")

    # 2. Random Forest (50 Trees)
    print("\n2️⃣ Training Random Forest Classifier (50 Trees)...")
    t0 = time.time()
    rf = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    t_rf_train = time.time() - t0
    
    t0 = time.time()
    y_pred_rf = rf.predict(X_test)
    t_rf_infer = (time.time() - t0) * 1000
    acc_rf = accuracy_score(y_test, y_pred_rf)
    
    print(f"   ⏱️ Training Time : {t_rf_train:.3f} s")
    print(f"   ⚡ Inference Time: {t_rf_infer:.2f} ms for {len(X_test):,} test samples")
    print(f"   🎯 Accuracy      : {acc_rf * 100:.2f}%")

    # 3. K-Means Clustering
    print("\n3️⃣ Training Unsupervised K-Means Clustering (5 Clusters)...")
    X_cluster, _ = make_blobs(n_samples=10000, centers=5, n_features=10, random_state=42)
    t0 = time.time()
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    kmeans.fit(X_cluster)
    t_kmeans = time.time() - t0
    print(f"   ⏱️ Clustering Time (10,000 pts): {t_kmeans:.3f} s")

    print("\n" + "=" * 60)
    print("🏆 On-Device Machine Learning Benchmark Summary:")
    print(f"   • Successfully trained 3 models across {n_samples + 10000:,} samples.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    test_machine_learning()
