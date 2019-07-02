ios快速入门指南

为了能在IOS系统上开发TF Lite，我们推荐您先浏览以下内容
举个栗子：

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios">iOS
image classification example</a>

如果你想了解一些关于源码的说明，你还需阅读
[TensorFlow Lite iOS image classification](https://www.tensorflow.org/lite/models/image_classification/ios).

这些示例APP使用[image classification](https://www.tensorflow.org/lite/models/image_classification/overview)
连续不断地将后置摄像头的图像进行分类，并显示最有可能的分类。
它允许用户在浮点或者[quantized](https://www.tensorflow.org/lite/performance/post_training_quantization)
模型中选择然后挑选选择要对其执行推理的线程数。

笔记：其他IOS应用在[Examples](https://www.tensorflow.org/lite/examples)中展示了
非常多的可实施方案。

##向Objective-C或者Swift项目中添加TensorFlow Lite

TensorFlow Lite提供了用
[Swift](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/swift)
和
[Objective-C](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/objc).
写的一些本地化库，如此你可以快速上手书写你的IOS代码，我们推荐使用
[Swift image classification example](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios)
作为起始点。

下面这部分展示了如何向你的项目中添加TensorFlow Lite Swift或者Objective-C

### CocoaPods开发者

在Podfile中添加TensorFlow Lite pod然后运行`pod install`

#### Swift

```ruby
use_frameworks!
pod 'TensorFlowLiteSwift'
```

#### Objective-C

```ruby
pod 'TensorFlowLiteObjC'
```

### Bazel 开发者
在你的BUILD文件中，添加“TensorFlowLite”依赖项到target中

#### Swift
```python
swift_library(
  deps = [
      "//tensorflow/lite/experimental/swift:TensorFlowLite",
  ],
)
```

#### Objective-C
```python
objc_library(
  deps = [
      "//tensorflow/lite/experimental/objc:TensorFlowLite",
  ],
)
```

### 导入库

对于Swift文件，输入TF Lite模块：

```swift
import TensorFlowLite
```

对于Objective-C文件，输入umbrella header：

```objectivec
#import "TFLTensorFlowLite.h"
```

或者，如果你在Xcode项目中设置了`CLANG_ENABLE_MODULES = YES` 则输入以下模块：

```objectivec
@import TFLTensorFlowLite;
```

笔记：对于 CocoaPods开发者如果你想导入Objective-C TensorFlow Lite模块
必须保证`Podfile`中包括了 `use_frameworks!`头文件
