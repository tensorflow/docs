# コンバータのコマンドラインリファレンス

このページでは、TensorFlow 2.0 でコマンドラインから [TensorFlow Lite コンバータ](index.md) を使用する方法を説明します。 ただし、より好ましいのは [Python API](python_api.md) を使用する方法です。

[TOC]

## 概要の概要

TensorFlow Lite コンバータには基本的なモデルをサポートするコマンドラインツール `tflite_convert` がありますが、量子化やその他のパラメータ (SavedModel のシグネチャや Keras モデルのカスタムオブジェクトなど) を含む場合には、 `TFLiteConverter`[Python API](python_api.md) を使用してください。

## 使い方

以下のフラグで入力ファイルと出力ファイルを指定します。

*   `--output_file` 文字列型。 出力ファイルのパスを指定する。
*   `--saved_model_dir` 文字列型。 TensorFlow 1.x もしくは 2.0 で構築した SavedModel を含むディレクトリのパスを指定する。
*   `--keras_model_file` 文字列型。 TensorFlow 1.x もしくは 2.0 で構築した tf.keras モデルを含む HDF5ファイルのパスを指定する。


使用例は以下のとおりです。

```
tflite_convert \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```

## 追加の説明

### ソースからビルドする

TensorFlow Lite Converter の最新バージョンを利用するには [pip](https://www.tensorflow.org/install/pip) を使用してナイトリービルドをインストールする方法に加えて、[TensorFlow リポジトリを clone](https://www.tensorflow.org/install/source) して `bazel` を使う方法があります。

使用例は以下のとおりです。

```
bazel run //third_party/tensorflow/lite/python:tflite_convert -- \
  --saved_model_dir=/tmp/mobilenet_saved_model \
  --output_file=/tmp/mobilenet.tflite
```
