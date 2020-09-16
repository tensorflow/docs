description: Loads the [MNIST dataset](http://yann.lecun.com/exdb/mnist/).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.datasets.mnist.load_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.datasets.mnist.load_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/datasets/mnist.py#L27-L67">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads the [MNIST dataset](http://yann.lecun.com/exdb/mnist/).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.datasets.mnist.load_data`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.datasets.mnist.load_data(
    path='mnist.npz'
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a dataset of 60,000 28x28 grayscale images of the 10 digits,
along with a test set of 10,000 images.
More info can be found at the
(MNIST homepage)[http://yann.lecun.com/exdb/mnist/].


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`path`
</td>
<td>
path where to cache the dataset locally
(relative to ~/.keras/datasets).
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

**x_train, x_test**: uint8 arrays of grayscale image data with shapes
(num_samples, 28, 28).

**y_train, y_test**: uint8 arrays of digit labels (integers in range 0-9)
with shapes (num_samples,).
</td>
</tr>

</table>



#### License:

Yann LeCun and Corinna Cortes hold the copyright of MNIST dataset,
which is a derivative work from original NIST datasets.
MNIST dataset is made available under the terms of the
[Creative Commons Attribution-Share Alike 3.0 license.](
https://creativecommons.org/licenses/by-sa/3.0/)
