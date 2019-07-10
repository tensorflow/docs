page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.config.get_soft_device_placement

Get if soft device placement is enabled.

### Aliases:

* `tf.compat.v1.config.get_soft_device_placement`
* `tf.compat.v2.config.get_soft_device_placement`
* `tf.config.get_soft_device_placement`

``` python
tf.config.get_soft_device_placement()
```



Defined in [`python/framework/config.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/config.py).

<!-- Placeholder for "Used in" -->

If enabled, an op will be placed on CPU if any of the following are true
  1. there's no GPU implementation for the OP
  2. no GPU devices are known or registered
  3. need to co-locate with reftype input(s) which are from CPU

#### Returns:

If soft placement is enabled.
