description: Returns a <a href="../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> that represents the given value.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.type_spec_from_value" />
<meta itemprop="path" content="Stable" />
</div>

# tf.type_spec_from_value

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/type_spec.py#L508-L554">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a <a href="../tf/TypeSpec.md"><code>tf.TypeSpec</code></a> that represents the given `value`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.type_spec_from_value`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.type_spec_from_value(
    value
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Examples:


```
>>> tf.type_spec_from_value(tf.constant([1, 2, 3]))
TensorSpec(shape=(3,), dtype=tf.int32, name=None)
>>> tf.type_spec_from_value(np.array([4.0, 5.0], np.float64))
TensorSpec(shape=(2,), dtype=tf.float64, name=None)
>>> tf.type_spec_from_value(tf.ragged.constant([[1, 2], [3, 4, 5]]))
RaggedTensorSpec(TensorShape([2, None]), tf.int32, 1, tf.int64)
```

```
>>> example_input = tf.ragged.constant([[1, 2], [3]])
>>> @tf.function(input_signature=[tf.type_spec_from_value(example_input)])
... def f(x):
...   return tf.reduce_sum(x, axis=1)
```



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`value`
</td>
<td>
A value that can be accepted or returned by TensorFlow APIs.
Accepted types for `value` include <a href="../tf/Tensor.md"><code>tf.Tensor</code></a>, any value that can be
converted to <a href="../tf/Tensor.md"><code>tf.Tensor</code></a> using <a href="../tf/convert_to_tensor.md"><code>tf.convert_to_tensor</code></a>, and any subclass
of `CompositeTensor` (such as <a href="../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `TypeSpec` that is compatible with `value`.
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
If a TypeSpec cannot be built for `value`, because its type
is not supported.
</td>
</tr>
</table>

