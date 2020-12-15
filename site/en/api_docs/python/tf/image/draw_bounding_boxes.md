description: Draw bounding boxes on a batch of images.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.draw_bounding_boxes" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.draw_bounding_boxes

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L5424-L5476">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Draw bounding boxes on a batch of images.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.draw_bounding_boxes(
    images, boxes, colors, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Outputs a copy of `images` but draws on top of the pixels zero or more
bounding boxes specified by the locations in `boxes`. The coordinates of the
each bounding box in `boxes` are encoded as `[y_min, x_min, y_max, x_max]`.
The bounding box coordinates are floats in `[0.0, 1.0]` relative to the width
and the height of the underlying image.

For example, if an image is 100 x 200 pixels (height x width) and the bounding
box is `[0.1, 0.2, 0.5, 0.9]`, the upper-left and bottom-right coordinates of
the bounding box will be `(40, 10)` to `(180, 50)` (in (x,y) coordinates).

Parts of the bounding box may fall outside the image.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`images`
</td>
<td>
A `Tensor`. Must be one of the following types: `float32`, `half`.
4-D with shape `[batch, height, width, depth]`. A batch of images.
</td>
</tr><tr>
<td>
`boxes`
</td>
<td>
A `Tensor` of type `float32`. 3-D with shape `[batch,
num_bounding_boxes, 4]` containing bounding boxes.
</td>
</tr><tr>
<td>
`colors`
</td>
<td>
A `Tensor` of type `float32`. 2-D. A list of RGBA colors to cycle
through for the boxes.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor`. Has the same type as `images`.
</td>
</tr>

</table>



#### Usage Example:



```
>>> # create an empty image
>>> img = tf.zeros([1, 3, 3, 3])
>>> # draw a box around the image
>>> box = np.array([0, 0, 1, 1])
>>> boxes = box.reshape([1, 1, 4])
>>> # alternate between red and blue
>>> colors = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
>>> tf.image.draw_bounding_boxes(img, boxes, colors)
<tf.Tensor: shape=(1, 3, 3, 3), dtype=float32, numpy=
array([[[[1., 0., 0.],
        [1., 0., 0.],
        [1., 0., 0.]],
        [[1., 0., 0.],
        [0., 0., 0.],
        [1., 0., 0.]],
        [[1., 0., 0.],
        [1., 0., 0.],
        [1., 0., 0.]]]], dtype=float32)>
```