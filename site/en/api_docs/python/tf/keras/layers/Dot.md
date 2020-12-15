description: Layer that computes a dot product between samples in two tensors.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Dot" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Dot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/merge.py#L579-L737">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that computes a dot product between samples in two tensors.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Dot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Dot(
    axes, normalize=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

E.g. if applied to a list of two tensors `a` and `b` of shape
`(batch_size, n)`, the output will be a tensor of shape `(batch_size, 1)`
where each entry `i` will be the dot product between
`a[i]` and `b[i]`.

```
>>> x = np.arange(10).reshape(1, 5, 2)
>>> print(x)
[[[0 1]
  [2 3]
  [4 5]
  [6 7]
  [8 9]]]
>>> y = np.arange(10, 20).reshape(1, 2, 5)
>>> print(y)
[[[10 11 12 13 14]
  [15 16 17 18 19]]]
>>> tf.keras.layers.Dot(axes=(1, 2))([x, y])
<tf.Tensor: shape=(1, 2, 2), dtype=int64, numpy=
array([[[260, 360],
        [320, 445]]])>
```

```
>>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
>>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
>>> dotted = tf.keras.layers.Dot(axes=1)([x1, x2])
>>> dotted.shape
TensorShape([5, 1])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`axes`
</td>
<td>
Integer or tuple of integers,
axis or axes along which to take the dot product. If a tuple, should
be two integers corresponding to the desired axis from the first input
and the desired axis from the second input, respectively. Note that the
size of the two selected axes must match.
</td>
</tr><tr>
<td>
`normalize`
</td>
<td>
Whether to L2-normalize samples along the
dot product axis before taking the dot product.
If set to True, then the output of the dot product
is the cosine proximity between the two samples.
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



