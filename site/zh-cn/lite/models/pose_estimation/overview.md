# 姿势预测

<img src="../images/pose.png" class="attempt-right" />

## 开始使用

_PoseNet_ 能够通过预测图像或视频中人体的关键位置进行姿势的预测。

<a class="button button-primary" href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/multi_person_mobilenet_v1_075_float.tflite">下载此模块</a>

Android 和 iOS 设备上的一对一课程即将面世. 与此同时，如果您想要在web浏览器中体验此模块，可以访问
<a href="https://github.com/tensorflow/tfjs-models/tree/master/posenet">TensorFlow.js
GitHub 代码仓库</a>.

## 工作原理

姿势检测通过使用计算机图形技术来对图片和视频中的人进行检测和判断，如图片中的人露出了肘臂。

为了达到清晰的目的，该算法只是对图像中的人简单的预测身体关键位置所在，而不会去辨别此人是谁。

关键点检测使用“编号 部位”的格式进行索引，并对部位的探测结果伴随一个信任值。信任值取值范围在0.0至1.0，1.0为最高信任值。

<table style="width: 30%;">
  <thead>
    <tr>
      <th>编号</th>
      <th>部位</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>鼻子</td>
    </tr>
    <tr>
      <td>1</td>
      <td>左眼</td>
    </tr>
    <tr>
      <td>2</td>
      <td>右眼</td>
    </tr>
    <tr>
      <td>3</td>
      <td>左耳</td>
    </tr>
    <tr>
      <td>4</td>
      <td>右耳</td>
    </tr>
    <tr>
      <td>5</td>
      <td>左肩</td>
    </tr>
    <tr>
      <td>6</td>
      <td>右肩</td>
    </tr>
    <tr>
      <td>7</td>
      <td>左肘</td>
    </tr>
    <tr>
      <td>8</td>
      <td>右肘</td>
    </tr>
    <tr>
      <td>9</td>
      <td>左腕</td>
    </tr>
    <tr>
      <td>10</td>
      <td>右腕</td>
    </tr>
    <tr>
      <td>11</td>
      <td>左髋</td>
    </tr>
    <tr>
      <td>12</td>
      <td>右髋</td>
    </tr>
    <tr>
      <td>13</td>
      <td>左膝</td>
    </tr>
    <tr>
      <td>14</td>
      <td>右膝</td>
    </tr>
    <tr>
      <td>15</td>
      <td>左踝</td>
    </tr>
    <tr>
      <td>16</td>
      <td>右踝</td>
    </tr>
  </tbody>
</table>

## 示例输出

<img alt="Animation showing pose estimation" src="https://www.tensorflow.org/images/lite/models/pose_estimation.gif"/>

## 模块性能

性能很大程度取决于您的设备性能以及输出的幅度(热点图和偏移向量). The PoseNet model is image size invariant, which means it can predict
pose positions in the same scale as the original image regardless of whether the
image is downscaled. This means PoseNet can be configured to have a higher
accuracy at the expense of performance.

The output stride determines how much we’re scaling down the output relative to
the input image size. It affects the size of the layers and the model outputs.
The higher the output stride, the smaller the resolution of layers in the
network and the outputs, and correspondingly their accuracy. In this
implementation, the output stride can have values of 8, 16, or 32. In other
words, an output stride of 32 will result in the fastest performance but lowest
accuracy, while 8 will result in the highest accuracy but slowest performance.
We recommend starting with 16.

The following image shows how the output stride determines how much we’re
scaling down the output relative to the input image size. A higher output stride
is faster but results in lower accuracy.

<img alt="Output stride and heatmap resolution" src="../images/output_stride.png" >

## 关于此模块的更多内容

<ul>
  <li><a href="https://medium.com/tensorflow/real-time-human-pose-estimation-in-the-browser-with-tensorflow-js-7dd0bc881cd5">Blog post: Real-time Human Pose Estimation in the Browser with TensorFlow.js</a></li>
  <li><a href="https://github.com/tensorflow/tfjs-models/tree/master/posenet">TF.js GitHub: Pose Detection in the Browser: PoseNet Model</a></li>
</ul>

### 使用案例

<ul>
  <li><a href="https://vimeo.com/128375543">‘PomPom Mirror’</a></li>
  <li><a href="https://youtu.be/I5__9hq-yas">Amazing Art Installation Turns You Into A Bird | Chris Milk "The Treachery of Sanctuary"</a></li>
  <li><a href="https://vimeo.com/34824490">Puppet Parade - Interactive Kinect Puppets</a></li>
  <li><a href="https://vimeo.com/2892576">Messa di Voce (Performance), Excerpts</a></li>
  <li><a href="https://www.instagram.com/p/BbkKLiegrTR/">Augmented reality</a></li>
  <li><a href="https://www.instagram.com/p/Bg1EgOihgyh/">Interactive animation</a></li>
  <li><a href="https://www.runnersneed.com/expert-advice/gear-guides/gait-analysis.html">Gait analysis</a></li>
</ul>
