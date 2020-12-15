description: Retrieve multiple values from the computation outfeed. Device ordinal is a

robots: noindex

# tf.raw_ops.OutfeedDequeueTupleV2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Retrieve multiple values from the computation outfeed. Device ordinal is a

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.raw_ops.OutfeedDequeueTupleV2`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.raw_ops.OutfeedDequeueTupleV2(
    device_ordinal, dtypes, shapes, name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->
tensor allowing dynamic outfeed.

  This operation will block indefinitely until data is available. Output `i`
  corresponds to XLA tuple element `i`.

  Args:
    device_ordinal: A `Tensor` of type `int32`.
      An int scalar tensor, representing the TPU device to use. This should be -1 when
      the Op is running on a TPU device, and >= 0 when the Op is running on the CPU
      device.
    dtypes: A list of `tf.DTypes` that has length `>= 1`.
      The element types of each element in `outputs`.
    shapes: A list of shapes (each a <a href="../../tf/TensorShape.md"><code>tf.TensorShape</code></a> or list of `ints`).
      The shapes of each tensor in `outputs`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `dtypes`.
  