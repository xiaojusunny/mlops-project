# 部署说明（DEPLOYMENT）

## 环境划分

| 环境 | 分支 | 触发方式 | 镜像 tag |
|---|---|---|---|
| staging（预发布） | `staging` | push 到 staging | `mlops-app:staging` |
| production（生产） | `main` | push 到 main | `mlops-app:latest` |

## 部署流程

1. 合并到 `staging` → GitHub Actions 读取 `STAGING_ENV` secret，生成 staging `.env`，构建 staging 镜像。
2. 合并到 `main` → GitHub Actions 读取 `PROD_ENV` secret，生成生产 `.env`，构建生产镜像。

## 需要配置的 GitHub Secrets

在 GitHub 仓库 → Settings → Secrets and variables → Actions 中添加：

- `STAGING_ENV`：staging 环境的 `.env` 内容
- `PROD_ENV`：生产环境的 `.env` 内容

## 本地构建

```bash
docker build -t mlops-app .
docker run -p 8000:8000 mlops-app
```
