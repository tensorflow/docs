

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.get_optimizer_variables

``` python
get_optimizer_variables(optimizer)
```



Defined in [`tensorflow/contrib/eager/python/saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/eager/python/saver.py).

Returns a list of variables for the given `tf.train.Optimizer`.

Equivalent to `optimizer.variables()`.

#### Args:

* <b>`optimizer`</b>: An instance of `tf.train.Optimizer` which has created variables
    (typically after a call to `Optimizer.minimize`).

#### Returns:

A list of variables which have been created by the `Optimizer`.