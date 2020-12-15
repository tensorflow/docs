description: Logical XOR function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.logical_xor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.logical_xor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/math_ops.py#L1519-L1565">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Logical XOR function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.logical_xor`, `tf.compat.v1.math.logical_xor`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.logical_xor(
    x, y, name='LogicalXor'
)
</code></pre>



<!-- Placeholder for "Used in" -->

x ^ y = (x | y) & ~(x & y)

The operation works for the following input types:

- Two single elements of type `bool`
- One <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type `bool` and one single `bool`, where the result will
  be calculated by applying logical XOR with the single element to each
  element in the larger Tensor.
- Two <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> objects of type `bool` of the same shape. In this case,
  the result will be the element-wise logical XOR of the two input tensors.

#### Usage:



```
>>> a = tf.constant([True])
>>> b = tf.constant([False])
>>> tf.math.logical_xor(a, b)
<tf.Tensor: shape=(1,), dtype=bool, numpy=array([ True])>
```

```
>>> c = tf.constant([True])
>>> x = tf.constant([False, True, True, False])
>>> tf.math.logical_xor(c, x)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([ True, False, False,  True])>
```

```
>>> y = tf.constant([False, False, True, True])
>>> z = tf.constant([False, True, False, True])
>>> tf.math.logical_xor(y, z)
<tf.Tensor: shape=(4,), dtype=bool, numpy=array([False,  True,  True, False])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> type bool.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> of type bool with the same size as that of x or y.
</td>
</tr>

</table>

