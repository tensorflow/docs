page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.add_gan_model_image_summaries

Adds image summaries for real and fake images.

### Aliases:

* `tf.contrib.gan.eval.add_gan_model_image_summaries`
* `tf.contrib.gan.eval.summaries.add_gan_model_image_summaries`

``` python
tf.contrib.gan.eval.add_gan_model_image_summaries(
    gan_model,
    grid_size=4,
    model_summaries=True
)
```



Defined in [`contrib/gan/python/eval/python/summaries_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/eval/python/summaries_impl.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`gan_model`</b>: A GANModel tuple.
* <b>`grid_size`</b>: The size of an image grid.
* <b>`model_summaries`</b>: Also add summaries of the model.


#### Raises:


* <b>`ValueError`</b>: If real and generated data aren't images.