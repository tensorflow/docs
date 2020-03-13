# 在 C 中安装 TensorFlow 

TensorFlow 提供了 C API 用于构建并
[绑定至其他语言](../extend/language_bindings.md)。 API的定义在
<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/c/c_api.h" class="external"><code>c_api.h</code></a>
中，并被简化和统一设计，而不是为了方便。

提示：当前未提供 TensorFlow 2 的 `libtensorflow` 支持。未来发行版本将提供该支持。

## 支持的平台

C 中的 TensorFlow 支持如下系统：

* Linux, 64-bit, x86
* macOS X, 版本 10.12.6 (Sierra) 或更高
* Windows, 64位 x86

## 安装

### 下载

<table>
  <tr><th>TensorFlow C 库</th><th>URL</th></tr>
  <tr class="alt"><td colspan="2">Linux</td></tr>
  <tr>
    <td>Linux 仅 CPU 版</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.15.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.15.0.tar.gz</a></td>
  </tr>
  <tr>
    <td>Linux 支持 GPU 版</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.15.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.15.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">macOS</td></tr>
  <tr>
    <td>macOS 仅 CPU 版</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.15.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.15.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">Windows</td></tr>
  <tr>
    <td>Windows 仅 CPU 版</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-windows-x86_64-1.15.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-windows-x86_64-1.15.0.zip</a></td>
  </tr>
  <tr>
    <td>Windows 仅 GPU 版</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-windows-x86_64-1.15.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-windows-x86_64-1.15.0.zip</a></td>
  </tr>
</table>

### 解压

解压上一步下载的压缩文档，该压缩文档包含了您的 C 程序需引用的头文件和链接程序所需共享库。

在 Linux 和 macOS 中，您也可解压至 `/usr/local/lib`：

<pre class="devsite-terminal devsite-click-to-copy">
sudo tar -C /usr/local -xzf <var>(下载的文件)</var>
</pre>

### 链接

在 Linux/macOS 中，如果 TensorFlow C 库解压到系统目录下，如 `/usr/local`， 需要通过 `ldconfig` 配置链接：

<pre class="devsite-terminal devsite-click-to-copy">
sudo ldconfig
</pre>

如果 TensorFlow C 库解压到非系统目录下，如`~/mydir`，则按照如下步骤配置环境变量的链接：

<div class="ds-selector-tabs">
<section>
<h3>Linux</h3>
<pre class="prettyprint lang-bsh">
export LIBRARY_PATH=$LIBRARY_PATH:~/mydir/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/mydir/lib
</pre>
</section>
<section>
<h3>mac OS</h3>
<pre class="prettyprint lang-bsh">
export LIBRARY_PATH=$LIBRARY_PATH:~/mydir/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:~/mydir/lib
</pre>
</section>
</div><!--/ds-selector-tabs-->


## 构建

### 实例程序

在 TensorFlow C 库安装后，通过如下源码创建示例程序 （`hello_tf.c`）：

```c
#include <stdio.h>
#include <tensorflow/c/c_api.h>

int main() {
  printf("Hello from TensorFlow C library version %s\n", TF_Version());
  return 0;
}
```

### 编译

编译源码创建可执行程序，并随后运行：

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">gcc hello_tf.c -ltensorflow -o hello_tf</code>

<code class="devsite-terminal">./hello_tf</code>
</pre>

该命令输出： <code>Hello from TensorFlow C library version <em>number</em></code>

成功：TensorFlow C 库已配置。

如果程序无法编译，请确保 `gcc` 能够访问到 TensorFlow C 库。
如果解压的目录是 `/usr/local`，需要另外传递库文件地址给编译器：

<pre class="devsite-terminal devsite-click-to-copy">
gcc -I/usr/local/include -L/usr/local/lib hello_tf.c -ltensorflow -o hello_tf
</pre>


## 从源码构建

TensorFlow 是开源的。您可以浏览
[该手册](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/lib_package/README.md){:.external}
从源码来构建 TensorFlow C 库。