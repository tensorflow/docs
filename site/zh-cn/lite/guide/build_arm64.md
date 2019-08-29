# 在ARM64板上构建Tensorflow Lite

## 交叉编译

### 安装工具链

```bash
sudo apt-get update
sudo apt-get install crossbuild-essential-arm64
```

> 如果你使用docker，可能不需要加上`sudo`

### 构建

复制Tensorflow代码仓库。在代码仓库根目录下运行下面的脚本来下载依赖：

> 你也可以尝试使用docker镜像`tensorflow/tensorflow:nightly-devel`，
> tensorflow代码仓库在`/tensorflow`

```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```

注意你只需要做一次这个操作

编译:

```bash
./tensorflow/lite/tools/make/build_aarch64_lib.sh
```

这会编译出一个静态库在：
`tensorflow/lite/tools/make/gen/aarch64_armv8-a/lib/libtensorflow-lite.a`.

## 原生编译

以下步骤在 HardKernel Odroid C2 和gcc 5.4.0版本上测试过.

登录你的开发板，安装工具链

```bash
sudo apt-get install build-essential
```

首先，复制Tensorflow代码仓库。在代码仓库根目录下运行：

```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```

注意你只需要做一次这个操作

编译:

```bash
./tensorflow/lite/tools/make/build_aarch64_lib.sh
```

这会编译出一个静态库在：
`tensorflow/lite/tools/make/gen/aarch64_armv8-a/lib/libtensorflow-lite.a`.
