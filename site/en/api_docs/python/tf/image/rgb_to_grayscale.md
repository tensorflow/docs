page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.rgb_to_grayscale

Converts one or more images from RGB to Grayscale.

### Aliases:

* `tf.compat.v1.image.rgb_to_grayscale`
* `tf.compat.v2.image.rgb_to_grayscale`
* `tf.image.rgb_to_grayscale`

``` python
tf.image.rgb_to_grayscale(
    images,
    name=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

Outputs a tensor of the same `DType` and rank as `images`.  The size of the
last dimension of the output is 1, containing the Grayscale value of the
pixels.

#### Args:


* <b>`images`</b>: The RGB tensor to convert. Last dimension must have size 3 and
  should contain RGB values.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The converted grayscale image(s).
