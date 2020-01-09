page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.AGNCustomGetter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/agn_optimizer.py#L33-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `AGNCustomGetter`

Custom_getter class is used to do:



<!-- Placeholder for "Used in" -->

1. Change trainable variables to local collection and place them at worker
  device
2. Generate global variables(global center variables)
3. Generate grad variables(gradients) which record the gradients sum
  and place them at worker device
  Notice that the class should be used with tf.replica_device_setter,
  so that the global center variables and global step variable can be placed
  at ps device.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/agn_optimizer.py#L46-L53">View source</a>

``` python
__init__(worker_device)
```

Args:
  worker_device: put the grad_variables on worker device



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/agn_optimizer.py#L55-L91">View source</a>

``` python
__call__(
    getter,
    name,
    trainable,
    collections,
    *args,
    **kwargs
)
```

Call self as a function.
