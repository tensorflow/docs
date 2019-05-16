# 变量

TensorFlow **变量**是表示程序处理共享持久状态的最佳方式。

变量通过`tf.Variable`类进行操作。`tf.Variable`表示张量，其值可以通过在其上运行ops来改变。
特定的ops允许您读取和修改此张量的值。像`tf.keras`这样的高级库使用`tf.Variable`来存储模型参数。
本指南介绍了如何在TensorFlow中创建，更新和管理`tf.Variable`s。

## 创建变量

要创建变量，只需提供初始值即可。

``` python
my_variable = tf.Variable(tf.zeros([1., 2., 3.]))
```

这创建了一个变量，它是一个三维张量，形状为`[1,2,3]`，用零填充。
默认情况下，此变量将具有`dtype` `tf.float32`。如果未指定，则从初始值推断出dtype。

如果有一个`tf.device`范围处于活动状态，那么该变量将放在该范围内设备;
否则变量将放在与其dtype兼容的“最快”设备上（这意味着如果有可用的话，大多数变量会自动放在GPU上）。
例如，以下代码段创建一个名为的变量`v`并将其放在第二个GPU设备上：

``` python
with tf.device("/device:GPU:1"):
  v = tf.Variable(tf.zeros([10, 10]))
```

理想情况下，您应该使用`tf.distribute` API，因为这允许您编写一次代码并使其在许多不同的分布式设置下工作。

## 使用变量

要在TensorFlow图中使用`tf.Variable`的值，简单地将它视为正常的`tf.Tensor`：

``` python
v = tf.Variable(0.0)
w = v + 1  # w是tf.Tensor，它是根据v的值计算的。
           # 只要在表达式中使用变量，它就会自动转换为表示其值的tf.Tensor。
```

要为变量赋值，请使用方法`assign`，`assign_add`，以及`tf.Variable`。
例如，以下是调用这些方法的方法：

``` python
v = tf.Variable(0.0)
v.assign_add(1)
```

大多数TensorFlow优化器都有专门的操作系统，可以根据类似梯度下降的算法有效地更新变量值。
有关如何使用优化器的说明，请参见`tf.keras.optimizers.Optimizer`。

您还可以使用显式读取变量的当前值
`read_value`：

```python
v = tf.Variable(0.0)
v.assign_add(1)
v.read_value()  # 1.0
```

当对`tf.Variable`的最后一次引用超出范围时，它的内存被释放。

### 跟踪变量

TensorFlow中的变量是一个Python对象。在构建图层，模型，优化器和其他相关工具时，
您可能希望获得（假设）模型中所有变量的列表。

虽然您可以在自己的Python代码中特别跟踪变量，但我们建议您使用`tf.Module`作为拥有变量的类的基类。
 `tf.Module`的实例有一个`variables`和一个`trainable_variables`方法，
 返回从该模型可到达的所有（可训练）变量，可以潜在地通过其他模型。

```python
class MyModuleOne(tf.Module):
  def __init__(self):
    self.v0 = tf.Variable(1.0)
    self.vs = [tf.Variable(x) for x in range(10)]
    
class MyOtherModule(tf.Module):
  def __init__(self):
    self.m = MyModuleOne()
    self.v = tf.Variable(10.0)
    
m = MyOtherModule()
len(m.variables)  # 12; 11 从m.m和另一个m.v.

```

请注意，您正在实现一个图层，`tf.keras.Layer`可能是一个更好的基类，
实现其界面将让您的图层完全集成Keras，允许您使用`model.fit`和其他良好集成的API。
`tf.keras.Layer`的变量跟踪与`tf.Module`的变量跟踪相同。



