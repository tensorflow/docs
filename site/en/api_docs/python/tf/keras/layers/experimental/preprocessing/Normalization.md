description: Feature-wise normalization of the data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.Normalization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
</div>

# tf.keras.layers.experimental.preprocessing.Normalization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/normalization.py#L42-L128">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Feature-wise normalization of the data.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.Normalization(
    axis=-1, dtype=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer will coerce its inputs into a normal distribution centered around
0 with standard deviation 1. It accomplishes this by precomputing the mean and
variance of the data, and calling (input-mean)/sqrt(var) at runtime.

What happens in `adapt`: Compute mean and variance of the data and store them
  as the layer's weights. `adapt` should be called before `fit`, `evaluate`,
  or `predict`.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`axis`
</td>
<td>
Integer or tuple of integers, the axis or axes that should be
normalized (typically the features axis). We will normalize each element
in the specified axis. The default is '-1' (the innermost axis); 0 (the
batch axis) is not allowed.
</td>
</tr>
</table>



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/engine/base_preprocessing_layer.py#L129-L197">View source</a>

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
The data to train on. It can be passed either as a tf.data Dataset,
or as a numpy array.
</td>
</tr><tr>
<td>
`reset_state`
</td>
<td>
Optional argument specifying whether to clear the state of
the layer at the start of the call to `adapt`, or whether to start from
the existing state. Subclasses may choose to throw if reset_state is set
to 'False'.
</td>
</tr>
</table>





