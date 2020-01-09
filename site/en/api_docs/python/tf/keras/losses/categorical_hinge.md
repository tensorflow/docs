page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.categorical_hinge


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/losses.py#L866-L882">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the categorical hinge loss between `y_true` and `y_pred`.

### Aliases:

* `tf.compat.v1.keras.losses.categorical_hinge`
* `tf.compat.v2.keras.losses.categorical_hinge`
* `tf.compat.v2.losses.categorical_hinge`
* `tf.losses.categorical_hinge`


``` python
tf.keras.losses.categorical_hinge(
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

A tensor.
