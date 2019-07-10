page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.while_loop

Builds a training loop for TPUs.

``` python
tf.contrib.tpu.while_loop(
    condition,
    body,
    inputs=None,
    infeed_queue=None,
    name=None
)
```



Defined in [`python/tpu/training_loop.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/tpu/training_loop.py).

<!-- Placeholder for "Used in" -->

The set of loop-carried tensors corresponds to `inputs`.  Both
`condition` and `body` take the current value of the loop-carried
tensors. 'body' additionally takes a tuple of infeed from
infeed_queue if infeed_queue is not None. `condition` must return a
single boolean value that determines whether iteration
continues. `body` must return an updated list of values for the
loop-carried tensors.

#### Args:


* <b>`condition`</b>: a Python function that builds the loop condition.
* <b>`body`</b>: a Python function that builds the loop body.
* <b>`inputs`</b>: a list of initial values passed into the training loop, or
  None (equivalent to an empty list).
* <b>`infeed_queue`</b>: if not None, the infeed queue from which to append a tuple
  of arguments as inputs to condition.
* <b>`name`</b>: (Deprecated) Does nothing.


#### Returns:

The final values of the loop-carried tensors.



#### Raises:


* <b>`TypeError`</b>: if body or condition has the wrong signature.