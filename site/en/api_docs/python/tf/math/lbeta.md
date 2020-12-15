description: Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.lbeta" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.lbeta

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/special_math_ops.py#L50-L103">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes \\(ln(|Beta(x)|)\\), reducing along the last dimension.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lbeta`, `tf.compat.v1.math.lbeta`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.lbeta(
    x, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Given one-dimensional $z = [z_1,...,z_K]$, we define

$$Beta(z) = \frac{\prod_j \Gamma(z_j)}{\Gamma(\sum_j z_j)},$$

where $\Gamma$ is the gamma function.

And for $n + 1$ dimensional $x$ with shape $[N_1, ..., N_n, K]$, we define

$$lbeta(x)[i_1, ..., i_n] = \log{|Beta(x[i_1, ..., i_n, :])|}.$$

In other words, the last dimension is treated as the $z$ vector.

Note that if $z = [u, v]$, then

$$Beta(z) = \frac{\Gamma(u)\Gamma(v)}{\Gamma(u + v)}
  = \int_0^1 t^{u-1} (1 - t)^{v-1} \mathrm{d}t,$$

which defines the traditional bivariate beta function.

If the last dimension is empty, we follow the convention that the sum over
the empty set is zero, and the product is one.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A rank `n + 1` `Tensor`, `n >= 0` with type `float`, or `double`.
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
The logarithm of \\(|Beta(x)|\\) reducing along the last dimension.
</td>
</tr>

</table>

