page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.StandardInputStep

## Class `StandardInputStep`

Inherits From: [`Step`](../../../tf/contrib/distribute/Step)



Defined in [`tensorflow/contrib/distribute/python/step_fn.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/distribute/python/step_fn.py).

Step with a standard implementation of input handling.

#### Args:

* <b>`dataset_fn`</b>: a function that returns a tf.data Dataset that produces the
    input for the model.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dataset_fn,
    distribution
)
```





## Properties

<h3 id="distribution"><code>distribution</code></h3>





## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__()
```

Perform one step of this training algorithm.



