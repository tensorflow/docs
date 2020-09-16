description: Representation of HDF5 dataset to be used instead of a Numpy array.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.HDF5Matrix" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__getitem__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__len__"/>
<meta itemprop="property" content="refs"/>
</div>

# tf.keras.utils.HDF5Matrix

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/utils/io_utils.py#L37-L185">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Representation of HDF5 dataset to be used instead of a Numpy array.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.utils.HDF5Matrix`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.utils.HDF5Matrix(
    datapath, dataset, start=0, end=None, normalizer=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

THIS CLASS IS DEPRECATED.
Training with HDF5Matrix may not be optimized for performance, and might
not work with every distribution strategy.

We recommend using https://github.com/tensorflow/io to load your
HDF5 data into a tf.data Dataset and passing that dataset to Keras.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`datapath`
</td>
<td>
string, path to a HDF5 file
</td>
</tr><tr>
<td>
`dataset`
</td>
<td>
string, name of the HDF5 dataset in the file specified
in datapath
</td>
</tr><tr>
<td>
`start`
</td>
<td>
int, start of desired slice of the specified dataset
</td>
</tr><tr>
<td>
`end`
</td>
<td>
int, end of desired slice of the specified dataset
</td>
</tr><tr>
<td>
`normalizer`
</td>
<td>
function to be called on data when retrieved
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>
<tr class="alt">
<td colspan="2">
ImportError if HDF5 & h5py are not installed
</td>
</tr>

</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
Gets the datatype of the dataset.
</td>
</tr><tr>
<td>
`ndim`
</td>
<td>
Gets the number of dimensions (rank) of the dataset.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Gets a numpy-style shape tuple giving the dataset dimensions.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
Gets the total dataset size (number of elements).
</td>
</tr>
</table>



## Methods

<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/utils/io_utils.py#L104-L134">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__getitem__(
    key
)
</code></pre>




<h3 id="__len__"><code>__len__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/utils/io_utils.py#L101-L102">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__len__()
</code></pre>






## Class Variables

* `refs` <a id="refs"></a>
