description: Creates a tensor with the given shape.

robots: noindex

# tf.raw_ops.Empty

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Creates a tensor with the given shape.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.Empty`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.Empty(
    shape, dtype, init=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This operation creates a tensor of `shape` and `dtype`.

  Args:
    shape: A `Tensor` of type `int32`.
      1-D. Represents the shape of the output tensor.
    dtype: A <a href="../../tf/dtypes/DType.md"><code>tf.DType</code></a>.
    init: An optional `bool`. Defaults to `False`.
      If True, initialize the returned tensor with the default value of dtype.  Otherwise, the implementation is free not to initializethe tensor's content.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  