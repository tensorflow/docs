page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.bucket_by_sequence_length


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/data/experimental/bucket_by_sequence_length">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/data/experimental/ops/grouping.py#L127-L244">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A transformation that buckets elements in a `Dataset` by length.

### Aliases:

* <a href="/api_docs/python/tf/data/experimental/bucket_by_sequence_length"><code>tf.compat.v1.data.experimental.bucket_by_sequence_length</code></a>
* <a href="/api_docs/python/tf/data/experimental/bucket_by_sequence_length"><code>tf.compat.v2.data.experimental.bucket_by_sequence_length</code></a>


``` python
tf.data.experimental.bucket_by_sequence_length(
    element_length_func,
    bucket_boundaries,
    bucket_batch_sizes,
    padded_shapes=None,
    padding_values=None,
    pad_to_bucket_boundary=False,
    no_padding=False,
    drop_remainder=False
)
```



<!-- Placeholder for "Used in" -->

Elements of the `Dataset` are grouped together by length and then are padded
and batched.

This is useful for sequence tasks in which the elements have variable length.
Grouping together elements that have similar lengths reduces the total
fraction of padding in a batch which increases training step efficiency.

#### Args:


* <b>`element_length_func`</b>: function from element in `Dataset` to <a href="../../../tf#int32"><code>tf.int32</code></a>,
  determines the length of the element, which will determine the bucket it
  goes into.
* <b>`bucket_boundaries`</b>: `list<int>`, upper length boundaries of the buckets.
* <b>`bucket_batch_sizes`</b>: `list<int>`, batch size per bucket. Length should be
  `len(bucket_boundaries) + 1`.
* <b>`padded_shapes`</b>: Nested structure of <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> to pass to
  <a href="../../../tf/data/Dataset#padded_batch"><code>tf.data.Dataset.padded_batch</code></a>. If not provided, will use
  `dataset.output_shapes`, which will result in variable length dimensions
  being padded out to the maximum length in each batch.
* <b>`padding_values`</b>: Values to pad with, passed to
  <a href="../../../tf/data/Dataset#padded_batch"><code>tf.data.Dataset.padded_batch</code></a>. Defaults to padding with 0.
* <b>`pad_to_bucket_boundary`</b>: bool, if `False`, will pad dimensions with unknown
  size to maximum length in batch. If `True`, will pad dimensions with
  unknown size to bucket boundary minus 1 (i.e., the maximum length in each
  bucket), and caller must ensure that the source `Dataset` does not contain
  any elements with length longer than `max(bucket_boundaries)`.
* <b>`no_padding`</b>: `bool`, indicates whether to pad the batch features (features
  need to be either of type <a href="../../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a> or of same shape).
* <b>`drop_remainder`</b>: (Optional.) A <a href="../../../tf#bool"><code>tf.bool</code></a> scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>, representing
  whether the last batch should be dropped in the case it has fewer than
  `batch_size` elements; the default behavior is not to drop the smaller
  batch.


#### Returns:

A `Dataset` transformation function, which can be passed to
<a href="../../../tf/data/Dataset#apply"><code>tf.data.Dataset.apply</code></a>.



#### Raises:


* <b>`ValueError`</b>: if `len(bucket_batch_sizes) != len(bucket_boundaries) + 1`.
