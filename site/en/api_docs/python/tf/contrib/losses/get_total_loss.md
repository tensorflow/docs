page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.get_total_loss

Returns a tensor whose value represents the total loss. (deprecated)

``` python
tf.contrib.losses.get_total_loss(
    add_regularization_losses=True,
    name='total_loss'
)
```



Defined in [`contrib/losses/python/losses/loss_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/losses/python/losses/loss_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.get_total_loss instead.

Notice that the function adds the given losses to the regularization losses.

#### Args:


* <b>`add_regularization_losses`</b>: A boolean indicating whether or not to use the
  regularization losses in the sum.
* <b>`name`</b>: The name of the returned tensor.


#### Returns:

A `Tensor` whose value represents the total loss.



#### Raises:


* <b>`ValueError`</b>: if `losses` is not iterable.