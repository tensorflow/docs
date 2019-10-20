# TensorFlow variables

A TensorFlow **variable** is the best way to represent shared, persistent state
manipulated by your program.

Variables are manipulated via the `tf.Variable` class. A `tf.Variable`
represents a tensor whose value can be changed by running ops on it.  Specific
ops allow you to read and modify the values of this tensor. Higher level
libraries like `tf.keras` use `tf.Variable` to store model parameters. This
guide covers how to create, update, and manage `tf.Variable`s in TensorFlow.

## Create a variable

To create a variable, simply provide the initial value

``` python
my_variable = tf.Variable(tf.zeros([1., 2., 3.]))
```

This creates a variable which is a three-dimensional tensor with shape `[1, 2,
3]` filled with zeros. This variable will, by default, have the `dtype`
`tf.float32`. The dtype is, if not specified, inferred from the initial
value.

If there's a `tf.device` scope active, the variable will be placed on that
device; otherwise the variable will be placed on the "fastest" device compatible
with its dtype (this means most variables are automatically placed on a GPU if
one is available). For example, the following snippet creates a variable named
`v` and places it on the second GPU device:

``` python
with tf.device("/device:GPU:1"):
  v = tf.Variable(tf.zeros([10, 10]))
```

Ideally though you should use the `tf.distribute` API, as that allows you to
write your code once and have it work under many different distributed setups.

## Use a variable

To use the value of a `tf.Variable` in a TensorFlow graph, simply treat it like
a normal `tf.Tensor`:

``` python
v = tf.Variable(0.0)
w = v + 1  # w is a tf.Tensor which is computed based on the value of v.
           # Any time a variable is used in an expression it gets automatically
           # converted to a tf.Tensor representing its value.
```

To assign a value to a variable, use the methods `assign`, `assign_add`, and
friends in the `tf.Variable` class. For example, here is how you can call these
methods:

``` python
v = tf.Variable(0.0)
v.assign_add(1)
```

Most TensorFlow optimizers have specialized ops that efficiently update the
values of variables according to some gradient descent-like algorithm. See
`tf.keras.optimizers.Optimizer` for an explanation of how to use optimizers.

You can also explicitly read the current value of a variable, using
`read_value`:

```python
v = tf.Variable(0.0)
v.assign_add(1)
v.read_value()  # 1.0
```

When the last reference to a `tf.Variable` goes out of scope its memory is
freed.

### Keep track of variables

A Variable in TensorFlow is a Python object. As you build your layers, models,
optimizers, and other related tools, you will likely want to get a list of all
variables in a (say) model.

A common use case is [implementing `Layer` subclasses](
https://www.tensorflow.org/guide/keras/custom_layers_and_models#the_layer_class).
The `Layer` class recursively tracks variables set as instance attributes:

```python
class MyLayer(tf.keras.layers.Layer):

  def __init__(self):
    super(MyLayer, self).__init__()
    self.my_var = tf.Variable(1.0)
    self.my_var_list = [tf.Variable(x) for x in range(10)]

class MyOtherLayer(tf.keras.layers.Layer):

  def __init__(self):
    super(MyOtherLayer, self).__init__()
    self.sublayer = MyLayer()
    self.my_other_var = tf.Variable(10.0)

m = MyOtherLayer()
print(len(m.variables))  # 12 (11 from MyLayer, plus my_other_var)
```

If you aren't developing a new `Layer`, TensorFlow also features a more
generic `tf.Module` base class which _only_ implements variable tracking.
Instances of `tf.Module` have a `variables` and a `trainable_variables`
property which return all (trainable) variables reachable from that model,
potentially navigating through other modules (much like the tracking done by
the `Layer` class).
