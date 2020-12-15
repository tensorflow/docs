description: Creates a grad-pass-through op with the forward behavior provided in f.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.grad_pass_through" />
<meta itemprop="path" content="Stable" />
</div>

# tf.grad_pass_through

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/custom_gradient.py#L561-L611">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Creates a grad-pass-through op with the forward behavior provided in f.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.grad_pass_through`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.grad_pass_through(
    f
)
</code></pre>



<!-- Placeholder for "Used in" -->

Use this function to wrap any op, maintaining its behavior in the forward
pass, but replacing the original op in the backward graph with an identity.
For example:

```python
x = tf.Variable(1.0, name="x")
z = tf.Variable(3.0, name="z")

with tf.GradientTape() as tape:
  # y will evaluate to 9.0
  y = tf.grad_pass_through(x.assign)(z**2)
# grads will evaluate to 6.0
grads = tape.gradient(y, z)
```

Another example is a 'differentiable' moving average approximation, where
gradients are allowed to flow into the last value fed to the moving average,
but the moving average is still used for the forward pass:

```python
x = ... # Some scalar value
# A moving average object, we don't need to know how this is implemented
moving_average = MovingAverage()
with backprop.GradientTape() as tape:
  # mavg_x will evaluate to the current running average value
  mavg_x = tf.grad_pass_through(moving_average)(x)
grads = tape.gradient(mavg_x, x) # grads will evaluate to 1.0
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`f`
</td>
<td>
function `f(*x)` that returns a `Tensor` or nested structure of `Tensor`
outputs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A function `h(x)` which returns the same values as `f(x)` and whose
gradients are the same as those of an identity function.
</td>
</tr>

</table>

