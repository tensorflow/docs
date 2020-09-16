description: Bucketizes 'input' based on 'boundaries'.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.raw_ops.Bucketize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.raw_ops.Bucketize

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Bucketizes 'input' based on 'boundaries'.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Bucketize`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Bucketize(
    input, boundaries, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, if the inputs are
    boundaries = [0, 10, 100]
    input = [[-5, 10000]
             [150,   10]
             [5,    100]]

then the output will be
    output = [[0, 3]
              [3, 2]
              [1, 3]]

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input`
</td>
<td>
A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
Any shape of Tensor contains with int or float type.
</td>
</tr><tr>
<td>
`boundaries`
</td>
<td>
A list of `floats`.
A sorted list of floats gives the boundary of the buckets.
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
A `Tensor` of type `int32`.
</td>
</tr>

</table>

