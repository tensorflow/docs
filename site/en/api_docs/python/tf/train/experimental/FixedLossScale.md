page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.experimental.FixedLossScale

## Class `FixedLossScale`

Loss scale with a fixed value.

Inherits From: [`LossScale`](../../../tf/train/experimental/LossScale)

### Aliases:

* Class `tf.compat.v1.train.experimental.FixedLossScale`
* Class `tf.compat.v2.train.experimental.FixedLossScale`
* Class `tf.train.experimental.FixedLossScale`



Defined in [`python/training/experimental/loss_scale.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/experimental/loss_scale.py).

<!-- Placeholder for "Used in" -->

The loss scale is not updated for the lifetime of instances of this class.
A given instance of this class always returns the same number when called.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(loss_scale_value)
```

Creates the fixed loss scale.


#### Args:


* <b>`loss_scale_value`</b>: A Python float. Its ideal value varies depending on
  models to run. Choosing a too small loss_scale might affect model
  quality; a too big loss_scale might cause inf or nan. There is no single
  right loss_scale to apply. There is no harm choosing a relatively big
  number as long as no nan or inf is encountered in training.


#### Raises:


* <b>`ValueError`</b>: If loss_scale is less than 1.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__()
```




<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Creates the LossScale from its config.


<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```




<h3 id="update"><code>update</code></h3>

``` python
update(grads)
```






