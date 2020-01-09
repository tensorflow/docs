page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.mixed_precision.FixedLossScaleManager


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L73-L101">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `FixedLossScaleManager`

Loss scale manager with a fixed loss scale.

Inherits From: [`LossScaleManager`](../../../tf/contrib/mixed_precision/LossScaleManager)

<!-- Placeholder for "Used in" -->

The loss scale is not updated for the lifetime of the class.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L79-L94">View source</a>

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



## Methods

<h3 id="get_loss_scale"><code>get_loss_scale</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L96-L97">View source</a>

``` python
get_loss_scale()
```

Returns the loss scale as a scalar `float32` tensor.


<h3 id="update_loss_scale"><code>update_loss_scale</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/python/loss_scale_manager.py#L99-L101">View source</a>

``` python
update_loss_scale(finite_grads)
```

Updates loss scale based on if gradients are finite in current step.


#### Args:


* <b>`finite_grads`</b>: bool scalar tensor indicating if all gradients are
  finite (i.e., not inf or nan).


#### Returns:

An op, when executed updates the loss scale. If eager execution is
enabled, does not return anything.
