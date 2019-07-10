page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.RandomStrategy

## Class `RandomStrategy`

Returns a random PS task for op placement.





Defined in [`contrib/training/python/training/device_setter.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/training/python/training/device_setter.py).

<!-- Placeholder for "Used in" -->

This may perform better than the default round-robin placement if you
have a large number of variables. Depending on your architecture and
number of parameter servers, round-robin can lead to situations where
all of one type of variable is placed on a single PS task, which may
lead to contention issues.

This strategy uses a hash function on the name of each op for deterministic
placement.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_ps_tasks,
    seed=0
)
```

Creates a new `RandomStrategy`.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(op)
```

Chooses a ps task index for the given `Operation`.




