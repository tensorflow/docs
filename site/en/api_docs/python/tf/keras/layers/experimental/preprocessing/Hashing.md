description: Implements categorical feature hashing, also known as "hashing trick".

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.experimental.preprocessing.Hashing" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="adapt"/>
</div>

# tf.keras.layers.experimental.preprocessing.Hashing

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/layers/preprocessing/hashing.py#L44-L279">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Implements categorical feature hashing, also known as "hashing trick".

Inherits From: [`PreprocessingLayer`](../../../../../tf/keras/layers/experimental/preprocessing/PreprocessingLayer.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.experimental.preprocessing.Hashing`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.experimental.preprocessing.Hashing(
    num_bins, salt=None, name=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

This layer transforms single or multiple categorical inputs to hashed output.
It converts a sequence of int or string to a sequence of int. The stable hash
function uses tensorflow::ops::Fingerprint to produce universal output that
is consistent across platforms.

This layer uses [FarmHash64](https://github.com/google/farmhash) by default,
which provides a consistent hashed output across different platforms and is
stable across invocations, regardless of device and context, by mixing the
input bits thoroughly.

If you want to obfuscate the hashed output, you can also pass a random `salt`
argument in the constructor. In that case, the layer will use the
[SipHash64](https://github.com/google/highwayhash) hash function, with
the `salt` value serving as additional input to the hash function.

Example (FarmHash64):

```
>>> layer = tf.keras.layers.experimental.preprocessing.Hashing(num_bins=3)
>>> inp = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> layer(inp)
<tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[1],
         [0],
         [1],
         [1],
         [2]])>
```


Example (FarmHash64) with list of inputs:
>>> layer = tf.keras.layers.experimental.preprocessing.Hashing(num_bins=3)
>>> inp_1 = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> inp_2 = np.asarray([[5], [4], [3], [2], [1]])
>>> layer([inp_1, inp_2])
<tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[1],
         [1],
         [0],
         [2],
         [0]])>


Example (SipHash64):

```
>>> layer = tf.keras.layers.experimental.preprocessing.Hashing(num_bins=3,
...    salt=[133, 137])
>>> inp = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> layer(inp)
<tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[1],
         [2],
         [1],
         [0],
         [2]])>
```

Example (Siphash64 with a single integer, same as `salt=[133, 133]`

```
>>> layer = tf.keras.layers.experimental.preprocessing.Hashing(num_bins=3,
...    salt=133)
>>> inp = [['A'], ['B'], ['C'], ['D'], ['E']]
>>> layer(inp)
<tf.Tensor: shape=(5, 1), dtype=int64, numpy=
  array([[0],
         [0],
         [2],
         [1],
         [0]])>
```

Reference: [SipHash with salt](https://www.131002.net/siphash/siphash.pdf)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`num_bins`
</td>
<td>
Number of hash bins.
</td>
</tr><tr>
<td>
`salt`
</td>
<td>
A single unsigned integer or None.
If passed, the hash function used will be SipHash64, with these values
used as an additional input (known as a "salt" in cryptography).
These should be non-zero. Defaults to `None` (in that
case, the FarmHash64 hash function is used). It also supports
tuple/list of 2 unsigned integer numbers, see reference paper for details.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
Name to give to the layer.
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
Keyword arguments to construct a layer.
</td>
</tr>
</table>


Input shape: A single or list of string, int32 or int64 `Tensor`,
  `SparseTensor` or `RaggedTensor` of shape `[batch_size, ...,]`

Output shape: An int64 `Tensor`, `SparseTensor` or `RaggedTensor` of shape
  `[batch_size, ...]`. If any input is `RaggedTensor` then output is
  `RaggedTensor`, otherwise if any input is `SparseTensor` then output is
  `SparseTensor`, otherwise the output is `Tensor`.

## Methods

<h3 id="adapt"><code>adapt</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/engine/base_preprocessing_layer.py#L53-L66">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>adapt(
    data, reset_state=(True)
)
</code></pre>

Fits the state of the preprocessing layer to the data being passed.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`data`
</td>
<td>
The data to train on. It can be passed either as a tf.data
Dataset, or as a numpy array.
</td>
</tr><tr>
<td>
`reset_state`
</td>
<td>
Optional argument specifying whether to clear the state of
the layer at the start of the call to `adapt`, or whether to start
from the existing state. This argument may not be relevant to all
preprocessing layers: a subclass of PreprocessingLayer may choose to
throw if 'reset_state' is set to False.
</td>
</tr>
</table>





