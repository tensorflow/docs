

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.training.get_or_create_eval_step

``` python
tf.contrib.training.get_or_create_eval_step()
```



Defined in [`tensorflow/python/training/evaluation.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/training/evaluation.py).

Gets or creates the eval step `Tensor`.

#### Returns:

A `Tensor` representing a counter for the evaluation step.


#### Raises:

* <b>`ValueError`</b>: If multiple `Tensors` have been added to the
    <a href="../../../tf/GraphKeys#EVAL_STEP"><code>tf.GraphKeys.EVAL_STEP</code></a> collection.