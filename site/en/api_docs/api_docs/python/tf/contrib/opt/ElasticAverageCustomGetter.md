

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.opt.ElasticAverageCustomGetter

## Class `ElasticAverageCustomGetter`





Defined in [`tensorflow/contrib/opt/python/training/elastic_average_optimizer.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/opt/python/training/elastic_average_optimizer.py).

Custom_getter class is used to do:
1. Change trainable variables to local collection and place them at worker
  device
2. Generate global variables(global center variables)
3. Generate local variables(local center variables) which record the global
  variables and place them at worker device
  Notice that the class should be used with tf.replica_device_setter,
  so that the global center variables and global step variable can be placed
  at ps device. Besides, use 'tf.get_variable' instead of 'tf.Variable' to
  use this custom getter.

For example,
ea_custom_getter = ElasticAverageCustomGetter(worker_device)
with tf.device(
  tf.train.replica_device_setter(
    worker_device=worker_device,
    ps_device="/job:ps/cpu:0",
    cluster=cluster)),
  tf.variable_scope('',custom_getter=ea_custom_getter):
  hid_w = tf.get_variable(
    initializer=tf.truncated_normal(
        [IMAGE_PIXELS * IMAGE_PIXELS, FLAGS.hidden_units],
        stddev=1.0 / IMAGE_PIXELS),
    name="hid_w")
  hid_b = tf.get_variable(initializer=tf.zeros([FLAGS.hidden_units]),
                          name="hid_b")

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(worker_device)
```

Create a new `ElasticAverageCustomGetter`.

#### Args:

* <b>`worker_device`</b>: String.  Name of the `worker` job.

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





