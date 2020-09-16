description: Iterator yielding data from a Numpy array.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.NumpyArrayIterator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="next"/>
<meta itemprop="property" content="on_epoch_end"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="white_list_formats"/>
</div>

# tf.keras.preprocessing.image.NumpyArrayIterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/preprocessing/image.py#L258-L318">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Iterator yielding data from a Numpy array.

Inherits From: [`Iterator`](../../../../tf/keras/preprocessing/image/Iterator.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.NumpyArrayIterator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.NumpyArrayIterator(
    x, y, image_data_generator, batch_size=32, shuffle=(False), sample_weight=None,
    seed=None, data_format=None, save_to_dir=None, save_prefix='',
    save_format='png', subset=None, dtype=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Numpy array of input data or tuple.
If tuple, the second elements is either
another numpy array or a list of numpy arrays,
each of which gets passed
through as an output without any modifications.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Numpy array of targets data.
</td>
</tr><tr>
<td>
`image_data_generator`
</td>
<td>
Instance of `ImageDataGenerator`
to use for random transformations and normalization.
</td>
</tr><tr>
<td>
`batch_size`
</td>
<td>
Integer, size of a batch.
</td>
</tr><tr>
<td>
`shuffle`
</td>
<td>
Boolean, whether to shuffle the data between epochs.
</td>
</tr><tr>
<td>
`sample_weight`
</td>
<td>
Numpy array of sample weights.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Random seed for data shuffling.
</td>
</tr><tr>
<td>
`data_format`
</td>
<td>
String, one of `channels_first`, `channels_last`.
</td>
</tr><tr>
<td>
`save_to_dir`
</td>
<td>
Optional directory where to save the pictures
being yielded, in a viewable format. This is useful
for visualizing the random transformations being
applied, for debugging purposes.
</td>
</tr><tr>
<td>
`save_prefix`
</td>
<td>
String prefix to use for saving sample
images (if `save_to_dir` is set).
</td>
</tr><tr>
<td>
`save_format`
</td>
<td>
Format to use for saving sample images
(if `save_to_dir` is set).
</td>
</tr><tr>
<td>
`subset`
</td>
<td>
Subset of data (`"training"` or `"validation"`) if
validation_split is set in ImageDataGenerator.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Dtype to use for the generated arrays.
</td>
</tr>
</table>



## Methods

<h3 id="next"><code>next</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>next()
</code></pre>

For python 2.x.

# Returns
    The next batch.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_epoch_end()
</code></pre>




<h3 id="reset"><code>reset</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>




<h3 id="__getitem__"><code>__getitem__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    idx
)
</code></pre>




<h3 id="__iter__"><code>__iter__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>






## Class Variables

* `white_list_formats` <a id="white_list_formats"></a>
