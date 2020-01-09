page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.Assert


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/Assert">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/control_flow_ops.py#L112-L176">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Asserts that the given condition is true.

### Aliases:

* <a href="/api_docs/python/tf/debugging/Assert"><code>tf.Assert</code></a>
* <a href="/api_docs/python/tf/debugging/Assert"><code>tf.compat.v1.Assert</code></a>
* <a href="/api_docs/python/tf/debugging/Assert"><code>tf.compat.v1.debugging.Assert</code></a>
* <a href="/api_docs/python/tf/debugging/Assert"><code>tf.compat.v2.Assert</code></a>
* <a href="/api_docs/python/tf/debugging/Assert"><code>tf.compat.v2.debugging.Assert</code></a>


``` python
tf.debugging.Assert(
    condition,
    data,
    summarize=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

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
<a href="../../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a> if `condition` is not true.



#### Raises:





**NOTE** The output of this function should be used.  If it is not, a warning will be logged.  To mark the output as used, call its .mark_used() method.

#### Eager Compatibility
<a href="../../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a> if `condition` is not true
