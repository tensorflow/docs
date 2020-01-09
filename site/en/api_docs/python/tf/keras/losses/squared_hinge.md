page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.squared_hinge


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/losses.py#L829-L845">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the squared hinge loss between `y_true` and `y_pred`.

### Aliases:

* `tf.compat.v1.keras.losses.squared_hinge`
* `tf.compat.v1.keras.metrics.squared_hinge`
* `tf.compat.v2.keras.losses.squared_hinge`
* `tf.compat.v2.keras.metrics.squared_hinge`
* `tf.compat.v2.losses.squared_hinge`
* `tf.compat.v2.metrics.squared_hinge`
* `tf.keras.metrics.squared_hinge`
* `tf.losses.squared_hinge`
* `tf.metrics.squared_hinge`


``` python
tf.keras.losses.squared_hinge(
    y_true,
    y_pred
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`y_true`</b>: The ground truth values. `y_true` values are expected to be -1 or 1.
  If binary (0 or 1) labels are provided we will convert them to -1 or 1.
* <b>`y_pred`</b>: The predicted values.


#### Returns:

Tensor with one scalar loss entry per sample.
