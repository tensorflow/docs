# Go用のTensorFlowをインストールする

TensorFlowは[Go API](https://godoc.org/github.com/tensorflow/tensorflow/tensorflow/go){:.external}を提供します。
このAPIは、Pythonで作成したモデルを読み込んでGoアプリケーション内で実行する場合に特に便利です。

注意: TensorFlowのGo APIはTensorFlowの
[APIの安定性保証](../guide/version_compat.md)に*カバーされていません*。


## サポートされているプラットフォーム

Go用のTensorFlowは以下のシステムでサポートされています:

* Linux, 64-bit, x86
* macOS X, Version 10.12.6 (Sierra) 以降


## セットアップ

### TensorFlowのCライブラリ

TensorFlowのGoパッケージに必要な
[TensorFlowのCライブラリ](./lang_c.md)をインストールします。

### ダウンロード

TensorFlowのGoパッケージとその依存関係をダウンロードしてインストールします:

<pre class="devsite-terminal devsite-click-to-copy">
go get github.com/tensorflow/tensorflow/tensorflow/go
</pre>

次にインストール結果を検証します:

<pre class="devsite-terminal devsite-click-to-copy">
go test github.com/tensorflow/tensorflow/tensorflow/go
</pre>


## ビルド

### プログラム例

TensorFlowのGoライブラリをインストールした状態で、
以下のソースコード(`hello_tf.go`)のようにプログラム例を作成してください:

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

### 実行

プログラム例を実行してください:

<pre class="devsite-terminal devsite-click-to-copy">
go run hello_tf.go
</pre>

このコマンドの出力: <code>Hello from TensorFlow version <em>number</em></code>

成功: TensorFlowのGoライブラリが設定されました。

このプログラムは次の警告メッセージを生成することがありますが、無視してかまいません:

<pre>
W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library
wasn't compiled to use *Type* instructions, but these are available on your
machine and could speed up CPU computations.
</pre>

## ソースからビルドする

TensorFlowはオープンソースです。
ソースコードからTensorFlowのGoライブラリをビルドする場合は
[手順](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/go/README.md){:.external}
を参照してください。
