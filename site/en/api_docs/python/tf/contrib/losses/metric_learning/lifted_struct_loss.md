page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.losses.metric_learning.lifted_struct_loss

Computes the lifted structured loss.

``` python
tf.contrib.losses.metric_learning.lifted_struct_loss(
    labels,
    embeddings,
    margin=1.0
)
```



Defined in [`contrib/losses/python/metric_learning/metric_loss_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/losses/python/metric_learning/metric_loss_ops.py).

<!-- Placeholder for "Used in" -->

The loss encourages the positive distances (between a pair of embeddings
with the same labels) to be smaller than any negative distances (between a
pair of embeddings with different labels) in the mini-batch in a way
that is differentiable with respect to the embedding vectors.
See: https://arxiv.org/abs/1511.06452.

#### Args:


* <b>`labels`</b>: 1-D tf.int32 `Tensor` with shape [batch_size] of
  multiclass integer labels.
* <b>`embeddings`</b>: 2-D float `Tensor` of embedding vectors. Embeddings should not
  be l2 normalized.
* <b>`margin`</b>: Float, margin term in the loss definition.


#### Returns:


* <b>`lifted_loss`</b>: tf.float32 scalar.