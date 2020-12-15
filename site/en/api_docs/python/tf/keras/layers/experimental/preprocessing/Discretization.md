description: Buckets data into discrete ranges.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.Discretization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
</div>

# tf.keras.layers.experimental.preprocessing.Discretization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/discretization.py#L36-L129">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Buckets data into discrete ranges.

Inherits From: [`PreprocessingLayer`](../../../../../tf/keras/layers/experimental/preprocessing/PreprocessingLayer.md)

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
array([[0, 1, 3, 1],
       [0, 3, 2, 0]], dtype=int32)>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`bins`
</td>
<td>
Optional boundary specification. Bins exclude the left boundary and
include the right boundary, so `bins=[0., 1., 2.]` generates bins
`(-inf, 0.)`, `[0., 1.)`, `[1., 2.)`, and `[2., +inf)`.
</td>
</tr>
</table>



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/engine/base_preprocessing_layer.py#L53-L66">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adapt(
    data, reset_state=(True)
)
</code></pre>

Fits the state of the preprocessing layer to the data being passed.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
The data to train on. It can be passed either as a tf.data
Dataset, or as a numpy array.
</td>
</tr><tr>
<td>
`reset_state`
</td>
<td>
Optional argument specifying whether to clear the state of
the layer at the start of the call to `adapt`, or whether to start
from the existing state. This argument may not be relevant to all
preprocessing layers: a subclass of PreprocessingLayer may choose to
throw if 'reset_state' is set to False.
</td>
</tr>
</table>





