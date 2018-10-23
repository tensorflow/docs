

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.Assert

``` python
tf.Assert(
    condition,
    data,
    summarize=None,
    name=None
)
```



Defined in [`tensorflow/python/ops/control_flow_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/ops/control_flow_ops.py).

See the guide: [Control Flow > Debugging Operations](../../../api_guides/python/control_flow_ops#Debugging_Operations)

Asserts that the given condition is true.

If `condition` evaluates to false, print the list of tensors in `data`.
`summarize` determines how many entries of the tensors to print.

NOTE: In graph mode, to ensure that Assert executes, one usually attaches
a dependency:

```python
# Ensure maximum element of x is smaller or equal to 1
assert_op = tf.Assert(tf.less_equal(tf.reduce_max(x), 1.), [x])
with tf.control_dependencies([assert_op]):
  ... code using x ...
```

#### Args:

* <b>`condition`</b>: The condition to evaluate.
* <b>`data`</b>: The tensors to print out when condition is false.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

* <b>`assert_op`</b>: An `Operation` that, when executed, raises a
  <a href="../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a> if `condition` is not true.
  @compatibility{eager} returns None.


#### Raises:

  @compatibility{eager} <a href="../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a> if `condition`
  is not true


**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.