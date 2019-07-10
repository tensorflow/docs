page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sequence_mask

``` python
tf.sequence_mask(
    lengths,
    maxlen=None,
    dtype=tf.bool,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Returns a mask tensor representing the first N positions of each cell.

If `lengths` has shape `[d_1, d_2, ..., d_n]` the resulting tensor `mask` has
dtype `dtype` and shape `[d_1, d_2, ..., d_n, maxlen]`, with

```
mask[i_1, i_2, ..., i_n, j] = (j < lengths[i_1, i_2, ..., i_n])
```

Examples:

```python
tf.sequence_mask([1, 3, 2], 5)  # [[True, False, False, False, False],
                                #  [True, True, True, False, False],
                                #  [True, True, False, False, False]]

tf.sequence_mask([[1, 3],[2,0]])  # [[[True, False, False],
                                  #   [True, True, True]],
                                  #  [[True, True, False],
                                  #   [False, False, False]]]
```

#### Args:

* <b>`lengths`</b>: integer tensor, all its values <= maxlen.
* <b>`maxlen`</b>: scalar integer tensor, size of last dimension of returned tensor.
    Default is the maximum value in `lengths`.
* <b>`dtype`</b>: output type of the resulting tensor.
* <b>`name`</b>: name of the op.

#### Returns:

A mask tensor of shape `lengths.shape + (maxlen,)`, cast to specified dtype.

#### Raises:

* <b>`ValueError`</b>: if `maxlen` is not a scalar.