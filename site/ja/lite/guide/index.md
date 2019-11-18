# TensorFlow Liteガイド

TensorFlow Liteは開発者がTensorFlowモデルをモバイル、組み込み、
そしてIoTデバイス上で走らせるのを助けるためのツール群である。
それは低レイテンシーで小さなバイナリサイズでのオンデバイスの機械学習推論を可能にする。

TensorFlow Liteは2つの大きな要素から成っている：

-   特別に最適されたモデルを、携帯電話、
    組み込みLinuxデバイス、そしてマイクロコントローラーで走らせる[TensorFlow Liteインタープリター](inference.md)
-   TensorFlowモデルをインタープリターに使われるために効率的な形式に変換し、最適化を加えてバイナリサイズと性能を向上させる[TensorFlow Lite今ベーター](../convert/index.md)。

### エッジでの機械学習

TensorFlow Liteは機械学習をデバイス上で、サーバーとデータのやり取りをせずに、ネットワークの「エッジ（端）で」行うことを容易にするために設計された。
開発者にとって、機械学習をオンデバイスで行うことで次が向上させる：

*   *レイテンシー:* サーバーへの往復がない
*   *プライバシー:* データはデバイスを離れなくていい
*   *接続性:* インターネット接続は必要でない
*   *電源消費:* ネットワーク接続は電源を食う

TensorFlow Liteは小さなマイクロコントローラーから強力な携帯電話まで莫大な幅のデバイスで動作する。

キーポイント: TensorFlow Liteバイナリは全てのサポートされたオペレーターがリンクされた場合に300KBより小さく、 普通の画像分類モデルInceptionV3とMobileNetをサポートするために必要なオペレーターのみを使うときには200KBより小さい。

## 始めよう

TensorFlow Liteをモバイルデバイス上で扱い始めるには、
[始めよう](get_started.md)を見なさい。
もしもTensorFlow Liteモデルをマイクロコントローラーにデプロイしたかったら、
[Microcontrollers](../microcontrollers)をみなさい。

## 主な機能

*   オンデバイスのアプリケーション用に最適化されたコアオペレータをサポートし、また小さなバイナリサイズの、
    *オンデバイスのML用に調整された[インタープリター](inference.md)*。
*   *多様なプラットフォームのサポート*, [Android](android.md)と[iOS](ios.md)
    デバイス、組み込みLinux、そしてマイクロコントローラーを含み、プラットフォームのAPIを使って
    推論お高速化を行う。
*   Java、Swift、Objective-C、C++、そして
    Pythonを含む*複数の言語用のAPI*。
*   *高い性能*、サポートされたデバイスでの[ハードウェアアクセレレーション](../performance/gpu.md)、dバイス最適されたカーネル、そして
    [pre-fused activations and biases](ops_compatibility.md)。
*   *モデル最適化のためのツール*、including
    正確さを犠牲にせずにモデルのサイズを小さくし、性能を向上させることのできる[量子化](../performance/post_training_quantization.md)。
*   *効果的なモデルの形式*、小さなサイズと可搬性に最適化された[FlatBuffer](../convert/index.md)の使用
*   あなたのアプリケーション用にカスタマイズできる、共通の機械学習タスクの*[Pre-trainedモデル](../models)* *   機械学習モデルをサポートされたプラットフォームにデプロイする方法をあなたに見せる*[サンプルとチュートリアル](https://www.tensorflow.org/examples)*。

## 開発のワークフロー

TensorFlow Liteを使うワークフローは次のステップからなります：

1.  **モデルを選ぶ**

    あなた自身のTensorFlowモデルを追ってくる、オンラインでモデルを見つける、または
    私たちの[Pre-trained models](../models)をそのまま使うか再学習する。

1.  **モデルを変換する**

    カスタムモデルをあなたが使っているならば、
    [TensorFlow Lite converter](../convert/index.md)を使い、
    数行のPythonでTensorFlow Lite形式に変換する。

1.  **あなたのデバイスへデプロイする**

    あなたのモデルをオンデバイスで、
    たくさんの言語のAPIを使い、[TensorFlow Lite interpreter](inference.md)で使い走らせる。

1.  **あなたのモデルを最適化する**

    私たちの[Model Optimization Toolkit](../performance/model_optimization.md)
    を使い、モデルのサイズを小さくし、正確さには影響を与えずに効率を高める。

あなたのプロジェクトでのTensorFlow Liteの使い方についてさらに学ぶには、[Get started](get_started.md)を見てください。

## 技術的な制約

TensorFlow Liteは高性能のオンデバイス推論を任意のTensorFlowモデルに提供しようと計画しています。
しかしながら、TensorFlow Liteインタープリターが現在サポートするのは
オンデバイスでの使用の最適化された、TensorFlowオペレーターのサブセットです。
これはいくつかのモデルはTensorFlow Liteで動かすには追加のステップが必要であることを意味します。

どのオペレーターが利用可能かを学ぶには、[Operator compatibility](ops_compatibility.md)
を見てください。

あなたのモデルがTensorFlow Liteインタープリターでまだサポートされていなオペレーターを使用している場合は、
interpreter, you can use [TensorFlowセレクト](ops_select.md)を使用して
あなたのTensorFlow LiteビルドにTensorFlowオペレーターを含めることができます。
しかしながら、これによりバイナリサイズは増えます。

TensorFlow Liteは現在オンデバイスのトレーニングをサポートしませんが、
それは他の予定されている改良とともに私たちの
[ロードマップ](roadmap.md)にあります。

## 次のステップ

TensorFlow Liteについて学び続けたいですか?
下記がいくつかの次のステップです：

*   [始めよう](get_started.md)を見てTensorFlow Liteを使う際のプロセスをたどってみる。
*   あなたがモバイル開発者ならば、[Android quickstart](android.md)または
    [iOS quickstart](ios.md)を見る。
*   [TensorFlow Lite for Microcontrollers](../microcontrollers)について学ぶ。
*   私たちの[pre-trained models](../models)を探検する。
*   私たちの[例アプリ](https://www.tensorflow.org/lite/examples)を試してみる。

