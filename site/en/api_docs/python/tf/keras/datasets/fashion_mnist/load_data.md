description: Loads the Fashion-MNIST dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.datasets.fashion_mnist.load_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.datasets.fashion_mnist.load_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/datasets/fashion_mnist.py#L30-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads the Fashion-MNIST dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.datasets.fashion_mnist.load_data`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.datasets.fashion_mnist.load_data()
</code></pre>



<!-- Placeholder for "Used in" -->

This is a dataset of 60,000 28x28 grayscale images of 10 fashion categories,
along with a test set of 10,000 images. This dataset can be used as
a drop-in replacement for MNIST. The class labels are:

| Label | Description |
|:-----:|-------------|
|   0   | T-shirt/top |
|   1   | Trouser     |
|   2   | Pullover    |
|   3   | Dress       |
|   4   | Coat        |
|   5   | Sandal      |
|   6   | Shirt       |
|   7   | Sneaker     |
|   8   | Bag         |
|   9   | Ankle boot  |

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

**x_train, x_test**: uint8 arrays of grayscale image data with shape
(num_samples, 28, 28).

**y_train, y_test**: uint8 arrays of labels (integers in range 0-9)
with shape (num_samples,).
</td>
</tr>

</table>



#### License:

The copyright for Fashion-MNIST is held by Zalando SE.
Fashion-MNIST is licensed under the [MIT license](
https://github.com/zalandoresearch/fashion-mnist/blob/master/LICENSE).
