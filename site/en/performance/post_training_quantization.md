
### Post-training quantization

Post-training quantization is a general technique to reduce the model size while also
providing up to 3x lower latency with little degradation in model accuracy. Post-training
quantization quantizes weights to 8-bits of precision from floating-point. This technique
is enabled  in `tflite_convert`:

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/some_quantized_graph.pb \
  --post_training_quantize
```

At inference, weights are converted from 8-bits of precision to floating-point and
computed using floating point kernels. This conversion is done once and cached to reduce latency.

To further improve latency, hybrid operators dynamically quantize activations to 8-bits and
perform computations with 8-bit weights and activations. This optimization provides latencies
close to fully fixed-point inference. However, the outputs are still stored using
floating-point, so the speedup with hybrid ops is less than a full fixed-point computation.
Hybrid ops are available for the most compute-intensive operators in a network:

*  [tf.contrib.layers.fully_connected](https://www.tensorflow.org/api_docs/python/tf/contrib/layers/fully_connected)
*  [tf.nn.conv2d](https://www.tensorflow.org/api_docs/python/tf/nn/conv2d)
*  [tf.nn.embedding_lookup](https://www.tensorflow.org/api_docs/python/tf/nn/embedding_lookup)
*  [BasicRNN](https://www.tensorflow.org/api_docs/python/tf/contrib/rnn/BasicRNNCell)
*  [tf.nn.bidirectional_dynamic_rnn for cells are tf.nn.rnn_cell.BasicRNNCell](https://www.tensorflow.org/api_docs/python/tf/nn/bidirectional_dynamic_rnn)
*  [tf.nn.dynamic_rnn for LSTM and BasicRNN Cell types](https://www.tensorflow.org/api_docs/python/tf/nn/dynamic_rnn)


Since weights are quantized post-training, there could be an accuracy loss, particularly for
smaller networks. Pre-trained fully quantized models are provided for specific networks in
the [TensorFlow Lite model repository](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/g3doc/models.md#image-classification-quantized-models){:.external}. It is important to check the accuracy of the quantized model to verify that any degradation
in accuracy is within acceptable limits. There is a tool to evaluate [TensorFlow Lite model accuracy](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/lite/tools/accuracy/README.md){:.external}.

