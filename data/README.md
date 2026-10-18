# 数据目录

原始数据放在这里，**由 DVC 管理，不提交到 Git**。

用法：
```bash
# 把数据加入 DVC（会生成 data/<文件名>.dvc 指针文件）
dvc add data/iris.csv

# 只有 .dvc 指针文件提交到 Git，原始数据 push 到远程存储
git add data/iris.csv.dvc
dvc push
```
