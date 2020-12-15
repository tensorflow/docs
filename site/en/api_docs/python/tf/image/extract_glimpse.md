description: Extracts a glimpse from the input tensor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.extract_glimpse" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.extract_glimpse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L4688-L4772">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Extracts a glimpse from the input tensor.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.extract_glimpse(
    input, size, offsets, centered=(True), normalized=(True), noise='uniform',
    name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Returns a set of windows called glimpses extracted at location
`offsets` from the input tensor. If the windows only partially
overlaps the inputs, the non-overlapping areas will be filled with
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

#### Usage Example:



```
>>> x = [[[[0.0],
...           [1.0],
...           [2.0]],
...          [[3.0],
...           [4.0],
...           [5.0]],
...          [[6.0],
...           [7.0],
...           [8.0]]]]
>>> tf.image.extract_glimpse(x, size=(2, 2), offsets=[[1, 1]],
...                         centered=False, normalized=False)
<tf.Tensor: shape=(1, 2, 2, 1), dtype=float32, numpy=
array([[[[4.],
         [5.]],
        [[7.],
         [8.]]]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor` of type `float32`. A 4-D float tensor of shape
`[batch_size, height, width, channels]`.
</td>
</tr><tr>
<td>
`size`
</td>
<td>
A `Tensor` of type `int32`. A 1-D tensor of 2 elements containing the
size of the glimpses to extract.  The glimpse height must be specified
first, following by the glimpse width.
</td>
</tr><tr>
<td>
`offsets`
</td>
<td>
A `Tensor` of type `float32`. A 2-D integer tensor of shape
`[batch_size, 2]` containing the y, x locations of the center of each
window.
</td>
</tr><tr>
<td>
`centered`
</td>
<td>
An optional `bool`. Defaults to `True`. indicates if the offset
coordinates are centered relative to the image, in which case the (0, 0)
offset is relative to the center of the input images. If false, the (0,0)
offset corresponds to the upper left corner of the input images.
</td>
</tr><tr>
<td>
`normalized`
</td>
<td>
An optional `bool`. Defaults to `True`. indicates if the offset
coordinates are normalized.
</td>
</tr><tr>
<td>
`noise`
</td>
<td>
An optional `string`. Defaults to `uniform`. indicates if the noise
should be `uniform` (uniform distribution), `gaussian` (gaussian
distribution), or `zero` (zero padding).
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
A `Tensor` of type `float32`.
</td>
</tr>

</table>

