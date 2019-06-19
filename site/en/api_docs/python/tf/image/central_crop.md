page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.central_crop

``` python
tf.image.central_crop(
    image,
    central_fraction
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Cropping](../../../../api_guides/python/image#Cropping)

Crop the central region of the image(s).

Remove the outer parts of an image but retain the central region of the image
along each dimension. If we specify central_fraction = 0.5, this function
returns the region marked with "X" in the below diagram.

     --------
    |        |
    |  XXXX  |
    |  XXXX  |
    |        |   where "X" is the central 50% of the image.
     --------

This function works on either a single image (`image` is a 3-D Tensor), or a
batch of images (`image` is a 4-D Tensor).

#### Args:

* <b>`image`</b>: Either a 3-D float Tensor of shape [height, width, depth], or a 4-D
    Tensor of shape [batch_size, height, width, depth].
* <b>`central_fraction`</b>: float (0, 1], fraction of size to crop


#### Raises:

* <b>`ValueError`</b>: if central_crop_fraction is not within (0, 1].


#### Returns:

3-D / 4-D float Tensor, as per the input.