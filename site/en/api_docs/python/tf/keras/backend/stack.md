description: Stacks a list of rank R tensors into a rank R+1 tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.stack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.stack

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/backend.py#L3375-L3399">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Stacks a list of rank `R` tensors into a rank `R+1` tensor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.backend.stack`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.backend.stack(
    x, axis=0
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
List of tensors.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
Axis along which to perform stacking.
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
>>> a = tf.constant([[1, 2],[3, 4]])
>>> b = tf.constant([[10, 20],[30, 40]])
>>> tf.keras.backend.stack((a, b))
<tf.Tensor: shape=(2, 2, 2), dtype=int32, numpy=
array([[[ 1,  2],
        [ 3,  4]],
       [[10, 20],
        [30, 40]]], dtype=int32)>
```
