page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.compute_weighted_loss


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/losses/losses_impl.py#L138-L203">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the weighted loss.

### Aliases:

* <a href="/api_docs/python/tf/losses/compute_weighted_loss"><code>tf.compat.v1.losses.compute_weighted_loss</code></a>


``` python
tf.losses.compute_weighted_loss(
    losses,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`losses`</b>: `Tensor` of shape `[batch_size, d1, ... dN]`.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `losses`, and must be broadcastable to `losses` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: the scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: the loss will be added to these collections.
* <b>`reduction`</b>: Type of reduction to apply to loss.


#### Returns:

Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
`NONE`, this has the same shape as `losses`; otherwise, it is scalar.



#### Raises:


* <b>`ValueError`</b>: If `weights` is `None` or the shape is not compatible with
  `losses`, or if the number of dimensions (rank) of either `losses` or
  `weights` is missing.


#### Note:

When calculating the gradient of a weighted loss contributions from
both `losses` and `weights` are considered. If your `weights` depend
on some model parameters but you do not want this to affect the loss
gradient, you need to apply <a href="../../tf/stop_gradient"><code>tf.stop_gradient</code></a> to `weights` before
passing them to `compute_weighted_loss`.




#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a>.
