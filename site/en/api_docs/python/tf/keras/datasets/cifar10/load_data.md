description: Loads [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.datasets.cifar10.load_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.datasets.cifar10.load_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/datasets/cifar10.py#L31-L82">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads [CIFAR10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.datasets.cifar10.load_data`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.datasets.cifar10.load_data()
</code></pre>



<!-- Placeholder for "Used in" -->

This is a dataset of 50,000 32x32 color training images and 10,000 test
images, labeled over 10 categories. See more info at the
[CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

**x_train, x_test**: uint8 arrays of RGB image data with shape
(num_samples, 3, 32, 32) if the <a href="../../../../tf/keras/backend/image_data_format.md"><code>tf.keras.backend.image_data_format</code></a> is
'channels_first', or (num_samples, 32, 32, 3) if the data format
is 'channels_last'.

**y_train, y_test**: uint8 arrays of category labels
(integers in range 0-9) each with shape (num_samples, 1).
</td>
</tr>

</table>

