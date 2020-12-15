description: Outputs deterministic pseudorandom values from a uniform distribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.random.stateless_uniform" />
<meta itemprop="path" content="Stable" />
</div>

# tf.random.stateless_uniform

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/ops/stateless_random_ops.py#L116-L208">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Outputs deterministic pseudorandom values from a uniform distribution.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.random.stateless_uniform`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.random.stateless_uniform(
    shape, seed, minval=0, maxval=None, dtype=tf.dtypes.float32, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a stateless version of <a href="../../tf/random/uniform.md"><code>tf.random.uniform</code></a>: if run twice with the
same seeds and shapes, it will produce the same pseudorandom numbers.  The
output is consistent across multiple runs on the same hardware (and between
CPU and GPU), but may change between versions of TensorFlow or on non-CPU/GPU
hardware.

The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while
the upper bound `maxval` is excluded.

For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
be specified explicitly.

In the integer case, the random integers are slightly biased unless
`maxval - minval` is an exact power of two.  The bias is small for values of
`maxval - minval` significantly smaller than the range of the output (either
`2**32` or `2**64`).

For full-range (i.e. inclusive of both max and min) random integers, pass
`minval=None` and `maxval=None` with an integer `dtype`. For an integer dtype
either both `minval` and `maxval` must be `None` or neither may be `None`. For
example:
```python
ints = tf.random.stateless_uniform(
    [10], seed=(2, 3), minval=None, maxval=None, dtype=tf.int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`shape`
</td>
<td>
A 1-D integer Tensor or Python array. The shape of the output tensor.
</td>
</tr><tr>
<td>
`seed`
</td>
<td>
A shape [2] Tensor, the seed to the random number generator. Must have
dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
</td>
</tr><tr>
<td>
`minval`
</td>
<td>
A Tensor or Python value of type `dtype`, broadcastable with
`shape` (for integer types, broadcasting is not supported, so it needs to
be a scalar). The lower bound on the range of random values to
generate. Pass `None` for full-range integers.  Defaults to 0.
</td>
</tr><tr>
<td>
`maxval`
</td>
<td>
A Tensor or Python value of type `dtype`, broadcastable with
`shape` (for integer types, broadcasting is not supported, so it needs to
be a scalar). The upper bound on the range of random values to generate.
Defaults to 1 if `dtype` is floating point. Pass `None` for full-range
integers.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
The type of the output: `float16`, `float32`, `float64`, `int32`, or
`int64`. For unbounded uniform ints (`minval`, `maxval` both `None`),
`uint32` and `uint64` may be used.
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
A tensor of the specified shape filled with random uniform values.
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
If `dtype` is integral and only one of `minval` or `maxval` is
specified.
</td>
</tr>
</table>

