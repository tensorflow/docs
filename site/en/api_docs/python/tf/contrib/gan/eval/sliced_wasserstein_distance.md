page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.eval.sliced_wasserstein_distance

Compute the Wasserstein distance between two distributions of images.

``` python
tf.contrib.gan.eval.sliced_wasserstein_distance(
    real_images,
    fake_images,
    resolution_min=16,
    patches_per_image=64,
    patch_size=7,
    random_sampling_count=1,
    random_projection_dim=(7 * 7 * 3),
    use_svd=False
)
```



Defined in [`contrib/gan/python/eval/python/sliced_wasserstein_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/gan/python/eval/python/sliced_wasserstein_impl.py).

<!-- Placeholder for "Used in" -->

Note that measure vary with the number of images. Use 8192 images to get
numbers comparable to the ones in the original paper.

#### Args:


* <b>`real_images`</b>: (tensor) Real images (batch, height, width, channels).
* <b>`fake_images`</b>: (tensor) Fake images (batch, height, width, channels).
* <b>`resolution_min`</b>: (int) Minimum resolution for the Laplacian pyramid.
* <b>`patches_per_image`</b>: (int) Number of patches to extract per image per
  Laplacian level.
* <b>`patch_size`</b>: (int) Width of a square patch.
* <b>`random_sampling_count`</b>: (int) Number of random projections to average.
* <b>`random_projection_dim`</b>: (int) Dimension of the random projection space.
* <b>`use_svd`</b>: experimental method to compute a more accurate distance.

#### Returns:

List of tuples (distance_real, distance_fake) for each level of the
Laplacian pyramid from the highest resolution to the lowest.
  distance_real is the Wasserstein distance between real images
  distance_fake is the Wasserstein distance between real and fake images.


#### Raises:


* <b>`ValueError`</b>: If the inputs shapes are incorrect. Input tensor dimensions
(batch, height, width, channels) are expected to be known at graph
construction time. In addition height and width must be the same and the
number of colors should be exactly 3. Real and fake images must have the
same size.