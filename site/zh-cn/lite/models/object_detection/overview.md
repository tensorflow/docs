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

An object detection model is trained to detect the presence and location of
multiple classes of objects. For example, a model might be trained with images
that contain various pieces of fruit, along with a _label_ that specifies the
class of fruit they represent (e.g. an apple, a banana, or a strawberry), and
data specifying where each object appears in the image.

When we subsequently provide an image to the model, it will output a list of the
objects it detects, the location of a bounding box that contains each object,
and a score that indicates the confidence that detection was correct.

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

To interpret these results, we can look at the score and the location for each
detected object. The score is a number between 0 and 1 that indicates confidence
that the object was genuinely detected. The closer the number is to 1, the more
confident the model is.

Depending on your application, you can decide a cut-off threshold below which
you will discard detection results. For our example, we might decide a sensible
cut-off is a score of 0.5 (meaning a 50% probability that the detection is
valid). In that case, we would ignore the last two objects in the array, because
those confidence scores are below 0.5:

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
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">Banana</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">0.23</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">[42, 66, 57, 83]</td>
    </tr>
    <tr>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">Apple</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">0.11</td>
      <td style="background-color: #e9cecc; text-decoration-line: line-through;">[6, 42, 31, 58]</td>
    </tr>
  </tbody>
</table>

The cut-off you use should be based on whether you are more comfortable with
false positives (objects that are wrongly identified, or areas of the image that
are erroneously identified as objects when they are not), or false negatives
(genuine objects that are missed because their confidence was low).

For example, in the following image, a pear (which is not an object that the
model was trained to detect) was misidentified as a "person". This is an example
of a false positive that could be ignored by selecting an appropriate cut-off.
In this case, a cut-off of 0.6 (or 60%) would comfortably exclude the false
positive.

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
注意：
Note: Object detection models accept input images of a specific size. This is likely to be different from the size of the raw image captured by your device’s camera, and you will have to write code to crop and scale your raw image to fit the model’s input size (there are examples of this in our <a href="#get_started">example applications</a>).<br /><br />The pixel values output by the model refer to the position in the cropped and scaled image, so you must scale them to fit the raw image in order to interpret them correctly.

## 初始模块

We recommend starting with this pre-trained quantized COCO SSD MobileNet v1
model.

<a class="button button-primary" href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">Download
starter model and labels</a>

### Uses and limitations

The object detection model we provide can identify and locate up to 10 objects
in an image. It is trained to recognize 80 classes of object. For a full list of
classes, see the labels file in the
<a href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">model
zip</a>.

If you want to train a model to recognize new classes, see
<a href="#customize_model">Customize model</a>.

For the following use cases, you should use a different type of model:

<ul>
  <li>Predicting which single label the image most likely represents (see <a href="../image_classification/overview.md">image classification</a>)</li>
  <li>Predicting the composition of an image, for example subject versus background (see <a href="../segmentation/overview.md">segmentation</a>)</li>
</ul>

### Input

The model takes an image as input. The expected image is 300x300 pixels, with
three channels (red, blue, and green) per pixel. This should be fed to the model
as a flattened buffer of 270,000 byte values (300x300x3). Since the model is
<a href="../../performance/post_training_quantization.md">quantized</a>, each
value should be a single byte representing a value between 0 and 255.

### Output

The model outputs four arrays, mapped to the indices 0-4. Arrays 0, 1, and 2
describe 10 detected objects, with one element in each array corresponding to
each object. There will always be 10 objects detected.

<table>
  <thead>
    <tr>
      <th>Index</th>
      <th>Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Locations</td>
      <td>Multidimensional array of [10][4] floating point values between 0 and 1, the inner arrays representing bounding boxes in the form [top, left, bottom, right]</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Classes</td>
      <td>Array of 10 integers (output as floating point values) each indicating the index of a class label from the labels file</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Scores</td>
      <td>Array of 10 floating point values between 0 and 1 representing probability that a class was detected</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Number and detections</td>
      <td>Array of length 1 containing a floating point value expressing the total number of detection results</td>
    </tr>
  </tbody>
</table>

## Customize model

The pre-trained models we provide are trained to detect 80 classes of object.
For a full list of classes, see the labels file in the
<a href="http://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip">model
zip</a>.

You can use a technique known as transfer learning to re-train a model to
recognize classes not in the original set. For example, you could re-train the
model to detect multiple types of vegetable, despite there only being one
vegetable in the original training data. To do this, you will need a set of
training images for each of the new labels you wish to train.

Learn how to perform transfer learning in
<a href="https://medium.com/tensorflow/training-and-serving-a-realtime-mobile-object-detector-in-30-minutes-with-cloud-tpus-b78971cf1193">Training
and serving a real-time mobile object detector in 30 minutes</a>.
