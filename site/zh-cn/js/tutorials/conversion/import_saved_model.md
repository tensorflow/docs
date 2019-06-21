# 在TensorFlow.js中引入TensorFlow GraphDef模型

TensorFlow GraphDef模型（一般是通过Python API创建的）可以保存成以下几种格式：
1. TensorFlow [SavedModel](https://www.tensorflow.org/programmers_guide/saved_model#overview_of_saving_and_restoring_models)
2. [Frozen Model](https://www.tensorflow.org/mobile/prepare_models#how_do_you_get_a_model_you_can_use_on_mobile)
3. [Session Bundle](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/session_bundle/README.md)
4. [Tensorflow Hub module](https://www.tensorflow.org/hub/)

以上所有格式都可以被[TensorFlow.js converter](https://github.com/tensorflow/tfjs-converter)转换成TensorFlow.js可读取的模型格式，并用于推算（inference）。

（注意：TensorFlow已经淘汰了session bundle格式，请将您的模型转换成SavedModel格式。）

## 必要条件

模型转换的工作需要用到Python环境；你可以用[pipenv](https://github.com/pypa/pipenv) 或 [virtualenv](https://virtualenv.pypa.io)创建一个隔离的环境。用这条命令安装模型转换器：

```bash
 pip install tensorflowjs
```

将TensorFlow模型引入到TensorFlow.js需要两个步骤。首先，将您的模型转换为TensorFlow.js可用的web格式，然后载入到TensorFlow.js中。

## 第一步：将TensorFlow模型转换至TensorFlow.js可用的 web 格式模型

运行转换器提供的转换脚本：

用法：以SavedModel为例：

```bash
tensorflowjs_converter \
    --input_format=tf_saved_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    --saved_model_tags=serve \
    /mobilenet/saved_model \
    /mobilenet/web_model
```

Frozen model 为例:

```bash
tensorflowjs_converter \
    --input_format=tf_frozen_model \
    --output_node_names='MobilenetV1/Predictions/Reshape_1' \
    /mobilenet/frozen_model.pb \
    /mobilenet/web_model
```

Tensorflow Hub module 为例:

```bash
tensorflowjs_converter \
    --input_format=tf_hub \
    'https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/1' \
    /mobilenet/web_model
```

|脚本参数 | 描述 |
|---|---|
|`input_path`  | saved model, session bundle 或 frozen model的完整的路径，或TensorFlow Hub模块的路径。|
|`output_path` | 输出文件的保存路径。|

| 选项 | 描述
|---|---|
|`--input_format`     | 要转换的模型的格式。SavedModel 为 tf_saved_model, frozen model 为 tf_frozen_model, session bundle 为 tf_session_bundle, TensorFlow Hub module 为 tf_hub，Keras HDF5 为 keras。 |
|`--output_node_names`| 输出节点的名字，每个名字用逗号分离。|
|`--saved_model_tags` | 只对SavedModel转换用的选项：输入需要加载的MetaGraphDef相对应的tag，多个tag请用逗号分隔。默认为 `serve`。|
|`--signature_name`   | 只对TensorFlow Hub module转换用的选项：对应要加载的签名，默认为`default`。请参考 https://www.tensorflow.org/hub/common_signatures/.|

用以下命令查看帮助信息：

```bash
tensorflowjs_converter --help
```

### 转换器产生的文件

转换脚本会产生两种文件：

* `model.json` （数据流图和权重清单）
* `group1-shard\*of\*` （二进制权重文件）

这里举例Mobilenet v2模型转换后输出的文件：

```html
  output_directory/model.json
  output_directory/group1-shard1of5
  ...
  output_directory/group1-shard5of5
```

## 第二步：在浏览器加载和运行模型

1. 安装tfjs-convert npm包：

`yarn add @tensorflow/tfjs` 或 `npm install @tensorflow/tfjs`

2. 创建 [FrozenModel class](https://github.com/tensorflow/tfjs-converter/blob/master/src/executor/frozen_model.ts) 并开始推算：

```js
import * as tf from '@tensorflow/tfjs';
import {loadGraphModel} from '@tensorflow/tfjs-converter';

const MODEL_URL = 'model_directory/model.json';

const model = await loadGraphModel(MODEL_URL);
const cat = document.getElementById('cat');
model.execute(tf.fromPixels(cat));
```

具体代码请参考 [MobileNet 演示](https://github.com/tensorflow/tfjs-converter/tree/master/demo/mobilenet).

`loadGraphModel` API中的`LoadOptions`参数可以用来发送密钥或者自定义请求中的头文件。更多信息请参考 [loadGraphModel() 文档](https://js.tensorflow.org/api/1.0.0/#loadGraphModel)。

## 支持的操作

目前，TensorFlow.js只支持部分TensorFlow算子。若您的模型包含了不被支持的算子，`tensorflowjs_converter`脚本会报错并列出您的模型中不被支持的算子。请在github上发起 [issue](https://github.com/tensorflow/tfjs/issues)让我们知道您需要支持的算子。

## 加载模型权重

若您只需要加载模型的权重，请参考以下代码：

```js
import * as tf from '@tensorflow/tfjs';

const weightManifestUrl = "https://example.org/model/weights_manifest.json";

const manifest = await fetch(weightManifestUrl);
this.weightManifest = await manifest.json();
const weightMap = await tf.io.loadWeights(
        this.weightManifest, "https://example.org/model");
```
