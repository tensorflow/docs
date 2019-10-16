# 物体检测

<img src="../images/detection.png" class="attempt-right">

使用矩形框识别图片中的多个对象。可以辨别出80多种不同种类的物体。

## 开始使用

如果你是 TensorFlow Lite 新手并且使用 Android 或 iOS 进行工作，我们推进您使用如下的应用实例帮助您进行探索。

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/android"> Android 
示例</a>
<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/ios"> iOS 
示例</a>

如果您使用的不是 Android 或 iOS 平台，或者您对于 <a href="https://www.tensorflow.org/api_docs/python/tf/lite">TensorFlow Lite APIs</a> 较为熟悉, 您可以下载我们的初始对象检测模块以及对应的标签。

<a class="button button-primary" href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">下载初始模块和标签</a>

更多关于初始模块的内容，请参考
<a href="#starter_model">初始模块</a>.

## 何为物体检测?

对于给定的图片或者视频流，对象检测模块可以识别出已知的物体和该物体在图片中的位置。例如，如下的<a href="#get_started">示例应用</a>屏幕截图中展示了如何辨识物体以及标注对应的坐标:

<img src="images/android_apple_banana.png" alt="Screenshot of Android example" width="30%">

物体检测模块被训练用于检测多种物体的存在以及他们的位置。例如，模型可使用包含多个水果的图片和水果所分别代表（如，苹果，香蕉，草莓）的 _label_  进行训练，返回的数据指明了图像中对象所出现的位置。

随后，当我们为模型提供图片，模型将会返回一个列表，其中包含检测到的对象，包含对象矩形框的坐标和代表检测可信度的分数。
### 模块输出

想象一下一个模块被训练用于检测苹果，香蕉和草莓。当我们输入一幅图片后，模块将会返回给我们一组本示例的检测结果。

<table style="width: 60%;">
  <thead>
    <tr>
      <th>类别</th>
      <th>分数</th>
      <th>坐标</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>苹果</td>
      <td>0.92</td>
      <td>[18, 21, 57, 63]</td>
    </tr>
    <tr>
      <td>香蕉</td>
      <td>0.88</td>
      <td>[100, 30, 180, 150]</td>
    </tr>
    <tr>
      <td>草莓</td>
      <td>0.87</td>
      <td>[7, 82, 89, 163] </td>
    </tr>
    <tr>
      <td>香蕉</td>
      <td>0.23</td>
      <td>[42, 66, 57, 83]</td>
    </tr>
    <tr>
      <td>苹果</td>
      <td>0.11</td>
      <td>[6, 42, 31, 58]</td>
    </tr>
  </tbody>
</table>

### 信任分数

我们使用信任分数和所检测到对象的坐标来表示检测结果。分数反应了被检测到物体的可信度，范围在 0 和 1 之间。最大值为1，数值越大可信度越高。

您可以检测到裁切的极限值并据此放弃检测结果，这取决于您的应用。 在我们的示例中，我们检测到裁切的极限值为 0.5 （这意味50%的检测是可信的）。在此示例中，我们将会忽略数组中最后两个对象，因为他们的信任分数低于了 0.5 。
<table style="width: 60%;">
  <thead>
    <tr>
      <th>类型</th>
      <th>分数</th>
      <th>坐标</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>苹果</td>
      <td>0.92</td>
      <td>[18, 21, 57, 63]</td>
    </tr>
    <tr>
      <td>香蕉</td>
      <td>0.88</td>
      <td>[100, 30, 180, 150]</td>
    </tr>
    <tr>
      <td>草莓</td>
      <td>0.87</td>
      <td>[7, 82, 89, 163] </td>
    </tr>
    <tr>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">香蕉</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">0.23</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">[42, 66, 57, 83]</td>
    </tr>
    <tr>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">苹果</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">0.11</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">[6, 42, 31, 58]</td>
    </tr>
  </tbody>
</table>

使用裁切功能必须基于误判位置（物体识别错误或物体位置识别有误）或错误（由于可信度过低导致的物体未被捕捉）。
如下图所示，梨子（未被模块训练检测的物体）被误判为“人”。实例中的误判可以通过适当的图片裁切来忽略。在此示例中，裁剪 0.6 （或 60% ）可以适当的排除误判。

