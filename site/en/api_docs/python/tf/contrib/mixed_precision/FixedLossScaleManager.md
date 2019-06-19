page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.mixed_precision.FixedLossScaleManager

## Class `FixedLossScaleManager`

Inherits From: [`LossScaleManager`](../../../tf/contrib/mixed_precision/LossScaleManager)



Defined in [`tensorflow/contrib/mixed_precision/python/loss_scale_manager.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py).

Loss scale manager with a fixed loss scale.

The loss scale is not updated for the lifetime of the class.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(loss_scale)
```

Creates the fixed loss scale manager.

#### Args:

* <b>`loss_scale`</b>: A Python float. Its ideal value varies depending on models to
    run. Choosing a too small loss_scale might affect model quality; a too
    big loss_scale might cause inf or nan. There is no single right
    loss_scale to apply. There is no harm choosing a relatively big number
    as long as no nan or inf is encountered in training.


#### Raises:

* <b>`ValueError`</b>: If loss_scale is less than 1.

<h3 id="get_loss_scale"><code>get_loss_scale</code></h3>

``` python
get_loss_scale()
```



<h3 id="update_loss_scale"><code>update_loss_scale</code></h3>

``` python
update_loss_scale(finite_grads)
```





