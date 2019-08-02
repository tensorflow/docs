# 性能跑分

本文档列出了在一些 Android 和 iOS 设备上运行常见模型时 TensorFlow Lite 的跑分。

这些跑分数据由 [Android TFLite benchmark binary](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark) 及 [iOS benchmark app](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark/ios) 产生。

# 安卓环境的跑分

对于安卓环境的跑分，为了减少设备间的差异性，CPU 亲和性被设置为使用大核跑分。 (查看[详情](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark#reducing-variance-between-runs-on-android))

假设模型被下载并解压缩到 `/data/local/tmp/tflite_models` 路径。用于跑分的二进制文件

使用 [这些命令构建](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark#on-android)。
此外，我们假设该文件位于 `/data/local/tmp` 目录。

使用以下语句运行跑分:

```
adb shell taskset ${CPU_MASK} /data/local/tmp/benchmark_model \
  --num_threads=1 \
  --graph=/data/local/tmp/tflite_models/${GRAPH} \
  --warmup_runs=1 \
  --num_runs=50 \
  --use_nnapi=false
```

在这里， `${GRAPH}`是模型的名字， `${CPU_MASK}` 是CPU亲和度设置。
请从下表中选择:

Device | CPU_MASK 
-------| ----------
Pixel 2 | f0 
Pixel xl | 0c 

<table>
  <thead>
    <tr>
      <th>模型名称</th>
      <th>设备</th>
      <th>平均推理时间</th>
    </tr>
  </thead>
  <tr>
    <td rowspan = 2>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224.tgz">Mobilenet_1.0_224(float)</a>
    </td>
    <td>Pixel 2 </td>
    <td>123.3 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>113.3 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz">Mobilenet_1.0_224 (quant)</a>
    </td>
    <td>Pixel 2 </td>
    <td>65.4 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>74.6 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/nasnet_mobile_2018_04_27.tgz">NASNet mobile</a>
    </td>
    <td>Pixel 2 </td>
    <td>273.8 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>210.8 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/squeezenet_2018_04_27.tgz">SqueezeNet</a>
    </td>
    <td>Pixel 2 </td>
    <td>234.0 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>158.0 ms</td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_resnet_v2_2018_04_27.tgz">Inception_ResNet_V2</a>
    </td>
    <td>Pixel 2 </td>
    <td>2846.0 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>1973.0 ms </td>
  </tr>
  <tr>
    <td rowspan = 2>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_v4_2018_04_27.tgz">Inception_V4</a>
    </td>
    <td>Pixel 2 </td>
    <td>3180.0 ms</td>
  </tr>
   <tr>
     <td>Pixel XL </td>
     <td>2262.0 ms</td>
  </tr>


# iOS 跑分

要运行 iOS 跑分，  [跑分应用程序](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/benchmark/ios)应含有合适的模型，且 benchmark_params.json` 中的` `num_threads` 被设置为 1。

<table>
  <thead>
    <tr>
      <th>模型名称</th>
      <th>设备</th>
      <th>平均推理时间</th>
    </tr>
  </thead>
  <tr>
    <td>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224.tgz">Mobilenet_1.0_224(float)</a>
    </td>
    <td>iPhone 8 </td>
    <td>32.2 ms</td>
  </tr>
  <tr>
    <td>
      <a href="http://download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz)">Mobilenet_1.0_224 (quant)</a>
    </td>
    <td>iPhone 8 </td>
    <td>24.4 ms</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/nasnet_mobile_2018_04_27.tgz">NASNet mobile</a>
    </td>
    <td>iPhone 8 </td>
    <td>60.3 ms</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/squeezenet_2018_04_27.tgz">SqueezeNet</a>
    </td>
    <td>iPhone 8 </td>
    <td>44.3</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_resnet_v2_2018_04_27.tgz">Inception_ResNet_V2</a>
    </td>
    <td>iPhone 8</td>
    <td>562.4 ms</td>
  </tr>
  <tr>
    <td>
      <a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_v4_2018_04_27.tgz">Inception_V4</a>
    </td>
    <td>iPhone 8 </td>
    <td>661.0 ms</td>
  </tr>
 </table>

 