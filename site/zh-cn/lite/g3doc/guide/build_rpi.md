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
### 构建
克隆此Tensorflow库，在库的根目录下运行此脚本以下载所有依赖项：
> tensorflow库在 /tensorflow 下。如果您使用的是 docker 镜像 tensorflow/tensorflow:nightly-develimage，则会使用Tensorflow存储库，尝试使用以下命令即可。
```
./tensorflow/lite/tools/make/download_dependencies.sh
```
请注意，您只需要执行一次此操作。
然后你应该能够编译：
```
./tensorflow/lite/tools/make/build_rpi_lib.sh
```
这应该编译一个静态库,位于：
tensorflow/lite/tools/make/gen/rpi_armv7l/lib/libtensorflow-lite.a.
## 本地编译
这已经在Raspberry Pi 3b，Raspbian GNU / Linux 9.1（stretch），gcc版本6.3.0 20170516（Raspbian 6.3.0-18 + rpi1）上进行了测试。
登录Raspberry Pi，安装工具链。
```
sudo apt-get install build-essential
```
首先，克隆TensorFlow库。在库的根目录运行：
```
./tensorflow/lite/tools/make/download_dependencies.sh
```
请注意，您只需要执行一次此操作。
然后你应该能够编译：
```
./tensorflow/lite/tools/make/build_rpi_lib.sh
```
这应该编译一个静态库,位于：
tensorflow/lite/tools/make/gen/lib/rpi_armv7/libtensorflow-lite.a 。
