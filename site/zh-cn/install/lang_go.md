#  Go 中安装 TensorFlow

TensorFlow 提供了一个[Go API](https://pkg.go.dev/github.com/tensorflow/tensorflow/tensorflow/go){:.external}—
明确用于加载在Python下创建的模型，并在Go程序中运行他们。

警告： TensorFlow Go API  *不* 包含 TensorFlow 所有的
[API 稳定保证](../guide/versions.md).


## 支持的平台

Go 版本 TensorFlow 支持的系统如下：

* Linux, 64位, x86
* macOS X, 版本 10.12.6 (Sierra) 或更高


## 安装

### TensorFlow C 库

安装 TensorFlow Go 包前必须安装 [TensorFlow C 库](./lang_c.md) 。

### 下载

下载并安装 TensorFlow Go包及其相关依赖：

<pre class="devsite-terminal devsite-click-to-copy">
go get github.com/tensorflow/tensorflow/tensorflow/go
</pre>

通过如下命令验证安装：

<pre class="devsite-terminal devsite-click-to-copy">
go test github.com/tensorflow/tensorflow/tensorflow/go
</pre>


## 构建

### 实例程序

在 TensorFlow 的 Go 包安装完毕后，通过如下源码创建实例程序（`hello_tf.go`）:

```go
package main

import (
	tf "github.com/tensorflow/tensorflow/tensorflow/go"
	"github.com/tensorflow/tensorflow/tensorflow/go/op"
	"fmt"
)

func main() {
	// Construct a graph with an operation that produces a string constant.
	s := op.NewScope()
	c := op.Const(s, "Hello from TensorFlow version " + tf.Version())
	graph, err := s.Finalize()
	if err != nil {
		panic(err)
	}

	// Execute the graph in a session.
	sess, err := tf.NewSession(graph, nil)
	if err != nil {
		panic(err)
	}
	output, err := sess.Run(nil, []tf.Output{c}, nil)
	if err != nil {
		panic(err)
	}
	fmt.Println(output[0].Value())
}
```

### 运行

运行示例程序：

<pre class="devsite-terminal devsite-click-to-copy">
go run hello_tf.go
</pre>

命令输出： <code>Hello from TensorFlow version <em>number</em></code>

成功：Go 的 TensorFlow 已经配置完毕。

程序可能出现如下警告信息，您可以忽略：

<pre>
W tensorflow/core/platform/cpu_feature_guard.cc:45]  TensorFlow 库未被编译用于使用 *Type* 指令，但这在您的机器上是可用的，并能加速CPU计算。
</pre>

## 从源码构建

TensorFlow 是开源的。浏览此
[说明](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/go/README.md){:.external}
来为Go从源码构建 TensorFlow 。