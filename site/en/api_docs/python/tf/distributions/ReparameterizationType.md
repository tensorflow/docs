page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distributions.ReparameterizationType

## Class `ReparameterizationType`

Instances of this class represent how sampling is reparameterized.



### Aliases:

* Class `tf.compat.v1.distributions.ReparameterizationType`
* Class `tf.contrib.distributions.ReparameterizationType`
* Class `tf.distributions.ReparameterizationType`



Defined in [`python/ops/distributions/distribution.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/distributions/distribution.py).

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

``` python
__init__(rep_type)
```

DEPRECATED FUNCTION

Warning: THIS FUNCTION IS DEPRECATED. It will be removed after 2019-01-01.
Instructions for updating:
The TensorFlow Distributions library has moved to TensorFlow Probability (https://github.com/tensorflow/probability). You should update all references to use `tfp.distributions` instead of <a href="../../tf/distributions"><code>tf.distributions</code></a>.



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

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




