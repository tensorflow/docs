description: Functional interface to the Concatenate layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.concatenate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.layers.concatenate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/merge.py#L899-L931">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Functional interface to the `Concatenate` layer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.concatenate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.concatenate(
    inputs, axis=-1, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

```
>>> x = np.arange(20).reshape(2, 2, 5)
>>> print(x)
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]]
 [[10 11 12 13 14]
  [15 16 17 18 19]]]
>>> y = np.arange(20, 30).reshape(2, 1, 5)
>>> print(y)
[[[20 21 22 23 24]]
 [[25 26 27 28 29]]]
>>> tf.keras.layers.concatenate([x, y],
...                             axis=1)
<tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
array([[[ 0,  1,  2,  3,  4],
      [ 5,  6,  7,  8,  9],
      [20, 21, 22, 23, 24]],
     [[10, 11, 12, 13, 14],
      [15, 16, 17, 18, 19],
      [25, 26, 27, 28, 29]]])>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`inputs`
</td>
<td>
A list of input tensors (at least 2).
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Concatenation axis.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Standard layer keyword arguments.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor, the concatenation of the inputs alongside axis `axis`.
</td>
</tr>

</table>

