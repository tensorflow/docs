page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.extract_glimpse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/image/extract_glimpse">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/image_ops_impl.py#L3711-L3787">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Extracts a glimpse from the input tensor.

### Aliases:

* <a href="/api_docs/python/tf/image/extract_glimpse"><code>tf.compat.v1.image.extract_glimpse</code></a>


``` python
tf.image.extract_glimpse(
    input,
    size,
    offsets,
    centered=True,
    normalized=True,
    uniform_noise=True,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Returns a set of windows called glimpses extracted at location
`offsets` from the input tensor. If the windows only partially
overlaps the inputs, the non overlapping areas will be filled with
random noise.

The result is a 4-D tensor of shape `[batch_size, glimpse_height,
glimpse_width, channels]`. The channels and batch dimensions are the
same as that of the input tensor. The height and width of the output
windows are specified in the `size` parameter.

The argument `normalized` and `centered` controls how the windows are built:

* If the coordinates are normalized but not centered, 0.0 and 1.0
  correspond to the minimum and maximum of each height and width
  dimension.
* If the coordinates are both normalized and centered, they range from
  -1.0 to 1.0. The coordinates (-1.0, -1.0) correspond to the upper
  left corner, the lower right corner is located at (1.0, 1.0) and the
  center is at (0, 0).
* If the coordinates are not normalized they are interpreted as
  numbers of pixels.

#### Args:


* <b>`input`</b>: A `Tensor` of type `float32`. A 4-D float tensor of shape
  `[batch_size, height, width, channels]`.
* <b>`size`</b>: A `Tensor` of type `int32`. A 1-D tensor of 2 elements containing the
  size of the glimpses to extract.  The glimpse height must be specified
  first, following by the glimpse width.
* <b>`offsets`</b>: A `Tensor` of type `float32`. A 2-D integer tensor of shape
  `[batch_size, 2]` containing the y, x locations of the center of each
  window.
* <b>`centered`</b>: An optional `bool`. Defaults to `True`. indicates if the offset
  coordinates are centered relative to the image, in which case the (0, 0)
  offset is relative to the center of the input images. If false, the (0,0)
  offset corresponds to the upper left corner of the input images.
* <b>`normalized`</b>: An optional `bool`. Defaults to `True`. indicates if the offset
  coordinates are normalized.
* <b>`uniform_noise`</b>: An optional `bool`. Defaults to `True`. indicates if the
  noise should be generated using a uniform distribution or a Gaussian
  distribution.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `float32`.



#### Usage Example:

```python
BATCH_SIZE = 1
IMAGE_HEIGHT = 3
IMAGE_WIDTH = 3
CHANNELS = 1
GLIMPSE_SIZE = (2, 2)
image = tf.reshape(tf.range(9, delta=1, dtype=tf.float32),
  shape=(BATCH_SIZE, IMAGE_HEIGHT, IMAGE_WIDTH, CHANNELS))
output = tf.image.extract_glimpse(image, size=GLIMPSE_SIZE,
  offsets=[[1, 1]], centered=False, normalized=False)
 ```
