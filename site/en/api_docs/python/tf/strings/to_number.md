description: Converts each string in the input Tensor to the specified numeric type.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.strings.to_number" />
<meta itemprop="path" content="Stable" />
</div>

# tf.strings.to_number

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/string_ops.py#L454-L479">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts each string in the input Tensor to the specified numeric type.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.strings.to_number(
    input, out_type=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

(Note that int32 overflow results in an error while float overflow
results in a rounded value.)

#### Examples:



```
>>> tf.strings.to_number("1.55")
<tf.Tensor: shape=(), dtype=float32, numpy=1.55>
>>> tf.strings.to_number("3", tf.int32)
<tf.Tensor: shape=(), dtype=int32, numpy=3>
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
A `Tensor` of type `string`.
</td>
</tr><tr>
<td>
`out_type`
</td>
<td>
An optional <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a> from: `tf.float32, tf.float64, tf.int32,
tf.int64`. Defaults to `tf.float32`.
The numeric type to interpret each string in `string_tensor` as.
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
A `Tensor` of type `out_type`.
</td>
</tr>

</table>

