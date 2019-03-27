# Java用のTensorFlowをインストールする

TensorFlowは[Java API](https://www.tensorflow.org/api_docs/java/reference/org/tensorflow/package-summary)を提供します。
このAPIは、Pythonで作成したモデルを読み込んでJavaアプリケーション内で実行する場合に特に便利です。

注意: TensorFlowのJava APIはTensorFlowの
[APIの安定性保証](../guide/version_compat.md)に*カバーされていません*。


## サポートされているプラットフォーム

Java用のTensorFlowは以下のシステムでサポートされています:

* Ubuntu 16.04 or higher; 64-bit, x86
* macOS 10.12.6 (Sierra) 以降
* Windows 7 or higher; 64-bit, x86

AndroidにTensorFlowをインストールするには、
[AndroidのTensorFlowサポート](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/android){:.external}
と
[TensorFlow Android Cameraデモ](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android){:.external}.
を参照してください。


## Apache Mavenを使ったTensorFlow

[Apache Maven](https://maven.apache.org){:.external}でTensorFlowを使う場合、
プロジェクトの`pom.xml`ファイルに次の依存関係を追加してください:

```xml
<dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>tensorflow</artifactId>
  <version>1.12.0</version>
</dependency>
```

### GPUサポート

ご使用のシステムが[GPUサポート](./gpu.md)に対応している場合、
プロジェクトの`pom.xml`ファイルに以下のTensorFlowの依存関係を追加してください:

```xml
<dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>libtensorflow</artifactId>
  <version>1.12.0</version>
</dependency>
<dependency>
  <groupId>org.tensorflow</groupId>
  <artifactId>libtensorflow_jni_gpu</artifactId>
  <version>1.12.0</version>
</dependency>
```

### プログラム例

この例は、TensorFlowを使用してApache Mavenプロジェクトをビルドする方法を示しています。
まず、プロジェクトの`pom.xml`ファイルにTensorFlowの依存関係を追加します:

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.myorg</groupId>
  <artifactId>hellotensorflow</artifactId>
  <version>1.0-SNAPSHOT</version>
  <properties>
    <exec.mainClass>HelloTensorFlow</exec.mainClass>
	<!-- The sample code requires at least JDK 1.7. -->
	<!-- The maven compiler plugin defaults to a lower version -->
	<maven.compiler.source>1.7</maven.compiler.source>
	<maven.compiler.target>1.7</maven.compiler.target>
  </properties>
  <dependencies>
    <dependency>
	  <groupId>org.tensorflow</groupId>
	  <artifactId>tensorflow</artifactId>
	  <version>1.12.0</version>
	</dependency>
  </dependencies>
</project>
```

ソース・ファイルを作成します (`src/main/java/HelloTensorFlow.java`):

```java
import org.tensorflow.Graph;
import org.tensorflow.Session;
import org.tensorflow.Tensor;
import org.tensorflow.TensorFlow;

public class HelloTensorFlow {
  public static void main(String[] args) throws Exception {
	try (Graph g = new Graph()) {
	  final String value = "Hello from " + TensorFlow.version();

	  // Construct the computation graph with a single operation, a constant
	  // named "MyConst" with a value "value".
	  try (Tensor t = Tensor.create(value.getBytes("UTF-8"))) {
	    // The Java API doesn't yet include convenience functions for adding operations.
		g.opBuilder("Const", "MyConst").setAttr("dtype", t.dataType()).setAttr("value", t).build();
	  }

	  // Execute the "MyConst" operation in a Session.
	  try (Session s = new Session(g);
	      // Generally, there may be multiple output tensors,
		  // all of them must be closed to prevent resource leaks.
		  Tensor output = s.runner().fetch("MyConst").run().get(0)) {
	    System.out.println(new String(output.bytesValue(), "UTF-8"));
	  }
    }
  }
}
```

コンパイルし、実行します:

<pre class="devsite-terminal prettyprint lang-bsh">
mvn -q compile exec:java  # Use -q to hide logging
</pre>

このコマンドの出力: <code>Hello from <em>version</em></code>

成功: Java用のTensorFlowが設定されました。


## JDKを使ったTensorFlow

TensorFlowは、Java Native Interface (JNI)を介してJDKともに使用できます。

### ダウンロード

1. TensorFlow Jar Archive (JAR)をダウンロードします: [libtensorflow.jar](https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-1.12.0.jar)
2. ご使用のオペレーティングシステムおよびプロセッサーサポート用のJava Native Interface (JNI)ファイルをダウンロードし、実行します:

<table>
  <tr><th>JNI version</th><th>URL</th></tr>
  <tr class="alt"><td colspan="2">Linux</td></tr>
  <tr>
    <td>Linux CPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-cpu-linux-x86_64-1.12.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-cpu-linux-x86_64-1.12.0.tar.gz</a></td>
  </tr>
  <tr>
    <td>Linux GPUサポート</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-gpu-linux-x86_64-1.12.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-gpu-linux-x86_64-1.12.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">macOS</td></tr>
  <tr>
    <td>macOS CPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-cpu-darwin-x86_64-1.12.0.tar.gz">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-cpu-darwin-x86_64-1.12.0.tar.gz</a></td>
  </tr>
  <tr class="alt"><td colspan="2">Windows</td></tr>
  <tr>
    <td>Windows CPUのみ</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-cpu-windows-x86_64-1.12.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-cpu-windows-x86_64-1.12.0.zip</a></td>
  </tr>
  <tr>
    <td>Windows GPUサポート</td>
    <td class="devsite-click-to-copy"><a href="https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-gpu-windows-x86_64-1.12.0.zip">https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow_jni-gpu-windows-x86_64-1.12.0.zip</a></td>
  </tr>
</table>

注: Windowsでは、ネイティブライブラリー (`tensorflow_jni.dll`)が実行時に`msvcp140.dll`を必要とします。
[Windows build from source](./source_windows.md)ガイドを参照して、
[Visual C++ 2015 Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=48145){:.external}をインストールしてください。


### コンパイル

[前の例](#example)の`HelloTensorFlow.java`ファイルを使って、
TensorFlowを使うプログラムをコンパイルしてください。
`libtensorflow.jar`が`classpath`にアクセス可能であることを確認してください:

<pre class="devsite-terminal devsite-click-to-copy">
javac -cp libtensorflow-1.12.0.jar HelloTensorFlow.java
</pre>

### 実行

TensorFlowのJavaプログラムを実行するために、
JVMは`libtensorflow.jar`と解凍されたJNIライブラリにアクセスしなければなりません。

<div class="ds-selector-tabs">
<section>
<h3>Linux / mac OS</h3>
<pre class="devsite-terminal devsite-click-to-copy">java -cp libtensorflow-1.12.0.jar:. -Djava.library.path=./jni HelloTensorFlow</pre>
</section>
<section>
<h3>Windows</h3>
<pre class="devsite-terminal tfo-terminal-windows devsite-click-to-copy">java -cp libtensorflow-1.12.0.jar;. -Djava.library.path=jni HelloTensorFlow</pre>
</section>
</div><!--/ds-selector-tabs-->

このコマンドの出力: <code>Hello from <em>version</em></code>

成功: Java用のTensorFlowが設定されました。


## ソースからビルドする

TensorFlowはオープンソースです。
ソースコードからTensorFlowのJavaとネイティブライブラリをビルドする場合は
[手順](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/java/README.md){:.external}
を参照してください。
