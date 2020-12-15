description: Maps strings from a vocabulary to integer indices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.experimental.preprocessing.StringLookup" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
<meta itemprop="property" content="get_vocabulary"/>
<meta itemprop="property" content="set_vocabulary"/>
<meta itemprop="property" content="vocab_size"/>
</div>

# tf.compat.v1.keras.layers.experimental.preprocessing.StringLookup

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/string_lookup_v1.py#L27-L47">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Maps strings from a vocabulary to integer indices.

Inherits From: [`StringLookup`](../../../../../../../tf/keras/layers/experimental/preprocessing/StringLookup.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.experimental.preprocessing.StringLookup(
    max_tokens=None, num_oov_indices=1, mask_token='', oov_token='[UNK]',
    vocabulary=None, encoding=None, invert=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/index_lookup.py#L178-L193">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adapt(
    data, reset_state=(True)
)
</code></pre>

Fits the state of the preprocessing layer to the dataset.

Overrides the default adapt method to apply relevant preprocessing to the
inputs before passing to the combiner.

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
the layer at the start of the call to `adapt`. This must be True for
this layer, which does not support repeated calls to `adapt`.
</td>
</tr>
</table>



<h3 id="get_vocabulary"><code>get_vocabulary</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/string_lookup.py#L207-L214">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_vocabulary()
</code></pre>




<h3 id="set_vocabulary"><code>set_vocabulary</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/index_lookup.py#L345-L363">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_vocabulary(
    vocab
)
</code></pre>

Sets vocabulary data for this layer with inverse=False.

This method sets the vocabulary for this layer directly, instead of
analyzing a dataset through 'adapt'. It should be used whenever the vocab
information is already known. If vocabulary data is already present in the
layer, this method will either replace it

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`vocab`
</td>
<td>
An array of string tokens.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If there are too many inputs, the inputs do not match, or
input data is missing.
</td>
</tr>
</table>



<h3 id="vocab_size"><code>vocab_size</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/index_lookup.py#L208-L209">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>vocab_size()
</code></pre>






