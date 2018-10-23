

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.get_or_create_eval_step

``` python
get_or_create_eval_step()
```



Defined in [`tensorflow/python/training/evaluation.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/training/evaluation.py).

Gets or creates the eval step `Tensor`.

#### Returns:

A `Tensor` representing a counter for the evaluation step.


#### Raises:

* <b>`ValueError`</b>: If multiple `Tensors` have been added to the
    `tf.GraphKeys.EVAL_STEP` collection.