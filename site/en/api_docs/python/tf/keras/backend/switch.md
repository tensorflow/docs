page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.switch

Switches between two operations depending on a scalar value.

### Aliases:

* `tf.compat.v1.keras.backend.switch`
* `tf.compat.v2.keras.backend.switch`
* `tf.keras.backend.switch`

``` python
tf.keras.backend.switch(
    condition,
    then_expression,
    else_expression
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->

Note that both `then_expression` and `else_expression`
should be symbolic tensors of the *same shape*.

#### Arguments:


* <b>`condition`</b>: tensor (`int` or `bool`).
* <b>`then_expression`</b>: either a tensor, or a callable that returns a tensor.
* <b>`else_expression`</b>: either a tensor, or a callable that returns a tensor.


#### Returns:

The selected tensor.



#### Raises:


* <b>`ValueError`</b>: If rank of `condition` is greater than rank of expressions.