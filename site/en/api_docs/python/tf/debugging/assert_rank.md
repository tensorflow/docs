page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.debugging.assert_rank


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/debugging/assert_rank">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/check_ops.py#L1096-L1155">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Assert `x` has rank equal to `rank`.

### Aliases:

* <a href="/api_docs/python/tf/debugging/assert_rank"><code>tf.assert_rank</code></a>
* <a href="/api_docs/python/tf/debugging/assert_rank"><code>tf.compat.v1.assert_rank</code></a>
* <a href="/api_docs/python/tf/debugging/assert_rank"><code>tf.compat.v1.debugging.assert_rank</code></a>


``` python
tf.debugging.assert_rank(
    x,
    rank,
    data=None,
    summarize=None,
    message=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Example of adding a dependency to an operation:

```python
with tf.control_dependencies([tf.compat.v1.assert_rank(x, 2)]):
  output = tf.reduce_sum(x)
```

#### Args:


* <b>`x`</b>:  Numeric `Tensor`.
* <b>`rank`</b>:  Scalar integer `Tensor`.
* <b>`data`</b>:  The tensors to print out if the condition is False.  Defaults to
  error message and the shape of `x`.
* <b>`summarize`</b>: Print this many entries of each tensor.
* <b>`message`</b>: A string to prefix to the default message.
* <b>`name`</b>: A name for this operation (optional).  Defaults to "assert_rank".


#### Returns:

Op raising `InvalidArgumentError` unless `x` has specified rank.
If static checks determine `x` has correct rank, a `no_op` is returned.



#### Raises:


* <b>`ValueError`</b>:  If static checks determine `x` has wrong rank.
