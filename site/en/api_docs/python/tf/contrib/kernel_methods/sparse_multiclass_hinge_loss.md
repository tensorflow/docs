

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kernel_methods.sparse_multiclass_hinge_loss

``` python
tf.contrib.kernel_methods.sparse_multiclass_hinge_loss(
    labels,
    logits,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS
)
```



Defined in [`tensorflow/contrib/kernel_methods/python/losses.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kernel_methods/python/losses.py).

Adds Ops for computing the multiclass hinge loss.

The implementation is based on the following paper:
On the Algorithmic Implementation of Multiclass Kernel-based Vector Machines
by Crammer and Singer.
link: http://jmlr.csail.mit.edu/papers/volume2/crammer01a/crammer01a.pdf

This is a generalization of standard (binary) hinge loss. For a given instance
with correct label c*, the loss is given by:
<div>   $$loss = max_{c != c*} logits_c - logits_{c*} + 1.$$ </div>
or equivalently
<div>   $$loss = max_c { logits_c - logits_{c*} + I_{c != c*} }$$ </div>
where \(I_{c != c*} = 1\      ext{if}\ c != c*\) and 0 otherwise.

#### Args:

* <b>`labels`</b>: `Tensor` of shape [batch_size] or [batch_size, 1]. Corresponds to
    the ground truth. Each entry must be an index in `[0, num_classes)`.
* <b>`logits`</b>: `Tensor` of shape [batch_size, num_classes] corresponding to the
    unscaled logits. Its dtype should be either `float32` or `float64`.
* <b>`weights`</b>: Optional (python) scalar or `Tensor`. If a non-scalar `Tensor`, its
    rank should be either 1 ([batch_size]) or 2 ([batch_size, 1]).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which the loss will be added.
* <b>`reduction`</b>: Type of reduction to apply to loss.


#### Returns:

Weighted loss float `Tensor`. If `reduction` is `NONE`, this has the same
shape as `labels`; otherwise, it is a scalar.


#### Raises:

* <b>`ValueError`</b>: If `logits`, `labels` or `weights` have invalid or inconsistent
    shapes.
* <b>`ValueError`</b>: If `labels` tensor has invalid dtype.