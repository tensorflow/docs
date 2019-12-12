# Segmentation

![segmentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/images/segmentation.png)

## Get started

DeepLab 是用于语义图像分割的最先进的深度学习模型，其目标是为图像中的每个像素分配语义标签(例如人，狗，猫)。

[Download starter model](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/deeplabv3_257_mv_gpu.tflite)

## How it works

语义图像分割预测图像的每个像素是否与某个类相关联。这与检测矩形区域中目标[目标检测]的任务(https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/object_detection/overview.md)和对整个图像进行分类[图像分类]的任务(https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/image_classification/overview.md)形成对照。

当前的实现包括以下功能：

1. DeepLabv1 :我们使用 atrous convolution 来显示地控制在深度卷积神经网络中计算特征响应部分的分辨率。
2. DeepLabv2 :我们应用 atrous spatial pyramid pooling(ASPP) ,使用多个采样率和有效视野的过滤器,在多种尺度上稳健地分割目标对象。
3. DeepLabv3 :我们使用图像级特征[5,6]来扩展ASPP模块以捕获更长距离的信息。我们还增加了批标准化[7]参数以加快训练。特别的，在训练和评估期间我们应用 atrous convolution 来提取不同输出步幅的输出特征，这在输出步幅等于16时有效的促进了批标准化训练,并在输出步幅为8时得到了更高的评估效果。
4. DeepLabv3+ :我们扩展了 DeepLabv3 ,增加了一个简单但有效的解码器模块，以优化细分结果，尤其是沿着对象边界。此外，在这种编码器-解码器结构中，可以通过 atrous convolution 任意地控制所提取的编码器特征的分辨率，以折衷精度和运行时间。

## Example output

该模型将以很高的精度在目标对象上创建掩膜。
![segmentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/models/segmentation/images/segmentation.gif)

## Read more about segmentation

* [Semantic Image Segmentation with DeepLab in TensorFlow](https://ai.googleblog.com/2018/03/semantic-image-segmentation-with.html)
* [TensorFlow Lite Now Faster with Mobile GPUs (Developer Preview)](https://medium.com/tensorflow/tensorflow-lite-now-faster-with-mobile-gpus-developer-preview-e15797e6dee7)
* [DeepLab: Deep Labelling for Semantic Image Segmentation](https://github.com/tensorflow/models/tree/master/research/deeplab)
