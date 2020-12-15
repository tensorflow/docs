description: Category encoding layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.CategoryEncoding" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
<meta itemprop="property" content="set_num_elements"/>
<meta itemprop="property" content="set_tfidf_data"/>
</div>

# tf.keras.layers.experimental.preprocessing.CategoryEncoding

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L57-L338">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Category encoding layer.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.CategoryEncoding(
    max_tokens=None, output_mode=BINARY, sparse=(False), **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer provides options for condensing data into a categorical encoding.
It accepts integer values as inputs and outputs a dense representation
(one sample = 1-index tensor of float values representing data about the
sample's tokens) of those inputs.

#### Examples:



```
>>> layer = tf.keras.layers.experimental.preprocessing.CategoryEncoding(
...           max_tokens=4, output_mode="count")
>>> layer([[0, 1], [0, 0], [1, 2], [3, 1]])
<tf.Tensor: shape=(4, 4), dtype=float32, numpy=
  array([[1., 1., 0., 0.],
         [2., 0., 0., 0.],
         [0., 1., 1., 0.],
         [0., 1., 0., 1.]], dtype=float32)>
```


Examples with weighted inputs:

```
>>> layer = tf.keras.layers.experimental.preprocessing.CategoryEncoding(
...           max_tokens=4, output_mode="count")
>>> count_weights = np.array([[.1, .2], [.1, .1], [.2, .3], [.4, .2]])
>>> layer([[0, 1], [0, 0], [1, 2], [3, 1]], count_weights=count_weights)
<tf.Tensor: shape=(4, 4), dtype=float64, numpy=
  array([[0.1, 0.2, 0. , 0. ],
         [0.2, 0. , 0. , 0. ],
         [0. , 0.2, 0.3, 0. ],
         [0. , 0.2, 0. , 0.4]])>
```


#### Call arguments:


* <b>`inputs`</b>: A 2D tensor `(samples, timesteps)`.
* <b>`count_weights`</b>: A 2D tensor in the same shape as `inputs` indicating the
  weight for each sample value when summing up in `count` mode. Not used in
  `binary` or `tfidf` mode.




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
`output_mode`
</td>
<td>
Specification for the output of the layer.
Defaults to "binary". Values can
be "binary", "count" or "tf-idf", configuring the layer as follows:
"binary": Outputs a single int array per batch, of either vocab_size or
max_tokens size, containing 1s in all elements where the token mapped
to that index exists at least once in the batch item.
"count": As "binary", but the int array contains a count of the number
of times the token at that index appeared in the batch item.
"tf-idf": As "binary", but the TF-IDF algorithm is applied to find the
value in each token slot.
</td>
</tr><tr>
<td>
`sparse`
</td>
<td>
Boolean. If true, returns a `SparseTensor` instead of a dense
`Tensor`. Defaults to `False`.
</td>
</tr>
</table>



## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L176-L195">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L236-L246">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_num_elements(
    num_elements
)
</code></pre>




<h3 id="set_tfidf_data"><code>set_tfidf_data</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/category_encoding.py#L248-L263">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>set_tfidf_data(
    tfidf_data
)
</code></pre>






