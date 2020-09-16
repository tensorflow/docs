description: Returns the index with the largest value across axes of a tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.argmax" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.argmax

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/math_ops.py#L261-L295">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the index with the largest value across axes of a tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.argmax`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.argmax(
    input, axis=None, output_type=tf.dtypes.int64, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

In case of identity returns the smallest index.

#### For example:



```
>>> A = tf.constant([2, 20, 30, 3, 6])
>>> tf.math.argmax(A)  # A[2] is maximum in tensor A
<tf.Tensor: shape=(), dtype=int64, numpy=2>
>>> B = tf.constant([[2, 20, 30, 3, 6], [3, 11, 16, 1, 8],
...                  [14, 45, 23, 5, 27]])
>>> tf.math.argmax(B, 0)
<tf.Tensor: shape=(5,), dtype=int64, numpy=array([2, 2, 0, 2, 2])>
>>> tf.math.argmax(B, 1)
<tf.Tensor: shape=(3,), dtype=int64, numpy=array([2, 2, 1])>
>>> C = tf.constant([0, 0, 0, 0])
>>> tf.math.argmax(C) # Returns smallest index in case of ties
<tf.Tensor: shape=(), dtype=int64, numpy=0>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
An integer, the axis to reduce across. Default to 0.
</td>
</tr><tr>
<td>
`output_type`
</td>
<td>
An optional output dtype (<a href="../../tf.md#int32"><code>tf.int32</code></a> or <a href="../../tf.md#int64"><code>tf.int64</code></a>). Defaults
to <a href="../../tf.md#int64"><code>tf.int64</code></a>.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
An optional name for the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` of type `output_type`.
</td>
</tr>

</table>

