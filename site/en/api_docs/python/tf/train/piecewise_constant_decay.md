page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.piecewise_constant_decay


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/training/learning_rate_decay.py#L106-L179">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Piecewise constant from boundaries and interval values.

### Aliases:

* <a href="/api_docs/python/tf/train/piecewise_constant_decay"><code>tf.compat.v1.train.piecewise_constant</code></a>
* <a href="/api_docs/python/tf/train/piecewise_constant_decay"><code>tf.compat.v1.train.piecewise_constant_decay</code></a>
* <a href="/api_docs/python/tf/train/piecewise_constant_decay"><code>tf.train.piecewise_constant</code></a>


``` python
tf.train.piecewise_constant_decay(
    x,
    boundaries,
    values,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Example: use a learning rate that's 1.0 for the first 100001 steps, 0.5
  for the next 10000 steps, and 0.1 for any additional steps.

```python
global_step = tf.Variable(0, trainable=False)
boundaries = [100000, 110000]
values = [1.0, 0.5, 0.1]
learning_rate = tf.compat.v1.train.piecewise_constant(global_step, boundaries,
values)

# Later, whenever we perform an optimization step, we increment global_step.
```

#### Args:


* <b>`x`</b>: A 0-D scalar `Tensor`. Must be one of the following types: `float32`,
  `float64`, `uint8`, `int8`, `int16`, `int32`, `int64`.
* <b>`boundaries`</b>: A list of `Tensor`s or `int`s or `float`s with strictly
  increasing entries, and with all elements having the same type as `x`.
* <b>`values`</b>: A list of `Tensor`s or `float`s or `int`s that specifies the values
  for the intervals defined by `boundaries`. It should have one more element
  than `boundaries`, and all elements should have the same type.
* <b>`name`</b>: A string. Optional name of the operation. Defaults to
  'PiecewiseConstant'.


#### Returns:

A 0-D Tensor. Its value is `values[0]` when `x <= boundaries[0]`,
`values[1]` when `x > boundaries[0]` and `x <= boundaries[1]`, ...,
and values[-1] when `x > boundaries[-1]`.



#### Raises:


* <b>`ValueError`</b>: if types of `x` and `boundaries` do not match, or types of all
    `values` do not match or
    the number of elements in the lists does not match.



#### Eager Compatibility
When eager execution is enabled, this function returns a function which in
turn returns the decayed learning rate Tensor. This can be useful for changing
the learning rate value across different invocations of optimizer functions.
