# 在树莓派上构建 TensorFlow Lite
## 交叉编译
### 安装工具链
此功能已在 ubuntu 16.04.3 64bit 和 Tensorflow devel docker image [ tensorflow/tensorflow:nightly-devel](https://hub.docker.com/r/tensorflow/tensorflow/tags/) 上测试。
要使用 TensorFlow Lite 交叉编译功能，应先安装工具链和相关的库。
```
sudo apt-get update
sudo apt-get install crossbuild-essential-armhf
```
如果你使用 Docker，你可能无法使用 sudo 。
### 
