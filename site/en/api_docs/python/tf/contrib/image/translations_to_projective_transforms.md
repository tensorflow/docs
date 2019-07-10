page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.translations_to_projective_transforms

Returns projective transform(s) for the given translation(s).

``` python
tf.contrib.image.translations_to_projective_transforms(
    translations,
    name=None
)
```



Defined in [`contrib/image/python/ops/image_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/image/python/ops/image_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`translations`</b>: A 2-element list representing [dx, dy] or a matrix of
    2-element lists representing [dx, dy] to translate for each image
    (for a batch of images). The rank must be statically known (the shape
    is not `TensorShape(None)`.
* <b>`name`</b>: The name of the op.


#### Returns:

A tensor of shape (num_images, 8) projective transforms which can be given
    to <a href="../../../tf/contrib/image/transform"><code>tf.contrib.image.transform</code></a>.
