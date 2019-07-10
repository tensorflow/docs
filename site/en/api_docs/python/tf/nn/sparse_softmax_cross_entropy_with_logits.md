page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.sparse_softmax_cross_entropy_with_logits

Computes sparse softmax cross entropy between `logits` and `labels`.

### Aliases:

* `tf.compat.v1.nn.sparse_softmax_cross_entropy_with_logits`
* `tf.nn.sparse_softmax_cross_entropy_with_logits`

``` python
tf.nn.sparse_softmax_cross_entropy_with_logits(
    _sentinel=None,
    labels=None,
    logits=None,
    name=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

Measures the probability error in discrete classification tasks in which the
classes are mutually exclusive (each entry is in exactly one class).  For
example, each CIFAR-10 image is labeled with one and only one label: an image
can be a dog or a truck, but not both.

**NOTE:**  For this operation, the probability of a given label is considered
exclusive.  That is, soft classes are not allowed, and the `labels` vector
must provide a single specific index for the true class for each row of
`logits` (each minibatch entry).  For soft softmax classification with
a probability distribution for each entry, see
`softmax_cross_entropy_with_logits_v2`.

**WARNING:** This op expects unscaled logits, since it performs a `softmax`
on `logits` internally for efficiency.  Do not call this op with the
output of `softmax`, as it will produce incorrect results.

A common use case is to have logits of shape
`[batch_size, num_classes]` and have labels of shape
`[batch_size]`, but higher dimensions are supported, in which
case the `dim`-th dimension is assumed to be of size `num_classes`.
`logits` must have the dtype of `float16`, `float32`, or `float64`, and
`labels` must have the dtype of `int32` or `int64`.

**Note that to avoid confusion, it is required to pass only named arguments to
this function.**

#### Args:


* <b>`_sentinel`</b>: Used to prevent positional parameters. Internal, do not use.
* <b>`labels`</b>: `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of
  `labels` and result) and dtype `int32` or `int64`. Each entry in `labels`
  must be an index in `[0, num_classes)`. Other values will raise an
  exception when this op is run on CPU, and return `NaN` for corresponding
  loss and gradient rows on GPU.
* <b>`logits`</b>: Per-label activations (typically a linear output) of shape
  `[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float16`, `float32`, or
  `float64`. These activation energies are interpreted as unnormalized log
  probabilities.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of the same shape as `labels` and of the same type as `logits`
with the softmax cross entropy loss.



#### Raises:


* <b>`ValueError`</b>: If logits are scalars (need to have rank >= 1) or if the rank
  of the labels is not equal to the rank of the logits minus one.