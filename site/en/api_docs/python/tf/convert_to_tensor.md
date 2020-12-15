description: Converts the given value to a Tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.convert_to_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.convert_to_tensor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/ops.py#L1319-L1382">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts the given `value` to a `Tensor`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.convert_to_tensor(
    value, dtype=None, dtype_hint=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function converts Python objects of various types to `Tensor`
objects. It accepts `Tensor` objects, numpy arrays, Python lists,
and Python scalars. For example:

```
>>> def my_func(arg):
...   arg = tf.convert_to_tensor(arg, dtype=tf.float32)
...   return arg
```

```
>>> # The following calls are equivalent.
>>> value_1 = my_func(tf.constant([[1.0, 2.0], [3.0, 4.0]]))
>>> print(value_1)
tf.Tensor(
  [[1. 2.]
   [3. 4.]], shape=(2, 2), dtype=float32)
>>> value_2 = my_func([[1.0, 2.0], [3.0, 4.0]])
>>> print(value_2)
tf.Tensor(
  [[1. 2.]
   [3. 4.]], shape=(2, 2), dtype=float32)
>>> value_3 = my_func(np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32))
>>> print(value_3)
tf.Tensor(
  [[1. 2.]
   [3. 4.]], shape=(2, 2), dtype=float32)
```

This function can be useful when composing a new operation in Python
(such as `my_func` in the example above). All standard Python op
constructors apply this function to each of their Tensor-valued
inputs, which allows those ops to accept numpy arrays, Python lists,
and scalars in addition to `Tensor` objects.

Note: This function diverges from default Numpy behavior for `float` and
  `string` types when `None` is present in a Python list or scalar. Rather
  than silently converting `None` values, an error will be thrown.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
An object whose type has a registered `Tensor` conversion function.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Optional element type for the returned tensor. If missing, the type
is inferred from the type of `value`.
</td>
</tr><tr>
<td>
`dtype_hint`
</td>
<td>
Optional element type for the returned tensor, used when dtype
is None. In some cases, a caller may not have a dtype in mind when
converting to a tensor, so dtype_hint can be used as a soft preference.
If the conversion to `dtype_hint` is not possible, this argument has no
effect.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name to use if a new `Tensor` is created.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` based on `value`.
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
If no conversion function is registered for `value` to `dtype`.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If a registered conversion function returns an invalid value.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the `value` is a tensor not of given `dtype` in graph mode.
</td>
</tr>
</table>

