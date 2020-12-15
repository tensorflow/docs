description: Computes softmax cross entropy between logits and labels. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/nn_ops.py#L3868-L3985">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Computes softmax cross entropy between `logits` and `labels`. (deprecated arguments)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(
    labels, logits, axis=None, name=None, dim=None
)
</code></pre>



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
backpropagation into `labels`, pass label tensors through <a href="../../../../tf/stop_gradient.md"><code>tf.stop_gradient</code></a>
before feeding it to this function.

**Note that to avoid confusion, it is required to pass only named arguments to
this function.**

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`labels`
</td>
<td>
Each vector along the class dimension should hold a valid
probability distribution e.g. for the case in which labels are of shape
`[batch_size, num_classes]`, each row of `labels[i]` must be a valid
probability distribution.
</td>
</tr><tr>
<td>
`logits`
</td>
<td>
Unscaled log probabilities.
</td>
</tr><tr>
<td>
`axis`
</td>
<td>
The class dimension. Defaulted to -1 which is the last dimension.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for the operation (optional).
</td>
</tr><tr>
<td>
`dim`
</td>
<td>
Deprecated alias for axis.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Tensor` that contains the softmax cross entropy loss. Its type is the
same as `logits` and its shape is the same as `labels` except that it does
not have the last dimension of `labels`.
</td>
</tr>

</table>

