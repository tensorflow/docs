description: A decorator for registering the gradient function for an op type.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.RegisterGradient" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.RegisterGradient

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2602-L2646">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A decorator for registering the gradient function for an op type.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.RegisterGradient`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.RegisterGradient(
    op_type
)
</code></pre>



<!-- Placeholder for "Used in" -->

This decorator is only used when defining a new op type. For an op
with `m` inputs and `n` outputs, the gradient function is a function
that takes the original `Operation` and `n` `Tensor` objects
(representing the gradients with respect to each output of the op),
and returns `m` `Tensor` objects (representing the partial gradients
with respect to each input of the op).

For example, assuming that operations of type `"Sub"` take two
inputs `x` and `y`, and return a single output `x - y`, the
following gradient function would be registered:

```python
@tf.RegisterGradient("Sub")
def _sub_grad(unused_op, grad):
  return grad, tf.negative(grad)
```

The decorator argument `op_type` is the string type of an
operation. This corresponds to the `OpDef.name` field for the proto
that defines the operation.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`op_type`
</td>
<td>
The string type of an operation. This corresponds to the
`OpDef.name` field for the proto that defines the operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `op_type` is not string.
</td>
</tr>
</table>



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/ops.py#L2643-L2646">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    f
)
</code></pre>

Registers the function `f` as gradient function for `op_type`.




