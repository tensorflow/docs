

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.gan.losses.wargs.combine_adversarial_loss

``` python
tf.contrib.gan.losses.wargs.combine_adversarial_loss(
    main_loss,
    adversarial_loss,
    weight_factor=None,
    gradient_ratio=None,
    gradient_ratio_epsilon=1e-06,
    variables=None,
    scalar_summaries=True,
    gradient_summaries=True,
    scope=None
)
```



Defined in [`tensorflow/contrib/gan/python/losses/python/losses_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/gan/python/losses/python/losses_impl.py).

Utility to combine main and adversarial losses.

This utility combines the main and adversarial losses in one of two ways.
1) Fixed coefficient on adversarial loss. Use `weight_factor` in this case.
2) Fixed ratio of gradients. Use `gradient_ratio` in this case. This is often
  used to make sure both losses affect weights roughly equally, as in
  https://arxiv.org/pdf/1705.05823.

One can optionally also visualize the scalar and gradient behavior of the
losses.

#### Args:

* <b>`main_loss`</b>: A floating scalar Tensor indicating the main loss.
* <b>`adversarial_loss`</b>: A floating scalar Tensor indication the adversarial loss.
* <b>`weight_factor`</b>: If not `None`, the coefficient by which to multiply the
    adversarial loss. Exactly one of this and `gradient_ratio` must be
    non-None.
* <b>`gradient_ratio`</b>: If not `None`, the ratio of the magnitude of the gradients.
    Specifically,
      gradient_ratio = grad_mag(main_loss) / grad_mag(adversarial_loss)
    Exactly one of this and `weight_factor` must be non-None.
* <b>`gradient_ratio_epsilon`</b>: An epsilon to add to the adversarial loss
    coefficient denominator, to avoid division-by-zero.
* <b>`variables`</b>: List of variables to calculate gradients with respect to. If not
    present, defaults to all trainable variables.
* <b>`scalar_summaries`</b>: Create scalar summaries of losses.
* <b>`gradient_summaries`</b>: Create gradient summaries of losses.
* <b>`scope`</b>: Optional name scope.


#### Returns:

A floating scalar Tensor indicating the desired combined loss.


#### Raises:

* <b>`ValueError`</b>: Malformed input.