

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.switch

### `tf.contrib.keras.backend.switch`

``` python
switch(
    condition,
    then_expression,
    else_expression
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/keras/python/keras/backend.py).

Switches between two operations depending on a scalar value.

Note that both `then_expression` and `else_expression`
should be symbolic tensors of the *same shape*.

#### Arguments:

    condition: scalar tensor (`int` or `bool`).
    then_expression: either a tensor, or a callable that returns a tensor.
    else_expression: either a tensor, or a callable that returns a tensor.


#### Returns:

    The selected tensor.