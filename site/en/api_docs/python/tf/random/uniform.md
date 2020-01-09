page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.random.uniform


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/random/uniform">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/random_ops.py#L186-L252">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Outputs random values from a uniform distribution.

### Aliases:

* <a href="/api_docs/python/tf/random/uniform"><code>tf.compat.v1.random.uniform</code></a>
* <a href="/api_docs/python/tf/random/uniform"><code>tf.compat.v1.random_uniform</code></a>
* <a href="/api_docs/python/tf/random/uniform"><code>tf.compat.v2.random.uniform</code></a>
* <a href="/api_docs/python/tf/random/uniform"><code>tf.random_uniform</code></a>


``` python
tf.random.uniform(
    shape,
    minval=0,
    maxval=None,
    dtype=tf.dtypes.float32,
    seed=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The generated values follow a uniform distribution in the range
`[minval, maxval)`. The lower bound `minval` is included in the range, while
the upper bound `maxval` is excluded.

For floats, the default range is `[0, 1)`.  For ints, at least `maxval` must
be specified explicitly.

In the integer case, the random integers are slightly biased unless
`maxval - minval` is an exact power of two.  The bias is small for values of
`maxval - minval` significantly smaller than the range of the output (either
`2**32` or `2**64`).

#### Args:


* <b>`shape`</b>: A 1-D integer Tensor or Python array. The shape of the output tensor.
* <b>`minval`</b>: A 0-D Tensor or Python value of type `dtype`. The lower bound on the
  range of random values to generate.  Defaults to 0.
* <b>`maxval`</b>: A 0-D Tensor or Python value of type `dtype`. The upper bound on
  the range of random values to generate.  Defaults to 1 if `dtype` is
  floating point.
* <b>`dtype`</b>: The type of the output: `float16`, `float32`, `float64`, `int32`,
  or `int64`.
* <b>`seed`</b>: A Python integer. Used to create a random seed for the distribution.
  See <a href="../../tf/random/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a>
  for behavior.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor of the specified shape filled with random uniform values.



#### Raises:


* <b>`ValueError`</b>: If `dtype` is integral and `maxval` is not specified.
