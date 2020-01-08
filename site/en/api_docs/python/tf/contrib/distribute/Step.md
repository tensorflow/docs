page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.distribute.Step

## Class `Step`





Defined in [`tensorflow/contrib/distribute/python/step_fn.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/distribute/python/step_fn.py).

Interface for performing each step of a training algorithm.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(distribution)
```





## Properties

<h3 id="distribution"><code>distribution</code></h3>





## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__()
```

Perform one step of this training algorithm.



