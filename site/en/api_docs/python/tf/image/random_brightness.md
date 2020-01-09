page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_brightness


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L1522-L1545">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adjust the brightness of images by a random factor.

### Aliases:

* `tf.compat.v1.image.random_brightness`
* `tf.compat.v2.image.random_brightness`


``` python
tf.image.random_brightness(
    image,
    max_delta,
    seed=None
)
```



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_brightness()` using a `delta` randomly picked in the
interval `[-max_delta, max_delta)`.

#### Args:


* <b>`image`</b>: An image or images to adjust.
* <b>`max_delta`</b>: float, must be non-negative.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
  <a href="../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.


#### Returns:

The brightness-adjusted image(s).



#### Raises:


* <b>`ValueError`</b>: if `max_delta` is negative.
