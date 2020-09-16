description: Zero-padding layer for 1D input (e.g. temporal sequence).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.ZeroPadding1D" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.ZeroPadding1D

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/convolutional.py#L2668-L2730">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Zero-padding layer for 1D input (e.g. temporal sequence).

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.ZeroPadding1D`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.ZeroPadding1D(
    padding=1, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Examples:



```
>>> input_shape = (2, 2, 3)
>>> x = np.arange(np.prod(input_shape)).reshape(input_shape)
>>> print(x)
[[[ 0  1  2]
  [ 3  4  5]]
 [[ 6  7  8]
  [ 9 10 11]]]
>>> y = tf.keras.layers.ZeroPadding1D(padding=2)(x)
>>> print(y)
tf.Tensor(
  [[[ 0  0  0]
    [ 0  0  0]
    [ 0  1  2]
    [ 3  4  5]
    [ 0  0  0]
    [ 0  0  0]]
   [[ 0  0  0]
    [ 0  0  0]
    [ 6  7  8]
    [ 9 10 11]
    [ 0  0  0]
    [ 0  0  0]]], shape=(2, 6, 3), dtype=int64)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`padding`
</td>
<td>
Int, or tuple of int (length 2), or dictionary.
- If int:
How many zeros to add at the beginning and end of
the padding dimension (axis 1).
- If tuple of int (length 2):
How many zeros to add at the beginning and the end of
the padding dimension (`(left_pad, right_pad)`).
</td>
</tr>
</table>



#### Input shape:

3D tensor with shape `(batch_size, axis_to_pad, features)`



#### Output shape:

3D tensor with shape `(batch_size, padded_axis, features)`


