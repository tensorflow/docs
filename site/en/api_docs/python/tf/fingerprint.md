page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.fingerprint


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/fingerprint">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L4671-L4717">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Generates fingerprint values.

### Aliases:

* <a href="/api_docs/python/tf/fingerprint"><code>tf.compat.v1.fingerprint</code></a>
* <a href="/api_docs/python/tf/fingerprint"><code>tf.compat.v2.fingerprint</code></a>


``` python
tf.fingerprint(
    data,
    method='farmhash64',
    name=None
)
```



<!-- Placeholder for "Used in" -->

Generates fingerprint values of `data`.

Fingerprint op considers the first dimension of `data` as the batch dimension,
and `output[i]` contains the fingerprint value generated from contents in
`data[i, ...]` for all `i`.

Fingerprint op writes fingerprint values as byte arrays. For example, the
default method `farmhash64` generates a 64-bit fingerprint value at a time.
This 8-byte value is written out as an <a href="../tf#uint8"><code>tf.uint8</code></a> array of size 8, in
little-endian order.

For example, suppose that `data` has data type <a href="../tf#int32"><code>tf.int32</code></a> and shape (2, 3, 4),
and that the fingerprint method is `farmhash64`. In this case, the output
shape is (2, 8), where 2 is the batch dimension size of `data`, and 8 is the
size of each fingerprint value in bytes. `output[0, :]` is generated from
12 integers in `data[0, :, :]` and similarly `output[1, :]` is generated from
other 12 integers in `data[1, :, :]`.

Note that this op fingerprints the raw underlying buffer, and it does not
fingerprint Tensor's metadata such as data type and/or shape. For example, the
fingerprint values are invariant under reshapes and bitcasts as long as the
batch dimension remain the same:

```python
tf.fingerprint(data) == tf.fingerprint(tf.reshape(data, ...))
tf.fingerprint(data) == tf.fingerprint(tf.bitcast(data, ...))
```

For string data, one should expect `tf.fingerprint(data) !=
tf.fingerprint(tf.string.reduce_join(data))` in general.

#### Args:


* <b>`data`</b>: A `Tensor`. Must have rank 1 or higher.
* <b>`method`</b>: A `Tensor` of type <a href="../tf#string"><code>tf.string</code></a>. Fingerprint method used by this op.
  Currently available method is `farmhash64`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A two-dimensional `Tensor` of type <a href="../tf#uint8"><code>tf.uint8</code></a>. The first dimension equals to
`data`'s first dimension, and the second dimension size depends on the
fingerprint algorithm.
