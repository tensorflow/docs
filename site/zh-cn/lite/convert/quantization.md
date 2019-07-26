# 转换量化模型
本文提供有关如何转换量化 TensorFlow Lite 模型的信息。详细信息，请参阅[模型优化](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/performance/model_optimization.md)。

# 训练后：针对特定 CPU 型号的量化模型
创建小模型的最简单方法是在推理期间将权重量化为 8 位并“在运行中”量化输入/激活。这具有延迟优势，但优先考虑减小尺寸。

在转换期间，将 optimizations 标志设置为针对大小进行优化：
```
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
```

# 训练过程中：仅用于整数执行的量化模型
仅用于整数执行的量化模型获得具有更低延迟，更小尺寸和仅针对整数加速器兼容模型的模型。目前，这需要训练具有["假量化"节点](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize)的模型 。

转换图表：
```
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.inference_type = tf.lite.constants.QUANTIZED_UINT8
input_arrays = converter.get_input_arrays()
converter.quantized_input_stats = {input_arrays[0] : (0., 1.)}  # mean, std_dev
tflite_model = converter.convert()
```
对于全整数模型，输入为 uint8。mean 和 std_dev values 指定在训练模型时这些 UINT8 的值是如何值映射到输入的浮点值。

mean 是 0 到 255 之间的整数值，映射到浮点数 0.0f。std_dev = 255 /（float_max - float_min）

对于大多数用户，我们建议使用训练后量化。我们正在研究用于后期训练和训练量化的新工具，我们希望这将简化生成量化模型。
