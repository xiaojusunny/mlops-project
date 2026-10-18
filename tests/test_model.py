"""测试模型训练与预测（含边界情况）。"""
import numpy as np
import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from ml.data_pipeline import load_data, preprocess


@pytest.fixture(scope="module")
def trained_model():
    X, y = preprocess(load_data())
    X_train, _, y_train, _ = train_test_split(X, y, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    return model


def test_model_accuracy_above_threshold(trained_model):
    X, y = preprocess(load_data())
    acc = trained_model.score(X, y)
    assert acc > 0.85  # 简单数据上必须达标


def test_predict_shape_and_range(trained_model):
    X, _ = preprocess(load_data())
    pred = trained_model.predict(X[:10])
    assert pred.shape == (10,)
    assert set(pred).issubset({0, 1, 2})


def test_predict_rejects_wrong_feature_count(trained_model):
    # 边界：特征数量不对应报错，而不是静默给错误结果
    with pytest.raises(ValueError):
        trained_model.predict(np.array([[1.0, 2.0]]))  # 只给了 2 个特征
