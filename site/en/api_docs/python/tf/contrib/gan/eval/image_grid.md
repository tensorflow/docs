

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.image_grid

### Aliases:

* `tf.contrib.gan.eval.eval_utils.image_grid`
* `tf.contrib.gan.eval.image_grid`

``` python
tf.contrib.gan.eval.image_grid(
    input_tensor,
    grid_shape,
    image_shape=(32, 32),
    num_channels=3
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/eval_utils_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/gan/python/eval/python/eval_utils_impl.py).

Arrange a minibatch of images into a grid to form a single image.

#### Args:

* <b>`input_tensor`</b>: Tensor. Minibatch of images to format, either 4D
      ([batch size, height, width, num_channels]) or flattened
      ([batch size, height * width * num_channels]).
* <b>`grid_shape`</b>: Sequence of int. The shape of the image grid,
      formatted as [grid_height, grid_width].
* <b>`image_shape`</b>: Sequence of int. The shape of a single image,
      formatted as [image_height, image_width].
* <b>`num_channels`</b>: int. The number of channels in an image.


#### Returns:

Tensor representing a single image in which the input images have been
arranged into a grid.


#### Raises:

* <b>`ValueError`</b>: The grid shape and minibatch size don't match, or the image
      shape and number of channels are incompatible with the input tensor.