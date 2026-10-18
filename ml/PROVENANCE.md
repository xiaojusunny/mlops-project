# 数据/模型来源追踪（PROVENANCE）

记录模型与数据之间的对应关系，保证可复现。

| 模型 | 数据集版本 | 代码 commit | 训练脚本 | 超参数 |
|---|---|---|---|---|
| model.pkl | v1 | <commit hash> | ml/train.py | n_estimators=100, random_state=42 |

## 复现步骤

```bash
# 1. 拉取数据（DVC）
dvc pull

# 2. 安装依赖
pip install -r requirements.txt

# 3. 重新训练
python ml/train.py
```
