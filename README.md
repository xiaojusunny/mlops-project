# ML + DevOps + MLOps 项目

一个由机器学习驱动的应用，完整实践 DevOps 与 MLOps 流程。

## 项目概述

使用 scikit-learn 训练一个分类模型（示例：鸢尾花分类），
通过 FastAPI 对外提供预测服务，并用 Git 分支、Docker、CI/CD、
DVC（数据版本化）和 MLflow（实验跟踪）管理整个生命周期。

## 目录结构

```
.
├── app/
│   └── main.py                 # 服务入口 / API 服务器
├── ml/
│   ├── train.py                # 训练脚本（调用 MLflow）
│   ├── data_pipeline.py        # 预处理 / 特征工程
│   ├── configs/config.yaml     # 超参数、训练配置
│   ├── registry/               # 模型注册
│   │   └── current_model.md    # 哪个模型是生产模型
│   ├── README_data.md
│   ├── README_experiments.md
│   └── PROVENANCE.md
├── tests/                      # 测试
├── data/                       # 数据（DVC 管理，不入库）
├── .github/workflows/ci.yml    # CI 流水线
├── .github/workflows/deploy.yml# 部署流水线
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── DEPLOYMENT.md
```

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 训练模型（会用 MLflow 记录实验）
python ml/train.py

# 3. 运行测试
pytest -v

# 4. 启动服务
uvicorn app.main:app --reload
# 打开 http://127.0.0.1:8000/docs 测试 /predict
```

## 分支方案

- `main`：生产环境
- `staging`：预发布环境
- `dev`：开发主线
- `feature/*`：功能分支

合并路径：`feature/*` → `dev` → `staging` → `main`

## CI/CD 说明

- **CI**（每个 PR 触发）：构建 Docker 镜像 + lint + 跑全部测试，失败则无法合并。
- **部署**（合并到 staging/main 触发）：用对应环境的 GitHub Secrets 生成 `.env` 并构建镜像。

详见 [DEPLOYMENT.md](DEPLOYMENT.md)。
