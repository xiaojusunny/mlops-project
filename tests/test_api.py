"""测试 API 端点。"""
import os

import joblib
import pytest
from fastapi.testclient import TestClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from ml.data_pipeline import load_data, preprocess


@pytest.fixture(scope="module", autouse=True)
def ensure_model():
    """测试前先保证有模型文件。"""
    X, y = preprocess(load_data())
    X_train, _, y_train, _ = train_test_split(X, y, random_state=42)
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    os.makedirs("ml/registry", exist_ok=True)
    joblib.dump(model, "ml/registry/model.pkl")


def test_root_endpoint():
    from app.main import app
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_predict_endpoint():
    from app.main import app
    client = TestClient(app)
    r = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert r.status_code == 200
    assert "prediction" in r.json()


def test_predict_missing_features():
    from app.main import app
    client = TestClient(app)
    # 边界：缺少 features 字段，应返回 422 校验错误
    r = client.post("/predict", json={})
    assert r.status_code == 422
