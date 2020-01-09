page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.ModelAverageCustomGetter


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/model_average_optimizer.py#L36-L100">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ModelAverageCustomGetter`

Custom_getter class is used to do.



<!-- Placeholder for "Used in" -->

1. Change trainable variables to local collection and place them at worker
  device
2. Generate global variables
  Notice that the class should be used with tf.replica_device_setter,
  so that the global center variables and global step variable can be placed
  at ps device. Besides, use 'tf.compat.v1.get_variable' instead of
  'tf.Variable' to
  use this custom getter.

For example,
ma_custom_getter = ModelAverageCustomGetter(worker_device)
with tf.device(
  tf.compat.v1.train.replica_device_setter(
    worker_device=worker_device,
    ps_device="/job:ps/cpu:0",
    cluster=cluster)),
  tf.compat.v1.variable_scope('',custom_getter=ma_custom_getter):
  hid_w = tf.compat.v1.get_variable(
    initializer=tf.random.truncated_normal(
        [IMAGE_PIXELS * IMAGE_PIXELS, FLAGS.hidden_units],
        stddev=1.0 / IMAGE_PIXELS),
    name="hid_w")
  hid_b =
  tf.compat.v1.get_variable(initializer=tf.zeros([FLAGS.hidden_units]),
                          name="hid_b")

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/model_average_optimizer.py#L66-L73">View source</a>

``` python
__init__(worker_device)
```

Create a new `ModelAverageCustomGetter`.


#### Args:


* <b>`worker_device`</b>: String.  Name of the `worker` job.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/opt/python/training/model_average_optimizer.py#L75-L100">View source</a>

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
