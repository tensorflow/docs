description: Adjust the saturation of RGB images by a random factor.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.random_saturation" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.random_saturation

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/image_ops_impl.py#L2689-L2732">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adjust the saturation of RGB images by a random factor.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.image.random_saturation`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.image.random_saturation(
    image, lower, upper, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Equivalent to `adjust_saturation()` but uses a `saturation_factor` randomly
picked in the interval `[lower, upper)`.

#### Usage Example:



```
>>> x = [[[1.0, 2.0, 3.0],
...       [4.0, 5.0, 6.0]],
...     [[7.0, 8.0, 9.0],
...       [10.0, 11.0, 12.0]]]
>>> tf.image.random_saturation(x, 5, 10)
<tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
array([[[ 0. ,  1.5,  3. ],
        [ 0. ,  3. ,  6. ]],
       [[ 0. ,  4.5,  9. ],
        [ 0. ,  6. , 12. ]]], dtype=float32)>
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
RGB image or images. The size of the last dimension must be 3.
</td>
</tr><tr>
<td>
`lower`
</td>
<td>
float.  Lower bound for the random saturation factor.
</td>
</tr><tr>
<td>
`upper`
</td>
<td>
float.  Upper bound for the random saturation factor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
An operation-specific seed. It will be used in conjunction with the
graph-level seed to determine the real seeds that will be used in this
operation. Please see the documentation of set_random_seed for its
interaction with the graph-level random seed.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Adjusted image(s), same shape and DType as `image`.
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
if `upper <= lower` or if `lower < 0`.
</td>
</tr>
</table>

