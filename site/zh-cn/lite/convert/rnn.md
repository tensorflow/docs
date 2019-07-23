# 转换 RNN 模型

TensorFlow Lite 解释器目前实现了部分 TensorFlow 操作。由于那些缺失的操作，部分模型架构不能立刻被转换。

一些基于 RNN 的架构将会受到这个情况的影响。下列文档概述了目前的现状，并提供了转换 RNN 模型的策略。

## 目前支持的转换

目前，只要没有指定 `sequence_length`，就可以成功转换使用[`tf.nn.static_rnn`](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn) 的 RNN 模型。

下列 `tf.nn.rnn_cell` 操作使用 `tf.nn.static_rnn`:

*   [tf.nn.rnn_cell.LSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/LSTMCell)
*   [tf.nn.rnn_cell.RNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/RNNCell)
*   [tf.nn.rnn_cell.GRUCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/GRUCell)
*   [tf.nn.rnn_cell.BasicLSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/BasicLSTMCell)
*   [tf.nn.rnn_cell.BasicRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/BasicRNNCell)

另外，TensorFlow Lite 提供了一些 RNN 操作的替代方法。这些方法使你可以在 TensorFlow Lite 中使用动态 RNN 架构。

可用的替代方法如下：

*   [tf.nn.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)
*   [tf.nn.bidirectional_dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)
*   [tf.nn.rnn_cell.RNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/RNNCell)
*   [tf.nn.rnn_cell.LSTMCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/LSTMCell)

## 暂不支持的转换

TensorFlow Lite 目前暂不支持 [Control Flow](https://www.tensorflow.org/api_docs/cc/group/control-flow-ops) 操作。这表示，除非使用下文中提到的转换策略，否则使用下列 TensorFlow 函数的模型将不能被成功转换：

*   [tf.nn.static_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn) 同时指明了 `sequence_length`
*   [tf.nn.dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)
*   [tf.nn.bidirectional_dynamic_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)

注意：TensorFlow Lite 计划在 2019 年底前实现所有必须的 Control Flow 操作。届时，所有的 RNN 架构将可以被成功转换。

## 转换策略

为了成功转换使用了上述函数的 RNN 模型，你需要修改它的架构并且重新训练。下列策略是可行的：

### 1. 重构

如果可能，最简单的策略是重构模型架构，使用不带有 `sequence_length` 的 [tf.nn.static_rnn](https://www.tensorflow.org/api_docs/python/tf/nn/static_rnn)。

### 2. 使用操作提示和融合操作的替代方法

TensorFlow Lite 为 RNN 操作提供了一些替代方法，使得在 TensorFlow Lite 中可以使用动态 RNN 架构。使用 [OpHints](https://www.tensorflow.org/lite/guide/ops_custom#converting_tensorflow_models_to_convert_graphs)，这些方法在训练时可以正常运行，但在 TensorFlow Lite 解释器中运行时，它们被替换为特殊的融合操作。

下列是可用的替代方法：

*   [tf.lite.experimental.nn.dynamic_rnn](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn.py#L41)
    *   替代 tf.nn.dynamic_rnn
*   [tf.lite.experimental.nn.bidirectional_dynamic_rnn](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn.py#L279)
    *   替代 tf.nn.bidirectional_dynamic_rnn
*   [tf.lite.experimental.nn.TfLiteRNNCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn_cell.py#L39)
    *   替代 tf.nn.rnn_cell.RNNCell
*   [tf.lite.experimental.nn.TfLiteLSTMCell](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/rnn_cell.py#L159)
    *   替代 tf.nn.rnn_cell.LSTMCell


注意：这些替代方法必须一起使用。例如，如果你正在使用 `tf.lite.experimental.nn.dynamic_rnn`，你必须将它和 `tf.lite.experimental.nn.TfLiteRNNCell` 配合使用，而不是使用 `tf.nn.rnn_cell.RNNCell`。


使用[tf.keras.layers.StackedRNNCells](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StackedRNNCells) 来替换 [tf.nn.rnn_cell.MultiRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/MultiRNNCell)。


[TensorFlow Lite LSTM ops API](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/g3doc/README.md) 提供了使用这些替代方法的教程。

有关的 Colab 教程，可以参阅 [TensorFlowLite_LSTM_Keras_Tutorial](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/examples/lstm/TensorFlowLite_LSTM_Keras_Tutorial.ipynb)。

注意：对于 [tf.nn.rnn_cell.GRUCell](https://www.tensorflow.org/api_docs/python/tf/nn/rnn_cell/GRUCell)，没有可替代的方法。