# 转换器的命令行实例

这个页面展示如何在命令行中使用 TensorFlow Lite 转换器

[TOC]

## 在命令行中使用的命令 <a name="tools"></a>

以下是在命令行中使用转换器的两种方法：

*   `tflite_convert`: 从 TensorFlow 1.9 起开始支持
    `tflite_convert` 作为 Python 包的一部分被安装。简便起见，以下所有示例使用 `tflite_convert` 指代。
    *   示例: `tflite_convert --output_file=...`
*   `bazel`: 为了使用最新版本的 TensorFlow Lite Converter，你可以使用
    [pip](https://www.tensorflow.org/install/pip) 或[克隆 TensorFlow 仓库](https://www.tensorflow.org/install/source) 来安装并使用 nightly 版本的的 `bazel`。
    *   示例: `bazel run //tensorflow/lite/python:tflite_convert ----output_file=...`

### 在低于 1.9 版本的 TensorFlow 中转换模型  <a name="pre_tensorflow_1.9"></a>

如果你安装有低于 1.9 版本的 Tensorflow，并想转换模型，我们推荐你使用
[Python API](python_api.md#pre_tensorflow_1.9)。 如果你想要使用命令行转换模型, 在 Tensorflow 1.7 中，你可使用 toco。

你可以通过在终端中键入`toco —help`来获取更多关于命令行参数的细节信息。

在 TensorFlow 1.8 中没有可用的命令行工具。

## 基础示例 <a name="basic"></a>

以下部分向你展示怎样将各种数据从支持的类型转换到 TensorFlow Lite FlatBuffers。

### 转换 TensorFlow GraphDef <a name="graphdef"></a>

以下部分向你展示如何将基本的 TensorFlow GraphDef (使用 [freeze_graph.py](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/tools/freeze_graph.py) 冻结)转换为 TensorFlow Lite FlatBuffer 来进行浮点数推理。被冻结的图包含存储在检查点文件中的变量，这些变量被作为 Const ops 保存。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1
```

`input_shapes` 的取值在可能时被自动确定。

### 转换 TensorFlow SavedModel <a name="savedmodel"></a>

以下部分向你展示如何将基本的 TensorFlow SavedModel 转换为 Tensorflow Lite FlatBuffer 来进行浮点数推理。

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --saved_model_dir=/tmp/saved_model
```

[SavedModel](https://www.tensorflow.org/guide/saved_model#using_savedmodel_with_estimators)
与冻结后的图比较，它需要更少的参数，这是由于保存在 SavedModel 中的附加数据所致。
 `--input_arrays`和 `--output_arrays` 所需要的值是 [MetaGraphDef](https://www.tensorflow.org/saved_model#apis_to_build_and_load_a_savedmodel) 中 [SignatureDefs](../../serving/signature_defs.md) 里的一个聚合起来的，按照字母顺序排列的输入输出列表，它由`—saved_model_tag_set`指定。
 和 GraphDef 一样, `input_shapes` 的值也在可能时被自动定义。

现阶段暂不提供对不带 SignatureDef 的 MetaGraphDefs 或是
使用[`assets/`directory](https://www.tensorflow.org/guide/saved_model#structure_of_a_savedmodel_directory) 的 MetaGraphDefs 的支持。

### 转换 tf.Keras 模型 <a name="keras"></a>

以下部分展示如何将一个 `tf.keras` 模型转换为一个 TensorFlow Lite Flatbuffer。 

 `tf.keras` 文件必须同时包含模型和权重。

```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --keras_model_file=/tmp/keras_model.h5
```

## 量化

### 将一个TensorFlow GraphDef 转换为量化的推理 <a name="graphdef_quant"></a>

TensorFlow Lite Converter 兼容定点量化模型，详情见[这里](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/quantize/README.md)。
浮点模型中有 `FakeQuant*` ops ，它们被插入在混合层的边界来记录最大最小值的范围信息。

这产生一个量化的推理工作流，它复现了训练期间被使用的量化行为。

下列命令从"量化的" TensorFlow GraphDef 中产生量化的 TensorFlow Lite FlatBuffer。


```
tflite_convert \
  --output_file=/tmp/foo.tflite \
  --graph_def_file=/tmp/some_quantized_graph.pb \
  --inference_type=QUANTIZED_UINT8 \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --mean_values=128 \
  --std_dev_values=127
```

### 使用 "dummy-quantization\" 在浮点数图上进行量化推理 <a name="dummy_quant"></a>

为了评估生成量化图的可能的好处，转换器允许在浮点图上进行 "dummy-quantization"。参数
`--default_ranges_min` 和 `--default_ranges_max` 在所有不含有最大最小值信息的 array 中指定最大最小值范围。"Dummy-quantization" 的精度低一些，但也近似于一个精确量化模型。

下方的例子展示了一个带有 Relu6 激活函数的模型。由此，我们可以得出一个合理的猜测，大部分的激活函数的范围应该在[0, 6]。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --output_file=/tmp/foo.cc \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --inference_type=QUANTIZED_UINT8 \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --default_ranges_min=0 \
  --default_ranges_max=6 \
  --mean_values=128 \
  --std_dev_values=127
```

## 确定输入和输出的数组

### 多输入数组

如下方的例子所示，参数 `input_arrays` 接受一个用逗号分隔的列表作为输入数组。

这对于有多输入的模型或子图来说是很有用的。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_2016_08_28_frozen.pb.tar.gz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/inception_v1_2016_08_28_frozen.pb \
  --output_file=/tmp/foo.tflite \
  --input_shapes=1,28,28,96:1,28,28,16:1,28,28,192:1,28,28,64 \
  --input_arrays=InceptionV1/InceptionV1/Mixed_3b/Branch_1/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_2/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_3/MaxPool_0a_3x3/MaxPool,InceptionV1/InceptionV1/Mixed_3b/Branch_0/Conv2d_0a_1x1/Relu \
  --output_arrays=InceptionV1/Logits/Predictions/Reshape_1
```

需要注意的是， `input_shapes` 是用冒号分割的列表。其中， 每个输入形状对应于各自数组中相同位置的输入数组。

### 多输出数组

如下方的例子所示，参数 `output_arrays` 接收一个用逗号分隔的列表作为输出数组。

这对于有多输出的模型或子图来说是很有用的。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_2016_08_28_frozen.pb.tar.gz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/inception_v1_2016_08_28_frozen.pb \
  --output_file=/tmp/foo.tflite \
  --input_arrays=input \
  --output_arrays=InceptionV1/InceptionV1/Mixed_3b/Branch_1/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_2/Conv2d_0a_1x1/Relu
```

### 指定子图

输入文件中的任何数组都可以被指定为输入或输出数组，以便从输入的图文件中提取子图。TensorFlow Lite
Converter 忽略指定子图范围之外的该图的其他部分。 可使用 [graph visualizations](#graph_visualizations) 来识别组成所需子图的输入和输出数组。

下列命令展示怎样从一个 TensorFlow GraphDef 中提取单个混合层。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_2016_08_28_frozen.pb.tar.gz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/inception_v1_2016_08_28_frozen.pb \
  --output_file=/tmp/foo.pb \
  --input_shapes=1,28,28,96:1,28,28,16:1,28,28,192:1,28,28,64 \
  --input_arrays=InceptionV1/InceptionV1/Mixed_3b/Branch_1/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_2/Conv2d_0a_1x1/Relu,InceptionV1/InceptionV1/Mixed_3b/Branch_3/MaxPool_0a_3x3/MaxPool,InceptionV1/InceptionV1/Mixed_3b/Branch_0/Conv2d_0a_1x1/Relu \
  --output_arrays=InceptionV1/InceptionV1/Mixed_3b/concat_v2
```

注意，TensorFlow Lite FlatBuffers 中的最终表示的粒度往往比 TensorFlow GraphDef 非常细的表示粒度更粗。例如，虽然在 TensorFlow GraphDef 中，一个全连接层通常被表示为至少四个单独的 op (变形，矩阵乘法，偏置项目加，Relu…)，但在转换器的最优表示和最终设备上的表示中，它通常被表示为单个“混合的op”。

由于粒度变粗，一些中间的数组 (例如 TensorFlow GraphDef 中矩阵乘和偏置项加之间的数组)将被丢弃。

当使用`--input_arrays` 和 `--output_arrays`指定中间数组时，推荐（有时是必须）指定在混合后生成的最终形式的图中保留的数组。它们通常是激活函数的输出（因为在每一层中，所有在激活函数前出现的部分都倾向于被混合）。

## 记录日志


## 可视化图

转换器可将图输出为 Graphviz Dot 格式，可使用`--output_format` 参数或是
`--dump_graphviz_dir`参数轻松地进行可视化。下面的小节概述了多个用例。

### 使用 `--output_format=GRAPHVIZ_DOT` <a name="using_output_format_graphviz_dot"></a>

第一种渲染 Graphviz 的方式是将 GRAPHVIZ_DOT` 参数传入
`、`—output_format`。这将生成可视化图。此操作降低了在 TensorFlow GraphDef 和 TensorFlow Lite FlatBuffer 间转换的要求。当到 TFLite 的转换失败时，此操作是很有用的。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --output_file=/tmp/foo.dot \
  --output_format=GRAPHVIZ_DOT \
  --input_shape=1,128,128,3 \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1
```

生成的`.dot` 文件可以使用以下命令渲染为pdf文件：

```
dot -Tpdf -O /tmp/foo.dot
```

生成的 `.dot.pdf` 文件可以在任何 PDF 阅读器上查看，但我们建议使用一个能够在大页面上缩放自如的查看工具，例如 Google Chrome ：

```
google-chrome /tmp/foo.dot.pdf
```

可在下一节中在线查看示例的 PDF。

### 使用 `--dump_graphviz_dir`

第二种渲染 Graphviz 的办法是传入 `—dump_graphviz_dir`参数，并指定保存渲染结果文件的目标目录。

和前一个方法不同的是，此方法保留了原始输出格式。它提供了由特定图生成实际图的可视化的转换过程。

```
curl https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_0.50_128_frozen.tgz \
  | tar xzv -C /tmp
tflite_convert \
  --graph_def_file=/tmp/mobilenet_v1_0.50_128/frozen_graph.pb \
  --output_file=/tmp/foo.tflite \
  --input_arrays=input \
  --output_arrays=MobilenetV1/Predictions/Reshape_1 \
  --dump_graphviz_dir=/tmp
```

此操作将在目标文件夹中生成一些文件。 其中，两个最重要的文件是 `toco_AT_IMPORT.dot` 和`/tmp/toco_AFTER_TRANSFORMATIONS.dot`。
`toco_AT_IMPORT.dot` 文件只包含转换的原始图，此操作在载入时就被完成。由于每个节点的信息有限，

这导致生成的可视化结果不好理解。此操作在转换命令失败时十分有用。

`toco_AFTER_TRANSFORMATIONS.dot` 含有模型在被输出之前，且在进行了所有的转换之后的信息。

通常，这个图文件比较小，且包含每个节点更多的细节信息。

和之前一样，这些文件可以被渲染为PDF文件：

```
dot -Tpdf -O /tmp/toco_*.dot
```

示例输出文件如下所示。需要注意的是，它们展示的都是图片右上角的同一个
`AveragePool` 节点。

<table><tr>
  <td>
    <a target="_blank" href="https://storage.googleapis.com/download.tensorflow.org/example_images/toco_AT_IMPORT.dot.pdf">
      <img src="../images/convert/sample_before.png"/>
    </a>
  </td>
  <td>
    <a target="_blank" href="https://storage.googleapis.com/download.tensorflow.org/example_images/toco_AFTER_TRANSFORMATIONS.dot.pdf">
      <img src="../images/convert/sample_after.png"/>
    </a>
  </td>
</tr>
<tr><td>before</td><td>after</td></tr>
</table>

### 像“拍视频”一样记录日志

当使用 `--dump_graphviz_dir` 命令时，通常会再传入一个
`—dump_graphviz_video`命令。这个命令使得每次图转换后，都会保存一个图可视化“快照”。这可能导致需要存储非常多的图可视化文件。
通常，人们通过查看这些文件来了解图的变化过程。

### 图形可视化的图例 <a name="graphviz_legend"></a>

*   “操作”为红色方块:
    *   大部分的操作看起来像是这样
        <span style="background-color:#db4437;color:white;border:1px;border-style:solid;border-color:black;padding:1px">bright
        red</span>。
    *   一些重量级操作 (比如卷积)看起来像是这样
        <span style="background-color:#c53929;color:white;border:1px;border-style:solid;border-color:black;padding:1px">darker
        red</span>。
*   数组看起来像是这样:
    *   常量数组
        <span style="background-color:#4285f4;color:white;border:1px;border-style:solid;border-color:black;padding:1px">blue</span>。
    *   激活数组
        *   内部 (中间) 激活数组
            <span style="background-color:#f5f5f5;border:1px;border-style:solid;border-color:black;border:1px;border-style:solid;border-color:black;padding:1px">light
            gray</span>。
        *   被指定为 `--input_arrays` 或`--output_arrays` 的激活数组
            <span style="background-color:#9e9e9e;border:1px;border-style:solid;border-color:black;padding:1px">dark
            gray</span>。
    *   RNN 的状态数组是绿色的。 由于转换器显式地表示RNN的回边，每个RNN 状态被表示为两个绿色数组:
        *   作为RNN回边输入的激活数组 (例如，当它的内容在被计算后复制到RNN的状态数组），此时它看起来像是这样
            <span style="background-color:#b7e1cd;border:1px;border-style:solid;border-color:black;padding:1px">light
            green</span>。
        *   实际的 RNN 状态数组看起来像这样
            <span style="background-color:#0f9d58;color:white;border:1px;border-style:solid;border-color:black;padding:1px">dark
            green</span>。它是RNN回边更新的目标。