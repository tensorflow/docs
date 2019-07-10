page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.add_image_comparison_summaries

Adds image summaries to compare triplets of images.

### Aliases:

* `tf.contrib.gan.eval.add_image_comparison_summaries`
* `tf.contrib.gan.eval.summaries.add_image_comparison_summaries`

``` python
tf.contrib.gan.eval.add_image_comparison_summaries(
    gan_model,
    num_comparisons=2,
    display_diffs=False
)
```



Defined in [`contrib/gan/python/eval/python/summaries_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/eval/python/summaries_impl.py).

<!-- Placeholder for "Used in" -->

The first image is the generator input, the second is the generator output,
and the third is the real data. This style of comparison is useful for
image translation problems, where the generator input is a corrupted image,
the generator output is the reconstruction, and the real data is the target.

#### Args:


* <b>`gan_model`</b>: A GANModel tuple.
* <b>`num_comparisons`</b>: The number of image triplets to display.
* <b>`display_diffs`</b>: Also display the difference between generated and target.


#### Raises:


* <b>`ValueError`</b>: If real data, generated data, and generator inputs aren't
  images.
* <b>`ValueError`</b>: If the generator input, real, and generated data aren't all the
  same size.