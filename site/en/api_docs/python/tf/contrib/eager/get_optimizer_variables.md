

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.get_optimizer_variables

``` python
tf.contrib.eager.get_optimizer_variables(optimizer)
```



Defined in [`tensorflow/contrib/eager/python/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/eager/python/saver.py).

Returns a list of variables for the given <a href="../../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a>.

Equivalent to `optimizer.variables()`.

#### Args:

* <b>`optimizer`</b>: An instance of <a href="../../../tf/train/Optimizer"><code>tf.train.Optimizer</code></a> which has created variables
    (typically after a call to `Optimizer.minimize`).

#### Returns:

A list of variables which have been created by the `Optimizer`.