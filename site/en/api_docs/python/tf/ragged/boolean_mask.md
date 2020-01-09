page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.boolean_mask


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/ragged/boolean_mask">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_array_ops.py#L41-L202">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Applies a boolean mask to `data` without flattening the mask dimensions.

### Aliases:

* <a href="/api_docs/python/tf/ragged/boolean_mask"><code>tf.compat.v1.ragged.boolean_mask</code></a>
* <a href="/api_docs/python/tf/ragged/boolean_mask"><code>tf.compat.v2.ragged.boolean_mask</code></a>


``` python
tf.ragged.boolean_mask(
    data,
    mask,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Returns a potentially ragged tensor that is formed by retaining the elements
in `data` where the corresponding value in `mask` is `True`.

* `output[a1...aA, i, b1...bB] = data[a1...aA, j, b1...bB]`

   Where `j` is the `i`th `True` entry of `mask[a1...aA]`.

Note that `output` preserves the mask dimensions `a1...aA`; this differs
from <a href="../../tf/boolean_mask"><code>tf.boolean_mask</code></a>, which flattens those dimensions.

#### Args:


* <b>`data`</b>: A potentially ragged tensor.
* <b>`mask`</b>: A potentially ragged boolean tensor.  `mask`'s shape must be a prefix
  of `data`'s shape.  `rank(mask)` must be known statically.
* <b>`name`</b>: A name prefix for the returned tensor (optional).


#### Returns:

A potentially ragged tensor that is formed by retaining the elements in
`data` where the corresponding value in `mask` is `True`.

* `rank(output) = rank(data)`.
* `output.ragged_rank = max(data.ragged_rank, rank(mask) - 1)`.



#### Raises:


* <b>`ValueError`</b>: if `rank(mask)` is not known statically; or if `mask.shape` is
  not a prefix of `data.shape`.

#### Examples:

>     >>> # Aliases for True & False so data and mask line up.
>     >>> T, F = (True, False)
>     
  >>> tf.ragged.boolean_mask(  # Mask a 2D Tensor.
  ...     data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  ...     mask=[[T, F, T], [F, F, F], [T, F, F]]).tolist()
  [[1, 3], [], [7]]

>     
  >>> tf.ragged.boolean_mask(  # Mask a 2D RaggedTensor.
  ...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
  ...     tf.ragged.constant([[F, F, T], [F], [T, T]])).tolist()
  [[3], [], [5, 6]]

>     
>     >>> tf.ragged.boolean_mask(  # Mask rows of a 2D RaggedTensor.
>     ...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
>     ...     tf.ragged.constant([True, False, True])).tolist()
>     [[1, 2, 3], [5, 6]]
