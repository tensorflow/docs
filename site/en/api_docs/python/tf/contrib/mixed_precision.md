page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.mixed_precision


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/mixed_precision/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Library for mixed precision training.

<!-- Placeholder for "Used in" -->


## Classes

[`class ExponentialUpdateLossScaleManager`](../../tf/contrib/mixed_precision/ExponentialUpdateLossScaleManager): Loss scale manager uses an exponential update strategy.

[`class FixedLossScaleManager`](../../tf/contrib/mixed_precision/FixedLossScaleManager): Loss scale manager with a fixed loss scale.

[`class LossScaleManager`](../../tf/contrib/mixed_precision/LossScaleManager): Abstract loss scale manager class.

[`class LossScaleOptimizer`](../../tf/contrib/mixed_precision/LossScaleOptimizer): An optimizer that applies loss scaling in backprop.
