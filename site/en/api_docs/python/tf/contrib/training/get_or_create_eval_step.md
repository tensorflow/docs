page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.get_or_create_eval_step

Gets or creates the eval step `Tensor`.

``` python
tf.contrib.training.get_or_create_eval_step()
```



Defined in [`python/training/evaluation.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/training/evaluation.py).

<!-- Placeholder for "Used in" -->


#### Returns:

A `Tensor` representing a counter for the evaluation step.



#### Raises:


* <b>`ValueError`</b>: If multiple `Tensors` have been added to the
  <a href="../../../tf/GraphKeys#EVAL_STEP"><code>tf.GraphKeys.EVAL_STEP</code></a> collection.