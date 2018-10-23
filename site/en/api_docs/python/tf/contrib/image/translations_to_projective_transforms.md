

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.image.translations_to_projective_transforms

``` python
tf.contrib.image.translations_to_projective_transforms(
    translations,
    name=None
)
```



Defined in [`tensorflow/contrib/image/python/ops/image_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/image/python/ops/image_ops.py).

Returns projective transform(s) for the given translation(s).

#### Args:

* <b>`translations`</b>: A 2-element list representing [dx, dy] or a matrix of
        2-element lists representing [dx, dy] to translate for each image
        (for a batch of images). The rank must be statically known (the shape
        is not `TensorShape(None)`.
* <b>`name`</b>: The name of the op.


#### Returns:

A tensor of shape (num_images, 8) projective transforms which can be given
    to <a href="../../../tf/contrib/image/transform"><code>tf.contrib.image.transform</code></a>.