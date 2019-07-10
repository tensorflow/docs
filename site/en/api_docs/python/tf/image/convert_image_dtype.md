page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.convert_image_dtype

Convert `image` to `dtype`, scaling its values if needed.

### Aliases:

* `tf.compat.v1.image.convert_image_dtype`
* `tf.compat.v2.image.convert_image_dtype`
* `tf.image.convert_image_dtype`

``` python
tf.image.convert_image_dtype(
    image,
    dtype,
    saturate=False,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Images that are represented using floating point values are expected to have
values in the range [0,1). Image data stored in integer data types are
expected to have values in the range `[0,MAX]`, where `MAX` is the largest
positive representable number for the data type.

This op converts between data types, scaling the values appropriately before
casting.

Note that converting from floating point inputs to integer types may lead to
over/underflow problems. Set saturate to `True` to avoid such problem in
problematic conversions. If enabled, saturation will clip the output into the
allowed range before performing a potentially dangerous cast (and only before
performing such a cast, i.e., when casting from a floating point to an integer
type, and when casting from a signed to an unsigned type; `saturate` has no
effect on casts between floats, or on casts that increase the type's range).

#### Args:


* <b>`image`</b>: An image.
* <b>`dtype`</b>: A `DType` to convert `image` to.
* <b>`saturate`</b>: If `True`, clip the input before casting (if necessary).
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

`image`, converted to `dtype`.
