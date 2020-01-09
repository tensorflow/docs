page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.quantized_relu_x


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_nn_ops.py`



Computes Quantized Rectified Linear X: `min(max(features, 0), max_value)`

### Aliases:

* <a href="/api_docs/python/tf/nn/quantized_relu_x"><code>tf.compat.v1.nn.quantized_relu_x</code></a>


``` python
tf.nn.quantized_relu_x(
    features,
    max_value,
    min_features,
    max_features,
    out_type=tf.dtypes.quint8,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`features`</b>: A `Tensor`. Must be one of the following types: `qint8`, `quint8`, `qint32`, `qint16`, `quint16`.
* <b>`max_value`</b>: A `Tensor` of type `float32`.
* <b>`min_features`</b>: A `Tensor` of type `float32`.
  The float value that the lowest quantized value represents.
* <b>`max_features`</b>: A `Tensor` of type `float32`.
  The float value that the highest quantized value represents.
* <b>`out_type`</b>: An optional <a href="../../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.qint8, tf.quint8, tf.qint32, tf.qint16, tf.quint16`. Defaults to <a href="../../tf#quint8"><code>tf.quint8</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (activations, min_activations, max_activations).


* <b>`activations`</b>: A `Tensor` of type `out_type`.
* <b>`min_activations`</b>: A `Tensor` of type `float32`.
* <b>`max_activations`</b>: A `Tensor` of type `float32`.
