page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_saturation


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/random_saturation">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L2050-L2080">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adjust the saturation of RGB images by a random factor.

### Aliases:

* <a href="/api_docs/python/tf/image/random_saturation"><code>tf.compat.v1.image.random_saturation</code></a>
* <a href="/api_docs/python/tf/image/random_saturation"><code>tf.compat.v2.image.random_saturation</code></a>


``` python
tf.image.random_saturation(
    image,
    lower,
    upper,
    seed=None
)
```



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_saturation()` but uses a `saturation_factor` randomly
picked in the interval `[lower, upper]`.

#### Args:


* <b>`image`</b>: RGB image or images. Size of the last dimension must be 3.
* <b>`lower`</b>: float.  Lower bound for the random saturation factor.
* <b>`upper`</b>: float.  Upper bound for the random saturation factor.
* <b>`seed`</b>: An operation-specific seed. It will be used in conjunction with the
  graph-level seed to determine the real seeds that will be used in this
  operation. Please see the documentation of set_random_seed for its
  interaction with the graph-level random seed.


#### Returns:

Adjusted image(s), same shape and DType as `image`.



#### Raises:


* <b>`ValueError`</b>: if `upper <= lower` or if `lower < 0`.
