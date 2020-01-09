page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.RegisterGradient


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/RegisterGradient">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L2445-L2487">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RegisterGradient`

A decorator for registering the gradient function for an op type.



### Aliases:

* Class <a href="/api_docs/python/tf/RegisterGradient"><code>tf.compat.v1.RegisterGradient</code></a>
* Class <a href="/api_docs/python/tf/RegisterGradient"><code>tf.compat.v2.RegisterGradient</code></a>


<!-- Placeholder for "Used in" -->

This decorator is only used when defining a new op type. For an op
with `m` inputs and `n` outputs, the gradient function is a function
that takes the original `Operation` and `n` `Tensor` objects
(representing the gradients with respect to each output of the op),
and returns `m` `Tensor` objects (representing the partial gradients
with respect to each input of the op).

For example, assuming that operations of type `"Sub"` take two
inputs `x` and `y`, and return a single output `x - y`, the
following gradient function would be registered:

```python
@tf.RegisterGradient("Sub")
def _sub_grad(unused_op, grad):
  return grad, tf.negative(grad)
```

The decorator argument `op_type` is the string type of an
operation. This corresponds to the `OpDef.name` field for the proto
that defines the operation.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L2470-L2482">View source</a>

``` python
__init__(op_type)
```

Creates a new decorator with `op_type` as the Operation type.


#### Args:


* <b>`op_type`</b>: The string type of an operation. This corresponds to the
  `OpDef.name` field for the proto that defines the operation.


#### Raises:


* <b>`TypeError`</b>: If `op_type` is not string.



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/ops.py#L2484-L2487">View source</a>

``` python
__call__(f)
```

Registers the function `f` as gradient function for `op_type`.
