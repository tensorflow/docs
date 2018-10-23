

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.image.grayscale_to_rgb

### `tf.image.grayscale_to_rgb`

``` python
grayscale_to_rgb(
    images,
    name=None
)
```



Defined in [`tensorflow/python/ops/image_ops_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/image_ops_impl.py).

See the guide: [Images > Converting Between Colorspaces](../../../../api_guides/python/image#Converting_Between_Colorspaces)

Converts one or more images from Grayscale to RGB.

Outputs a tensor of the same `DType` and rank as `images`.  The size of the
last dimension of the output is 3, containing the RGB value of the pixels.

#### Args:

* <b>`images`</b>: The Grayscale tensor to convert. Last dimension must be size 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  The converted grayscale image(s).