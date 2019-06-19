page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.TensorSpec

## Class `TensorSpec`





Defined in [`tensorflow/python/framework/tensor_spec.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/framework/tensor_spec.py).

Describes a tf.Tensor.

A TensorSpec allows an API to describe the Tensors that it accepts or
returns, before that Tensor exists. This allows dynamic and flexible graph
construction and configuration.

## Properties

<h3 id="dtype"><code>dtype</code></h3>

Returns the `dtype` of elements in the tensor.

<h3 id="is_continuous"><code>is_continuous</code></h3>

Whether spec is continuous.

<h3 id="is_discrete"><code>is_discrete</code></h3>

Whether spec is discrete.

<h3 id="name"><code>name</code></h3>

Returns the name of the described tensor.

<h3 id="shape"><code>shape</code></h3>

Returns the `TensorShape` that represents the shape of the tensor.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    shape,
    dtype,
    name=None
)
```

Creates a TensorSpec.

#### Args:

* <b>`shape`</b>: Value convertible to <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a>. The shape of the tensor.
* <b>`dtype`</b>: Value convertible to <a href="../../../tf/DType"><code>tf.DType</code></a>. The type of the tensor values.
* <b>`name`</b>: Optional name for the Tensor.


#### Raises:

* <b>`TypeError`</b>: If shape is not convertible to a <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a>, or dtype is
    not convertible to a <a href="../../../tf/DType"><code>tf.DType</code></a>.

<h3 id="__eq__"><code>__eq__</code></h3>

``` python
__eq__(other)
```



<h3 id="__ne__"><code>__ne__</code></h3>

``` python
__ne__(other)
```



<h3 id="__reduce__"><code>__reduce__</code></h3>

``` python
__reduce__()
```



<h3 id="from_spec"><code>from_spec</code></h3>

``` python
@classmethod
from_spec(
    cls,
    spec,
    name=None
)
```



<h3 id="from_tensor"><code>from_tensor</code></h3>

``` python
@classmethod
from_tensor(
    cls,
    tensor,
    name=None
)
```



<h3 id="is_bounded"><code>is_bounded</code></h3>

``` python
@classmethod
is_bounded(cls)
```



<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

``` python
is_compatible_with(spec_or_tensor)
```

True if the shape and dtype of `spec_or_tensor` are compatible.



