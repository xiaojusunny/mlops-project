"""应用入口：加载训练好的模型，提供预测 API。

运行：uvicorn app.main:app --reload
"""
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ML App")

MODEL_PATH = "ml/registry/model.pkl"

# 懒加载：模型在第一次请求时才读，避免"还没训练就启动崩溃"
_model = None


def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


class Features(BaseModel):
    features: list[float]


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/predict")
def predict(item: Features):
    model = get_model()
    x = np.array(item.features, dtype=float).reshape(1, -1)
    pred = int(model.predict(x)[0])
    return {"prediction": pred}
