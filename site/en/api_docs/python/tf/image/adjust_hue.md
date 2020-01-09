page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_hue


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L1913-L1954">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adjust hue of RGB images.

### Aliases:

* `tf.compat.v1.image.adjust_hue`
* `tf.compat.v2.image.adjust_hue`


``` python
tf.image.adjust_hue(
    image,
    delta,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This is a convenience method that converts an RGB image to float
representation, converts it to HSV, add an offset to the hue channel, converts
back to RGB and then back to the original data type. If several adjustments
are chained it is advisable to minimize the number of redundant conversions.

`image` is an RGB image.  The image hue is adjusted by converting the
image(s) to HSV and rotating the hue channel (H) by
`delta`.  The image is then converted back to RGB.

`delta` must be in the interval `[-1, 1]`.

#### Args:


* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`delta`</b>: float.  How much to add to the hue channel.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

Adjusted image(s), same shape and DType as `image`.



#### Usage Example:

```python
>> import tensorflow as tf
>> x = tf.random.normal(shape=(256, 256, 3))
>> tf.image.adjust_hue(x, 0.2)
```
