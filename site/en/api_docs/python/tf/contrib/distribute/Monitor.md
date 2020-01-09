page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.Monitor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distribute/python/monitor.py#L26-L65">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Monitor`

Executes training steps, recovers and checkpoints.



<!-- Placeholder for "Used in" -->

Note that this class is particularly preliminary, experimental, and
expected to change.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distribute/python/monitor.py#L36-L56">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/distribute/python/monitor.py#L58-L65">View source</a>

``` python
run_steps(num_steps=None)
```
