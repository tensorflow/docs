# 图像分类

<img src="../images/image.png" class="attempt-right">

使用优化的预训练模型来识别上百种对象，包括人、活动、动物、植物和地点。

## 开始

如果你对图像分类的概念不熟悉，你应该先阅读 <a href="#what_is_image_classification">什么是图像分类？</a>

关于如何在移动应用中使用图像分类，推荐查看我们提供的 <a href="#example_applications_and_guides">示例应用和指导</a>。

如果你使用 Android 和 iOS 之外的平台，或者你已经熟悉了 TensorFlow Lite 接口，你可以直接下载我们的新手图像分类模型及其附带的标签。

<a class="button button-primary" href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip">下载新手图像分类及标签</a>

当新手模型在你的目标设备运行起来之后，你可以尝试其他模型，在性能、准确率以及模型体积间找到最佳的平衡点。详见 <a href="#choose_a_different_model">选择不同模型</a>。

### 示例应用和指导

我们在 Android 和 iOS 平台上都有图像分类的示例应用，并解释了它们的工作原理。

#### Android

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android">查看Android示例</a>

阅读 [Android example guide](android.md) 以了解应用工作原理。

#### iOS

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios.md">查看iOS示例</a>

阅读 [iOS example guide](ios.md) 以了解应用工作原理。

#### 截屏

下面的截屏为 Android 图像分类示例应用。

<img src="images/android_banana.png" alt="Screenshot of Android example" width="30%">

## 什么是图像分类？

机器学习的一个常见应用是图像识别。比如，我们可能想要知道下图中出现了哪类动物。

<img src="images/dog.png" alt="dog" width="50%">

预测图像类别的任务被称为 _图像分类_ 。训练图像分类模型的目的是识别各类图像。比如，一个模型可能被训练用于识别三种动物的特征：兔子、仓鼠和狗。

当我们提供一张新的图片给模型时，它会输出这张图片含有这三种动物的概率。以下是一个输出示例：

<table style="width: 40%;">
  <thead>
    <tr>
      <th>动物种类</th>
      <th>概率</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>兔子</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>仓鼠</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td style="background-color: #fcb66d;">狗</td>
      <td style="background-color: #fcb66d;">0.91</td>
    </tr>
  </tbody>
</table>

基于输出，我们能够看到分类模型预测出，这张图片有很大概率表示的是一条狗。

注意：图像分类只能告诉你图片里出现的类别及其概率，并且只能是被训练过的类别。它不能告诉你图片里对象的位置或者名称。
如果你需要识别图片里对象的名称及位置，你应该使用 <a href="../object_detection/overview.md">物体检测</a> 模型。

### 训练、标签和推断

在训练中，用图像和其对应的 _标签_ 投喂一个图像分类模型。每个标签是一个概念或种类的名字。这个模型就要学会去识别这些标签。

给予足够多的训练数据（通常一个标签对应数以百计的图片），这个图像分类模型就能够学习去预测新的图片是否属于训练数据中的某些种类。这个预测的过程被称为 _推断_ 。

为了执行推断，一张图片被输入进模型中。接着，模型将输出一串代表概率的数组，元素大小介于 0 和 1 之间。结合我们的示例模型，这个过程可能如下所示：

<table style="width: 60%">
  <tr style="border-top: 0px;">
    <td style="width: 40%"><img src="images/dog.png" alt="dog"></td>
    <td style="width: 20%; font-size: 2em; vertical-align: middle; text-align: center;">→</td>
    <td style="width: 40%; vertical-align: middle; text-align: center;">[0.07, 0.02, 0.91]</td>
</table>

输出中的每个数字都对应训练数据中的一个标签。将我们的输出和这三个训练标签关联，我们能够看出，这个模型预测了这张图片中的对象有很大概率是一条狗。

<table style="width: 40%;">
  <thead>
    <tr>
      <th>标签</th>
      <th>概率</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>兔子</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>仓鼠</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td style="background-color: #fcb66d;">狗</td>
      <td style="background-color: #fcb66d;">0.91</td>
    </tr>
  </tbody>
</table>

你可能注意到这些概率的总和（兔子，仓鼠和狗的概率）是 1。这是多分类模型的常见输出。（详见：<a href="https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax">Softmax</a>）

### 模糊不清的结果

