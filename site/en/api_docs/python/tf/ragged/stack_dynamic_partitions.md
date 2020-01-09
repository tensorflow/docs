page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.stack_dynamic_partitions


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/ragged/stack_dynamic_partitions">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_array_ops.py#L553-L653">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stacks dynamic partitions of a Tensor or RaggedTensor.

### Aliases:

* <a href="/api_docs/python/tf/ragged/stack_dynamic_partitions"><code>tf.compat.v1.ragged.stack_dynamic_partitions</code></a>
* <a href="/api_docs/python/tf/ragged/stack_dynamic_partitions"><code>tf.compat.v2.ragged.stack_dynamic_partitions</code></a>


``` python
tf.ragged.stack_dynamic_partitions(
    data,
    partitions,
    num_partitions,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Returns a RaggedTensor `output` with `num_partitions` rows, where the row
`output[i]` is formed by stacking all slices `data[j1...jN]` such that
`partitions[j1...jN] = i`.  Slices of `data` are stacked in row-major
order.

If `num_partitions` is an `int` (not a `Tensor`), then this is equivalent to
`tf.ragged.stack(tf.dynamic_partition(data, partitions, num_partitions))`.

####Example:

>     >>> data           = ['a', 'b', 'c', 'd', 'e']
>     >>> partitions     = [  3,   0,   2,   2,   3]
>     >>> num_partitions = 5
>     >>> tf.ragged.stack_dynamic_partitions(data, partitions, num_partitions)
>     <RaggedTensor [['b'], [], ['c', 'd'], ['a', 'e'], []]>

#### Args:


* <b>`data`</b>: A `Tensor` or `RaggedTensor` containing the values to stack.
* <b>`partitions`</b>: An `int32` or `int64` `Tensor` or `RaggedTensor` specifying the
  partition that each slice of `data` should be added to.
  `partitions.shape` must be a prefix of `data.shape`.  Values must be
  greater than or equal to zero, and less than `num_partitions`.
  `partitions` is not required to be sorted.
* <b>`num_partitions`</b>: An `int32` or `int64` scalar specifying the number of
  partitions to output.  This determines the number of rows in `output`.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A `RaggedTensor` containing the stacked partitions.  The returned tensor
has the same dtype as `data`, and its shape is
`[num_partitions, (D)] + data.shape[partitions.rank:]`, where `(D)` is a
ragged dimension whose length is the number of data slices stacked for
each `partition`.
