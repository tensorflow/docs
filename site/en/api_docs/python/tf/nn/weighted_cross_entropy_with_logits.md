page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.weighted_cross_entropy_with_logits

Computes a weighted cross entropy. (deprecated arguments)

### Aliases:

* `tf.compat.v1.nn.weighted_cross_entropy_with_logits`
* `tf.nn.weighted_cross_entropy_with_logits`

``` python
tf.nn.weighted_cross_entropy_with_logits(
    labels=None,
    logits=None,
    pos_weight=None,
    name=None,
    targets=None
)
```



Defined in [`python/ops/nn_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/nn_impl.py).

<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(targets)`. They will be removed in a future version.
Instructions for updating:
targets is deprecated, use labels instead

This is like `sigmoid_cross_entropy_with_logits()` except that `pos_weight`,
allows one to trade off recall and precision by up- or down-weighting the
cost of a positive error relative to a negative error.
The usual cross-entropy cost is defined as:
    labels * -log(sigmoid(logits)) +
        (1 - labels) * -log(1 - sigmoid(logits))
A value `pos_weights > 1` decreases the false negative count, hence increasing
the recall.
Conversely setting `pos_weights < 1` decreases the false positive count and
increases the precision.
This can be seen from the fact that `pos_weight` is introduced as a
multiplicative coefficient for the positive labels term
in the loss expression:
    labels * -log(sigmoid(logits)) * pos_weight +
        (1 - labels) * -log(1 - sigmoid(logits))
For brevity, let `x = logits`, `z = labels`, `q = pos_weight`.
The loss is:
      qz * -log(sigmoid(x)) + (1 - z) * -log(1 - sigmoid(x))
    = qz * -log(1 / (1 + exp(-x))) + (1 - z) * -log(exp(-x) / (1 + exp(-x)))
    = qz * log(1 + exp(-x)) + (1 - z) * (-log(exp(-x)) + log(1 + exp(-x)))
    = qz * log(1 + exp(-x)) + (1 - z) * (x + log(1 + exp(-x))
    = (1 - z) * x + (qz +  1 - z) * log(1 + exp(-x))
    = (1 - z) * x + (1 + (q - 1) * z) * log(1 + exp(-x))
Setting `l = (1 + (q - 1) * z)`, to ensure stability and avoid overflow,
the implementation uses
    (1 - z) * x + l * (log(1 + exp(-abs(x))) + max(-x, 0))
`logits` and `labels` must have the same type and shape.
Args:
  labels: A `Tensor` of the same type and shape as `logits`.
  logits: A `Tensor` of type `float32` or `float64`.
  pos_weight: A coefficient to use on the positive examples.
  name: A name for the operation (optional).
  targets: Deprecated alias for labels.

#### Returns:

A `Tensor` of the same shape as `logits` with the componentwise
weighted logistic losses.


#### Raises:


* <b>`ValueError`</b>: If `logits` and `labels` do not have the same shape.