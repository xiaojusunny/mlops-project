# 当前生产模型（Current Model）

- 模型文件：`ml/registry/model.pkl`
- 来源实验：MLflow experiment `iris-classification` 中准确率最高的 run
- 数据集版本：v1
- 训练脚本：`ml/train.py`

> 每次更新生产模型时，把对应 MLflow run 的信息更新到这里。
