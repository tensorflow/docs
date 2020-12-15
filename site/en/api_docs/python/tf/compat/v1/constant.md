description: Creates a constant tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.constant" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.constant

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/constant_op.py#L101-L163">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a constant tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.constant(
    value, dtype=None, shape=None, name='Const', verify_shape=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

The resulting tensor is populated with values of type `dtype`, as
specified by arguments `value` and (optionally) `shape` (see examples
below).

The argument `value` can be a constant value, or a list of values of type
`dtype`. If `value` is a list, then the length of the list must be less
than or equal to the number of elements implied by the `shape` argument (if
specified). In the case where the list length is less than the number of
elements specified by `shape`, the last element in the list will be used
to fill the remaining entries.

The argument `shape` is optional. If present, it specifies the dimensions of
the resulting tensor. If not present, the shape of `value` is used.

If the argument `dtype` is not specified, then the type is inferred from
the type of `value`.

#### For example:



```python
# Constant 1-D Tensor populated with value list.
tensor = tf.constant([1, 2, 3, 4, 5, 6, 7]) => [1 2 3 4 5 6 7]

# Constant 2-D tensor populated with scalar value -1.
tensor = tf.constant(-1.0, shape=[2, 3]) => [[-1. -1. -1.]
                                             [-1. -1. -1.]]
```

<a href="../../../tf/constant.md"><code>tf.constant</code></a> differs from <a href="../../../tf/fill.md"><code>tf.fill</code></a> in a few ways:

*   <a href="../../../tf/constant.md"><code>tf.constant</code></a> supports arbitrary constants, not just uniform scalar
    Tensors like <a href="../../../tf/fill.md"><code>tf.fill</code></a>.
*   <a href="../../../tf/constant.md"><code>tf.constant</code></a> creates a `Const` node in the computation graph with the
    exact value at graph construction time. On the other hand, <a href="../../../tf/fill.md"><code>tf.fill</code></a>
    creates an Op in the graph that is expanded at runtime.
*   Because <a href="../../../tf/constant.md"><code>tf.constant</code></a> only embeds constant values in the graph, it does
    not support dynamic shapes based on other runtime Tensors, whereas
    <a href="../../../tf/fill.md"><code>tf.fill</code></a> does.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A constant value (or list) of output type `dtype`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the elements of the resulting tensor.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Optional dimensions of resulting tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Optional name for the tensor.
</td>
</tr><tr>
<td>
`verify_shape`
</td>
<td>
Boolean that enables verification of a shape of values.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Constant Tensor.
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
if shape is incorrectly specified or unsupported.
</td>
</tr>
</table>

