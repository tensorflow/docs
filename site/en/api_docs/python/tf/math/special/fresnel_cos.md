description: Computes Fresnel's cosine integral of x element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.special.fresnel_cos" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.special.fresnel_cos

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/special_math_ops.py#L165-L192">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes Fresnel's cosine integral of `x` element-wise.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.special.fresnel_cos`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.special.fresnel_cos(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The Fresnel cosine integral is defined as the integral of `cos(t^2)` from
`0` to `x`, with the domain of definition all real numbers.

The Fresnel cosine integral is odd.
>>> tf.math.special.fresnel_cos([-1., -0.1, 0.1, 1.]).numpy()
array([-0.7798934 , -0.09999753,  0.09999753,  0.7798934 ], dtype=float32)

This implementation is based off of the Cephes math library.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor` or `SparseTensor`. Must be one of the following types:
`float32`, `float64`.
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
A `Tensor` or `SparseTensor`, respectively. Has the same type as `x`.
</td>
</tr>

</table>




#### Scipy Compatibility
Equivalent to scipy.special.fresnel second output.

