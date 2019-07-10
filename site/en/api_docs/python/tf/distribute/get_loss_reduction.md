page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_loss_reduction

<a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

### Aliases:

* `tf.compat.v1.distribute.get_loss_reduction`
* `tf.contrib.distribute.get_loss_reduction`
* `tf.distribute.get_loss_reduction`

``` python
tf.distribute.get_loss_reduction()
```



Defined in [`python/distribute/distribute_lib.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/distribute_lib.py).

<!-- Placeholder for "Used in" -->

This is used to decide whether loss should be scaled in optimizer (used only
for estimator + v1 optimizer use case).

#### Returns:

<a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction for
estimator and v1 optimizer use case. <a href="../../tf/distribute/ReduceOp#SUM"><code>tf.distribute.ReduceOp.SUM</code></a> otherwise.
