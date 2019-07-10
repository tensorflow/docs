page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.mean_pairwise_squared_error

Adds a pairwise-errors-squared loss to the training procedure.

### Aliases:

* `tf.compat.v1.losses.mean_pairwise_squared_error`
* `tf.losses.mean_pairwise_squared_error`

``` python
tf.losses.mean_pairwise_squared_error(
    labels,
    predictions,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES
)
```



Defined in [`python/ops/losses/losses_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/losses/losses_impl.py).

<!-- Placeholder for "Used in" -->

Unlike `mean_squared_error`, which is a measure of the differences between
corresponding elements of `predictions` and `labels`,
`mean_pairwise_squared_error` is a measure of the differences between pairs of
corresponding elements of `predictions` and `labels`.

For example, if `labels`=[a, b, c] and `predictions`=[x, y, z], there are
three pairs of differences are summed to compute the loss:
  loss = [ ((a-b) - (x-y)).^2 + ((a-c) - (x-z)).^2 + ((b-c) - (y-z)).^2 ] / 3

Note that since the inputs are of shape `[batch_size, d0, ... dN]`, the
corresponding pairs are computed within each batch sample but not across
samples within a batch. For example, if `predictions` represents a batch of
16 grayscale images of dimension [batch_size, 100, 200], then the set of pairs
is drawn from each image, but not across images.

`weights` acts as a coefficient for the loss. If a scalar is provided, then
the loss is simply scaled by the given value. If `weights` is a tensor of size
`[batch_size]`, then the total loss for each sample of the batch is rescaled
by the corresponding element in the `weights` vector.

#### Args:


* <b>`labels`</b>: The ground truth output tensor, whose shape must match the shape of
  `predictions`.
* <b>`predictions`</b>: The predicted outputs, a tensor of size
  `[batch_size, d0, .. dN]` where N+1 is the total number of dimensions in
  `predictions`.
* <b>`weights`</b>: Coefficients for the loss a scalar, a tensor of shape
  `[batch_size]` or a tensor whose shape matches `predictions`.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which the loss will be added.


#### Returns:

A scalar `Tensor` that returns the weighted loss.



#### Raises:


* <b>`ValueError`</b>: If the shape of `predictions` doesn't match that of `labels` or
  if the shape of `weights` is invalid.  Also if `labels` or `predictions`
  is None.



#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a>.

