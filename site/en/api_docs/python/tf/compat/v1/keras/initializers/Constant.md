description: Initializer that generates tensors with constant values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.initializers.Constant" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.compat.v1.keras.initializers.Constant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/init_ops.py#L142-L237">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Initializer that generates tensors with constant values.

Inherits From: [`Initializer`](../../../../../tf/compat/v1/keras/initializers/Initializer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.constant_initializer`, `tf.compat.v1.initializers.constant`, `tf.compat.v1.keras.initializers.constant`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.initializers.Constant(
    value=0, dtype=tf.dtypes.float32, verify_shape=(False)
)
</code></pre>



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

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A Python scalar, list or tuple of values, or a N-dimensional numpy
array. All elements of the initialized variable will be set to the
corresponding value in the `value` argument.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Default data type, used if no `dtype` argument is provided when
calling the initializer.
</td>
</tr><tr>
<td>
`verify_shape`
</td>
<td>
Boolean that enables verification of the shape of `value`. If
`True`, the initializer will throw an error if the shape of `value` is not
compatible with the shape of the initialized tensor.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the input `value` is not one of the expected types.
</td>
</tr>
</table>



#### Examples:

The following example can be rewritten using a numpy.ndarray instead
of the `value` list, even reshaped, as shown in the two commented lines
below the `value` list initialization.


```
>>> value = [0, 1, 2, 3, 4, 5, 6, 7]
>>> init = tf.compat.v1.constant_initializer(value)
>>> # fitting shape
>>> with tf.compat.v1.Session():
...   x = tf.compat.v1.get_variable('x', shape=[2, 4], initializer=init)
...   x.initializer.run()
...   print(x.eval())
[[0. 1. 2. 3.]
 [4. 5. 6. 7.]]
>>> # Larger shape
>>> with tf.compat.v1.Session():
...   y = tf.compat.v1.get_variable('y', shape=[3, 4], initializer=init)
...   y.initializer.run()
...   print(y.eval())
[[0.  1.  2.  3.]
 [4.  5.  6.  7.]
 [7.  7.  7.  7.]]
>>> # Smaller shape
>>> with tf.compat.v1.Session():
...   z = tf.compat.v1.get_variable('z', shape=[2, 3], initializer=init)
Traceback (most recent call last):
...
ValueError: Too many elements provided. Needed at most 6, but received 8
>>> # Shape verification
>>> init_verify = tf.compat.v1.constant_initializer(value, verify_shape=True)
>>> with tf.compat.v1.Session():
...  u = tf.compat.v1.get_variable('u', shape=[3, 4],
...                                initializer=init_verify)
Traceback (most recent call last):
...
TypeError: Expected Tensor's shape: (3, 4), got (8,).
```

## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/init_ops.py#L78-L97">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>

Instantiates an initializer from a configuration dictionary.


#### Example:



```python
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config`
</td>
<td>
A Python dictionary. It will typically be the output of
`get_config`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An Initializer instance.
</td>
</tr>

</table>



<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/init_ops.py#L232-L237">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>

Returns the configuration of the initializer as a JSON-serializable dict.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A JSON-serializable Python dict.
</td>
</tr>

</table>



<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/init_ops.py#L224-L230">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    shape, dtype=None, partition_info=None, verify_shape=None
)
</code></pre>

Returns a tensor object initialized as specified by the initializer.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`shape`
</td>
<td>
Shape of the tensor.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Optional dtype of the tensor. If not provided use the initializer
dtype.
</td>
</tr><tr>
<td>
`partition_info`
</td>
<td>
Optional information about the possible partitioning of a
tensor.
</td>
</tr>
</table>





