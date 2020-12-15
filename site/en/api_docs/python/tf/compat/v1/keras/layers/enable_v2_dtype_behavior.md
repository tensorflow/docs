description: Enable the V2 dtype behavior for Keras layers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.enable_v2_dtype_behavior" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.keras.layers.enable_v2_dtype_behavior

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/base_layer_utils.py#L709-L741">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Enable the V2 dtype behavior for Keras layers.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.layers.enable_v2_dtype_behavior()
</code></pre>



<!-- Placeholder for "Used in" -->

By default, the V2 dtype behavior is enabled in TensorFlow 2, so this function
is only useful if <a href="../../../../../tf/compat/v1/disable_v2_behavior.md"><code>tf.compat.v1.disable_v2_behavior</code></a> has been called. Since
mixed precision requires V2 dtype behavior to be enabled, this function allows
you to use mixed precision in Keras layers if `disable_v2_behavior` has been
called.

When enabled, the dtype of Keras layers defaults to floatx (which is typically
float32) instead of None. In addition, layers will automatically cast
floating-point inputs to the layer's dtype.

```
>>> x = tf.ones((4, 4, 4, 4), dtype='float64')
>>> layer = tf.keras.layers.Conv2D(filters=4, kernel_size=2)
>>> print(layer.dtype)  # float32 since V2 dtype behavior is enabled
float32
>>> y = layer(x)  # Layer casts inputs since V2 dtype behavior is enabled
>>> print(y.dtype.name)
float32
```

A layer author can opt-out their layer from the automatic input casting by
passing `autocast=False` to the base Layer's constructor. This disables the
autocasting part of the V2 behavior for that layer, but not the defaulting to
floatx part of the V2 behavior.

When a global <a href="../../../../../tf/keras/mixed_precision/experimental/Policy.md"><code>tf.keras.mixed_precision.experimental.Policy</code></a> is set, a Keras
layer's dtype will default to the global policy instead of floatx. Layers
will automatically cast inputs to the policy's compute_dtype.