

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.op_queue.OpQueue

## Class `OpQueue`





Defined in [`tensorflow/contrib/kfac/python/ops/op_queue.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/kfac/python/ops/op_queue.py).

Class for choosing which Op to run next.

Constructs an infinitely repeating sequence of Ops in shuffled order.

In K-FAC, this can be used to distribute inverse update operations among
workers.

## Properties

<h3 id="ops"><code>ops</code></h3>

Ops this OpQueue can return in next_op().



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    ops,
    seed=None
)
```

Initializes an OpQueue.

#### Args:

* <b>`ops`</b>: list of TensorFlow Ops. Ops to be selected from. All workers must
    initialize with the same set of ops.
* <b>`seed`</b>: int or None. Random seed used when shuffling order of ops.

<h3 id="next_op"><code>next_op</code></h3>

``` python
next_op(sess)
```

Chooses which op to run next.

Note: This call will make a call to sess.run().

#### Args:

* <b>`sess`</b>: tf.Session.


#### Returns:

Next Op chosen from 'ops'.



