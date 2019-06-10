# 平台和环境

TensorFlow.js有两种工作平台：浏览器和Node.js。不同平台有很多不同的配置，平台间的差异影响着基于平台的应用开发。

在浏览器平台上，TensorFlow.js既支持移动设备，也支持台式设备。虽然设备之间有很多差异，TensorFlow.js提供的WebGL API能够自动检测并做相应的优化配置。

在Node.js平台上，TensorFlow.js既支持直接使用TensorFlow API，也支持更慢的CPU环境。

## [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#environments)环境

当一个用TensorFlow.js开发的程序运行时，所有的配置被统称为环境。它包含一个全局的backend，以及一些可以精确控制TensorFlow.js特性的标记。

### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#backends)Backends

TensorFlow.js支持多个不同的backend，用来实现张量的存储和数学操作。任何时候都只有一个backend生效。大部分时间，TensorFlow.js会根据当前环境自动选择使用最佳的backend。即使这样，你仍然需要知道，如何得知当前正在使用的是哪个backend，以及如何在不同backend之间切换。

下面命令用来获取当前正使用的backend
```js
console.log(tf.getBackend());
```

下面命令用来手动切换backend
```js
tf.setBackend(‘cpu’);
console.log(tf.getBackend());
```

#### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#webgl-backend)WebGL backend

WebGL backend，简称“webgl”，是在浏览器平台上最强大的一个backend。它比CPU backend要快100倍。部分原因是，Tensor是作为WebGL纹理保存的，数学运算操作实现在WebGL shader里面。

下面是在使用这个backend时需要了解的一些知识。

##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#avoid-blocking-the-ui-thread)避免阻塞UI线程
当调用一个操作，如tf.matMul(a,b)时，返回值tf.Tensor会同步返回，然而这时矩阵乘法运算还不一定完成。这意味着返回值tf.Tensor只是一个指向运算的句柄。当调用`x.data()`或`x.array()`时，只有当运算完成时才能取到实际值。因此在运算过程中，为避免阻塞UI线程，需要使用异步版本的`x.data()`和`x.array()`，而不是同步版本的`x.dataSync()`和`x.arraySync()`。
##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#memory-management)内存管理

强调一下，在使用WebGL backend时，需要显式管理内存。因为存储Tensor的WebGL纹理，不会被浏览器的垃圾收集机制自动清理。

调用dispose()清理tf.Tensor占用的内存

```js
const a = tf.tensor([[1,2], [3,4]]);
a.dispose();
```

在应用中，经常需要把多个操作组合起来。维持一个对所有中间变量的引用，然后清理其占用的内存，这种方法使代码可读性变差。TensorFlow.js提供tf.tidy()方法清理函数返回时不再需要的tf.Tensor，这就好像函数执行后，本地变量都会被清理一样。

```js
const a = tf.tensor([[1, 2], [3, 4]]);
const y = tf.tidy(() => {
  const result = a.square().log().neg();
  return result;
});
```

>注意：其他非WebGL环境（如Node.js TensorFlow backend或CPU backend）有自动垃圾回收机制，在这些环境下使用dispose()或tidy()没有副作用。实际上，主动调用通常会比垃圾回收的清理带来更好的性能。

##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#precision)精度

在移动设备，WebGL只支持16位浮点纹理操作。然而，大部分机器学习模型都用32位浮点的weight和activation训练的。由于16位浮点数字只能表示[0.000000059605， 65504]这个范围，当把模型移植到移动设备时，它会产生精度问题。你需要保证自己模型中的weight和activation不要超出这个范围。
##### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#shader-compilation--texture-uploads)编译Shader& texture 上传
TensorFlow.js在GPU里执行WebGL的shader程序。然而这些shader只有在被调用时才会被编译，即lazy-compile。编译过程在CPU上的主线程完成，这导致程序变慢。TensorFlow.js会自动缓存编译好的shader，下次再调用有同样shape，同样输入输出的tensor时能快很多。TensorFlow.js开发的应用一般会多次使用同样的操作，因此第二次运行会快很多。

TensorFlow.js还会把tf.Tensor数据存储为WebGL纹理。当一个tf.Tensor被创建后，不会被立即上传到GPU，而是当其被用到时才这么做。如果这个tf.Tensor被第二次使用，由于已经在GPU里，因此省掉了上传开销。在一个典型的机器学习模型中，这意味着weight在第一次预测时被上传，第二次就会快很多。

如果希望加快第一次预测的性能，我们推荐对模型进行预热，即传递一个有同样shape的输入Tensor。
例如:
```js
const model = await tf.loadLayersModel(modelUrl);
// 使用真实数据来预热模型
const warmupResult = model.predict(tf.zeros(inputShape));
warmupResult.dataSync();
warmupResult.dispose();

// 第二次执行 predict() 的时候将会更加快速
const result = model.predict(userData);
```

#### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#nodejs-tensorflow-backend)Node.js TensorFlow backend

在Node.js TensorFlow backend中，所谓“node”,即TensorFlow的C语言API被用来加速操作。它会尽可能使用机器的硬件加速模块，如CUDA。

在这个backend中，和WebGL backend一样，函数会同步返回`tf.Tensor`。然而，与WebGL backend不同的是，当你获得这个tensor返回值时，运算已经完成。这意味着`tf.matMul(a,b)`调用会阻塞UI线程。

因此，如果你在生产环境下使用这个方法，你需要在工作线程中调用，而不是主线程。

更多关于Node.js的信息，请查看相关文档。
#### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#cpu-backend)CPU backend

这个backend是性能最差的backend，然而是最简单的。所有操作都实现在vanilla JavaScript中，因此很少有并行化，并且会阻塞UI线程。

这个backend对测试有用，或者是用于WebGL不能使用的设备。

### [](https://github.com/tensorflow/tfjs-website/blob/master/docs/guide/platform_environment.md#flags)Flags

TensorFlow.js有一套环境标记，能够自动评估和检测，保证是当前平台上的最佳配置。这些标记大部分是内部使用，其中有一些全局标记可以被API控制。

-   `tf.enableProdMode():`  启用生产模式。它会去掉模型验证，NaN检查，以及其他错误校验操作，从而提高性能。
-   `tf.enableDebugMode()`: 启用调试模式。它会记录每种操作的日志并输出到到调试台，还记录运行性能信息，如内存footprint和内核执行时间。注意这将极大降低应用运行时间，不可在生产环境中使用。

注：这两种方法应该在程序的最前面调用，因为它们影响所有的其他标记。基于同样的原因，没有相应的disable方法。

注：所有标记在控制台都记录为tf.ENV.features。尽管没有对应的公开API（不需要考虑版本兼容），你可以使用tf.ENV.set来改变这些标记，从而对程序做微调或诊断。
