description: Concatenates a list of tensors alongside the specified axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.concatenate" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.concatenate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L2846-L2881">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Concatenates a list of tensors alongside the specified axis.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.concatenate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.concatenate(
    tensors, axis=-1
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`tensors`
</td>
<td>
list of tensors to concatenate.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
concatenation axis.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor.
</td>
</tr>

</table>



#### Example:


```
>>> a = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> b = tf.constant([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
>>> tf.keras.backend.concatenate((a, b), axis=-1)
<tf.Tensor: shape=(3, 6), dtype=int32, numpy=
array([[ 1,  2,  3, 10, 20, 30],
       [ 4,  5,  6, 40, 50, 60],
       [ 7,  8,  9, 70, 80, 90]], dtype=int32)>
```
