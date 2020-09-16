description: Text vectorization layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.experimental.preprocessing.TextVectorization" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
<meta itemprop="property" content="get_vocabulary"/>
<meta itemprop="property" content="set_vocabulary"/>
</div>

# tf.compat.v1.keras.layers.experimental.preprocessing.TextVectorization

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/text_vectorization_v1.py#L33-L97">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Text vectorization layer.

Inherits From: [`TextVectorization`](../../../../../../../tf/keras/layers/experimental/preprocessing/TextVectorization.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.experimental.preprocessing.TextVectorization(
    max_tokens=None, standardize=LOWER_AND_STRIP_PUNCTUATION,
    split=SPLIT_ON_WHITESPACE, ngrams=None, output_mode=INT,
    output_sequence_length=None, pad_to_max_tokens=(True), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer has basic options for managing text in a Keras model. It
transforms a batch of strings (one sample = one string) into either a list of
token indices (one sample = 1D tensor of integer token indices) or a dense
representation (one sample = 1D tensor of float values representing data about
the sample's tokens).

The processing of each sample contains the following steps:
  1) standardize each sample (usually lowercasing + punctuation stripping)
  2) split each sample into substrings (usually words)
  3) recombine substrings into tokens (usually ngrams)
  4) index tokens (associate a unique int value with each token)
  5) transform each sample using this index, either into a vector of ints or
     a dense float vector.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`max_tokens`
</td>
<td>
The maximum size of the vocabulary for this layer. If None,
there is no cap on the size of the vocabulary.
</td>
</tr><tr>
<td>
`standardize`
</td>
<td>
Optional specification for standardization to apply to the
input text. Values can be None (no standardization),
LOWER_AND_STRIP_PUNCTUATION (lowercase and remove punctuation) or a
Callable.
</td>
</tr><tr>
<td>
`split`
</td>
<td>
Optional specification for splitting the input text. Values can be
None (no splitting), SPLIT_ON_WHITESPACE (split on ASCII whitespace), or a
Callable.
</td>
</tr><tr>
<td>
`ngrams`
</td>
<td>
Optional specification for ngrams to create from the possibly-split
input text. Values can be None, an integer or tuple of integers; passing
an integer will create ngrams up to that integer, and passing a tuple of
integers will create ngrams for the specified values in the tuple. Passing
None means that no ngrams will be created.
</td>
</tr><tr>
<td>
`output_mode`
</td>
<td>
Optional specification for the output of the layer. Values can
be INT, BINARY, COUNT or TFIDF, which control the outputs as follows:
INT: Outputs integer indices, one integer index per split string token.
BINARY: Outputs a single int array per batch, of either vocab_size or
max_tokens size, containing 1s in all elements where the token mapped
to that index exists at least once in the batch item.
COUNT: As BINARY, but the int array contains a count of the number of
times the token at that index appeared in the batch item.
TFIDF: As BINARY, but the TF-IDF algorithm is applied to find the value
in each token slot.
</td>
</tr><tr>
<td>
`output_sequence_length`
</td>
<td>
Optional length for the output tensor. If set, the
output will be padded or truncated to this value in INT mode.
</td>
</tr><tr>
<td>
`pad_to_max_tokens`
</td>
<td>
If True, BINARY, COUNT, and TFIDF modes will have their
outputs padded to max_tokens, even if the number of unique tokens in the
vocabulary is less than max_tokens.
</td>
</tr>
</table>



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/text_vectorization.py#L366-L404">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/text_vectorization.py#L406-L407">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_vocabulary()
</code></pre>




<h3 id="set_vocabulary"><code>set_vocabulary</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/layers/preprocessing/text_vectorization.py#L429-L521">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_vocabulary(
    vocab, df_data=None, oov_df_value=None, append=(False)
)
</code></pre>

Sets vocabulary (and optionally document frequency) data for this layer.

This method sets the vocabulary and DF data for this layer directly, instead
of analyzing a dataset through 'adapt'. It should be used whenever the vocab
(and optionally document frequency) information is already known. If
vocabulary data is already present in the layer, this method will either
replace it, if 'append' is set to False, or append to it (if 'append' is set
to True).

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
</tr><tr>
<td>
`df_data`
</td>
<td>
An array of document frequency data. Only necessary if the layer
output_mode is TFIDF.
</td>
</tr><tr>
<td>
`oov_df_value`
</td>
<td>
The document frequency of the OOV token. Only necessary if
output_mode is TFIDF. OOV data is optional when appending additional
data in TFIDF mode; if an OOV value is supplied it will overwrite the
existing OOV value.
</td>
</tr><tr>
<td>
`append`
</td>
<td>
Whether to overwrite or append any existing vocabulary data.
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
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If the vocabulary cannot be set when this function is
called. This happens when "binary", "count", and "tfidf" modes,
if "pad_to_max_tokens" is False and the layer itself has already been
called.
</td>
</tr>
</table>





