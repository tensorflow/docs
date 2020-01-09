page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.StandardSingleLossStep


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L61-L114">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StandardSingleLossStep`

A step function that implements a training step for a feed forward network.

Inherits From: [`StandardInputStep`](../../../tf/contrib/distribute/StandardInputStep)

<!-- Placeholder for "Used in" -->

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L88-L93">View source</a>

``` python
__init__(
    dataset_fn,
    loss_fn,
    optimizer,
    distribution,
    iterations_per_step=1
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="distribution"><code>distribution</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L95-L114">View source</a>

``` python
__call__()
```

Perform one step of this training algorithm.


<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L57-L58">View source</a>

``` python
initialize()
```
