# TensorFlow Liteガイド

TensorFlow Liteは開発者がTensorFlowモデルをモバイル、組み込み、
そしてIoTデバイス上で走らせるのを助けるツール群です。
それは低レイテンシーで小さなバイナリサイズでのオンデバイスの機械学習推論を可能にします。

TensorFlow Liteは2つの大きな要素から成っています：

-   特別に最適化されたモデルを、携帯電話、
    組み込みLinuxデバイス、そしてマイクロコントローラーで走らせる[TensorFlow Liteインタープリター](inference.md)。
-   TensorFlowモデルをインタープリターで使うために、効率的な形式に変換して最適化を加え、バイナリサイズと性能を向上させる[TensorFlow Liteコンバーター](../convert/index.md)。

### エッジでの機械学習

TensorFlow Liteは機械学習をデバイス上で、サーバーとデータのやり取りをせずに、ネットワークの「エッジ(端)で」行うことを容易にするために設計されました。
開発者にとっては、機械学習をオンデバイスで行うことで次が向上します：

*   *レイテンシー:* サーバーへの往復がない
*   *プライバシー:* データはデバイスから出ない
*   *接続性:* インターネット接続は必要でない
*   *電源消費:* ネットワーク接続は電源を食う

TensorFlow Liteは小さなマイクロコントローラーから強力な携帯電話まで非常に多くのデバイスで動作します。

要点: TensorFlow Liteバイナリは全てのサポートされたオペレーターがリンクされた場合には300KBより小さく、
通常の画像分類モデルであるInceptionV3とMobileNetをサポートするために必要なオペレーターのみを使うときには200KBより小さいです。

## 始めよう

TensorFlow Liteをモバイルデバイス上で扱い始めるには、
[始めよう](get_started.md)を見てください。
もしもTensorFlow Liteモデルをマイクロコントローラーにデプロイしたかったら、
[マイクロコントローラ](../microcontrollers)をみてください。

## 主な機能

*   オンデバイスのアプリケーション用に最適化されたコアオペレータをサポートし、また小さなバイナリサイズの、
    *オンデバイスのML用に調整された[インタープリター](inference.md)*。
*   [Android](android.md)と[iOS](ios.md)
    デバイス、組み込みLinux、そしてマイクロコントローラを含み、推論の高速化のためにプラットフォームのAPIを使った
    *多様なデバイスのサポート*。
*   Java、Swift、Objective-C、C++、そして
    Pythonを含む*複数の言語用のAPI*。
*   サポートされたデバイスでの[ハードウェアアクセレレーション](../performance/gpu.md)、デバイス最適されたカーネル、そして
    [pre-fused activations and biases](ops_compatibility.md)による*高い性能*。
*   正確さを犠牲にせずにモデルのサイズを小さくし、性能を向上させることのできる[量子化](../performance/post_training_quantization.md)を含む
    *モデル最適化のためのツール*。
*   *効果的なモデルの形式*、小さなサイズと可搬性に最適化された[フラットバッファ](../convert/index.md)の使用
*   あなたのアプリケーション用にカスタマイズできる、共通の機械学習タスクの*[学習済みモデル](../models)*
*   機械学習モデルをサポートされたプラットフォームにデプロイする方法をあなたに見せる*[サンプルとチュートリアル](https://www.tensorflow.org/examples)*。

## 開発のワークフロー

TensorFlow Liteを使うワークフローは次のステップからなります：

1.  **モデルを選ぶ**

    あなた自身のTensorFlowモデルを持ってくる、オンラインでモデルを見つける、または
    私たちの[学習済みモデル](../models)をそのまま使うか再学習させる。

1.  **モデルを変換する**

    カスタムモデルをあなたが使っているならば、
    [TensorFlow Liteコンバータ](../convert/index.md)を使い、
    数行のPythonでTensorFlow Lite形式に変換する。

1.  **あなたのデバイスへデプロイする**

    あなたのモデルをオンデバイスで、
    種々の言語のAPIを使い、[TensorFlow Liteインタープリタ](inference.md)を使い走らせる。

1.  **あなたのモデルを最適化する**

    私たちの[モデル最適化ツールキット](../performance/model_optimization.md)
    を使い、モデルのサイズを小さくし、正確さには影響を与えずに効率を高める。

あなたのプロジェクトでのTensorFlow Liteの使い方についてさらに学ぶには、[Get started](get_started.md)を見てください。

## 技術的な制約

TensorFlow Liteは高性能のオンデバイス推論を任意のTensorFlowモデルに提供しようと計画しています。
しかしながら、TensorFlow Liteインタープリタが現在サポートするのは
オンデバイスでの使用の最適化された、TensorFlowオペレーターのサブセットです。
これはいくつかのモデルはTensorFlow Liteで動かすには追加のステップが必要であることを意味します。

どのオペレーターが利用可能かを学ぶには、[オペレータ互換性](ops_compatibility.md)
を見てください。

あなたのモデルがTensorFlow Liteインタープリタで未サポートのオペレータを使用している場合は、
[TensorFlowセレクト](ops_select.md)を使用して
あなたのTensorFlow LiteビルドにTensorFlowオペレーターを含めることができます。
しかしながら、これによりバイナリサイズは増えます。

TensorFlow Liteは現在オンデバイスの学習をサポートしていませんが、
これは他の予定されている改良とともに私たちの
[ロードマップ](roadmap.md)にあります。

## 次のステップ

TensorFlow Liteについて学び続けたいですか?
下記がいくつかの次のステップです：

*   [始めよう](get_started.md)を見てTensorFlow Liteを使う際のプロセスをたどってみる。
*   あなたがモバイル開発者ならば、[Androidクイックスタート](android.md)または
    [iOSクイックスタート](ios.md)を見る。
*   [TensorFlow Lite for Microcontrollers](../microcontrollers)について学ぶ。
*   私たちの[学習済みモデル](../models)を探検する。
*   私たちの[見本アプリ](https://www.tensorflow.org/lite/examples)を試してみる。

