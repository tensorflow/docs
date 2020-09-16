description: Compute the cumulative log-sum-exp of the tensor x along axis.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.math.cumulative_logsumexp" />
<meta itemprop="path" content="Stable" />
</div>

# tf.math.cumulative_logsumexp

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/math_ops.py#L3624-L3676">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Compute the cumulative log-sum-exp of the tensor `x` along `axis`.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.math.cumulative_logsumexp`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.math.cumulative_logsumexp(
    x, axis=0, exclusive=(False), reverse=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

By default, this op performs an inclusive cumulative log-sum-exp, which means
that the first element of the input is identical to the first element of
the output.

This operation is significantly more numerically stable than the equivalent
tensorflow operation `tf.math.log(tf.math.cumsum(tf.math.exp(x)))`, although
computes the same result given infinite numerical precision. However, note
that in some cases, it may be less stable than <a href="../../tf/math/reduce_logsumexp.md"><code>tf.math.reduce_logsumexp</code></a>
for a given element, as it applies the "log-sum-exp trick" in a different
way.

More precisely, where <a href="../../tf/math/reduce_logsumexp.md"><code>tf.math.reduce_logsumexp</code></a> uses the following trick:

```
log(sum(exp(x))) == log(sum(exp(x - max(x)))) + max(x)
```

it cannot be directly used here as there is no fast way of applying it
to each prefix `x[:i]`. Instead, this function implements a prefix
scan using pairwise log-add-exp, which is a commutative and associative
(up to floating point precision) operator:

```
log_add_exp(x, y) = log(exp(x) + exp(y))
                  = log(1 + exp(min(x, y) - max(x, y))) + max(x, y)
```

However, reducing using the above operator leads to a different computation
tree (logs are taken repeatedly instead of only at the end), and the maximum
is only computed pairwise instead of over the entire prefix. In general, this
leads to a different and slightly less precise computation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
A `Tensor`. Must be one of the following types: `float16`, `float32`,
`float64`.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
A `Tensor` of type `int32` or `int64` (default: 0). Must be in the
range `[-rank(x), rank(x))`.
</td>
</tr><tr>
<td>
`exclusive`
</td>
<td>
If `True`, perform exclusive cumulative log-sum-exp.
</td>
</tr><tr>
<td>
`reverse`
</td>
<td>
If `True`, performs the cumulative log-sum-exp in the reverse
direction.
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
A `Tensor`. Has the same shape and type as `x`.
</td>
</tr>

</table>

