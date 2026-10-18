"""测试数据管线：加载与预处理。"""
from ml.data_pipeline import load_data, preprocess


def test_load_data_shape():
    df = load_data()
    # iris：150 行，5 列（4 特征 + 1 标签）
    assert df.shape[0] == 150
    assert df.shape[1] == 5


def test_preprocess_no_missing_values():
    df = load_data()
    X, y = preprocess(df)
    # 边界：处理后不能有缺失值
    assert not X.isna().any().any()
    assert len(X) == len(y)


def test_preprocess_feature_count():
    df = load_data()
    X, _ = preprocess(df)
    assert X.shape[1] == 4  # 4 个特征
