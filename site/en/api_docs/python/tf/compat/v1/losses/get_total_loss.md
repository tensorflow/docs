page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.losses.get_total_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/losses/util.py#L242-L271">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a tensor whose value represents the total loss.

``` python
tf.compat.v1.losses.get_total_loss(
    add_regularization_losses=True,
    name='total_loss',
    scope=None
)
```



<!-- Placeholder for "Used in" -->

In particular, this adds any losses you have added with `tf.add_loss()` to
any regularization losses that have been added by regularization parameters
on layers constructors e.g. `tf.layers`. Be very sure to use this if you
are constructing a loss_op manually. Otherwise regularization arguments
on `tf.layers` methods will not function.

#### Args:


* <b>`add_regularization_losses`</b>: A boolean indicating whether or not to use the
  regularization losses in the sum.
* <b>`name`</b>: The name of the returned tensor.
* <b>`scope`</b>: An optional scope name for filtering the losses to return. Note that
  this filters the losses added with `tf.add_loss()` as well as the
  regularization losses to that scope.


#### Returns:

A `Tensor` whose value represents the total loss.



#### Raises:


* <b>`ValueError`</b>: if `losses` is not iterable.
