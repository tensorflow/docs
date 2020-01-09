page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.random_flip_left_right


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L344-L363">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Randomly flip an image horizontally (left to right).

### Aliases:

* `tf.compat.v1.image.random_flip_left_right`
* `tf.compat.v2.image.random_flip_left_right`


``` python
tf.image.random_flip_left_right(
    image,
    seed=None
)
```



### Used in the tutorials:

* [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)



With a 1 in 2 chance, outputs the contents of `image` flipped along the
second dimension, which is `width`.  Otherwise output the image as-is.

#### Args:


* <b>`image`</b>: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
  of shape `[height, width, channels]`.
* <b>`seed`</b>: A Python integer. Used to create a random seed. See
  <a href="../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.


#### Returns:

A tensor of the same type and shape as `image`.



#### Raises:


* <b>`ValueError`</b>: if the shape of `image` not supported.
