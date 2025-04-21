# ZED YOLOv8 + SAM2 实时追踪与分割系统

基于 ZED 相机、YOLOv8、SAM2 实现的实时目标追踪与分割系统，支持多平台部署，集成 PowerShell 脚本便于自动化运行。

## 📦 功能特点
- 实时目标检测与分割
- 跨平台部署支持（Windows的PowerShell）
- 模块化结构，易于扩展
- 支持 ZED SDK 5.0

## 🛠️ 安装环境一sam2

```bash
conda create -n sam2 python=3.10.15
git clone https://github.com/zdata-inc/sam2_realtime.git
cd sam2_realtime
pip install -e .
pip install -e ".[notebooks]"
cd checkpoints
./download_ckpts.sh
cd ..
```


## 🛠️ 安装环境二zed

```bash
conda create -n zed python=3.9 -y
conda activate zed
pip install ultralytics opencv-python numpy
```
## 🛠️ 配置zed+python
在新版本的zed SDK中缺少pyzed的安装，在安装好zed SDK后运行C:\Program Files (x86)\ZED SDK中的get_python_api.py
即可配置完pyzed



