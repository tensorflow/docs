description: Computes the SiLU or Swish activation function: x * sigmoid(x).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nn.silu" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nn.silu

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_impl.py#L512-L551">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes the SiLU or Swish activation function: `x * sigmoid(x)`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.nn.swish`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nn.silu`, `tf.compat.v1.nn.swish`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nn.silu(
    features
)
</code></pre>



<!-- Placeholder for "Used in" -->

The SiLU activation function was introduced in "Gaussian Error Linear Units
(GELUs)" [Hendrycks et al. 2016](https://arxiv.org/abs/1606.08415) and
"Sigmoid-Weighted Linear Units for Neural Network Function Approximation in
Reinforcement Learning"
[Elfwing et al. 2017](https://arxiv.org/abs/1702.03118) and was independently
discovered (and called swish) in "Searching for Activation Functions"
[Ramachandran et al. 2017](https://arxiv.org/abs/1710.05941)

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`features`
</td>
<td>
A `Tensor` representing preactivation values.
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
The activation value.
</td>
</tr>

</table>

