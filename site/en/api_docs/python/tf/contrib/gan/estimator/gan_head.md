page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.estimator.gan_head

### Aliases:

* `tf.contrib.gan.estimator.gan_head`
* `tf.contrib.gan.estimator.head.gan_head`

``` python
tf.contrib.gan.estimator.gan_head(
    generator_loss_fn,
    discriminator_loss_fn,
    generator_optimizer,
    discriminator_optimizer,
    use_loss_summaries=True,
    get_hooks_fn=tfgan_train.get_sequential_train_hooks(),
    get_eval_metric_ops_fn=None,
    name=None
)
```



Defined in [`tensorflow/contrib/gan/python/estimator/python/head_impl.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/gan/python/estimator/python/head_impl.py).

Creates a `GANHead`. (deprecated)

THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Please use tf.contrib.gan.GANEstimator without explicitly making a GANHead.

#### Args:

* <b>`generator_loss_fn`</b>: A TFGAN loss function for the generator. Takes a
    `GANModel` and returns a scalar.
* <b>`discriminator_loss_fn`</b>: Same as `generator_loss_fn`, but for the
    discriminator.
* <b>`generator_optimizer`</b>: The optimizer for generator updates.
* <b>`discriminator_optimizer`</b>: Same as `generator_optimizer`, but for the
    discriminator updates.
* <b>`use_loss_summaries`</b>: If `True`, add loss summaries. If `False`, does not.
    If `None`, uses defaults.
* <b>`get_hooks_fn`</b>: A function that takes a `GANTrainOps` tuple and returns a
    list of hooks.
* <b>`get_eval_metric_ops_fn`</b>: A function that takes a `GANModel`, and returns a
    dict of metric results keyed by name. The output of this function is
    passed into `tf.estimator.EstimatorSpec` during evaluation.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`.


#### Returns:

An instance of `GANHead`.