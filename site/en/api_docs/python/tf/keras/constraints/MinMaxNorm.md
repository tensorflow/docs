page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.constraints.MinMaxNorm


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/constraints/MinMaxNorm">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L122-L171">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `MinMaxNorm`

MinMaxNorm weight constraint.

Inherits From: [`Constraint`](../../../tf/keras/constraints/Constraint)

### Aliases:

* Class <a href="/api_docs/python/tf/keras/constraints/MinMaxNorm"><code>tf.compat.v1.keras.constraints.MinMaxNorm</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/MinMaxNorm"><code>tf.compat.v1.keras.constraints.min_max_norm</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/MinMaxNorm"><code>tf.compat.v2.keras.constraints.MinMaxNorm</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/MinMaxNorm"><code>tf.compat.v2.keras.constraints.min_max_norm</code></a>
* Class <a href="/api_docs/python/tf/keras/constraints/MinMaxNorm"><code>tf.keras.constraints.min_max_norm</code></a>


<!-- Placeholder for "Used in" -->

Constrains the weights incident to each hidden unit
to have the norm between a lower bound and an upper bound.

#### Arguments:


* <b>`min_value`</b>: the minimum norm for the incoming weights.
* <b>`max_value`</b>: the maximum norm for the incoming weights.
* <b>`rate`</b>: rate for enforcing the constraint: weights will be
    rescaled to yield
    `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`.
    Effectively, this means that rate=1.0 stands for strict
    enforcement of the constraint, while rate<1.0 means that
    weights will be rescaled at each step to slowly move
    towards a value inside the desired interval.
* <b>`axis`</b>: integer, axis along which to calculate weight norms.
    For instance, in a `Dense` layer the weight matrix
    has shape `(input_dim, output_dim)`,
    set `axis` to `0` to constrain each weight vector
    of length `(input_dim,)`.
    In a `Conv2D` layer with `data_format="channels_last"`,
    the weight tensor has shape
    `(rows, cols, input_depth, output_depth)`,
    set `axis` to `[0, 1, 2]`
    to constrain the weights of each filter tensor of size
    `(rows, cols, input_depth)`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L151-L155">View source</a>

``` python
__init__(
    min_value=0.0,
    max_value=1.0,
    rate=1.0,
    axis=0
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L157-L163">View source</a>

``` python
__call__(w)
```

Call self as a function.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/constraints.py#L165-L171">View source</a>

``` python
get_config()
```
