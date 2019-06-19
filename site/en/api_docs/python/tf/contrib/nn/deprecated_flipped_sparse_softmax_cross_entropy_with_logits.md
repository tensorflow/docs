page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.nn.deprecated_flipped_sparse_softmax_cross_entropy_with_logits

``` python
tf.contrib.nn.deprecated_flipped_sparse_softmax_cross_entropy_with_logits(
    logits,
    labels,
    name=None
)
```



Defined in [`tensorflow/contrib/nn/python/ops/cross_entropy.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/nn/python/ops/cross_entropy.py).

Computes sparse softmax cross entropy between `logits` and `labels`.

This function diffs from tf.nn.sparse_softmax_cross_entropy_with_logits only
in the argument order.

Measures the probability error in discrete classification tasks in which the
classes are mutually exclusive (each entry is in exactly one class).  For
example, each CIFAR-10 image is labeled with one and only one label: an image
can be a dog or a truck, but not both.

**NOTE:**  For this operation, the probability of a given label is considered
exclusive.  That is, soft classes are not allowed, and the `labels` vector
must provide a single specific index for the true class for each row of
`logits` (each minibatch entry).  For soft softmax classification with
a probability distribution for each entry, see
`softmax_cross_entropy_with_logits`.

**WARNING:** This op expects unscaled logits, since it performs a softmax
on `logits` internally for efficiency.  Do not call this op with the
output of `softmax`, as it will produce incorrect results.

A common use case is to have logits of shape `[batch_size, num_classes]` and
labels of shape `[batch_size]`. But higher dimensions are supported.

#### Args:


* <b>`logits`</b>: Unscaled log probabilities of rank `r` and shape
    `[d_0, d_1, ..., d_{r-2}, num_classes]` and dtype `float32` or `float64`.
* <b>`labels`</b>: `Tensor` of shape `[d_0, d_1, ..., d_{r-2}]` and dtype `int32` or
    `int64`. Each entry in `labels` must be an index in `[0, num_classes)`.
    Other values will raise an exception when this op is run on CPU, and
    return `NaN` for corresponding corresponding loss and gradient rows
    on GPU.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of the same shape as `labels` and of the same type as `logits`
with the softmax cross entropy loss.


#### Raises:

* <b>`ValueError`</b>: If logits are scalars (need to have rank >= 1) or if the rank
    of the labels is not equal to the rank of the logits minus one.