page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.image.draw_bounding_boxes

``` python
tf.image.draw_bounding_boxes(
    images,
    boxes,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_image_ops.py`.

See the guide: [Images > Working with Bounding Boxes](../../../../api_guides/python/image#Working_with_Bounding_Boxes)

Draw bounding boxes on a batch of images.

Outputs a copy of `images` but draws on top of the pixels zero or more bounding
boxes specified by the locations in `boxes`. The coordinates of the each
bounding box in `boxes` are encoded as `[y_min, x_min, y_max, x_max]`. The
bounding box coordinates are floats in `[0.0, 1.0]` relative to the width and
height of the underlying image.

For example, if an image is 100 x 200 pixels (height x width) and the bounding
box is `[0.1, 0.2, 0.5, 0.9]`, the upper-left and bottom-right coordinates of
the bounding box will be `(40, 10)` to `(180, 50)` (in (x,y) coordinates).

Parts of the bounding box may fall outside the image.

#### Args:

* <b>`images`</b>: A `Tensor`. Must be one of the following types: `float32`, `half`.
    4-D with shape `[batch, height, width, depth]`. A batch of images.
* <b>`boxes`</b>: A `Tensor` of type `float32`.
    3-D with shape `[batch, num_bounding_boxes, 4]` containing bounding
    boxes.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `images`.