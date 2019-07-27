# 理解 C++ 库

微控制器版 TensorFlow Lite C++ 库是
[TensorFlow 仓库](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro)
的一部分。它可读、易修改，测试结果良好，易整合，并且与标准 TensorFlow Lite 兼容。

下面的文档列出了 C++ 库的基本结构，提供了编译所需的命令，并给出了将程序写入新设备的概览。

在
[README.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/README.md#如何将用于微控制器的TensorFlow-Lite写入一个新的平台)
中包含更多关于所有这些话题的更多深入信息。

## 文件结构

在
[`micro`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro)
根目录中有一个相对简单的结构。然而，因为它位于巨大的 TensorFlow 仓库中，所以我们创建了一些脚本和预生成的项目文件，为多种嵌入式开发环境（如 Arduino, Keil, Make 和 Mbed）提供分离的相关源文件。

### 关键文件

使用微控制器版 TensorFlow Lite 解释器时最重要的文件在项目的根目录中，并附带测试：

-   [`all_ops_resolver.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h)
    提供解释器运行模型的运算符。
-   [`micro_error_reporter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_error_reporter.h)
    输出调试信息。
-   [`micro_interpreter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_interpreter.h)
    包含控制和运行模型的代码。

在 [开始使用微控制器](get_started.md) 可以找到典型的用途的展示。

构建系统提供某些文件在特定平台的实现。它们在以平台名称命名的目录下，例如：
[`sparkfun_edge`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/sparkfun_edge)。

还有许多其他目录，包括：

-   [`kernel`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/kernels),
    包含运算符的实现和相关代码。
-   [`tools`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/tools),
    包含构建工具和它们的输出。
-   [`examples`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples),
    包含示例代码。

### 生成项目文件

项目中的 `Makefile` 能够生成包含所有必需源文件的独立项目，这些源文件可以被导入嵌入式开发环境。目前被支持的环境是 Arduino, Keil, Make 和 Mbed。

注意：我们为其中一些环境托管预建项目。参阅
[支持的平台](overview.md#supported-platforms)
以下载。

要在 Make 中生成项目，请使用如下指令：

```bash
make -f tensorflow/lite/experimental/micro/tools/make/Makefile generate_projects
```

这需要几分钟，因为它需要下载一些大型工具链依赖。结束后，你应看到像这样的路径中，创建了一些文件夹：
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/` （确切的路径取决于您的主机操作系统）。这些文件夹包含生成的项目和源文件。例如：
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/keil`
包含了 Keil uVision 目标。

## 构建库

如果您在使用一个已生成的项目，参阅它内含的 README 以获取构建指南。

要构建库并从主 TensorFlow 存储库中运行测试，请执行以下命令：

1.  从 GitHub 中把 TensorFlow 存储库克隆到方便的地方。

    ```bash
    git clone --depth 1 https://github.com/tensorflow/tensorflow.git
    ```

2.  进入上一步创建的目录。

    ```bash
    cd tensorflow
    ```

3.  调用 `Makefile` 来构建项目并运行测试。
    注意这将会下载所有需要的依赖：

    ```bash
    make -f tensorflow/lite/experimental/micro/tools/make/Makefile test
    ```

## 写入新设备

把微控制器版 TensorFlow Lite 写入新平台和设备的指南，可在
[README.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro#如何将用于微控制器的TensorFlow-Lite写入一个新的平台)
中查看。
