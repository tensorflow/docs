page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.keras.initializers.Constant


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops.py#L142-L251">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Constant`

Initializer that generates tensors with constant values.

Inherits From: [`Initializer`](../../../../../tf/compat/v1/keras/initializers/Initializer)

### Aliases:

* Class `tf.compat.v1.constant_initializer`
* Class `tf.compat.v1.initializers.constant`
* Class `tf.compat.v1.keras.initializers.constant`


<!-- Placeholder for "Used in" -->

The resulting tensor is populated with values of type `dtype`, as
specified by arguments `value` following the desired `shape` of the
new tensor (see examples below).

The argument `value` can be a constant value, or a list of values of type
`dtype`. If `value` is a list, then the length of the list must be less
than or equal to the number of elements implied by the desired shape of the
tensor. In the case where the total number of elements in `value` is less
than the number of elements required by the tensor shape, the last element
in `value` will be used to fill the remaining entries. If the total number of
elements in `value` is greater than the number of elements required by the
tensor shape, the initializer will raise a `ValueError`.

#### Args:


* <b>`value`</b>: A Python scalar, list or tuple of values, or a N-dimensional numpy
  array. All elements of the initialized variable will be set to the
  corresponding value in the `value` argument.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
  calling the initializer.
* <b>`verify_shape`</b>: Boolean that enables verification of the shape of `value`. If
  `True`, the initializer will throw an error if the shape of `value` is not
  compatible with the shape of the initialized tensor.


#### Raises:


* <b>`TypeError`</b>: If the input `value` is not one of the expected types.


#### Examples:

The following example can be rewritten using a numpy.ndarray instead
of the `value` list, even reshaped, as shown in the two commented lines
below the `value` list initialization.

  <pre class="devsite-click-to-copy prettyprint lang-py">
  <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}import numpy as np{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> import tensorflow as tf{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  ```{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> value = [0, 1, 2, 3, 4, 5, 6, 7]{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> # value = np.array(value){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> # value = value.reshape([2, 4]){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> init = tf.compat.v1.constant_initializer(value){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> print('fitting shape:'){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> with tf.compat.v1.Session():{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   x = tf.compat.v1.get_variable('x', shape=[2, 4], initializer=init){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   x.initializer.run(){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   print(x.eval()){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     fitting shape:{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     [[ 0.  1.  2.  3.]{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>      [ 4.  5.  6.  7.]]{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> print('larger shape:'){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> with tf.compat.v1.Session():{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   x = tf.compat.v1.get_variable('x', shape=[3, 4], initializer=init){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   x.initializer.run(){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   print(x.eval()){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     larger shape:{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     [[ 0.  1.  2.  3.]{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>      [ 4.  5.  6.  7.]{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>      [ 7.  7.  7.  7.]]{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> print('smaller shape:'){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> with tf.compat.v1.Session():{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   x = tf.compat.v1.get_variable('x', shape=[2, 3], initializer=init){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     ValueError: Too many elements provided. Needed at most 6, but received 8{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> print('shape verification:'){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> init_verify = tf.compat.v1.constant_initializer(value,{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  verify_shape=True){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>> with tf.compat.v1.Session():{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  >>>   x = tf.compat.v1.get_variable('x', shape=[3, 4],{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}  initializer=init_verify){% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>     {% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}>       TypeError: Expected Tensor's shape: (3, 4), got (8,).{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}<h2 id="__init__"><code>__init__</code></h2>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops.py#L223-L236">View source</a>{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}``` python{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}__init__({% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}    value=0,{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}    dtype=tf.dtypes.float32,{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}    verify_shape=False{% endhtmlescape %}</code>
  <code class="no-select nocode">{% htmlescape %}){% endhtmlescape %}</code>
  </pre>

DEPRECATED FUNCTION ARGUMENTS (deprecated arguments)

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dtype)`. They will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor

Warning: SOME ARGUMENTS ARE DEPRECATED: `(verify_shape)`. They will be removed in a future version.
Instructions for updating:
Objects must now be the required shape or no shape can be specified



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops.py#L238-L244">View source</a>

``` python
__call__(
    shape,
    dtype=None,
    partition_info=None,
    verify_shape=None
)
```

Returns a tensor object initialized as specified by the initializer.


#### Args:


* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. If not provided use the initializer
  dtype.
* <b>`partition_info`</b>: Optional information about the possible partitioning of a
  tensor.

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops.py#L78-L97">View source</a>

``` python
from_config(
    cls,
    config
)
```

Instantiates an initializer from a configuration dictionary.


#### Example:



```python
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

#### Args:


* <b>`config`</b>: A Python dictionary. It will typically be the output of
  `get_config`.


#### Returns:

An Initializer instance.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/init_ops.py#L246-L251">View source</a>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.


#### Returns:

A JSON-serializable Python dict.
