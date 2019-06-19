

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.StandardInputStep

## Class `StandardInputStep`

Inherits From: [`Step`](../../../tf/contrib/distribute/Step)



Defined in [`tensorflow/contrib/distribute/python/step_fn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/distribute/python/step_fn.py).

Step with a standard implementation of input handling.

#### Args:

* <b>`input_dataset`</b>: a tf.data Dataset that provides input.

## Properties

<h3 id="distribution"><code>distribution</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    input_dataset,
    distribution
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__()
```

Perform one step of this training algorithm.

<h3 id="inputs"><code>inputs</code></h3>

``` python
inputs()
```



<h3 id="step"><code>step</code></h3>

``` python
step(inputs)
```

Perform the main computation of this training algorithm.



