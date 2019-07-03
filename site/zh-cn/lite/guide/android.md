# Android 快速上手

在您开始在Android上使用TensorFlow Lite之前，我们推荐您探索下面的例子。

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android">Android
图像分类例子</a>

有关源代码的说明，您也应该阅读
[TensorFlow Lite Android 图像分类](https://www.tensorflow.org/lite/models/image_classification/android).

这个例子使用了
[图像分类](https://www.tensorflow.org/lite/models/image_classification/overview)
来将设备的后置摄像头拍到的东西进行持续分类。
该应用程序可以在设备或者模拟器上都可以运行。

推断(Inference)通过TensorFlow Lite的Java API来实现。演示应用程序可以对实时帧进行分类，并显示最有可能的类别。应用程序可以允许用户选择浮点或
[量化](https://www.tensorflow.org/lite/performance/post_training_quantization)
模型，选择线程数，或者决定在CPU，GPU上运行，亦或是通过
[NNAPI](https://developer.android.com/ndk/guides/neuralnetworks)运行。

注意: 你可以在[例子](https://www.tensorflow.org/lite/examples)中查看其他的使用TensorFlow Lite的各种用例。

## 在Android Studio中构建

如果您要在Android Studio 构建例子，请遵循该说明
[README.md](https://github.com/tensorflow/examples/blob/master/lite/examples/image_classification/android/README.md).

## 创建您自己的Android应用程序

如果您要快速编写您的Android代码, 我们推荐使用
[Android 图像分类代码例子](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android)
作为起始点。

下面的部分包含了一些有关如何在Android上使用TensorFlow Lite的有用的信息。

### 使用JCenter中的TensorFlow Lite AAR

如果您要在您的Android应用程序中使用TensorFlow Lite，我们推荐使用
[在JCenter中托管TensorFlow Lite AAR](https://bintray.com/google/tensorflow/tensorflow-lite)。

您可以像下面这样写您的`build.gradle` 依赖:

```build
dependencies {
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly'
}
```

这个AAR包含了
[Android ABIs](https://developer.android.com/ndk/guides/abis)中的所有的二进制文件。您可以通过只包含您需要的ABIs支持来减少您应用程序的二进制文件大小。

我们推荐大部分的开发者忽略 `x86`，`x86_64`，和`arm32` 的ABIs。您可以通过如下的Gradle配置实现，这个配置只包括了  `armeabi-v7a`和`arm64-v8a`，使用该配置会涵盖了大部分的主流Android设备。

```build
android {
    defaultConfig {
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
        }
    }
}
```

如果需要了解更多有关的 `abiFilters`的信息, 请查看Android Gradle文档中的
[`NdkOptions`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkOptions.html)。

### 在本地构建TensorFlow Lite

在某些情况下，您可能希望使用一个本地构建的TensorFlow Lite. 比如说，您可能正在构建一个自定义的二进制文件其中包含了
[从TensorFlow中选择的操作](https://www.tensorflow.org/lite/guide/ops_select).

在这个例子中，请参照
[自定义 AAR 构建说明](https://www.tensorflow.org/lite/guide/ops_select#android_aar)
来创建你自己的AAR并将其包含在您的APP中.
