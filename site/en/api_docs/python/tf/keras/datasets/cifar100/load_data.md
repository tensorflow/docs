description: Loads [CIFAR100 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.datasets.cifar100.load_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.datasets.cifar100.load_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/datasets/cifar100.py#L31-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads [CIFAR100 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.datasets.cifar100.load_data`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.datasets.cifar100.load_data(
    label_mode='fine'
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a dataset of 50,000 32x32 color training images and
10,000 test images, labeled over 100 fine-grained classes that are
grouped into 20 coarse-grained classes. See more info at the
[CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`label_mode`
</td>
<td>
one of "fine", "coarse". If it is "fine" the category labels
are the fine-grained labels, if it is "coarse" the output labels are the
coarse-grained superclasses.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

**x_train, x_test**: uint8 arrays of RGB image data with shape
`(num_samples, 3, 32, 32)` if <a href="../../../../tf/keras/backend/image_data_format.md"><code>tf.keras.backend.image_data_format()</code></a> is
`'channels_first'`, or `(num_samples, 32, 32, 3)` if the data format
is `'channels_last'`.

**y_train, y_test**: uint8 arrays of category labels with shape
(num_samples, 1).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
in case of invalid `label_mode`.
</td>
</tr>
</table>

