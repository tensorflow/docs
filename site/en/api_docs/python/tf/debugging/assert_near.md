description: Assert the condition x and y are close element-wise.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.debugging.assert_near" />
<meta itemprop="path" content="Stable" />
</div>

# tf.debugging.assert_near

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/check_ops.py#L723-L774">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Assert the condition `x` and `y` are close element-wise.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.debugging.assert_near(
    x, y, rtol=None, atol=None, message=None, summarize=None, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This Op checks that `x[i] - y[i] < atol + rtol * tf.abs(y[i])` holds for every
pair of (possibly broadcast) elements of `x` and `y`. If both `x` and `y` are
empty, this is trivially satisfied.

If any elements of `x` and `y` are not close, `message`, as well as the first
`summarize` entries of `x` and `y` are printed, and `InvalidArgumentError`
is raised.

The default `atol` and `rtol` is `10 * eps`, where `eps` is the smallest
representable positive number such that `1 + eps != 1`.  This is about
`1.2e-6` in `32bit`, `2.22e-15` in `64bit`, and `0.00977` in `16bit`.
See `numpy.finfo`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`x`
</td>
<td>
Float or complex `Tensor`.
</td>
</tr><tr>
<td>
`y`
</td>
<td>
Float or complex `Tensor`, same dtype as and broadcastable to `x`.
</td>
</tr><tr>
<td>
`rtol`
</td>
<td>
`Tensor`.  Same `dtype` as, and broadcastable to, `x`.
The relative tolerance.  Default is `10 * eps`.
</td>
</tr><tr>
<td>
`atol`
</td>
<td>
`Tensor`.  Same `dtype` as, and broadcastable to, `x`.
The absolute tolerance.  Default is `10 * eps`.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
A string to prefix to the default message.
</td>
</tr><tr>
<td>
`summarize`
</td>
<td>
Print this many entries of each tensor.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).  Defaults to "assert_near".
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Op that raises `InvalidArgumentError` if `x` and `y` are not close enough.
This can be used with <a href="../../tf/control_dependencies.md"><code>tf.control_dependencies</code></a> inside of <a href="../../tf/function.md"><code>tf.function</code></a>s
to block followup computation until the check has executed.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`InvalidArgumentError`
</td>
<td>
if the check can be performed immediately and
`x != y` is False for any pair of elements in `x` and `y`. The check can
be performed immediately during eager execution or if `x` and `y` are
statically known.
</td>
</tr>
</table>




#### Eager Compatibility
returns None



#### Numpy Compatibility
Similar to `numpy.testing.assert_allclose`, except tolerance depends on data
type. This is due to the fact that `TensorFlow` is often used with `32bit`,
`64bit`, and even `16bit` data.

