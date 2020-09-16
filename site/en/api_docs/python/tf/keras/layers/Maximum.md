description: Layer that computes the maximum (element-wise) a list of inputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.Maximum" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.Maximum

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/merge.py#L364-L390">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Layer that computes the maximum (element-wise) a list of inputs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.Maximum`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.Maximum(
    **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

It takes as input a list of tensors, all of the same shape, and returns
a single tensor (also of the same shape).

```
>>> tf.keras.layers.Maximum()([np.arange(5).reshape(5, 1),
...                            np.arange(5, 10).reshape(5, 1)])
<tf.Tensor: shape=(5, 1), dtype=int64, numpy=
array([[5],
     [6],
     [7],
     [8],
     [9]])>
```

```
>>> x1 = tf.keras.layers.Dense(8)(np.arange(10).reshape(5, 2))
>>> x2 = tf.keras.layers.Dense(8)(np.arange(10, 20).reshape(5, 2))
>>> maxed = tf.keras.layers.Maximum()([x1, x2])
>>> maxed.shape
TensorShape([5, 8])
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
standard layer keyword arguments.
</td>
</tr>
</table>



