page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.StandardSingleLossStep

## Class `StandardSingleLossStep`

Inherits From: [`StandardInputStep`](../../../tf/contrib/distribute/StandardInputStep)



Defined in [`tensorflow/contrib/distribute/python/step_fn.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/distribute/python/step_fn.py).

A step function that implements a training step for a feed forward network.

An instance of this class is intended to be used as a callable:

```python
...
step = step_fn.StandardSingleLossStep(
    dataset, loss_fn, optimizer, distribution)

# Run a single training step on a given DistributionStrategy:
step(distribution)
...
```

#### Args:

* <b>`dataset_fn`</b>: a function that returns a tf.data Dataset that produces the
    input for the model.
* <b>`loss_fn`</b>: a function that takes a context and inputs as arguments. It returns
    the loss for those inputs. `context` is an instance of
    `values.MultiStepContext` that will be passed when `loss_fn` is run.
    `context` can be used to specify the outputs to be returned from
    `loss_fn`, among other things.
* <b>`optimizer`</b>: an optimizer that implements an update rule.
* <b>`distribution`</b>: a `DistributionStrategy` object.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dataset_fn,
    loss_fn,
    optimizer,
    distribution,
    iterations_per_step=1
)
```





## Properties

<h3 id="distribution"><code>distribution</code></h3>





## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__()
```





