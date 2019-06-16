# 将Keras模型导入Tensorflow.js

Keras模型（通常通过Python API创建）可能被保存成[多种格式之一](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model). 整个模型格式可以被转换为Tensorflow.js的层(Layer)格式，这个格式可以被加载并直接用作Tensorflow.js的推断或是进一步的训练。

转换后的TensorFlow.js图层(Layer)格式是一个包含model.json文件和一组二进制格式的分片权重文件的目录。 model.json文件包含模型拓扑结构（又名“架构(architecture)”或“图形(graph)”：它是对图层(Layer)及其连接方式的描述）和权重文件的清单。

## 要求

转换过程要求Python的编程环境，您可能需要独立的使用[pipenv](https://github.com/pypa/pipenv)或是[virtualenv](https://virtualenv.pypa.io)。并使用 `pip install tensorflowjs`安装转换器

将Keras模型导入Tensorflow.js需要两步过程。首先，将已有Keras模型转换成TF.js层(Layer)格式，然后将其加载进Tensorflow.js。

## Step 1. 将已有Keras模型转换成TF.js层(Layer)格式

Keras模型通常通过 `model.save(filepath)`进行保存，这样做会产生一个同时含有模型拓扑结构以及权重的HDF5(.h5)文件。如需要转换这样一个文件成为TF.js层格式，则可以运行以下代码。这里的`path/to/my_model.h5`为Keras .h5文件地址，而`path/to/tfjs_target_dir`则是对应输出的TF.js目录。

```sh
# bash

tensorflowjs_converter --input_format keras \
                       path/to/my_model.h5 \
                       path/to/tfjs_target_dir
```

## 另一种方式: 使用 Python API 直接导出为 TF.js 图层(Layer)格式

如果您有一个Python的Keras模型，您可以用以下方法直接输出一个Tensoflow.js图层(Layers)格式:


```py
# Python

import tensorflowjs as tfjs

def train(...):
    model = keras.models.Sequential()   # for example
    ...
    model.compile(...)
    model.fit(...)
    tfjs.converters.save_keras_model(model, tfjs_target_dir)
```

## Step 2: 将模型加载进Tensorflow.js

使用一个web服务器为您在步骤1中生成的转换后的模型文件提供服务。注意，您可能需要将您的服务器配置为[允许跨源资源共享(CORS)](https://enable-cors.org/), 以允许在 JavaScript 中提取文件。

然后通过提供model.json文件的URL将模型加载到TensorFlow.js中：


```js
// JavaScript

import * as tf from '@tensorflow/tfjs';

const model = await tf.loadLayersModel('https://foo.bar/tfjs_artifacts/model.json');
```

现在，该模型已准备好进行推理(inference)，评估(evaluation)或重新训练(re-training)。例如，模型完成加载后可以立即进行预测(predict)：


```js
// JavaScript

const example = tf.fromPixels(webcamElement);  // for example
const prediction = model.predict(example);
```

很多[Tensorflow.js样例](https://github.com/tensorflow/tfjs-examples)采用这种方法，使用已在 Google 云存储上转换和托管的预训练模型。

注意，您使用`model.json`文件名引用整个模型。`loadModel(...)` 获取 `model.json`，并且通过额外的HTTP(S)请求以获取`model.json`权重清单中引用的分片权重文件。 此方法允许浏览器将这些文件全部缓存(可还能被缓存在互联网上其他缓存服务器中)。这是因为 `model.json`和权重分块都小于典型的缓存文件大小限制。因此这个模型可能在随后的场景中加载地更快。


## 已支持的特性

TensorFlow.js的图层(Layers)目前仅支持基于标准Keras结构的Keras模型。 使用不支持的操作(ops)或层(layers)的模型 - 例如 自定义图层，Lambda图层，自定义损失(loss)或自定义指标(metrics)无法自动导入，因为它们依赖于无法被可靠地转换为JavaScript的Python代码。
