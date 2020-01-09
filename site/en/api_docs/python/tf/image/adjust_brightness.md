page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_brightness


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L1579-L1621">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adjust the brightness of RGB or Grayscale images.

### Aliases:

* `tf.compat.v1.image.adjust_brightness`
* `tf.compat.v2.image.adjust_brightness`


``` python
tf.image.adjust_brightness(
    image,
    delta
)
```



<!-- Placeholder for "Used in" -->

This is a convenience method that converts RGB images to float
representation, adjusts their brightness, and then converts them back to the
original data type. If several adjustments are chained, it is advisable to
minimize the number of redundant conversions.

The value `delta` is added to all components of the tensor `image`. `image` is
converted to `float` and scaled appropriately if it is in fixed-point
representation, and `delta` is converted to the same data type. For regular
images, `delta` should be in the range `[0,1)`, as it is added to the image in
floating point representation, where pixel values are in the `[0,1)` range.

#### Args:


* <b>`image`</b>: RGB image or images to adjust.
* <b>`delta`</b>: A scalar. Amount to add to the pixel values.


#### Returns:

A brightness-adjusted tensor of the same shape and type as `image`.



#### Usage Example:

```python
import tensorflow as tf
x = tf.random.normal(shape=(256, 256, 3))
tf.image.adjust_brightness(x, delta=0.1)
```
