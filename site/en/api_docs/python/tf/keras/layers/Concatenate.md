description: Layer that concatenates a list of inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Concatenate" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Concatenate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/merge.py#L424-L575">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that concatenates a list of inputs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Concatenate`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Concatenate(
    axis=-1, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It takes as input a list of tensors, all of the same shape except
for the concatenation axis, and returns a single tensor that is the
concatenation of all inputs.

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
>>> tf.keras.layers.Concatenate(axis=1)([x, y])
<tf.Tensor: shape=(2, 3, 5), dtype=int64, numpy=
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [20, 21, 22, 23, 24]],
       [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [25, 26, 27, 28, 29]]])>
```

```
>>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
>>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
>>> concatted = tf.keras.layers.Concatenate()([x1, x2])
>>> concatted.shape
TensorShape([5, 16])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Axis along which to concatenate.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
standard layer keyword arguments.
</td>
</tr>
</table>



