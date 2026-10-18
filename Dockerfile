# ---------- 构建阶段：安装依赖 ----------
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---------- 运行阶段：更小的镜像 ----------
FROM python:3.11-slim
WORKDIR /app

# 从构建阶段复制已安装的依赖
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# 复制应用与模型代码（模型文件不入镜像，运行时挂载或用 DVC 拉取）
COPY app ./app
COPY ml ./ml

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
