

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.kfac.utils.batch_execute

``` python
tf.contrib.kfac.utils.batch_execute(
    global_step,
    thunks,
    batch_size,
    name=None
)
```



Defined in [`tensorflow/contrib/kfac/python/ops/utils.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/kfac/python/ops/utils.py).

Executes a subset of ops per global step.

Given a list of thunks, each of which produces a single stateful op,
ensures that exactly 'batch_size' ops are run per global step. Ops are
scheduled in a round-robin fashion. For example, with 3 ops

  global_step | op0 | op1 | op2
  ------------+-----+-----+-----
      0       |  x  |  x  |
  ------------+-----+-----+-----
      1       |  x  |     |  x
  ------------+-----+-----+-----
      2       |     |  x  |  x
  ------------+-----+-----+-----
      3       |  x  |  x  |
  ------------+-----+-----+-----
      4       |  x  |     |  x

Does not guarantee order of op execution within a single global step.

#### Args:

* <b>`global_step`</b>: Tensor indicating time. Determines which ops run.
* <b>`thunks`</b>: List of thunks. Each thunk encapsulates one op. Return values are
    ignored.
* <b>`batch_size`</b>: int. Number of ops to execute per global_step.
* <b>`name`</b>: string or None. Name scope for newly added ops.


#### Returns:

List of ops. Exactly 'batch_size' ops are guaranteed to have an effect
every global step.