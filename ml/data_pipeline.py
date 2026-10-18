"""数据管线：加载数据 + 预处理。

这里用 sklearn 自带的鸢尾花(iris)数据集作示例，
你可以把 load_data() 换成读你自己的 CSV/图片等，其余流程不变。
"""
from sklearn.datasets import load_iris


def load_data():
    """加载数据，返回 pandas DataFrame。"""
    data = load_iris(as_frame=True)
    return data.frame


def preprocess(df):
    """预处理：清洗缺失值，拆分特征 X 与标签 y。"""
    df = df.dropna()
    X = df.drop(columns=["target"])
    y = df["target"]
    return X, y
