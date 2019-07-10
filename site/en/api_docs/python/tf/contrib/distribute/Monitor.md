page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.Monitor

## Class `Monitor`

Executes training steps, recovers and checkpoints.





Defined in [`contrib/distribute/python/monitor.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/distribute/python/monitor.py).

<!-- Placeholder for "Used in" -->

Note that this class is particularly preliminary, experimental, and
expected to change.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    step_callable,
    session=None
)
```

Initialize the Monitor with components for executing training steps.


#### Args:


* <b>`step_callable`</b>: a training `Step` that's capable of signaling when done.
* <b>`session`</b>: a `Session` instance that's needed for graph mode.


#### Raises:


* <b>`ValueError`</b>: if `session` was provided for eager mode or not provided for
  graph mode.



## Methods

<h3 id="run_steps"><code>run_steps</code></h3>

``` python
run_steps(num_steps=None)
```






