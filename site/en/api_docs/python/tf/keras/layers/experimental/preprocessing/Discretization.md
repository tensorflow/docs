description: Buckets data into discrete ranges.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.Discretization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.keras.layers.experimental.preprocessing.Discretization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/discretization.py#L32-L101">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Buckets data into discrete ranges.

Inherits From: [`Layer`](../../../../../tf/keras/layers/Layer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.Discretization`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.Discretization(
    bins, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer will place each element of its input data into one of several
contiguous ranges and output an integer index indicating which range each
element was placed in.

#### Input shape:

Any <a href="../../../../../tf/Tensor.md"><code>tf.Tensor</code></a> or <a href="../../../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> of dimension 2 or higher.



#### Output shape:

Same as input shape.



#### Examples:



Bucketize float values based on provided buckets.
>>> input = np.array([[-1.5, 1.0, 3.4, .5], [0.0, 3.0, 1.3, 0.0]])
>>> layer = tf.keras.layers.experimental.preprocessing.Discretization(
...          bins=[0., 1., 2.])
>>> layer(input)
<tf.Tensor: shape=(2, 4), dtype=int32, numpy=
array([[0, 2, 3, 1],
       [1, 3, 2, 1]], dtype=int32)>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`bins`
</td>
<td>
Optional boundary specification. Bins include the left boundary and
exclude the right boundary, so `bins=[0., 1., 2.]` generates bins
`(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`.
</td>
</tr>
</table>



