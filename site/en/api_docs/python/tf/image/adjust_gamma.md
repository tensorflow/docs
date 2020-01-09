page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.adjust_gamma


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L1674-L1725">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Performs Gamma Correction on the input image.

### Aliases:

* `tf.compat.v1.image.adjust_gamma`
* `tf.compat.v2.image.adjust_gamma`


``` python
tf.image.adjust_gamma(
    image,
    gamma=1,
    gain=1
)
```



<!-- Placeholder for "Used in" -->

Also known as Power Law Transform. This function converts the
input images at first to float representation, then transforms them
pixelwise according to the equation `Out = gain * In**gamma`,
and then converts the back to the original data type.

#### Args:


* <b>`image`</b>: RGB image or images to adjust.
* <b>`gamma`</b>: A scalar or tensor. Non negative real number.
* <b>`gain`</b>: A scalar or tensor. The constant multiplier.


#### Returns:

A Tensor. A Gamma-adjusted tensor of the same shape and type as `image`.


#### Usage Example:

```python
>> import tensorflow as tf
>> x = tf.random.normal(shape=(256, 256, 3))
>> tf.image.adjust_gamma(x, 0.2)
```


#### Raises:


* <b>`ValueError`</b>: If gamma is negative.

#### Notes:

For gamma greater than 1, the histogram will shift towards left and
the output image will be darker than the input image.
For gamma less than 1, the histogram will shift towards right and
the output image will be brighter than the input image.


#### References:

[1] http://en.wikipedia.org/wiki/Gamma_correction
