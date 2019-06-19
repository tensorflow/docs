

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.wargs.acgan_discriminator_loss

``` python
tf.contrib.gan.losses.wargs.acgan_discriminator_loss(
    discriminator_real_classification_logits,
    discriminator_gen_classification_logits,
    one_hot_labels,
    label_smoothing=0.0,
    real_weights=1.0,
    generated_weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

ACGAN loss for the discriminator.

The ACGAN loss adds a classification loss to the conditional discriminator.
Therefore, the discriminator must output a tuple consisting of
  (1) the real/fake prediction and
  (2) the logits for the classification (usually the last conv layer,
      flattened).

For more details:
  ACGAN: https://arxiv.org/abs/1610.09585

#### Args:

* <b>`discriminator_real_classification_logits`</b>: Classification logits for real
    data.
* <b>`discriminator_gen_classification_logits`</b>: Classification logits for generated
    data.
* <b>`one_hot_labels`</b>: A Tensor holding one-hot labels for the batch.
* <b>`label_smoothing`</b>: A float in [0, 1]. If greater than 0, smooth the labels for
    "discriminator on real data" as suggested in
    https://arxiv.org/pdf/1701.00160
* <b>`real_weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `discriminator_real_outputs`, and must be broadcastable to
    `discriminator_real_outputs` (i.e., all dimensions must be either `1`, or
    the same as the corresponding dimension).
* <b>`generated_weights`</b>: Same as `real_weights`, but for
    `discriminator_gen_classification_logits`.
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.
* <b>`reduction`</b>: A <a href="../../../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> to apply to loss.
* <b>`add_summaries`</b>: Whether or not to add summaries for the loss.


#### Returns:

A loss Tensor. Shape depends on `reduction`.


#### Raises:

* <b>`TypeError`</b>: If the discriminator does not output a tuple.