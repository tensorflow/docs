description: Loads the Boston Housing dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.datasets.boston_housing.load_data" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.datasets.boston_housing.load_data

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/datasets/boston_housing.py#L27-L79">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Loads the Boston Housing dataset.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.datasets.boston_housing.load_data`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.datasets.boston_housing.load_data(
    path='boston_housing.npz', test_split=0.2, seed=113
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a dataset taken from the StatLib library which is maintained at
Carnegie Mellon University.

Samples contain 13 attributes of houses at different locations around the
Boston suburbs in the late 1970s. Targets are the median values of
the houses at a location (in k$).

The attributes themselves are defined in the
[StatLib website](http://lib.stat.cmu.edu/datasets/boston).

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
</tr><tr>
<td>
`test_split`
</td>
<td>
fraction of the data to reserve as test set.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
Random seed for shuffling the data
before computing the test split.
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

**x_train, x_test**: numpy arrays with shape (num_samples, 13) containing
either the training samples (for x_train), or test samples (for y_train)

**y_train, y_test**: numpy arrays of shape (num_samples, ) containing the
target scalars. The targets are float scalars typically between 10 and
50 that represent the home prices in k$.
</td>
</tr>

</table>

