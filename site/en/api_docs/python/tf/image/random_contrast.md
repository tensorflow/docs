page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_contrast


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L1548-L1576">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adjust the contrast of an image or images by a random factor.

### Aliases:

* `tf.compat.v1.image.random_contrast`
* `tf.compat.v2.image.random_contrast`


``` python
tf.image.random_contrast(
    image,
    lower,
    upper,
    seed=None
)
```



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_contrast()` but uses a `contrast_factor` randomly
picked in the interval `[lower, upper]`.

#### Args:


* <b>`image`</b>: An image tensor with 3 or more dimensions.
* <b>`lower`</b>: float.  Lower bound for the random contrast factor.
* <b>`upper`</b>: float.  Upper bound for the random contrast factor.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
  <a href="../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.


#### Returns:

The contrast-adjusted image(s).



#### Raises:


* <b>`ValueError`</b>: if `upper <= lower` or if `lower < 0`.