<img src="images/false_positive.png" alt="Screenshot of Android example showing a false positive" width="30%">

### 坐标

针对每个被检测的物体，模块将会返回一个由四个数字组成的数组，该四个数字代表了围绕物体的一个矩形框。在我们提供的示例模块中，返回的数组中的元素按照如下顺序：
<table style="width: 50%; margin: 0 auto;">
  <tbody>
    <tr style="border-top: none;">
      <td>[</td>
      <td>top,</td>
      <td>left,</td>
      <td>bottom,</td>
      <td>right</td>
      <td>]</td>
    </tr>
  </tbody>
</table>

top 的值代表了矩形框的顶部距离图片上部的距离，单位为像素。 left 的值代表了矩形框的左边距离图片左边的距离。bottom 和 right 值的表示方法同理。
注意：对象检测模块接受特定尺寸的模型作为输入。这很有可能与您的图像设备生成的原始图片尺寸不同，所以您需要编写代码将原始图片缩放至模型可接受的尺寸(我们提供了 <a href="#get_started">示范程序</a>)。 <br /><br />模块输出的像素值表示在缩放后的图片中的位置，所以您需要调整调整原始图片等尺寸来保证正确。

## 初始模型

我们推荐使用预训练的量化 COCO SSD MobileNet v1 模型来入门。

<a class="button button-primary" href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">下载初始模型和标签</a>

### 用法和限制

物体检测模块最多能够在一张图中识别和定位10个物体。目前支持80种物体的识别，详细列表如下：
<a href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">model
zip</a>.

如果您需为识别新类型而训练模型，请参考
<a href="#customize_model">自定义模块</a>.

接下来的使用案例中，您可能用到不同种类的模块：

<ul>
  <li>预测所表达内容  (参考 <a href="../image_classification/overview.md">图片分类</a>)</li>
  <li>预测图片的构成，如主题与背景 (参考 <a href="../segmentation/overview.md">分割</a>)</li>
</ul>

### 输入

模块使用单个图片作为输入。理想的图片尺寸是 300x300 像素，每个像素有3个通道（红，蓝，和绿）。这将反馈给模块一个 27000 字节（ 300 x 300 x 3 ）的扁平化缓存。由于该模块经过标准化处理，每一个字节代表了 0 到 255 之间的一个值。
### 输出

该模型输出四个数组，分别对应索引的 0-4。前三个数组描述10个被检测到的物体，每个数组的最后一个元素匹配每个对象。检测到的物体数量总是10。
<table>
  <thead>
    <tr>
      <th>索引</th>
      <th>名称</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>坐标</td>
      <td> [10][4] 多维数组，每一个元素由 0 到1 之间的浮点数，内部数组表示了矩形边框的  [top, left, bottom, right]</td>
    </tr>
    <tr>
      <td>1</td>
      <td>类型</td>
      <td>10个整型元素组成的数组（输出为浮点型值），每一个元素代表标签文件中的索引。</td>
    </tr>
    <tr>
      <td>2</td>
      <td>分数</td>
      <td>10个整型元素组成的数组，元素值为 0 至 1 之间的浮点数，代表检测到的类型</td>
    </tr>
    <tr>
      <td>3</td>
      <td>检测到的物体和数量</td>
      <td>长度为1的数组，元素为检测到的总数</td>
    </tr>
  </tbody>
</table>

## 自定义模块

我们提供预训练模块可被用于检测80多种物体。详细的列表如下：
<a href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">model
zip</a>.

您可以使用转移学习等技术来重新训练模型从而能够辨识初始设置之外的物品种类。例如，您可以重新训练模型来辨识各种蔬菜，哪怕原始训练数据中只有一种蔬菜。为达成此目标，您需要为每一个需要训练的标签准备一系列训练图片。
了解如何实时转移学习
<a href="https://medium.com/tensorflow/training-and-serving-a-realtime-mobile-object-detector-in-30-minutes-with-cloud-tpus-b78971cf1193">30分钟内训练和运行实时移动物体检测器</a>.
