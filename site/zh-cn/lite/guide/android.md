# Android 快速上手

要在Android上使用TensorFlow Lite，我们推荐您探索下面的例子。

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android">Android
图像分类示例</a>

有关源代码的说明，您还应该阅读
[TensorFlow Lite Android 图像分类](https://www.tensorflow.org/lite/models/image_classification/android).

该示例应用程序使用
[图像分类](https://www.tensorflow.org/lite/models/image_classification/overview)
来连续地对设备的后置摄像头所看到的内容进行分类。
该应用程序可以运行在真实设备或者模拟器上。

使用 TensorFlow Lite Java API 来执行推理。该演示应用程序实时地对图像帧进行分类，显示最可能的分类结果。它允许用户选择浮点或
[量化](https://www.tensorflow.org/lite/performance/post_training_quantization)
模型，选择线程数，并决定运行在CPU，GPU上，亦或是通过
[NNAPI](https://developer.android.com/ndk/guides/neuralnetworks)运行。

注意: 这些[示例](https://www.tensorflow.org/lite/examples)提供了其他的在多种用例中演示使用TensorFlow Lite的应用程序。 

## 在Android Studio中构建

如果您要在Android Studio 构建例子，请遵循
[README.md](https://github.com/tensorflow/examples/blob/master/lite/examples/image_classification/android/README.md)中的说明。

## 创建您自己的Android应用程序

如果您想快速编写您的Android代码, 我们推荐使用
[Android 图像分类代码例子](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android)
作为起始点。

下面的部分包含了一些有关如何在Android上使用TensorFlow Lite的有用信息。

### 使用JCenter中的TensorFlow Lite AAR

如果您要在您的Android应用程序中使用TensorFlow Lite，我们推荐使用
[在JCenter中托管的TensorFlow Lite AAR](https://bintray.com/google/tensorflow/tensorflow-lite)。

您可以像下面这样在您的`build.gradle`依赖中指定它:

```build
dependencies {
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly'
}
```

这个AAR包含了
[Android ABIs](https://developer.android.com/ndk/guides/abis)中的所有的二进制文件。您可以通过只包含您需要支持的ABIs来减少您应用程序的二进制文件大小。

我们推荐大部分的开发者删简 `x86`，`x86_64`，和`arm32` 的ABIs。您可以通过如下的Gradle配置实现，这个配置只包括了 `armeabi-v7a`和`arm64-v8a`，该配置能涵盖住大部分的现代Android设备。

```build
android {
    defaultConfig {
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
        }
    }
}
```

想要了解更多有关 `abiFilters`的信息, 请查看Android Gradle文档中的
[`NdkOptions`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkOptions.html)。

### 在本地构建TensorFlow Lite

在某些情况下，您可能希望使用一个本地构建的TensorFlow Lite. 比如说，您可能正在构建一个自定义的包含了
[从TensorFlow中选择的操作](https://www.tensorflow.org/lite/guide/ops_select)的二进制文件。

在这种情况下，请参照
[自定义 AAR 构建说明](https://www.tensorflow.org/lite/guide/ops_select#android_aar)
来创建你自己的AAR并将其包含在您的APP中.
