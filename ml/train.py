"""训练脚本：训练模型并用 MLflow 记录实验。

运行（在项目根目录下）：
    python ml/train.py
"""
import os

import joblib
import mlflow
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from data_pipeline import load_data, preprocess


def main():
    # 1. 读取超参数配置
    with open("ml/configs/config.yaml", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # 2. 加载数据 + 切分
    df = load_data()
    X, y = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=cfg["test_size"],
        random_state=cfg["random_state"],
        stratify=y,
    )

    # 3. 训练模型
    model = RandomForestClassifier(
        n_estimators=cfg["n_estimators"],
        random_state=cfg["random_state"],
    )
    model.fit(X_train, y_train)

    # 4. 评估
    acc = accuracy_score(y_test, model.predict(X_test))

    # 5. 保存模型
    os.makedirs("ml/registry", exist_ok=True)
    model_path = "ml/registry/model.pkl"
    joblib.dump(model, model_path)

    # 6. 用 MLflow 记录实验
    mlflow.set_experiment("iris-classification")
    with mlflow.start_run():
        mlflow.log_param("n_estimators", cfg["n_estimators"])
        mlflow.log_param("dataset_version", cfg["dataset_version"])
        mlflow.log_metric("accuracy", acc)
        mlflow.log_artifact(model_path)

    print(f"训练完成，准确率 accuracy = {acc:.4f}")


if __name__ == "__main__":
    main()
