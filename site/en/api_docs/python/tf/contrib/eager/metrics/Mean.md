page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.metrics.Mean


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L293-L362">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Mean`

Computes the (weighted) mean of the given values.

Inherits From: [`Metric`](../../../../tf/contrib/eager/metrics/Metric)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L296-L300">View source</a>

``` python
__init__(
    name=None,
    dtype=tf.dtypes.double,
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L302-L311">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L313-L338">View source</a>

``` python
call(
    values,
    weights=None
)
```

Accumulate statistics for computing the mean.

For example, if values is [1, 3, 5, 7] then the mean is 4.
If the weights were specified as [1, 1, 0, 0] then the mean would be 2.

#### Args:


* <b>`values`</b>: Tensor with the per-example value.
* <b>`weights`</b>: Optional weighting of each example. Defaults to 1.


#### Returns:

The arguments, for easy chaining.


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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L340-L362">View source</a>

``` python
result(write_summary=True)
```

Returns the result of the Metric.


#### Args:


* <b>`write_summary`</b>: bool indicating whether to feed the result to the summary
  before returning.

#### Returns:

aggregated metric as float.


#### Raises:


* <b>`ValueError`</b>: if the optional argument is not bool

<h3 id="value"><code>value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/eager/python/metrics_impl.py#L217-L222">View source</a>

``` python
value()
```

In graph mode returns the result Tensor while in eager the callable.
