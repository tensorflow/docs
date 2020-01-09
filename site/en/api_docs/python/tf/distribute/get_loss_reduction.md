page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.get_loss_reduction


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/distribute/distribute_lib.py#L172-L191">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



<a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction.

### Aliases:

* <a href="/api_docs/python/tf/distribute/get_loss_reduction"><code>tf.compat.v1.distribute.get_loss_reduction</code></a>
* <a href="/api_docs/python/tf/distribute/get_loss_reduction"><code>tf.contrib.distribute.get_loss_reduction</code></a>


``` python
tf.distribute.get_loss_reduction()
```



<!-- Placeholder for "Used in" -->

This is used to decide whether loss should be scaled in optimizer (used only
for estimator + v1 optimizer use case).

#### Returns:

<a href="../../tf/distribute/ReduceOp"><code>tf.distribute.ReduceOp</code></a> corresponding to the last loss reduction for
estimator and v1 optimizer use case. <a href="../../tf/distribute/ReduceOp#SUM"><code>tf.distribute.ReduceOp.SUM</code></a> otherwise.
