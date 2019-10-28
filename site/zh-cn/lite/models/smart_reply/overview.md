# 智能回复

<img src="https://github.com/tensorflow/tensorflow/raw/master/tensorflow/lite/g3doc/models/images/smart_reply.png" class="attempt-right" />

## 开始

我们的智能回复模型基于聊天消息生成回复建议。该建议是主要是依据上下文的相关内容，一触即发的响应帮助用户轻松回复传入的消息。

<a class="button button-primary" href="http://download.tensorflow.org/models/tflite/smartreply_1.0_2017_11_01.zip">下载入门模型和标签</a>

### 应用示例

在 Android 上，演示 TensorFlow Lite 智能回复模型的示例

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/smart_reply/android">查看
Android 示例应用</a>

阅读该
[GitHub 页面](https://github.com/tensorflow/examples/tree/master/lite/examples/smart_reply/android/)
以了解该应用的工作原理。其中，你还会学到如何定制化 C++ ops。

## 怎么运行

该模型为会话聊天消息生成回复建议。

该设备内置的模型可以带来以下优势：
<ul>
  <li>运行快速：该模型内置在设备中和无需网络连接。因此，模型推理快速，同时平均延迟只有几毫秒。</li>
  <li>资源高效：该模型在设备中占用的内存很小。</li>
  <li>隐私保护：用户数据从不离开设备。</li>
</ul>

## 例子展示

<img alt="Animation showing smart reply" src="https://github.com/tensorflow/tensorflow/raw/master/tensorflow/lite/g3doc/models/smart_reply/images/smart_reply.gif" />

## 了解更多

<ul>
  <li><a href="https://arxiv.org/pdf/1708.00630.pdf">论文</a></li>
  <li><a href="https://github.com/tensorflow/examples/tree/master/lite/examples/smart_reply/android">源码</a></li>
</ul>

## 落地场景

<ul>
  <li><a href="https://www.blog.google/products/gmail/save-time-with-smart-reply-in-gmail/">Gmail</a></li>
  <li><a href="https://www.blog.google/products/gmail/computer-respond-to-this-email/">Inbox</a></li>
  <li><a href="https://blog.google/products/allo/google-allo-smarter-messaging-app/">Allo</a></li>
  <li><a href="https://research.googleblog.com/2017/02/on-device-machine-intelligence.html">智能回复在上 Android Wear 的应用</a></li>
</ul>
