# 在 iOS 上构建 TensorFlow Lite

本文档描述了如何构建 TensorFlow Lite iOS 库。如果仅需使用，可以直接使用 TensorFlow Lite CocoaPod 版本。参阅 [TensorFlow Lite iOS Demo](ios.md) 获取示例。

## 构建

TensorFlow Lite 的通用 iOS 库需要在 MacOS 机器上，通过 Xcode 的命令行工具来构建。
如果你还没有配置好环境，可以通过 `xcode-select` 来安装 Xcode 8(或更高版本) 和工具:

```bash
xcode-select --install
```

如果这是第一次安装，你需要先运行一次 XCode 并同意它的许可。

(你也需要安装好 [Homebrew](http://brew.sh/))

下面安装 [automake](https://en.wikipedia.org/wiki/Automake)/[libtool](https://en.wikipedia.org/wiki/GNU_Libtool):

```bash
brew install automake
brew install libtool
```

如果你遇到了 automake  和 libtool 已经安装但未正确链接的错误，首先输入以下命令:
```bash
sudo chown -R $(whoami) /usr/local/*
```
然后使用下面的命令来使链接生效:
```bash
brew link automake
brew link libtool
```

接着你需用通过 shell 脚本来下载所需的依赖:
```bash
tensorflow/lite/tools/make/download_dependencies.sh
```

这会从网上获取库和数据的拷贝，并安装在`tensorflow/lite/downloads`目录

所有的依赖都已经创建完毕，你现在可以在 iOS 上为五个支持的体系架构构建库:

```bash
tensorflow/lite/tools/make/build_ios_universal_lib.sh
```

它使用 `tensorflow/lite` 中的 makefile 来构建不同版本的库，然后调用 `lipo` 将它们捆绑到包含 armv7, armv7s, arm64, i386, 和 x86_64 架构的通用文件中。生成的库在: `tensorflow/lite/tools/make/gen/lib/libtensorflow-lite.a`

如果你在运行 `build_ios_universal_lib.sh` 时，遇到了如 `no such file or directory: 'x86_64'` 的错误:
打开 Xcode > Preferences > Locations，确保在"Command Line Tools"下拉菜单中有一个选中值。

## 在应用中使用

你需要更新一些你的应用设置来链接 TensorFlow Lite。你可以在示例项目
`tensorflow/lite/examples/ios/simple/simple.xcodeproj` 查看这些设置，
但下面提供了一个完整的纲要:

-   你需要将库 `tensorflow/lite/gen/lib/libtensorflow-lite.a` 加入你的链接构建阶段，并且在 Search Paths 的 Library Search Paths 设置中添加 `tensorflow/lite/gen/lib`

-   _Header Search_ 路径需要包含:

    -   tensorflow 的根目录,
    -   `tensorflow/lite/downloads`
    -   `tensorflow/lite/downloads/flatbuffers/include`

-   设置 `C++ Language Dialect` 为 `GNU++11` (或 `GNU++14`), 同时设置 `C++ Standard Library` 为 `libc++` 来启用 C++11 支持 (或更高版本)
