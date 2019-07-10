page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.losses.categorical_crossentropy

Computes the categorical crossentropy loss.

### Aliases:

* `tf.compat.v1.keras.losses.categorical_crossentropy`
* `tf.compat.v1.keras.metrics.categorical_crossentropy`
* `tf.compat.v2.keras.losses.categorical_crossentropy`
* `tf.compat.v2.keras.metrics.categorical_crossentropy`
* `tf.compat.v2.losses.categorical_crossentropy`
* `tf.compat.v2.metrics.categorical_crossentropy`
* `tf.keras.losses.categorical_crossentropy`
* `tf.keras.metrics.categorical_crossentropy`

``` python
tf.keras.losses.categorical_crossentropy(
    y_true,
    y_pred,
    from_logits=False,
    label_smoothing=0
)
```



Defined in [`python/keras/losses.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/losses.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`y_true`</b>: tensor of true targets.
* <b>`y_pred`</b>: tensor of predicted targets.
* <b>`from_logits`</b>: Whether `y_pred` is expected to be a logits tensor. By default,
  we assume that `y_pred` encodes a probability distribution.
* <b>`label_smoothing`</b>: Float in [0, 1]. If > `0` then smooth the labels.


#### Returns:

Categorical crossentropy loss value.
