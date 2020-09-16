description: Returns the next representable value of x1 in the direction of x2, element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.nextafter" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.nextafter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Returns the next representable value of `x1` in the direction of `x2`, element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.nextafter`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.nextafter(
    x1, x2, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation returns the same result as the C++ std::nextafter function.

It can also return a subnormal number.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x1`
</td>
<td>
A `Tensor`. Must be one of the following types: `float64`, `float32`.
</td>
</tr><tr>
<td>
`x2`
</td>
<td>
A `Tensor`. Must have the same type as `x1`.
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
A `Tensor`. Has the same type as `x1`.
</td>
</tr>

</table>



#### Cpp Compatibility
Equivalent to C++ std::nextafter function.

