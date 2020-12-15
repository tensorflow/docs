description: Base class for image data iterators.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.image.Iterator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="next"/>
<meta itemprop="property" content="on_epoch_end"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="white_list_formats"/>
</div>

# tf.keras.preprocessing.image.Iterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/preprocessing/image.py#L304-L305">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for image data iterators.

Inherits From: [`Sequence`](../../../../tf/keras/utils/Sequence.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.image.Iterator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.image.Iterator(
    n, batch_size, shuffle, seed
)
</code></pre>



<!-- Placeholder for "Used in" -->

Every `Iterator` must implement the `_get_batches_of_transformed_samples`
method.

# Arguments
    n: Integer, total number of samples in the dataset to loop over.
    batch_size: Integer, size of a batch.
    shuffle: Boolean, whether to shuffle the data between epochs.
    seed: Random seeding for data shuffling.

## Methods

<h3 id="next"><code>next</code></h3>

<a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/image/iterator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>next()
</code></pre>

For python 2.x.

# Returns
    The next batch.

<h3 id="on_epoch_end"><code>on_epoch_end</code></h3>

<a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/image/iterator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>on_epoch_end()
</code></pre>




<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/image/iterator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>




<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/image/iterator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    idx
)
</code></pre>




<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/image/iterator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/image/iterator.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>






## Class Variables

* `white_list_formats` <a id="white_list_formats"></a>
