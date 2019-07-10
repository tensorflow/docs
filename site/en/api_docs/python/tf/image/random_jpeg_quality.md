page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_jpeg_quality

Randomly changes jpeg encoding quality for inducing jpeg noise.

### Aliases:

* `tf.compat.v1.image.random_jpeg_quality`
* `tf.compat.v2.image.random_jpeg_quality`
* `tf.image.random_jpeg_quality`

``` python
tf.image.random_jpeg_quality(
    image,
    min_jpeg_quality,
    max_jpeg_quality,
    seed=None
)
```



Defined in [`python/ops/image_ops_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/image_ops_impl.py).

<!-- Placeholder for "Used in" -->

`min_jpeg_quality` must be in the interval `[0, 100]` and less than
`max_jpeg_quality`.
`max_jpeg_quality` must be in the interval `[0, 100]`.

#### Args:


* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`min_jpeg_quality`</b>: Minimum jpeg encoding quality to use.
* <b>`max_jpeg_quality`</b>: Maximum jpeg encoding quality to use.
* <b>`seed`</b>: An operation-specific seed. It will be used in conjunction with the
  graph-level seed to determine the real seeds that will be used in this
  operation. Please see the documentation of set_random_seed for its
  interaction with the graph-level random seed.


#### Returns:

Adjusted image(s), same shape and DType as `image`.



#### Raises:


* <b>`ValueError`</b>: if `min_jpeg_quality` or `max_jpeg_quality` is invalid.