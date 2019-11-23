# TensorFlow Liteを始めよう

TensorFlow Liteは、TensorFlowの
モデルをモバイル、組み込み、そしてIoTデバイスで走らせるために必要なツールを全て提供します。
下記のガイドは開発者のワークフローのステップを一つ一つ辿り、また
その次の説明へのリンクを提供します。

[TOC]

## 1. モデルを選ぶ

<a id="1_choose_a_model"></a>

TensorFlowのモデルは、ある問題を解決するために訓練された機械学習のネットワークの、
論理と知識を含むデータ構造です。
TensorFlowのモデルを手に入れるにはたくさんの方法があります、
学習済みのモデルを使うことからあなた独自のものを訓練することまで。

TensorFlow Liteでモデルを使うためには、あなたはフルの
TensorFlowモデルをTensorFlow Lite形式に変換しなければいけません—
TensorFlow Liteを使ってモデルを作ったり訓練したりはできません。
したがってあなたは
普通のTensorFlowモデルから始めて、そして
[モデルを変換](#2_convert_the_model_format)しなければいけません。

付記: TensorFlow LiteがサポートするのはTensorFlowオペレーションの限られたサブセットですから、
全てのモデルが変換できるわけではありません。
詳しくは、
[TensorFlow Liteオペレータ互換性](ops_compatibility.md)を呼んでください。


### 学習済みのモデルを使う

TensorFlow Liteチームは各種の機械学習の問題を解くための一揃いの学習済みモデルを提供しています。
これらのモデルはTensorFlow Liteで動くように変換されていて、あなたのアプリケーションで
すぐに使えます。

学習済みモデルは下記を含みます:

*   [画像分類](../models/image_classification/overview.md)
*   [オブジェクト検知](../models/object_detection/overview.md)
*   [スマートリプライ](../models/smart_reply/overview.md)
*   [姿勢推定](../models/pose_estimation/overview.md)
*   [セグメンテーション](../models/segmentation/overview.md)

学習済みモデルの全リストは[Models](../models)をみてください。

#### 他の入手元からのモデル

学習済みのTensorFlowモデルを入手できる場所はたくさんあり
その中には[TensorFlow Hub](https://www.tensorflow.org/hub)があります。
多くの場合、これらのモデルは
TensorFlow Lite形式では提供されてはおらず、あなたは
それらを[変換](#2_convert_the_model_format)してから使います。

### モデルを再訓練する(転移学習)
転移学習によってあなたは学習済みモデルを別の仕事をさせるために再学習させることができます。
例えば、
[画像分類](../models/image_classification/overview.md)モデルは再学習して
新しい分類の画像を認識させることができます。
再学習は一からモデルを学習させるよりも
短い時間と少ないデータで行えます。

転移学習で学習済みモデルをあなたのアプリケーション用にカスタマイズできます。
転移学習のやり方は
<a href="https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android">TensorFlowで花を認識する</a>コードラボで、習得してください。

### カスタムモデルを訓練する

あなたが自身のTensorFlowモデルを設計し訓練したり、
どこかから持ってきたモデルを訓練している場合、
あなたは
[それをTensorFlow Lite形式に変換しなければいけません](#2_convert_the_model_format)。

## 2. モデルを変換する

<a id="2_convert_the_model_format"></a>

TensorFlow Liteはモデルを効率的に、計算やメモリの資源が限られたモバイルやその他の組み込みデバイスで
実行するために設計されました。
この効率性はモデルを保存するための特別な形式を使っていることから来ています。
TensorFlowモデルはこの形式に変換してからTensorFlow Liteで使用しなければいけません。

モデルを変換するとファイルサイズが減少し正確性には影響しない最適化がなされます。
TensorFlow Liteコンバータの提供するオプションにより、
幾らかのトレードオフ付きでさらにファイルサイズを減少させ実行スピードを増すこともできます。

付記: TensorFlow LiteはTensorFlowオペレーションの限られたサブセットをサポートします、
したがって全てのモデルが変換できるわけではありません。
詳しくは、[TensorFlow Liteオペレータ互換性](ops_compatibility.md)を読んでください。


### TensorFlow Liteコンバータ

[TensorFlow Liteコンバータ](../convert)はPython APIとして利用できるツールで、
学習したTensorFlowモデルをTensorFlow Lite形式に変換します。
さらに最適化も加えることができ、これはセクション4の、
[あなたのモデルを最適化する](#4_optimize_your_model_optional)に説明があります。

次は
TensorFlowの`SavedModel`がTensorFlow Lite形式に変換する例です:

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)
```

あなたは[TensorFlow 2.0モデルの変換](../convert/index.md)も同様に行えます。

コンバータはまた
[コマンド行から](../convert/cmdline.md)も使えますが、Python APIをお勧めします。

### オプション

コンバータは様々な入力型から変換を行えます。

[TensorFlow 1.xモデルから変換](../convert/python_api.md)する時には、それらは:

*   [SavedModelディレクトリ](https://www.tensorflow.org/guide/saved_model)
*   凍結したGraphDef (
    [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)で生成したモデル)
*   [Keras](https://keras.io) HDF5 models
*   `tf.Session`から取得したモデル

[TensorFlow 2.xモデルを変換](../convert/python_api.md)する時には、それらは:

*   [SavedModelディレクトリ](https://www.tensorflow.org/guide/saved_model)
*   [`tf.keras`モデル](https://www.tensorflow.org/guide/keras/overview)
*   [具体関数](../convert/concrete_function.md)

コンバータは各種の最適化を加えて性能を向上させたり、ファイルサイズを減らしたりするように設定できます。
これはセクション4、
[あなたのモデルを最適化する](#4_optimize_your_model_optional)で説明しています。

### Opsの互換性

TensorFlow Liteが現在サポートしているのは[TensorFlow
オペレーションの限られたサブセット](ops_compatibility.md)です。
長期的な目標は全てのTensorFlowオペレーションが
サポートされることです。

変換したいモデルが含むオペレーションのうちにサポートされないものがあれば、
あなたは
[TensorFlowセレクト](ops_select.md)を使ってTensorFlowからオペレーションを含むことができます。
これによりデバイス上にデプロイされるバイナリのサイズは大きくなります。

## 3. モデルを使い推論する

<a id="3_use_the_tensorflow_lite_model_for_inference_in_a_mobile_app"></a>

*推論*は予測を得るためにデータをモデルに通して走らせるプロセスです。
これにはモデル、インタープリター、そして入力データが必要です。

### TensorFlow Liteインタープリタ

[TensorFlow Liteインタープリタ](inference.md)ライブラリは、
モデルファイルを取り込み、そこに定義されたオペレーションを入力データに対して実行し、そして出力へのアクセスを可能にします。

インタープリタは複数のプラットフォームで動作し、
TensorFlow LiteモデルをJava、Swift、Objective-C、C++、そしてPythonから走らせるための簡単なAPIを提供します。

下記のコードはインタープリタがJavaから起動されるところです:

```java
try (Interpreter interpreter = new Interpreter(tensorflow_lite_model_file)) {
  interpreter.run(input, output);
}
```

### GPU高速化とデレゲート

いくつかのデバイスはハードウェアの高速化を機械学習オペレーションに提供します。
例えば、ほとんどの携帯電話はGPUを持ち、それはCPUよりも速く浮動少数行列演算を行えます。

相当なスピードアップが可能です。
例えば、MobileNet v1イメージ分類モデルはGPU高速化を使うと
5.5倍速くPixel 3端末上で走ります。

TensorFlow Liteインタープリタで
[デレゲート](../performance/delegates.md)を設定すると異なるデバイスで
ハードウェアの高速化を使うことができます。
[GPUデレゲート](../performance/gpu.md)によりインタープリタに
適切なオペレーションをデバイスのGPU上で走らせることができます。

下記のコードはGPUデレゲートがJavaから使われるところです:

```java
GpuDelegate delegate = new GpuDelegate();
Interpreter.Options options = (new Interpreter.Options()).addDelegate(delegate);
Interpreter interpreter = new Interpreter(tensorflow_lite_model_file, options);
try {
  interpreter.run(input, output);
}
```

新しいハードウェアアクセレレータのサポートを追加するには、あなたは
[独自のデレゲートを定義](../performance/delegates.md#how_to_add_a_delegate)します。

### AndroidとiOS

TensorFlow Liteインタープリタは容易にこれら主要なモバイルプラットフォームで利用できます。
始めるには、[Androidクイックスタート](android.md)と
[iOSクイックスタート](ios.md)ガイドを調べてください。
[アプリケーションの例](https://www.tensorflow.org/lite/examples)はどちらのプラットフォーム用にも
用意されています。

必要なライブラリを入手するためには、Android開発者は
[TensorFlow Lite AAR](android.md#use_the_tensorflow_lite_aar_from_jcenter)を使います。
iOS
開発者は
[CocoaPods for SwiftまたはObjective-C](ios.md#add_tensorflow_lite_to_your_swift_or_objective-c_project)を使います。

### Linux

組み込みLinuxは機械学習をデプロイするための重要なプラットフォームです。
Pythonを使ってあなたのTensorFlow Liteモデルで推論を行うためには、
[Pythonクイックスタート](python.md)に倣ってください。

その代わりにC++ライブラリをインストールには、
[Raspberry Pi](build_rpi.md)用
もしくは[Arm64ベースの基板](build_arm64.md)(Odroid C2、Pine64、そして
NanoPiなどの基板)用のビルド手順を見てください。


### マイクロコントローラ

[マイクロコントローラ用TensorFlow Lite](../microcontrollers)は
TensorFlow Liteのほんの数キロバイトのメモリしかないマイクロコンピュータ用の実験的な移植です。

### オペレーション

あなたのモデルが必要とするTensorFlowオペレーションがまだ
TensorFlow Liteで実装されていない場合は、
あなたは[TensorFlowセレクト](ops_select.md)であなたのモデルでそれらを使うことができます。
あんたはカスタム版のインタープリタをビルドしてTensorFlowオペレーションを取り込まなければなりません。

あなたは[カスタムオペレーション](ops_custom.md)を使ってあなただけのぺレーションを記述するか、
新しいオペレーションをTensorFlow Liteに移植します。

[オペレータバージョン](ops_version.md)によって、あなたは新しい機能をすでに存在するオペレーションに
追加できます。

## 4. モデルの最適化

<a id="4_optimize_your_model_optional"></a>

TensorFlow Liteが提供するツールはあなたのモデルのサイズと性能を最適化しますが、
正確さへの影響はたいてい最小限です。
最適化したモデルはほんの少し
複雑な学習、変換またはインテグレーションが必要です。

機械学習の最適化は進化中の分野で、TensorFlow Liteの
[モデル最適化ツールキット](#model-optimization-toolkit)は新しいテクニックの開発に伴い
常に育っています。

### 性能

モデルの最適化の目標は性能と、モデルのサイズと、正確さの理想的なバランスに
与えられたデバイスの上で達することです。
[性能のベストプラクティス](../performance/best_practices.md)はこのプロセスを
たどる手助けをします。

### 量子化

モデルの中の値とオペレーションの制度を落とすことによって、
量子化は推論に必要な時間とモデルのサイズの両方を少なくすることができます。
多くのモデルでは、失われる正確さは最小限です。

TensorFlow LiteコンバータはTensorFlowモデルの量子化を行いやすくします。
次のPythonコードは`SavedModel`モデルを量子化してディスクに保存します:

```python
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quantized_model)
```

TensorFlow Liteは値の制度ををフルの浮動小数点から半精度の浮動小数点(float16)または8ビット整数に落とします。
モデルのサイズと正確さのトレードオフは常にあり、
いくつかのオペレーションではこれら減少した精度の型に最適化して実装されています。

量子化についてさらに学ぶには、
[学習前の量子化](../performance/post_training_quantization.md)
を見てください。

### モデル最適化ツールキット

[モデル最適化ツールキット](../performance/model_optimization.md)は
開発者がモデルを最適化するために設計されたツールとテクニックの集まりです。
テクニックの多くは全てのTensorFlowモデルに適用でき、また
TensorFlow Lite特有のものではありません、
しかしそれらは推論を限られたリソースのデバイス上で走らせる際に特に有用です。

## 次のステップ

あなたはもうTensorFlow Liteのことを知っています、次のリソースのいくつかを探ってみてください:

*   あなたがモバイル開発者であれば、[Androidクイックスタート](android.md)もしくは
    [iOSクイックスタート](ios.md)を訪れてください。
*   あなたがLinuxの組み込みデバイスを作っているならば、[Pythonクイックスタート](
    python.md)または[Raspberry Pi](build_rpi.md)と
    [Arm64ベースの基板](build_arm64.md)向けのC++ビルド説明を見てください。
*   私たちの[学習済みモデル](../models)を見てください。
*   私たちの[例アプリ](https://www.tensorflow.org/lite/examples)を確かめてください。
