page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.softmax_cross_entropy_with_logits

Computes softmax cross entropy between `logits` and `labels`. (deprecated)

### Aliases:

* `tf.compat.v1.nn.softmax_cross_entropy_with_logits`
* `tf.nn.softmax_cross_entropy_with_logits`

``` python
tf.nn.softmax_cross_entropy_with_logits(
    _sentinel=None,
    labels=None,
    logits=None,
    dim=-1,
    name=None,
    axis=None
)
```



Defined in [`python/ops/nn_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_ops.py).

<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:

Future major versions of TensorFlow will allow gradients to flow
into the labels input on backprop by default.

See <a href="../../tf/nn/softmax_cross_entropy_with_logits_v2"><code>tf.nn.softmax_cross_entropy_with_logits_v2</code></a>.


Measures the probability error in discrete classification tasks in which the
classes are mutually exclusive (each entry is in exactly one class).  For
example, each CIFAR-10 image is labeled with one and only one label: an image
can be a dog or a truck, but not both.

**NOTE:**  While the classes are mutually exclusive, their probabilities
need not be.  All that is required is that each row of `labels` is
a valid probability distribution.  If they are not, the computation of the
gradient will be incorrect.

If using exclusive `labels` (wherein one and only
one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

**WARNING:** This op expects unscaled logits, since it performs a `softmax`
on `logits` internally for efficiency.  Do not call this op with the
output of `softmax`, as it will produce incorrect results.

A common use case is to have logits and labels of shape
`[batch_size, num_classes]`, but higher dimensions are supported, with
the `dim` argument specifying the class dimension.

Backpropagation will happen only into `logits`.  To calculate a cross entropy
loss that allows backpropagation into both `logits` and `labels`, see
<a href="../../tf/nn/softmax_cross_entropy_with_logits_v2"><code>tf.nn.softmax_cross_entropy_with_logits_v2</code></a>.

**Note that to avoid confusion, it is required to pass only named arguments to
this function.**

#### Args:


* <b>`_sentinel`</b>: Used to prevent positional parameters. Internal, do not use.
* <b>`labels`</b>: Each vector along the class dimension should hold a valid
  probability distribution e.g. for the case in which labels are of shape
  `[batch_size, num_classes]`, each row of `labels[i]` must be a valid
  probability distribution.
* <b>`logits`</b>: Per-label activations, typically a linear output. These activation
  energies are interpreted as unnormalized log probabilities.
* <b>`dim`</b>: The class dimension. Defaulted to -1 which is the last dimension.
* <b>`name`</b>: A name for the operation (optional).
* <b>`axis`</b>: Alias for dim.


#### Returns:

A `Tensor` that contains the softmax cross entropy loss. Its type is the
same as `logits` and its shape is the same as `labels` except that it does
not have the last dimension of `labels`.
