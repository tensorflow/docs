# 转换器命令行参考

本页为 TensorFlow 1.9 至 TensorFlow 最新版本中 TensorFlow Lite 转换器命令行使用的命令行参数提供全面参考。

## 高级命令行参数

下列高级命令行参数指定输入文件和输出文件的细节。命令行参数 `--output_file` 总是需要指定。此外，`--graph_def_file`，`--saved_model_dir` 和 `--keras_model_file` 至少需要指定一个。

* `--output_file`。类型：字符串。指定输出文件的全路径。

* `--graph_def_file`。类型：字符串。指定输入 GraphDef 文件（使用 [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py)冻结）的全路径。

* `--saved_model_dir`。类型：字符串。指定包含 SavedModel 的目录的全路径。

* `--keras_model_file`。类型：字符串。指定包含 tf.keras 模型的 HDF5 文件的全路径。 

* `--output_format`。类型：字符串。缺省值：`TFLITE`。指定输出文件的格式。允许下列值：

    * `TFLITE`：TensorFlow Lite FlatBuffer 格式。    
    * `GRAPHVIZ_DOT`：GraphViz `.dot` 格式包含图变换后生成一个图可视化。 

* 请注意，将 `--output_format` 设为 `GRAPHVIZ_DOT` 会对 TFLite 特定变换造成损失。因此，所得的可视化可能无法反映最终的图变换。如果想获得反映所有图变换的最终可视化，请使用 `--dump_graphviz_dir`。

以下命令行参数指定使用 SavedModels 时的可选函数参数。

* `--saved_model_tag_set`。类型：字符串。缺省值： [kSavedModelTagServe](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/cc/saved_model/tag_constants.h)。指定一组以逗号分隔的标签，用于识别要分析的 SavedModel 内的 MetaGraphDef。标签组中的所有标签都必须指定。

* `--saved_model_signature_key`：类型: 字符串。缺省值：`tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY`。指定识别包含输入和输出的 SignatureDef 的键。

## 模型命令行参数

模型命令行参数提供有关储存在输入文件中的模型的额外信息。

* `--input_arrays`。类型：以逗号分隔的字符串列表。指定一个包含输入激活张量名称的列表。

* `--output_arrays`。类型：以逗号分隔的字符串列表。 指定一个包含输出激活张量名称的列表。

以下命令行参数定义输入张量的属性。命令行参数 `--input_arrays` 中的每一项应该根据索引对应以下命令行参数中的每一项。

* `--input_shapes`。类型：以冒号分隔的列表，列表由以逗号分隔的整数组成的子列表组成。每个子列表指定一个输入数组的形状，形状的格式参见 [TensorFlow 惯例](https://www.tensorflow.org/guide/tensor#shape)。

* 例： `--input_shapes=1,60,80,3` 对于一个典型的视觉模型，表示批量大小为 1 ， 输入图像的高为 60 ， 输入图像的宽为 80 ， 输入图像的深为 3 （代表红绿蓝通道）。

* 例： `--input_arrays=foo,bar --input_shapes=2,3:4,5,6` 表示 "foo" 的形状为 [2, 3]， "bar" 的形状为 [4, 5, 6]。
    
* `--std_dev_values`， `--mean_values`。 类型：以逗号分隔的浮点列表。它们指定当输入数组量化时，输入数组的量化（或反量化）函数参数。只有当 `inference_input_type` 被指定为 `QUANTIZED_UINT8` 时，才需要设定它们。

    * `mean_values` 与 `std_dev_values` 的意义如下：量化输入数组中的每个量化值将根据如下公式被解读为一个数学实数（即一个输入激活值）：

    * `real_value = (quantized_input_value - mean_value) / std_dev_value`。

* 当对一个量化输入进行浮点推断 （`--inference_type=FLOAT`） 时，在进行浮点推断之前，推断代码将立即根据上述公式对量化输入进行反量化。

* 当进行量化推断 （`--inference_type=QUANTIZED_UINT8`） 时，推断代码不会进行反量化。然而，所有数组的量化函数参数，包括输入数组通过 `mean_value` 和 `std_dev_value` 指定的量化函数参数，决定了量化推断代码中使用的不动点乘数。`mean_value` 在进行量化推断时必须是整数。

## 变换命令行参数

变换命令行参数指定应用在图上的可选变换，即它们指定输出文件应具有哪些属性。

* `--inference_type`。类型：字符串。缺省值：`FLOAT`。输出文件中所有实数数组的数据类型，输入数组 （用 `--inference_input_type` 指定）除外。必须是 `{FLOAT, QUANTIZED_UINT8}`。

    这个命令行参数只影响实数数组，包括浮点数组和量化数组。这不包括其他所有数据类型，包括通常整数（plain integer）数组和字符串数组。具体如下：
    
    * 如果指定为 `FLOAT`，那么输出文件中的实数数组将是浮点型。如果它们在输入文件中被量化，则它们将被反量化。

    * 如果指定为 `QUANTIZED_UINT8`，那么输出文件中的实数数组将被量化为 uint8。如果它们在输入文件中是浮点型，则它们将被量化。

* `--inference_input_type`。类型：字符串。输出文件中的一个实数输入数组的数据类型。所有输入数组的数据类型的缺省值是与 `--inference_type`的指定相同。这个命令行参数的主要目的是生成一个具有量化输入数组的浮点图。在输入数组之后紧接着添加一个反量化算子。必须是 `{FLOAT, QUANTIZED_UINT8}`。

    这个命令行参数主要用于这样的视觉模型：输入是位图，但是要求浮点推断。对于这样的图像模型，其 uint8 输入将被量化，并且这样的输入数组使用的量化函数参数是它们的 `mean_value` 和 `std_dev_value` 函数参数。

* `--default_ranges_min`， `--default_ranges_max`。类型：浮点型。指定缺省（最小，最大）区间值，用于所有没有指定区间的数组。允许用户对未量化的输入文件或者错误量化的输入文件进行量化。这些命令行参数导致模型准确率降低。它们的目的在于通过“虚拟量化”来简单试验一下量化。

* `--drop_control_dependency`。类型：布尔型。 缺省值：True。指定是否静默丢弃控制依赖。这是由于 TensorFlow Lite 不支持控制依赖。

* `--reorder_across_fake_quant`。类型：布尔型。 缺省值：False。指定是否对预料之外的位置上的 FakeQuant 节点进行重新排序。用于 FakeQuant 节点的位置阻碍图变换，以至于影响转换图的情况。它会导致生成的图与量化训练图不同，有可能会造成不同的算术行为。

* `--allow_custom_ops`。类型：字符串。 缺省值：False。指定是否允许自定义操作。当设定为 false 时，所有未知操作都会报错。当定义为 true 时，所有未知操作会生成自定义操作。开发者需通过在 TensorFlow Lite runtime 配置自定义解析器来提供这些信息。

* `--post_training_quantize`。类型：布尔型。 缺省值：False。指定是否量化被转换的浮点模型的权重。模型将变小，延迟将改善（以准确率降低为代价）。

## 日志命令行参数

下列命令行参数在图变换过程中的多个时间点生成 [GraphViz](https://www.graphviz.org/) `.dot` 文件的图可视化。

- `--dump_graphviz_dir`。类型：字符串。指定 GraphViz `.dot` 文件输出到的目录的全路径。在读入图之后，以及所有变换完成之后，会输出图。

- `--dump_graphviz_video`。类型：布尔型。指定是否在每次图变换之后输出 GraphViz 文件。它要求 `--dump_graphviz_dir` 有指定值。
