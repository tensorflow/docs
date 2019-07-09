page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.gan.CycleGANLoss

## Class `CycleGANLoss`





Defined in [`tensorflow/contrib/gan/python/namedtuples.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/gan/python/namedtuples.py).

CycleGANLoss contains the losses for `CycleGANModel`.

See https://arxiv.org/abs/1703.10593 for more details.

#### Args:

* <b>`loss_x2y`</b>: A `GANLoss` namedtuple representing the loss of `model_x2y`.
* <b>`loss_y2x`</b>: A `GANLoss` namedtuple representing the loss of `model_y2x`.

## Properties

<h3 id="loss_x2y"><code>loss_x2y</code></h3>

Alias for field number 0

<h3 id="loss_y2x"><code>loss_y2x</code></h3>

Alias for field number 1



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
__new__(
    _cls,
    loss_x2y,
    loss_y2x
)
```

Create new instance of CycleGANLoss(loss_x2y, loss_y2x)



