

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.sequence_mask

### `tf.sequence_mask`

``` python
sequence_mask(
    lengths,
    maxlen=None,
    dtype=tf.bool,
    name=None
)
```



Defined in [`tensorflow/python/ops/array_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/array_ops.py).

See the guide: [Tensor Transformations > Slicing and Joining](../../../api_guides/python/array_ops#Slicing_and_Joining)

Return a mask tensor representing the first N positions of each row.

Example:

```python
tf.sequence_mask([1, 3, 2], 5) =
  [[True, False, False, False, False],
   [True, True, True, False, False],
   [True, True, False, False, False]]
```

#### Args:

* <b>`lengths`</b>: 1D integer tensor, all its values < maxlen.
* <b>`maxlen`</b>: scalar integer tensor, maximum length of each row. Default: use
          maximum over lengths.
* <b>`dtype`</b>: output type of the resulting tensor.
* <b>`name`</b>: name of the op.
Returns:
  A 2D mask tensor, as shown in the example above, cast to specified dtype.


#### Raises:

* <b>`ValueError`</b>: if the arguments have invalid rank.