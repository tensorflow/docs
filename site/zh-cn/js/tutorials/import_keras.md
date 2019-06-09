# 将Keras模型导入Tensorflow.js

Keras模型（通常通过Python API创建）可能被保存成[多种格式之一](https://keras.io/getting-started/faq/#how-can-i-save-a-keras-model). 整个模型格式可以被转换为Tensorflow.js的层(Layer)格式，这个格式可以被加载并直接用作Tensorflow.js的推断或是进一步的训练。

Tensorflow.js 的层(Layer)格式目标是一个可以容纳`model.json`文件和一系列可共享的二进制权重文件的容器。

## 要求

转换过程要求Python的编程环境，你可能需要独立的使用[pipenv](https://github.com/pypa/pipenv)或是[virtualenv](https://virtualenv.pypa.io)。并使用 `pip install tensorflowjs`安装转换器

将Keras模型导入Tensorflow.js需要两步过程。首先，将已有Keras模型转换成TF.js层(Layer)格式，然后将其加载进Tensorflow.js。

## Step 1. 将已有Keras模型转换成TF.js层(Layer)格式

Keras模型通常通过 `model.save(filepath)`进行保存，这样做会产生一个同时含有模型拓扑结构以及权重的HDF5(.h5)文件。如需要转换这样一个文件成为TF.js层格式，则可以运行以下代码。这里的`path/to/my_model.h5`为Keras .h5文件地址，而`path/to/tfjs_target_dir`则是对应输出的TF.js目录。

```sh
# bash

tensorflowjs_converter --input_format keras \
                       path/to/my_model.h5 \
                       path/to/tfjs_target_dir
```

## 代替: 使用 Python API 直接导出到 TF.js 层格式

如果你有一个Python的Keras模型，你可以用以下方法直接输出一个Tensoflow.js层格式:


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

使用一个web服务器为您在步骤1中生成的转换后的模型文件提供服务。注意，你可能需要将你的服务器配置为[允许跨源资源共享(CORS)](https://enable-cors.org/), 以允许在 JavaScript 中提取文件。

然后,通过在model.json文件中提供模型的URL,加载模型到Tensorflow.js中。


```js
// JavaScript

import * as tf from '@tensorflow/tfjs';

const model = await tf.loadLayersModel('https://foo.bar/tfjs_artifacts/model.json');
```

现在模型已经做好了推理,评价或是重新训练了。如果是为了推理，模型可以立刻被用来做出预测:


```js
// JavaScript

const example = tf.fromPixels(webcamElement);  // for example
const prediction = model.predict(example);
```

很多[Tensorflow.js样例](https://github.com/tensorflow/tfjs-examples)采用这种方法，使用已在 Google 云存储上转换和托管的预训练模型。

注意，你使用`model.json`文件名引用整个模型。`loadModel(...)` 获取 `model.json`，并且制造额外的HTTP(S)请求保持被共享的权重文件在`model.json` 的权重清单中被引用。这种方法允许所有这些文件由浏览器缓存 (也许还有互联网上的其他缓存服务器)。这是由于 `model.json`和权重的分块都小于典型的缓存文件大小限制。因此这个模型可能在随后的场景中加载的更快。


## 支持的特性

目前Tensorflow.js 层只支持使用标准Keras结构的Keras模型。那些使用非支持的操作(ops)，层(layers)将无法被自动导入，因为它们依赖于无法可靠地转换为 JavaScript 的 Python 代码。这其中涵盖了客制化的层，Lambda层，客制化的损失函数以及客制化的评价标准。