既然概率的总和总是等于 1，那么如果这张图片没有被模型识别出来，也就是不属于被训练的种类，你可能会发现它的几个标签都没有特别大的概率。

比如，下表可能表示了一个模糊不清的结果：

<table style="width: 40%;">
  <thead>
    <tr>
      <th>标签</th>
      <th>概率</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>兔子</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>仓鼠</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>狗</td>
      <td>0.34</td>
    </tr>
  </tbody>
</table>

### 使用和限制

我们提供的这些图形分类模型对单标签分类很有用。单标签分类是指预测图像最有可能表示的某一个标签。这些模型被训练用于识别 1000 类图像。完整的标签列表：<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip">模型压缩包</a>

如果你想要训练模型识别新的类别：<a href="#customize_model">自定义模型</a>.

针对以下使用案例，你应该采用不同的模型：

<ul>
  <li>预测图片里的一个或多个对象的种类和位置（详见：<a href="../object_detection/overview.md">物体检测</a>）</li>
  <li>预测图像的组成，比如主体与背景（详见：<a href="../segmentation/overview.md">分割</a>）</li>
</ul>


当新手模型在你的目标设备运行起来之后，你可以尝试其他模型，在性能、准确率以及模型体积间找到最佳的平衡点。详见：<a href="#choose_a_different_model">选择不同模型</a>。

## 选择不同模型

我们的 <a href="../../guide/hosted_models.md">模型列表</a> 中有许多图像分类模型供你选择。
你应该在它们的性能、准确率和模型体积之间进行权衡，以选择对你来说最优的模型。

### 性能

我们根据在同样的硬件条件下，一个模型执行推断所花费的时间来衡量性能。时间越短，模型越快。

你需要的性能取决于你的应用。对实时视频这类应用来说，性能可能非常重要。因为需要在下一帧绘制完之前及时分析每一帧（例如：推断用时必须少于 33 ms 才能实时推断 30 fps 的视频流）。

我们经过量化的MobileNet 模型的性能范围为 3.7 ms 至 80.3 ms。

### 准确率

我们根据模型正确分类图像的频率来衡量准确度。比如，一个准确率为 60% 的模型平均有 60% 的时间能正确分类一张图片。

我们的 <a href="../../guide/hosted_models.md">模型列表</a> 提供 Top-1 和 Top-5 准确率数据。Top-1 是指模型输出正确标签的概率为最高的频率。Top-5 是指模型输出正确标签的概率在前五的频率。

我们经过量化的 MobileNet 模型的准确率范围为 64.4% 至 89.9%。

### 体积

磁盘上模型的体积因其性能和准确性而异。体积可能对移动开发（可能影响应用的下载体积）或者硬件开发（可用存储可能是有限的）很重要。

我们经过量化的 MobileNet 模型的准确率范围为 0.5 Mb 至 3.4 Mb。

### 模型结构

<a href="../../guide/hosted_models.md">模型列表</a> 中的模型有不同的结构，从模型名可以看出，比如，你可以选择 MobileNet、Inception 或者其他的结构。

模型的结构影响它的性能、准确率和体积。我们提供的模型都是用同样的数据训练的，意味着你可以通过我们提供的统计数据对比这些模型，来选择最适合你的应用的。

注意：我们提供的图像分类模型接受的输入尺寸不同。有些模型将其标注在文件名上。比如，Mobilenet_V1_1.0_224 模型接受 224x224 像素的输入。<br /><br />
所有模型都要求每个像素有三个颜色通道（红、绿、蓝）。经过量化的模型中每个通道需要 1 个字节，浮点模型中每个通道需要 4 个字节。<br /><br />
我们的 <a href="android.md">Android</a> 和 <a href="ios.md">iOS</a> 代码样本展示了如何将全尺寸相机图像处理为每个模型需要的格式。

## 自定义模型

我们提供的预训练模型被训练用于识别 1000 类图像。完整的标签列表：<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip">模型压缩包</a>。

你能使用 _迁移学习_ 技术来再训练(re-train)一个模型，以识别新的类别。比如你能再训练一个模型来区分不同品种的树，尽管原始训练数据中并没有树。为了达到这个目的，你的每个新标签都需要一组训练图片。

学习如何实现迁移学习：<a href="https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android/#0">用 TensorFlow 识别花卉</a> codelab。