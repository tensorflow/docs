page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.add_stargan_image_summaries

### Aliases:

* `tf.contrib.gan.eval.add_stargan_image_summaries`
* `tf.contrib.gan.eval.summaries.add_stargan_image_summaries`

``` python
tf.contrib.gan.eval.add_stargan_image_summaries(
    stargan_model,
    num_images=2,
    display_diffs=False
)
```



Defined in [`tensorflow/contrib/gan/python/eval/python/summaries_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/gan/python/eval/python/summaries_impl.py).

Adds image summaries to see StarGAN image results.

If display_diffs is True, each image result has `2` rows and `num_domains + 1`
columns.
The first row looks like:
  [original_image, transformed_to_domain_0, transformed_to_domain_1, ...]
The second row looks like:
  [no_modification_baseline, transformed_to_domain_0-original_image, ...]
If display_diffs is False, only the first row is shown.

IMPORTANT:
  Since the model originally does not transformed the image to every domains,
  we will transform them on-the-fly within this function in parallel.

#### Args:

* <b>`stargan_model`</b>: A StarGANModel tuple.
* <b>`num_images`</b>: The number of examples/images to be transformed and shown.
* <b>`display_diffs`</b>: Also display the difference between generated and target.


#### Raises:

* <b>`ValueError`</b>: If input_data is not images.
* <b>`ValueError`</b>: If input_data_domain_label is not rank 2.
* <b>`ValueError`</b>: If dimension 2 of input_data_domain_label is not fully defined.