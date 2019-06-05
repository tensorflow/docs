# 模型转换

TensorFlow.js 配备了各种预训练模型，这些模型可以在浏览器中使用，[模型仓库](https://github.com/tensorflow/tfjs-models) 中有相关介绍。但是，您可能已经在其他地方找到或创建了一个 TensorFlow 模型，并希望在 web 应用程序中使用该模型。为此，TensorFlow.js 提供了一个 [模型转换器](https://github.com/tensorflow/tfjs-converter) 。TensorFlow.js 转换器有两个组件:

1. 一个命令行程序，用于转换 Keras 和 TensorFlow 模型以在 TensorFlow.js 中使用。
2. 一个 API ，用于在浏览器中使用 TensorFlow.js 加载和执行模型。

## 转换您的模型

TensorFlow.js 转换器可以转换以下几种格式的模型:

**SavedModel**: 保存 TensorFlow 模型的默认格式。SavedModel 的格式细节请 [查阅此处](https://www.tensorflow.org/guide/saved_model)。

**Keras model**: Keras 模型通常保存为 HDF5 文件。有关保存 Keras 模型的更多信息，请访问 [此处](https://keras.io/getting-started/faq/#savingloading-whole-models-architecture-weights-optimizer-state)。

**TensorFlow Hub module**: 这些是打包后在 TensorFlow Hub 中进行分发的模型，TensorFlow Hub 是一个共享和发现模型的平台。模型库见 [此处](tfhub.dev)。

取决于尝试转换的模型的格式，您需要将不同的参数传递给转换器。比如，假设您保存了一个名为 `model.h5` 的 Keras 模型到 `tmp/` 目录。为了使用 TensorFlow.js 转换器转换模型，您可以运行以下命令: 

    $ tensorflowjs_converter --input_format=keras /tmp/model.h5 /tmp/tfjs_model

这会将路径为 `/tmp/model.h5` 的模型转换并输出 `model.json` 文件及其二进制权重文件到目录 `tmp/tfjs_model/` 中。

有关不同格式的模型相对应的命令行参数的更多信息，请参阅 TensorFlow.js 转换器 [自述文件](https://github.com/tensorflow/tfjs-converter)。

在转换过程中，我们会遍历模型图形并确认 TensorFlow.js 是否支持每个操作。如果是支持的，我们将图形转换成浏览器可以使用的格式。我们尝试通过将权重分成 4MB 的文件来优化模型以便在 web 上使用 - 这样它们就可以被浏览器缓存。我们也尝试使用开源工程 [Grappler](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/grappler) 简化模型图形。图形的简化包括相邻操作的折叠，消除常见子图像等。这些更改对模型的输出没有影响。为了进一步优化，用户可以输入参数以指示转换器将模型量化到特定的字节大小。量化是一种减少模型大小的技术，它是通过用更少的比特表示权重实现的。用户应务必确保量化后模型的准确度保持在可接受范围内。
如果在转换过程中遇到了不支持的操作，则该过程失败，我们将为用户打印出该操作的名称。请将此提交到我们的 [GitHub](https://github.com/tensorflow/tfjs/issues)  - 我们会尝试根据用户的需求实现更多新的操作。

### 最佳做法

虽然在转换过程中我们尽力优化您的模型，但通常确保您的模型顺利运行的最佳方式是在考虑资源受限的环境下构建。这意味着避免过于复杂的建构和尽可能减少参数（权重）的数目。

## 运行您的模型

成功转换模型之后，您将得到一组权重文件和一个模型拓扑文件。TensorFlow.js 提供模型加载 APIs ，您可以使用这些接口获取模型并且在浏览器中运行推断。

以下是加载转换后的 TensorFlow SavedModel 或 TensorFlow Hub 模块的 API :

```js
const model = await tf.loadGraphModel(‘path/to/model.json’);
```

以下是转换后的 Keras 模型的 API :

```js
const model = await tf.loadLayersModel(‘path/to/model.json’);
```

`tf.loadGraphModel` API 返回 `tf.FrozenModel`，这意味着各项参数是固定的并且您不能使用新数据对模型进行微调。`tf.loadLayersModel` API 返回可训练的 tf.Model。有关训练 tf.Model 的相关信息，请参阅[训练模型指南](train_models.md)。

在转换之后，我们建议您进行几次推断并且对模型的速度进行基准测试。基于这个目的，我们有一个独立的基准测试页面: https://github.com/tensorflow/tfjs-core/blob/master/integration_tests/benchmarks/benchmark.html。 您可能注意到我们丢弃了初始预热运行中的测量值 - 这是因为（通常情况）下，由于创建纹理和编译着色器的资源消耗，您的模型的第一次的推断将比后续推断慢几倍。
