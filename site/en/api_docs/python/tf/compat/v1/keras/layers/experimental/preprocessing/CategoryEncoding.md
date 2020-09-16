description: CategoryEncoding layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.experimental.preprocessing.CategoryEncoding" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
<meta itemprop="property" content="set_num_elements"/>
<meta itemprop="property" content="set_tfidf_data"/>
</div>

# tf.compat.v1.keras.layers.experimental.preprocessing.CategoryEncoding

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/category_encoding_v1.py#L27-L69">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



CategoryEncoding layer.

Inherits From: [`CategoryEncoding`](../../../../../../../tf/keras/layers/experimental/preprocessing/CategoryEncoding.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.experimental.preprocessing.CategoryEncoding(
    max_tokens=None, output_mode=BINARY, sparse=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer provides options for condensing input data into denser
representations. It accepts either integer values or strings as inputs,
allows users to map those inputs into a contiguous integer space, and
outputs either those integer values (one sample = 1D tensor of integer token
indices) or a dense representation (one sample = 1D tensor of float values
representing data about the sample's tokens).

If desired, the user can call this layer's adapt() method on a dataset.
When this layer is adapted, it will analyze the dataset, determine the
frequency of individual integer or string values, and create a 'vocabulary'
from them. This vocabulary can have unlimited size or be capped, depending
on the configuration options for this layer; if there are more unique
values in the input than the maximum vocabulary size, the most frequent
terms will be used to create the vocabulary.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`max_elements`
</td>
<td>
The maximum size of the vocabulary for this layer. If None,
there is no cap on the size of the vocabulary.
</td>
</tr><tr>
<td>
`output_mode`
</td>
<td>
Optional specification for the output of the layer. Values can
be "int", "binary", "count" or "tf-idf", configuring the layer as follows:
"int": Outputs integer indices, one integer index per split string
token.
"binary": Outputs a single int array per batch, of either vocab_size or
max_elements size, containing 1s in all elements where the token
mapped to that index exists at least once in the batch item.
"count": As "binary", but the int array contains a count of the number
of times the token at that index appeared in the batch item.
"tf-idf": As "binary", but the TF-IDF algorithm is applied to find the
value in each token slot.
</td>
</tr><tr>
<td>
`output_sequence_length`
</td>
<td>
Only valid in INT mode. If set, the output will have
its time dimension padded or truncated to exactly `output_sequence_length`
values, resulting in a tensor of shape [batch_size,
output_sequence_length] regardless of the input shape.
</td>
</tr><tr>
<td>
`pad_to_max_elements`
</td>
<td>
Only valid in  "binary", "count", and "tf-idf" modes.
If True, the output will have its feature axis padded to `max_elements`
even if the number of unique values in the vocabulary is less than
max_elements, resulting in a tensor of shape [batch_size, max_elements]
regardless of vocabulary size. Defaults to False.
</td>
</tr>
</table>



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L181-L203">View source</a>

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



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
if the layer cannot be adapted at this time.
</td>
</tr>
</table>



<h3 id="set_num_elements"><code>set_num_elements</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L240-L250">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_num_elements(
    num_elements
)
</code></pre>




<h3 id="set_tfidf_data"><code>set_tfidf_data</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L252-L267">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_tfidf_data(
    tfidf_data
)
</code></pre>






