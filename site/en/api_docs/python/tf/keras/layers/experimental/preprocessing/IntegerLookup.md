description: Maps integers from a vocabulary to integer indices.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.IntegerLookup" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
<meta itemprop="property" content="get_vocabulary"/>
<meta itemprop="property" content="set_vocabulary"/>
<meta itemprop="property" content="vocab_size"/>
</div>

# tf.keras.layers.experimental.preprocessing.IntegerLookup

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/integer_lookup.py#L28-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Maps integers from a vocabulary to integer indices.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.IntegerLookup(
    max_values=None, num_oov_indices=1, mask_value=0, oov_value=-1, vocabulary=None,
    invert=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer translates a set of arbitrary integers into an integer output via a
table-based lookup, with optional out-of-vocabulary handling.

If desired, the user can call this layer's `adapt()` method on a data set,
which will analyze the data set, determine the frequency of individual string
values, and create a vocabulary from them. This vocabulary can have
unlimited size or be capped, depending on the configuration options for this
layer; if there are more unique values in the input than the maximum
vocabulary size, the most frequent terms will be used to create the
vocabulary.

#### Examples:



Creating a lookup layer with a known vocabulary

This example creates a lookup layer with a pre-existing vocabulary.

```
>>> vocab = [12, 36, 1138, 42]
>>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]])
>>> layer = IntegerLookup(vocabulary=vocab)
>>> layer(data)
<tf.Tensor: shape=(2, 3), dtype=int64, numpy=
array([[2, 4, 5],
       [5, 1, 3]])>
```


Creating a lookup layer with an adapted vocabulary

This example creates a lookup layer and generates the vocabulary by analyzing
the dataset.

```
>>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]])
>>> layer = IntegerLookup()
>>> layer.adapt(data)
>>> layer.get_vocabulary()
[0, -1, 42, 1138, 1000, 36, 12]
```

Note how the mask value 0 and the OOV value -1 have been added to the
vocabulary. The remaining values are sorted by frequency (1138, which has
2 occurrences, is first) then by inverse sort order.

```
>>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]])
>>> layer = IntegerLookup()
>>> layer.adapt(data)
>>> layer(data)
<tf.Tensor: shape=(2, 3), dtype=int64, numpy=
array([[6, 3, 2],
       [2, 4, 5]])>
```


Lookups with multiple OOV tokens.

This example demonstrates how to use a lookup layer with multiple OOV tokens.
When a layer is created with more than one OOV token, any OOV values are
hashed into the number of OOV buckets, distributing OOV values in a
deterministic fashion across the set.

```
>>> vocab = [12, 36, 1138, 42]
>>> data = tf.constant([[12, 1138, 42], [37, 1000, 36]])
>>> layer = IntegerLookup(vocabulary=vocab, num_oov_indices=2)
>>> layer(data)
<tf.Tensor: shape=(2, 3), dtype=int64, numpy=
array([[3, 5, 6],
       [2, 1, 4]])>
```

Note that the output for OOV value 37 is 2, while the output for OOV value
1000 is 1. The in-vocab terms have their output index increased by 1 from
earlier examples (12 maps to 3, etc) in order to make space for the extra OOV
value.


Inverse lookup

This example demonstrates how to map indices to values using this layer. (You
can also use adapt() with inverse=True, but for simplicity we'll pass the
vocab in this example.)

```
>>> vocab = [12, 36, 1138, 42]
>>> data = tf.constant([[1, 3, 4], [4, 5, 2]])
>>> layer = IntegerLookup(vocabulary=vocab, invert=True)
>>> layer(data)
<tf.Tensor: shape=(2, 3), dtype=int64, numpy=
array([[  12, 1138,   42],
       [  42,   -1,   36]])>
```

Note that the integer 5, which is out of the vocabulary space, returns an OOV
token.


Forward and inverse lookup pairs

This example demonstrates how to use the vocabulary of a standard lookup
layer to create an inverse lookup layer.

```
>>> vocab = [12, 36, 1138, 42]
>>> data = tf.constant([[12, 1138, 42], [42, 1000, 36]])
>>> layer = IntegerLookup(vocabulary=vocab)
>>> i_layer = IntegerLookup(vocabulary=layer.get_vocabulary(), invert=True)
>>> int_data = layer(data)
>>> i_layer(int_data)
<tf.Tensor: shape=(2, 3), dtype=int64, numpy=
array([[  12, 1138,   42],
       [  42,   -1,   36]])>
```

In this example, the input value 1000 resulted in an output of -1, since
1000 was not in the vocabulary - it got represented as an OOV, and all OOV
values are returned as -1 in the inverse layer. Also, note that for the
inverse to work, you must have already set the forward layer vocabulary
either directly or via fit() before calling get_vocabulary().



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`max_values`
</td>
<td>
The maximum size of the vocabulary for this layer. If None,
there is no cap on the size of the vocabulary. Note that this vocabulary
includes the OOV and mask values, so the effective number of values is
(max_values - num_oov_values - (1 if mask_token else 0))
</td>
</tr><tr>
<td>
`num_oov_indices`
</td>
<td>
The number of out-of-vocabulary values to use; defaults to
1. If this value is more than 1, OOV inputs are modulated to determine
their OOV value; if this value is 0, passing an OOV input will result in
a '-1' being returned for that value in the output tensor. (Note that,
because the value is -1 and not 0, this will allow you to effectively drop
OOV values from categorical encodings.)
</td>
</tr><tr>
<td>
`mask_value`
</td>
<td>
A value that represents masked inputs, and which is mapped to
index 0. Defaults to 0. If set to None, no mask term will be added and the
OOV values, if any, will be indexed from (0...num_oov_values) instead of
(1...num_oov_values+1).
</td>
</tr><tr>
<td>
`oov_value`
</td>
<td>
The value representing an out-of-vocabulary value. Defaults to
-1.
</td>
</tr><tr>
<td>
`vocabulary`
</td>
<td>
An optional list of values, or a path to a text file containing
a vocabulary to load into this layer. The file should contain one value
per line. If the list or file contains the same token multiple times, an
error will be thrown.
</td>
</tr><tr>
<td>
`invert`
</td>
<td>
If true, this layer will map indices to vocabulary items instead
of mapping vocabulary items to indices.
</td>
</tr>
</table>



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/index_lookup.py#L195-L206">View source</a>

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






