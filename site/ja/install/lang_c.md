# C用のTensorFlowをインストールする

TensorFlowは[他プログラミング言語用のバインディング](../extend/language_bindings.md)のビルドに使用できるC用のAPIを提供します。
APIは<a href="https://github.com/tensorflow/tensorflow/blob/master/tensorflow/c/c_api.h" class="external"><code>c_api.h</code></a>
で定義されており、利便性よりも単純さと統一性を重視して設計されています。


## サポートされているプラットフォーム

C用のTensorFlowは以下のシステムでサポートされています:

* Linux, 64-bit, x86
* macOS X, Version 10.12.6 (Sierra) 以降
* Windows, 64-bit x86

## セットアップ

### ダウンロード

<table>
  <tr><th>TensorFlowのCライブラリ</th><th>URL</th></tr>
  <tr class="alt"><td colspan="2">Linux</td></tr>
  <tr>
    <td>Linux CPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.12.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-1.12.0.tar.gz</a></td>
  </tr>
  <tr>
    <td>Linux GPUサポート</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.12.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.12.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">macOS</td></tr>
  <tr>
    <td>macOS CPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.12.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-darwin-x86_64-1.12.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">Windows</td></tr>
  <tr>
    <td>Windows CPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-windows-x86_64-1.12.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-windows-x86_64-1.12.0.zip</a></td>
  </tr>
  <tr>
    <td>Windows GPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-windows-x86_64-1.12.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-windows-x86_64-1.12.0.zip</a></td>
  </tr>
</table>

### 解凍

ダウンロードしたアーカイブを解凍します。
これには、Cプログラムに含めるヘッダーファイルとリンク先の共有ライブラリが含まれています。

LinuxとmacOSでは、`/usr/local/lib`に展開するといいでしょう:

<pre class="devsite-terminal devsite-click-to-copy">
sudo tar -C /usr/local -xzf <var>(downloaded file)</var>
</pre>

### リンカ

Linux/macOSで、TensorFlowのCライブラリを`/usr/local`などのシステムディレクトリーに展開する場合は、
`ldconfig`を使用してリンカを設定します:

<pre class="devsite-terminal devsite-click-to-copy">
sudo ldconfig
</pre>

TensorFlowのCライブラリを`~/mydir`のような非システムディレクトリーに展開する場合は、
リンカ環境変数を設定してください:

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


## ビルド

### プログラム例

TensorFlowのCライブラリをインストールした状態で、
以下のソースコード(`hello_tf.c`)のようにプログラム例を作成してください:

```c
#include <stdio.h>
#include <tensorflow/c/c_api.h>

int main() {
  printf("Hello from TensorFlow C library version %s\n", TF_Version());
  return 0;
}
```

### コンパイル

サンプルプログラムをコンパイルして実行ファイルを作成してから、次のコマンドを実行します:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">gcc hello_tf.c -ltensorflow -o hello_tf</code>

<code class="devsite-terminal">./hello_tf</code>
</pre>

このコマンドの出力: <code>Hello from TensorFlow C library version <em>number</em></code>

成功: TensorFlowのCライブラリが設定されました。


プログラムがビルドされない場合は、`gcc`がTensorFlowのCライブラリにアクセスできることを確認してください。
`/usr/local`に展開されている場合は、ライブラリの場所をコンパイラに明示的に渡します:

<pre class="devsite-terminal devsite-click-to-copy">
gcc -I/usr/local/include -L/usr/local/lib hello_tf.c -ltensorflow -o hello_tf
</pre>


## ソースからビルドする

TensorFlowはオープンソースです。
ソースコードからTensorFlowのCライブラリをビルドする場合は
[手順](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/lib_package/README.md){:.external}
を参照してください。
