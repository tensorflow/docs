# 保存并加载 tf.Model

TensorFlow.js提供了保存和加载模型的功能，这些模型可以是使用[`Layers`](https://js.tensorflow.org/api/0.14.2/#Models)API创建的或从现有TensorFlow模型转换来的。可能是您自己训练过的模型，也可能是别人训练的模型。使用Layers API的一个主要好处是使用它创建的模型是可序列化的，这就是我们将在本教程中探讨的内容。

本教程将会介绍如何在 TensorFlow.js 中保存和加载模型(可通过JSON文件识别)。我们同样可以导入Tensorflow Python模型。

以下两个教程介绍了加载这些模型：

- [导入Keras模型](../tutorials/conversion/import_keras.md)
- [导入Graphdef模型](../tutorials/conversion/import_saved_model.md)


## 保存 tf.Model

[`tf.Model`](https://js.tensorflow.org/api/0.14.2/#class:Model) 和 [`tf.Sequential`](https://js.tensorflow.org/api/0.14.2/#class:Model)
同时提供了函数 [`model.save`](https://js.tensorflow.org/api/0.14.2/#tf.Model.save) 允许您保存一个模型的
_拓扑结构(topology)_ 和 _权重(weights)_ 。

-  拓扑结构(Topology): 这是一个描述模型结构的文件（例如它使用的了哪些操作）。它包含对存储在外部的模型权重的引用。

-  权重(Weights): 这些是以有效格式存储给定模型权重的二进制文件。它们通常存储在与拓扑结构相同的文件夹中。

让我们看看保存模型的代码是什么样子的

```js
const saveResult = await model.save('localstorage://my-model-1');
```

一些需要注意的地方:

- `save`  方法采用以 scheme 字符串开头的类 URL 字符串参数（下文简称 scheme）。它描述了我们想保存模型的地址的类型。 在本例中我们使用 localstorage:// scheme 将模型保存到本地存储。
- 在 scheme 之后是 **路径(path)**。 在上面的例子中，路径是'my-model-1'。
- `save` 方法是异步的。
- `model.save` 的返回值是一个 JSON 对象，它包含一些可能有用的信息，例如模型的拓扑结构和权重的大小。
- 用于保存模型的环境不会影响那些可以加载模型的环境。在 node.js 中保存模型时并不会阻碍模型在浏览器中被加载。


下面我们将介绍以下不同方案。

### 本地存储 (仅限浏览器)

**Scheme:** `localstorage://`

```js
await model.save('localstorage://my-model');
```
这样可以在浏览器的[本地存储](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)中以名称 `my-model` 来保存模型。这样存储能够在浏览器刷新后保持不变，而当存储空间成为问题时，用户或浏览器本身可以清除本地存储。 每个浏览器还可以对给定域在本地的存储空间设定限额。

### IndexedDB (仅限浏览器)

**Scheme:** `indexeddb://`

```js
await model.save('indexeddb://my-model');
```

这样会将模型保存到浏览器的[IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)存储中。
与本地存储一样，它在刷新后仍然存在，同时它往往也对存储的对象的大小有较大的限制。

### 文件下载 (仅限浏览器)

**Scheme:** `downloads://`

```js
await model.save('downloads://my-model');
```
这会让浏览器下载模型文件至用户的机器上，并生成两个文件：
 1. 一个名为 `[my-model].json` 的 JSON 文件，它包含了模型的拓扑结构和下面将要介绍的权重文件的引用。
 2. 一个二进制文件，其中包含名为 `[my-model].weights.bin` 的权重值。

您可以更换 `[my-model]` 的名称以获得一个不同的名称的文件。

由于`.json`使用相对路径指向 `.bin`，所以两个文件需要被安放在同一个文件夹中。

> 注意: 某些浏览器要求用户在同时下载多个文件之前授予权限。



### HTTP(S) Request

**Scheme:** `http://` or `https://`

```js
await model.save('http://model-server.domain/upload')
```

这将创建一个Web请求，以将模型保存到远程服务器。 您应该控制该远程服务器，以便确保它能够处理该请求。
模型将通过[POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) 请求发送到指定的 HTTP 服务器。
POST 请求的 body 遵守称为`multipart/form-data`的格式。它由以下两个文件组成

 1. 一个名为 `model.json` 的 JSON 文件，其中包含拓扑结构和对下面描述的权重文件的引用。
 2. 一个二进制文件，其中包含名为 `[my-model].weights.bin` 的权重值。

请注意，这两个文件的名称需要与上述介绍中的保持完全相同（因为名称内置于函数中，无法更改）。 此[ api 文档](https://js.tensorflow.org/api/latest/#tf.io.browserHTTPRequest)包含一个 Python 代码片段，演示了如何使用 [flask](http://flask.pocoo.org/) web 框架来处理源自 `save` 的请求。

通常，您必须向 HTTP 服务器传递更多参数或请求头（例如，用于身份验证，或者如果要指定应保存模型的文件夹）。您可以通过替换 `tf.io.browserHTTPRequest` 函数中的 URL字符串参数来获得对来自 `save` 函数的请求在这些方面的细粒度控制。这个API在控制 HTTP 请求方面提供了更大的灵活性。

例如：

```js
await model.save(tf.io.browserHTTPRequest(
    'http://model-server.domain/upload',
    {method: 'PUT', headers: {'header_key_1': 'header_value_1'}}));
```


### 本机文件系统 (仅限于Node.js)

**Scheme:** `file://`

```js
await model.save('file:///path/to/my-model');
```

当运行Node.js后我们当然可以直接访问文件系统并且保存模型。这个命令将会保存两个文件在`scheme`之后指定的`path`中。

 1. 一个名为 `model.json` 的 JSON 文件，其中包含拓扑结构和对下面描述的权重文件的引用。
1.  一个二进制文件，其中包含名为`model.weights.bin`. 的权重值。

请注意，这两个文件的名称将始终与上面指定的完全相同（该名称内置于函数中）。


## 加载 tf.Model

给定一个使用上述方法之一保存的模型，我们可以使用 `tf.loadLayersModel` API来加载它。

让我们看一下加载模型的代码是什么样子的

```js
const model = await tf.loadLayersModel('localstorage://my-model-1');
```

一些事情值得注意:
- 类似于`model.save()`,  `loadLayersModel`函数使用以 **scheme**开头的类似URL的字符串参数。它描述了我们试图从中加载模型的目标类型。
- scheme 由**path**指定。在上述例子中路径为`my-model-1`。
- URL字符串可以被替换为一个符合IOHandler接口的对象。
- `tf.loadLayersModel()`函数是异步的。
- `tf.loadLayersModel`返回的值是 `tf.Model`

下面我们将介绍可用的不同方案。


### 本地存储 (仅限浏览器)

**Scheme:** `localstorage://`

```js
const model = await tf.loadLayersModel('localstorage://my-model');
```

这将从浏览器的[本地存储](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).
加载一个名为`my-model`模型。

### IndexedDB (仅限浏览器)

**Scheme:** `indexeddb://`

```js
const model = await tf.loadLayersModel('indexeddb://my-model');
```
这将从浏览器的[IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).
加载一个模型。


### HTTP(S)

**Scheme:** `http://` or `https://`

```js
const model = await tf.loadLayersModel('http://model-server.domain/download/model.json');
```
这将从HTTP端点加载模型。加载`json` 文件后，函数将请求对应的`json` 文件引用的`.bin`文件。

> 注意：这个工具依赖于[`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)方法。如果您的环境没有提供原生的fetch方法，您可以提供全局方法名称[`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)从而满足接口要求或是使用类似于(`node-fetch`)[https://www.npmjs.com/package/node-fetch]的库。


### 本机文件系统 (仅限于Node.js)

**Scheme:** `file://`

```js
const model = await tf.loadLayersModel('file://path/to/my-model/model.json');
```

当运行在Node.js上时，我们可以直接访问文件系统并且从那里加载模型。注意，在上面的函数调用中，我们引用model.json文件本身（而在保存时，我们指定一个文件夹）。相应的`.bin`文件需要和`json` 文件在同一个文件夹中。

## 使用 IOHandlers 加载模型

如果上述方案没有满足您的需求，您可以使用`IOHandler`执行自定义的加载行为。Tensorflow.js的`IOHandler`提供了[`tf.io.browserFiles`](https://js.tensorflow.org/api/latest/#io.browserFiles) ，运行浏览器用户在浏览器中上传文件。您可以在 [文档](https://js.tensorflow.org/api/latest/#io.browserFiles)中查看更多信息。

# 使用自定义的 IOHandlers 保存或加载模型

如果上述方案没有满足您的保存和加载模型的需求，您可以通过执行`IOHandler`以执行自定义的序列化行为。

`IOHandler`是一个含有`save` 和 `load`方法的对象。

`save`函数接受一个与[ModelArtifacts](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L165)接口匹配的参数并且会返回一个解析为[SaveResult](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L107)的对象。

`load`函数没有接受参数而回返回一个解析为[ModelArtifacts](https://github.com/tensorflow/tfjs-core/blob/master/src/io/types.ts#L165)的对象。这和传递给`save`的相同对象。


查看[BrowserHTTPRequest](https://github.com/tensorflow/tfjs-core/blob/master/src/io/browser_http.ts)获取如何执行IOHandler的例子。
