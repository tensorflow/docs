page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.extract_volume_patches

``` python
tf.extract_volume_patches(
    input,
    ksizes,
    strides,
    padding,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_array_ops.py`.

Extract `patches` from `input` and put them in the "depth" output dimension. 3D extension of `extract_image_patches`.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    5-D Tensor with shape `[batch, in_planes, in_rows, in_cols, depth]`.
* <b>`ksizes`</b>: A list of `ints` that has length `>= 5`.
    The size of the sliding window for each dimension of `input`.
* <b>`strides`</b>: A list of `ints` that has length `>= 5`.
    1-D of length 5. How far the centers of two consecutive patches are in
    `input`. Must be: `[1, stride_planes, stride_rows, stride_cols, 1]`.
* <b>`padding`</b>: A `string` from: `"SAME", "VALID"`.
    The type of padding algorithm to use.

    We specify the size-related attributes as:

    ```python
          ksizes = [1, ksize_planes, ksize_rows, ksize_cols, 1]
          strides = [1, stride_planes, strides_rows, strides_cols, 1]
    ```
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.