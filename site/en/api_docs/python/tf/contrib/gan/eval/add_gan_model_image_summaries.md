

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.eval.add_gan_model_image_summaries

### Aliases:

* `tf.contrib.gan.eval.add_gan_model_image_summaries`
* `tf.contrib.gan.eval.summaries.add_gan_model_image_summaries`

``` python
tf.contrib.gan.eval.add_gan_model_image_summaries(
    gan_model,
    grid_size=4
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/summaries_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/gan/python/eval/python/summaries_impl.py).

Adds image summaries for real and fake images.

#### Args:

* <b>`gan_model`</b>: A GANModel tuple.
* <b>`grid_size`</b>: The size of an image grid.


#### Raises:

* <b>`ValueError`</b>: If real and generated data aren't images.