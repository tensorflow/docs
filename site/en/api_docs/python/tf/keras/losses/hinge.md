page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.hinge


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/losses.py#L848-L863">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the hinge loss between `y_true` and `y_pred`.

### Aliases:

* `tf.compat.v1.keras.losses.hinge`
* `tf.compat.v1.keras.metrics.hinge`
* `tf.compat.v2.keras.losses.hinge`
* `tf.compat.v2.keras.metrics.hinge`
* `tf.compat.v2.losses.hinge`
* `tf.compat.v2.metrics.hinge`
* `tf.keras.metrics.hinge`
* `tf.losses.hinge`
* `tf.metrics.hinge`


``` python
tf.keras.losses.hinge(
    y_true,
    y_pred
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`y_true`</b>: The ground truth values. `y_true` values are expected to be -1 or 1.
  If binary (0 or 1) labels are provided they will be converted to -1 or 1.
* <b>`y_pred`</b>: The predicted values.


#### Returns:

Tensor with one scalar loss entry per sample.
