page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random_crop

``` python
tf.random_crop(
    value,
    size,
    seed=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/random_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/random_ops.py).

See the guide: [Constants, Sequences, and Random Values > Random Tensors](../../../api_guides/python/constant_op#Random_Tensors)

Randomly crops a tensor to a given size.

Slices a shape `size` portion out of `value` at a uniformly chosen offset.
Requires `value.shape >= size`.

If a dimension should not be cropped, pass the full size of that dimension.
For example, RGB images can be cropped with
`size = [crop_height, crop_width, 3]`.

#### Args:

* <b>`value`</b>: Input tensor to crop.
* <b>`size`</b>: 1-D tensor with size the rank of `value`.
* <b>`seed`</b>: Python integer. Used to create a random seed. See
    <a href="../tf/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A cropped tensor of the same rank as `value` and shape `size`.