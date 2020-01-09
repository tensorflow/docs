page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L3108-L3224">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes softmax cross entropy between `logits` and `labels`. (deprecated arguments)

``` python
tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(
    labels,
    logits,
    axis=None,
    name=None,
    dim=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dim)`. They will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead

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
the `axis` argument specifying the class dimension.

`logits` and `labels` must have the same dtype (either `float16`, `float32`,
or `float64`).

Backpropagation will happen into both `logits` and `labels`.  To disallow
backpropagation into `labels`, pass label tensors through <a href="../../../../tf/stop_gradient"><code>tf.stop_gradient</code></a>
before feeding it to this function.

**Note that to avoid confusion, it is required to pass only named arguments to
this function.**

#### Args:


* <b>`labels`</b>: Each vector along the class dimension should hold a valid
  probability distribution e.g. for the case in which labels are of shape
  `[batch_size, num_classes]`, each row of `labels[i]` must be a valid
  probability distribution.
* <b>`logits`</b>: Unscaled log probabilities.
* <b>`axis`</b>: The class dimension. Defaulted to -1 which is the last dimension.
* <b>`name`</b>: A name for the operation (optional).
* <b>`dim`</b>: Deprecated alias for axis.


#### Returns:

A `Tensor` that contains the softmax cross entropy loss. Its type is the
same as `logits` and its shape is the same as `labels` except that it does
not have the last dimension of `labels`.
