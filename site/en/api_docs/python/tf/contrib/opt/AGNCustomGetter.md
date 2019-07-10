page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.AGNCustomGetter

## Class `AGNCustomGetter`





Defined in [`tensorflow/contrib/opt/python/training/agn_optimizer.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/opt/python/training/agn_optimizer.py).

Custom_getter class is used to do:

1. Change trainable variables to local collection and place them at worker
  device
2. Generate global variables(global center variables)
3. Generate grad variables(gradients) which record the gradients sum
  and place them at worker device
  Notice that the class should be used with tf.replica_device_setter,
  so that the global center variables and global step variable can be placed
  at ps device.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(worker_device)
```

Args:
  worker_device: put the grad_variables on worker device



## Methods

<h3 id="__call__"><code>__call__</code></h3>

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



