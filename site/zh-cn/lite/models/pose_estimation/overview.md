# 姿势预测

<img src="../images/pose.png" class="attempt-right" />

## 开始使用

_PoseNet_ 能够通过预测图像或视频中人体的关键位置进行姿势的预测。

<a class="button button-primary" href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/multi_person_mobilenet_v1_075_float.tflite">下载此模块</a>

Android 和 iOS 设备上的一对一课程即将面世. 与此同时，如果您想要在 web 浏览器中体验此模块，可以访问
<a href="https://github.com/tensorflow/tfjs-models/tree/master/posenet">TensorFlow.js
GitHub 代码仓库</a>.

## 工作原理

姿势检测通过使用计算机图形技术来对图片和视频中的人进行检测和判断，如图片中的人露出了肘臂。

为了达到清晰的目的，该算法只是对图像中的人简单的预测身体关键位置所在，而不会去辨别此人是谁。

关键点检测使用“编号 部位”的格式进行索引，并对部位的探测结果伴随一个信任值。信任值取值范围在 0.0 至 1.0，1.0 为最高信任值。

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

性能很大程度取决于您的设备性能以及输出的幅度(热点图和偏移向量)。PoseNet 对于不同尺寸的图片是不变式，也就是说在原始图像和缩小后图像中预测姿势位置是一样的。这也意味着 PostNet 能精确配置性能消耗。

输出幅度决定了缩小后的和输入的图片尺寸的相关程度。输出幅度同样影响到了图层的尺寸和输出的模型。更高的输出幅度决定了更小的网络和输出的图层分辨率，和更小的可信度。

在此示例中，输出幅度可以为 8、16 或 32。换句话说，当输出幅度为 32，则会拥有最高性能和最差的可信度；当输出幅度为 8，则会有用最高的可信度和最低的性能。我们给出的建议是 16。

下图展示了输出幅度的程度决定缩放后的输出和输入的图像的相关度。更高的输出幅度速度更快，但也会导致更低的可信度。

<img alt="Output stride and heatmap resolution" src="../images/output_stride.png" >

## 关于此模块的更多内容

<ul>
  <li><a href="https://medium.com/tensorflow/real-time-human-pose-estimation-in-the-browser-with-tensorflow-js-7dd0bc881cd5">博客: 使用 TensorFlow.js 在浏览器端上实现实时人体姿势检测</a></li>
  <li><a href="https://github.com/tensorflow/tfjs-models/tree/master/posenet">TF.js 代码库: 浏览器中的姿势检测: PoseNet Model</a></li>
</ul>

### 使用案例

<ul>
  <li><a href="https://vimeo.com/128375543">‘毛绒球镜子’</a></li>
  <li><a href="https://youtu.be/I5__9hq-yas">神奇艺术之将你变为鸟</a></li>
  <li><a href="https://vimeo.com/34824490">木偶队列</a></li>
  <li><a href="https://vimeo.com/2892576">弥撒的声音 (性能)</a></li>
  <li><a href="https://www.instagram.com/p/BbkKLiegrTR/">现实添加</a></li>
  <li><a href="https://www.instagram.com/p/Bg1EgOihgyh/">互动动画片</a></li>
  <li><a href="https://www.runnersneed.com/expert-advice/gear-guides/gait-analysis.html">步态分析</a></li>
</ul>
