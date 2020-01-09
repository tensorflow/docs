page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.metrics.Metric


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L40-L290">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Metric`

A metric holds state for aggregating statistics over an evaluation run.

Inherits From: [`CheckpointableBase`](../../../../tf/contrib/checkpoint/CheckpointableBase)

<!-- Placeholder for "Used in" -->

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
m_init = m.init_variables()  # or tf.compat.v1.global_variables_initializer()
m_result = m.result()
with tf.compat.v1.Session() as sess:
  sess.run(m_init)
  for input in ...:
    sess.run(m_update)
  print(sess.run(m_result))
```
Example use with graph execution with placeholders and feed_dict:

```python
m = SomeMetric(...)
m_placeholder = tf.compat.v1.placeholder(...)
m_update = m(m_placeholder)
# Variables defined in first call, so get the initialization op afterwards.
m_init = m.init_variables()  # or tf.compat.v1.global_variables_initializer()
m_result = m.result()
with tf.compat.v1.Session() as sess:
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

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L98-L132">View source</a>

``` python
__init__(
    name=None,
    use_global_variables=False
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Properties

<h3 id="name"><code>name</code></h3>




<h3 id="variables"><code>variables</code></h3>






## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L135-L150">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L260-L290">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L237-L256">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L180-L191">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L193-L211">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L160-L177">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L213-L215">View source</a>

``` python
result()
```

Computes and returns a final value for the metric.


<h3 id="value"><code>value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L217-L222">View source</a>

``` python
value()
```

In graph mode returns the result Tensor while in eager the callable.
