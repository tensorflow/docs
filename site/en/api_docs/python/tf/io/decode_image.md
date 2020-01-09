page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_image


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/image_ops_impl.py#L2204-L2317">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Function for `decode_bmp`, `decode_gif`, `decode_jpeg`, and `decode_png`.

### Aliases:

* `tf.compat.v1.image.decode_image`
* `tf.compat.v1.io.decode_image`
* `tf.compat.v2.image.decode_image`
* `tf.compat.v2.io.decode_image`
* `tf.image.decode_image`


``` python
tf.io.decode_image(
    contents,
    channels=None,
    dtype=tf.dtypes.uint8,
    name=None,
    expand_animations=True
)
```



### Used in the tutorials:

* [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)



Detects whether an image is a BMP, GIF, JPEG, or PNG, and performs the
appropriate operation to convert the input bytes `string` into a `Tensor`
of type `dtype`.

Note: `decode_gif` returns a 4-D array `[num_frames, height, width, 3]`, as
opposed to `decode_bmp`, `decode_jpeg` and `decode_png`, which return 3-D
arrays `[height, width, num_channels]`. Make sure to take this into account
when constructing your graph if you are intermixing GIF files with BMP, JPEG,
and/or PNG files. Alternately, set the `expand_animations` argument of this
function to `False`, in which case the op will return 3-dimensional tensors
and will truncate animated GIF files to the first frame.

#### Args:


* <b>`contents`</b>: 0-D `string`. The encoded image bytes.
* <b>`channels`</b>: An optional `int`. Defaults to `0`. Number of color channels for
  the decoded image.
* <b>`dtype`</b>: The desired DType of the returned `Tensor`.
* <b>`name`</b>: A name for the operation (optional)
* <b>`expand_animations`</b>: Controls the shape of the returned op's output. If
  `True`, the returned op will produce a 3-D tensor for PNG, JPEG, and BMP
  files; and a 4-D tensor for all GIFs, whether animated or not. If,
  `False`, the returned op will produce a 3-D tensor for all file types and
  will truncate animated GIFs to the first frame.


#### Returns:

`Tensor` with type `dtype` and a 3- or 4-dimensional shape, depending on
the file type and the value of the `expand_animations` parameter.



#### Raises:


* <b>`ValueError`</b>: On incorrect number of channels.
