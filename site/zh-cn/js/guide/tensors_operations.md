# 张量(Tensors) 和 操作(operations)

TensorFlow.js是一个在JavaScript中使用张量来定义并运行计算的框架。张量是向量和矩阵向更高维度的推广。

## 张量(Tensors)

`tf.Tensor`是TensorFlow.js中的最重要的数据单元，它是一个形状为一维或多维数组组成的数值的集合。`tf.Tensor`和多维数组其实非常的相似。

一个`tf.Tensor`还包含如下属性:

*   `rank`: 张量的维度
*   `shape`: 每个维度的数据大小
*   `dtype`: 张量中的数据类型

>注释：在后文中，我们将用术语“维度（dimension）”表示`rank（秩）`。在机器学习中，张量的“维数（dimensionality）”有时也指特定维度的大小。（例如，一个形状为[10, 5]的矩阵是一个rank-2 的张量，或者可以说成一个2-维的张量。第一个维度的维数是10。所以在这里用注释的方式，描述一下这个术语的双重用法，避免之后的理解错误。）

我们可以用`tf.tensor()`方法将一个数组(array)创建为一个`tf.Tensor`：

```js
// 从一个多维数组创建一个rank-2的张量矩阵
const a = tf.tensor([[1, 2], [3, 4]]);
console.log('shape:', a.shape);
a.print();
// 或者您可以用一个一维数组并指定特定的形状来创建一个张量
const shape = [2, 2];
const b = tf.tensor([1, 2, 3, 4], shape);
console.log('shape:', b.shape);
b.print();
```

在默认的情况下，`tf.Tensor`的数据类型也就是
`dtype`为32位浮点型(`float32`)。当然`tf.Tensor`也可以被创建为以下数据类型：布尔(`bool`), 32位整型(`int32`),
64位复数(`complex64`), 和字符串(`string`)：

```js
const a = tf.tensor([[1, 2], [3, 4]], [2, 2], 'int32');
console.log('shape:', a.shape);
console.log('dtype', a.dtype);
a.print();
```

TensorFlow.js同样也提供了一系列方便的模式用作创建随机张量，比如将张量填入特定的数值或是从`HTMLImageElement`中获取张量。当然您还可以在文档中找到更多的[方法](https://js.tensorflow.org/api/latest/#Tensors-Creation)。

#### 修改张量的形状

`tf.Tensor`中的元素数量是这个张量的形状的乘积(例如一个形状为[2,3]的张量所含有的元素个数为2*3=6个)。所以说在大部分时候不同形状的张量的大小却是相同的,那么将一个`tf.Tensor`改变形状(reshape)成为另外一个形状通常是有用且有效的。上述操作可以用`reshape()`
方法实现:

```js
const a = tf.tensor([[1, 2], [3, 4]]);
console.log('a shape:', a.shape);
a.print();

const b = a.reshape([4, 1]);
console.log('b shape:', b.shape);
b.print();
```

#### 获取张量的值

如果您想要获取一个`tf.Tensor`的值，可以使用`Tensor.array()` or `Tensor.data()`这两个方法:

```js
 const a = tf.tensor([[1, 2], [3, 4]]);
 //返回多维数组的值
 a.array().then(array => console.log(array));
 // 返回张量所包含的所有值的一维数组
 a.data().then(data => console.log(data));
```

我们同时也提供了这些方法能够更简单运用的同步执行版本，但是这些方法可能会导致您的应用程序遇到一些性能瓶颈。在生产环境的应用程序中，您应该始终优先使用异步方法。

```js
const a = tf.tensor([[1, 2], [3, 4]]);
 //返回多维数组的值
console.log(a.arraySync());
// 返回张量所包含的所有值的一维数组
console.log(a.dataSync());
```

## 操作

您可以使用张量存储数据，而操作(operation)可以让您操作这些数据。TensorFlow.js还提供了多种能在张量上执行，适用于线性代数和机器学习的操作。

例1: 给`tf.Tensor`中所有的元素执行x<sup>2</sup>函数:

```js
const x = tf.tensor([1, 2, 3, 4]);
const y = x.square();  // 相当于 tf.square(x)
y.print();
```

例2: 将两个 `tf.Tensor`中的元素对应相加:

```js
const a = tf.tensor([1, 2, 3, 4]);
const b = tf.tensor([10, 20, 30, 40]);
const y = a.add(b);  // 相当于 tf.add(a, b)
y.print();
```

因为张量是不可变的，所以这些运算并不会更改他们的值。相应的这些操作总会返回一个新的`tf.Tensor`。

> 注释: 大部分的操作会同步返回 `tf.Tensor`,
> 然而结果可能不会立刻被计算出来。这意味着您得到的`tf.Tensor`实际上是计算的一个句柄。当您调用`Tensor.data()`或是`Tensor.array()`时，这些方法将会等待计算完成之后才将数值解析出来。这意味着您应该始终优先选择这些方法的异步版本而不是同步版本，以避免在计算的过程中阻塞UI线程。

您可以在这里找到更多关于Tensorflow.js中[操作](https://js.tensorflow.org/api/latest/#Operations)的技术支持。

## 内存

当使用WebGL后端时, `tf.Tensor`的内存必须以显式管理。这是因为WebGL不足以让`tf.Tensor`超出生命周期后内存被自动释放。

您可以使用`dispose() `方法或是`tf.dispose()`方法用以释放`tf.Tensor`所占用的内存:

```js
const a = tf.tensor([[1, 2], [3, 4]]);
a.dispose(); // 相当于 tf.dispose(a)
```

在一个应用程序中，将多个操作链接在一起是非常常见的。保存对所有中间变量的引用以释放它们所占用的空间会降低代码的可读性。为了解决这个问题，TensorFlow.js提供了`tf.tidy()`方法。这个方法可以清除所有在执行函数后没有返回的`tf.Tensor`,这和执行函数时清除一些局部变量的方法有些类似:

```js
const a = tf.tensor([[1, 2], [3, 4]]);
const y = tf.tidy(() => {
  const result = a.square().log().neg();
  return result;
});
```

在这个例子中，`square()`和`log()`这两个函数因为没有返回任何值，所以它们的结果会自动的被释放。而`neg()`是`tf.tidy()`的返回值，所以它的结果不会被释放。

当然您还可以获取TensorFlow.js程序中张量的数量。

```js
console.log(tf.memory());
```

`tf.memory()`将会打印出有关当前分配了多少内存的信息。在[这里](https://js.tensorflow.org/api/latest/#memory)您可以获得更多的资料。
