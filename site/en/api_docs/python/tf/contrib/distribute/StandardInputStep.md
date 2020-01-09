page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.StandardInputStep


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L45-L58">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `StandardInputStep`

Step with a standard implementation of input handling.

Inherits From: [`Step`](../../../tf/contrib/distribute/Step)

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`dataset_fn`</b>: a function that returns a tf.data Dataset that produces the
  input for the model.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L53-L55">View source</a>

``` python
__init__(
    dataset_fn,
    distribution
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="distribution"><code>distribution</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L38-L40">View source</a>

``` python
__call__()
```

Perform one step of this training algorithm.


<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/step_fn.py#L57-L58">View source</a>

``` python
initialize()
```
