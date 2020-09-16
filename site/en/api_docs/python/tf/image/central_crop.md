description: Crop the central region of the image(s).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.central_crop" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.central_crop

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/image_ops_impl.py#L718-L847">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Crop the central region of the image(s).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.central_crop`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.central_crop(
    image, central_fraction
)
</code></pre>



<!-- Placeholder for "Used in" -->

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

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0],
...       [7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]],
...     [[13.0, 14.0, 15.0],
...       [16.0, 17.0, 18.0],
...       [19.0, 20.0, 21.0],
...       [22.0, 23.0, 24.0]],
...     [[25.0, 26.0, 27.0],
...       [28.0, 29.0, 30.0],
...       [31.0, 32.0, 33.0],
...       [34.0, 35.0, 36.0]],
...     [[37.0, 38.0, 39.0],
...       [40.0, 41.0, 42.0],
...       [43.0, 44.0, 45.0],
...       [46.0, 47.0, 48.0]]]
>>> tf.image.central_crop(x, 0.5)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[16., 17., 18.],
        [19., 20., 21.]],
       [[28., 29., 30.],
        [31., 32., 33.]]], dtype=float32)>
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`image`
</td>
<td>
Either a 3-D float Tensor of shape [height, width, depth], or a 4-D
Tensor of shape [batch_size, height, width, depth].
</td>
</tr><tr>
<td>
`central_fraction`
</td>
<td>
float (0, 1], fraction of size to crop
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if central_crop_fraction is not within (0, 1].
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
3-D / 4-D float Tensor, as per the input.
</td>
</tr>

</table>

