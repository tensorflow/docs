

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.estimator.GANHead

## Class `GANHead`



### Aliases:

* Class `tf.contrib.gan.estimator.GANHead`
* Class `tf.contrib.gan.estimator.head.GANHead`



Defined in [`tensorflow/contrib/gan/python/estimator/python/head_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/gan/python/estimator/python/head_impl.py).

`Head` for a GAN.

## Properties

<h3 id="logits_dimension"><code>logits_dimension</code></h3>



<h3 id="name"><code>name</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    generator_loss_fn,
    discriminator_loss_fn,
    generator_optimizer,
    discriminator_optimizer,
    use_loss_summaries=True,
    get_hooks_fn=None,
    get_eval_metric_ops_fn=None,
    name=None
)
```

`Head` for GAN training.

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
    list of hooks. Defaults to `train.get_sequential_train_hooks()`
* <b>`get_eval_metric_ops_fn`</b>: A function that takes a `GANModel`, and returns a
    dict of metric results keyed by name. The output of this function is
    passed into <a href="../../../../tf/estimator/EstimatorSpec"><code>tf.estimator.EstimatorSpec</code></a> during evaluation.
* <b>`name`</b>: name of the head. If provided, summary and metrics keys will be
    suffixed by `"/" + name`.

<h3 id="create_estimator_spec"><code>create_estimator_spec</code></h3>

``` python
create_estimator_spec(
    features,
    mode,
    logits,
    labels=None,
    train_op_fn=tf.contrib.gan.gan_train_ops
)
```

Returns `EstimatorSpec` that a model_fn can return.

See `Head` for more details.

#### Args:

* <b>`features`</b>: Must be `None`.
* <b>`mode`</b>: Estimator's `ModeKeys`.
* <b>`logits`</b>: A GANModel tuple.
* <b>`labels`</b>: Must be `None`.
* <b>`train_op_fn`</b>: Function that takes a GANModel, GANLoss, generator optimizer,
    and discriminator optimizer, and returns a `GANTrainOps` tuple. For
    example, this function can come from TFGAN's `train.py` library, or can
    be custom.


#### Returns:

`EstimatorSpec`.


#### Raises:

* <b>`ValueError`</b>: If `features` isn't `None`.
* <b>`ValueError`</b>: If `train_op_fn` isn't provided in train mode.

<h3 id="create_loss"><code>create_loss</code></h3>

``` python
create_loss(
    features,
    mode,
    logits,
    labels
)
```

Returns a GANLoss tuple from the provided GANModel.

See `Head` for more details.

#### Args:

* <b>`features`</b>: Input `dict` of `Tensor` objects. Unused.
* <b>`mode`</b>: Estimator's `ModeKeys`.
* <b>`logits`</b>: A GANModel tuple.
* <b>`labels`</b>: Must be `None`.


#### Returns:

A GANLoss tuple.



