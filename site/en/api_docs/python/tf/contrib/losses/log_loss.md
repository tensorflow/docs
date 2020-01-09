page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.log_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/losses/python/losses/loss_ops.py#L412-L449">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Adds a Log Loss term to the training procedure. (deprecated)

``` python
tf.contrib.losses.log_loss(
    predictions,
    labels=None,
    weights=1.0,
    epsilon=1e-07,
    scope=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2016-12-30.
Instructions for updating:
Use tf.losses.log_loss instead. Note that the order of the predictions and labels arguments has been changed.

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a tensor of size
[batch_size], then the total loss for each sample of the batch is rescaled
by the corresponding element in the `weights` vector. If the shape of
`weights` matches the shape of `predictions`, then the loss of each
measurable element of `predictions` is scaled by the corresponding value of
`weights`.

#### Args:


* <b>`predictions`</b>: The predicted outputs.
* <b>`labels`</b>: The ground truth output tensor, same dimensions as 'predictions'.
* <b>`weights`</b>: Coefficients for the loss a scalar, a tensor of shape
  [batch_size] or a tensor whose shape matches `predictions`.
* <b>`epsilon`</b>: A small increment to add to avoid taking a log of zero.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.


#### Returns:

A scalar `Tensor` representing the loss value.



#### Raises:


* <b>`ValueError`</b>: If the shape of `predictions` doesn't match that of `labels` or
  if the shape of `weights` is invalid.
