

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.metrics.Metric

## Class `Metric`





Defined in [`tensorflow/contrib/eager/python/metrics_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/eager/python/metrics_impl.py).

A metric holds state for aggregating statistics over an evaluation run.

Example use with eager execution:

```python
m = SomeMetric(...)
for input in ...:
  m(input)
print(m.result())
```

Example use with graph execution:

```python
m = SomeMetric(...)
inputs = ... # Some tensors to compute the metric on.
m_update = m(inputs)
# Variables defined in first call, so get the initialization op afterwards.
m_init = m.init_variables()  # or tf.global_variables_initializer()
m_result = m.result()
with tf.Session() as sess:
  sess.run(m_init)
  for input in ...:
    sess.run(m_update)
  print(sess.run(m_result))
```
Example use with graph execution with placeholders and feed_dict:

```python
m = SomeMetric(...)
m_placeholder = tf.placeholder(...)
m_update = m(m_placeholder)
# Variables defined in first call, so get the initialization op afterwards.
m_init = m.init_variables()  # or tf.global_variables_initializer()
m_result = m.result()
with tf.Session() as sess:
  sess.run(m_init)
  for input in ...:
    sess.run(m_update, feed_dict={m_placeholder: input})
  print(sess.run(m_result))
```

Descendants will implement:
* `build()`: All variables should be created in this method, by calling
  `self.add_variable()` as in: `self.var = self.add_variable(...)`
  build() will be called in the first invocation of `__call__()`, with
  the same arguments passed `call()`.
* `call()`: Has all updates to variables, as in:
    self.var.assign_add(...)
* `result()`: Computes and returns a final value for the metric
  from the variables in `self`.

Descendants may override `aggregate()`, but usually won't need to.  It
adds in the state from a list of metrics of the same type as `self`.
(Default is to sum all the variables.) Note that users should not call
`aggregate()`, it is for use by TensorFlow infrastructure.

## Properties

<h3 id="name"><code>name</code></h3>



<h3 id="variables"><code>variables</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    name=None,
    use_global_variables=False
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    *args,
    **kwargs
)
```

Returns op to execute to update this metric for these inputs.

Returns None if eager execution is enabled.
Returns a graph-mode function if graph execution is enabled.

#### Args:

* <b>`*args`</b>: * <b>`**kwargs`</b>: A mini-batch of inputs to the Metric, passed on to `call()`.

<h3 id="add_variable"><code>add_variable</code></h3>

``` python
add_variable(
    name,
    shape=None,
    dtype=None,
    initializer=None
)
```

***Only for use by descendants of Metric***.

<h3 id="aggregate"><code>aggregate</code></h3>

``` python
aggregate(metrics)
```

Adds in the state from a list of metrics.

Default implementation sums all the metric variables.

#### Args:

* <b>`metrics`</b>: A list of metrics with the same type as `self`.


#### Raises:

* <b>`ValueError`</b>: If metrics contains invalid data.

<h3 id="build"><code>build</code></h3>

``` python
build(
    *args,
    **kwargs
)
```

Method to create variables.

Called by `__call__()` before `call()` for the first time.

#### Args:

* <b>`*args`</b>: * <b>`**kwargs`</b>: The arguments to the first invocation of `__call__()`.
   `build()` may use the shape and/or dtype of these arguments
   when deciding how to create variables.

<h3 id="call"><code>call</code></h3>

``` python
call(
    *args,
    **kwargs
)
```

Accumulates statistics for the metric. Users should use __call__ instead.

Note: This function is executed as a graph function in graph mode.
This means:
a) Operations on the same resource are executed in textual order.
   This should make it easier to do things like add the updated
   value of a variable to another, for example.
b) You don't need to worry about collecting the update ops to execute.
   All update ops added to the graph by this function will be executed.
As a result, code should generally work the same way with graph or
eager execution.

#### Args:

* <b>`*args`</b>: * <b>`**kwargs`</b>: A mini-batch of inputs to the Metric, as passed to
    `__call__()`.

<h3 id="init_variables"><code>init_variables</code></h3>

``` python
init_variables()
```

Initializes this Metric's variables.

Should be called after variables are created in the first execution
of `__call__()`. If using graph execution, the return value should be
`run()` in a session before running the op returned by `__call__()`.
(See example above.)

#### Returns:

If using graph execution, this returns an op to perform the
initialization. Under eager execution, the variables are reset to their
initial values as a side effect and this function returns None.

<h3 id="result"><code>result</code></h3>

``` python
result()
```

Computes and returns a final value for the metric.

<h3 id="value"><code>value</code></h3>

``` python
value()
```

In graph mode returns the result Tensor while in eager the callable.



