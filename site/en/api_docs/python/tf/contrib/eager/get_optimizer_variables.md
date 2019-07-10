page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.get_optimizer_variables

Returns a list of variables for the given <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a>.

``` python
tf.contrib.eager.get_optimizer_variables(optimizer)
```



Defined in [`contrib/eager/python/saver.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/eager/python/saver.py).

<!-- Placeholder for "Used in" -->

Equivalent to `optimizer.variables()`.

#### Args:


* <b>`optimizer`</b>: An instance of <a href="../../../tf/train/Optimizer"><code>tf.compat.v1.train.Optimizer</code></a> which has created
  variables (typically after a call to `Optimizer.minimize`).


#### Returns:

A list of variables which have been created by the `Optimizer`.
