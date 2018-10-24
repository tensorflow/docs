

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.losses.wargs.modified_generator_loss

``` python
tf.contrib.gan.losses.wargs.modified_generator_loss(
    discriminator_gen_outputs,
    label_smoothing=0.0,
    weights=1.0,
    scope=None,
    loss_collection=tf.GraphKeys.LOSSES,
    reduction=losses.Reduction.SUM_BY_NONZERO_WEIGHTS,
    add_summaries=False
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

Modified generator loss for GANs.

L = -log(sigmoid(D(G(z))))

This is the trick used in the original paper to avoid vanishing gradients
early in training. See `Generative Adversarial Nets`
(https://arxiv.org/abs/1406.2661) for more details.

#### Args:

* <b>`discriminator_gen_outputs`</b>: Discriminator output on generated data. Expected
    to be in the range of (-inf, inf).
* <b>`label_smoothing`</b>: The amount of smoothing for positive labels. This technique
    is taken from `Improved Techniques for Training GANs`
    (https://arxiv.org/abs/1606.03498). `0.0` means no smoothing.
* <b>`weights`</b>: Optional `Tensor` whose rank is either 0, or the same rank as
    `discriminator_gen_outputs`, and must be broadcastable to `labels` (i.e.,
    all dimensions must be either `1`, or the same as the corresponding
    dimension).
* <b>`scope`</b>: The scope for the operations performed in computing the loss.
* <b>`loss_collection`</b>: collection to which this loss will be added.
* <b>`reduction`</b>: A <a href="../../../../../tf/losses/Reduction"><code>tf.losses.Reduction</code></a> to apply to loss.
* <b>`add_summaries`</b>: Whether or not to add summaries for the loss.


#### Returns:

A loss Tensor. The shape depends on `reduction`.