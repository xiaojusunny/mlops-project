# 数据说明（README_data）

## 数据来源（Source）

- 数据集：鸢尾花 Iris（sklearn 自带示例数据集）
- 来源：`sklearn.datasets.load_iris`（原始出处：UCI Machine Learning Repository）

## 数据集版本

### v1 — 首个可用数据集
- 原始 iris 数据集，150 条样本、4 个特征。

### v2 — 改进版
- 相对 v1 的改动：<在此填写，例如：移除异常值 / 补充合成样本 / 平衡类别 / 调整训练测试切分>

## 版本与提交的对应关系

| 数据集版本 | 对应 commit | 说明 |
|---|---|---|
| v1 | <commit hash> | 首个可用数据集 |
| v2 | <commit hash> | 改进版 |

> 用 `dvc add data/<文件>` 跟踪数据后，`data/<文件>.dvc` 指针文件里记录了
> 数据文件的哈希，可据此把「代码提交」与「数据集版本」关联起来。
