page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.distributions.ReparameterizationType


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/distributions/distribution.py#L216-L259">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ReparameterizationType`

Instances of this class represent how sampling is reparameterized.



<!-- Placeholder for "Used in" -->

Two static instances exist in the distributions library, signifying
one of two possible properties for samples from a distribution:

`FULLY_REPARAMETERIZED`: Samples from the distribution are fully
  reparameterized, and straight-through gradients are supported.

`NOT_REPARAMETERIZED`: Samples from the distribution are not fully
  reparameterized, and straight-through gradients are either partially
  unsupported or are not supported at all. In this case, for purposes of
  e.g. RL or variational inference, it is generally safest to wrap the
  sample results in a `stop_gradients` call and use policy
  gradients / surrogate loss instead.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/distributions/distribution.py#L233-L242">View source</a>

``` python
__init__(rep_type)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2019-01-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of `tf.distributions`.



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/distributions/distribution.py#L247-L259">View source</a>

``` python
__eq__(other)
```

Determine if this `ReparameterizationType` is equal to another.

Since RepaparameterizationType instances are constant static global
instances, equality checks if two instances' id() values are equal.

#### Args:


* <b>`other`</b>: Object to compare against.


#### Returns:

`self is other`.
