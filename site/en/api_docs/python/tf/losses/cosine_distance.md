page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.losses.cosine_distance

Adds a cosine-distance loss to the training procedure. (deprecated arguments)

### Aliases:

* `tf.compat.v1.losses.cosine_distance`
* `tf.losses.cosine_distance`

``` python
tf.losses.cosine_distance(
    labels,
    predictions,
    axis=None,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=Reduction.SUM_BY_NONZERO_WEIGHTS,
    dim=None
)
```



Defined in [`python/ops/losses/losses_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/losses/losses_impl.py).

<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead

Note that the function assumes that `predictions` and `labels` are already
unit-normalized.

#### Args:


* <b>`labels`</b>: `Tensor` whose shape matches 'predictions'
* <b>`predictions`</b>: An arbitrary matrix.
* <b>`axis`</b>: The dimension along which the cosine distance is computed.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
  `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
  be either `1`, or the same as the corresponding `losses` dimension).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.
* <b>`reduction`</b>: Type of reduction to apply to loss.
* <b>`dim`</b>: The old (deprecated) name for `axis`.


#### Returns:

Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
shape as `labels`; otherwise, it is scalar.



#### Raises:


* <b>`ValueError`</b>: If `predictions` shape doesn't match `labels` shape, or
  `axis`, `labels`, `predictions` or `weights` is `None`.



#### Eager Compatibility
The `loss_collection` argument is ignored when executing eagerly. Consider
holding on to the return value or collecting losses via a <a href="../../tf/keras/Model"><code>tf.keras.Model</code></a>.

