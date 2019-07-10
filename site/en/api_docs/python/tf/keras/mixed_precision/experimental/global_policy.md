page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.mixed_precision.experimental.global_policy

Returns the global Policy.

### Aliases:

* `tf.compat.v1.keras.mixed_precision.experimental.global_policy`
* `tf.compat.v2.keras.mixed_precision.experimental.global_policy`
* `tf.keras.mixed_precision.experimental.global_policy`

``` python
tf.keras.mixed_precision.experimental.global_policy()
```



Defined in [`python/keras/mixed_precision/experimental/policy.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/mixed_precision/experimental/policy.py).

<!-- Placeholder for "Used in" -->

The global policy is the default policy used for layers, if no policy is
passed to the layer constructor. When TensorFlow starts, the global policy is
set to an "infer" policy, and can be changed with `set_policy`.

#### Returns:

The global Policy.
