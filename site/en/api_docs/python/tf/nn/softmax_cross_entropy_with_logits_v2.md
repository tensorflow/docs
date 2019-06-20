page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.softmax_cross_entropy_with_logits_v2

``` python
tf.nn.softmax_cross_entropy_with_logits_v2(
    _sentinel=None,
    labels=None,
    logits=None,
    dim=-1,
    name=None
)
```



Defined in [`tensorflow/python/ops/nn_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/ops/nn_ops.py).

See the guide: [Neural Network > Classification](../../../../api_guides/python/nn#Classification)

Computes softmax cross entropy between `logits` and `labels`.

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

`logits` and `labels` must have the same dtype (either `float16`, `float32`,
or `float64`).

Backpropagation will happen into both `logits` and `labels`.  To disallow
backpropagation into `labels`, pass label tensors through <a href="../../tf/stop_gradient"><code>tf.stop_gradient</code></a>
before feeding it to this function.

**Note that to avoid confusion, it is required to pass only named arguments to
this function.**

#### Args:

* <b>`_sentinel`</b>: Used to prevent positional parameters. Internal, do not use.
* <b>`labels`</b>: Each vector along the class dimension should hold a valid
    probability distribution e.g. for the case in which labels are of shape
    `[batch_size, num_classes]`, each row of `labels[i]` must be a valid
    probability distribution.
* <b>`logits`</b>: Unscaled log probabilities.
* <b>`dim`</b>: The class dimension. Defaulted to -1 which is the last dimension.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of the same shape as `labels` and of the same type as `logits`
with the softmax cross entropy loss.