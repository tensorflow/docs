page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/ragged/stack">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_concat_ops.py#L74-L113">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

### Aliases:

* <a href="/api_docs/python/tf/ragged/stack"><code>tf.compat.v1.ragged.stack</code></a>
* <a href="/api_docs/python/tf/ragged/stack"><code>tf.compat.v2.ragged.stack</code></a>


``` python
tf.ragged.stack(
    values,
    axis=0,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Given a list of tensors or ragged tensors with the same rank `R`
(`R >= axis`), returns a rank-`R+1` `RaggedTensor` `result` such that
`result[i0...iaxis]` is `[value[i0...iaxis] for value in values]`.

#### Example:

>     >>> t1 = tf.ragged.constant([[1, 2], [3, 4, 5]])
>     >>> t2 = tf.ragged.constant([[6], [7, 8, 9]])
>     >>> tf.ragged.stack([t1, t2], axis=0)
>     [[[1, 2], [3, 4, 5]], [[6], [7, 9, 0]]]
>     >>> tf.ragged.stack([t1, t2], axis=1)
>     [[[1, 2], [6]], [[3, 4, 5], [7, 8, 9]]]

#### Args:


* <b>`values`</b>: A list of <a href="../../tf/Tensor"><code>tf.Tensor</code></a> or <a href="../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a>.  May not be empty. All
  `values` must have the same rank and the same dtype; but unlike
  <a href="../../tf/stack"><code>tf.stack</code></a>, they can have arbitrary dimension sizes.
* <b>`axis`</b>: A python integer, indicating the dimension along which to stack.
  (Note: Unlike <a href="../../tf/stack"><code>tf.stack</code></a>, the `axis` parameter must be statically known.)
  Negative values are supported only if the rank of at least one
  `values` value is statically known.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A `RaggedTensor` with rank `R+1`.
`result.ragged_rank=1+max(axis, max(rt.ragged_rank for rt in values]))`.



#### Raises:


* <b>`ValueError`</b>: If `values` is empty, if `axis` is out of bounds or if
  the input tensors have different ranks.
