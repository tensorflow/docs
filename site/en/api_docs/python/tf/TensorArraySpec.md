page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.TensorArraySpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/tensor_array_ops.py#L1243-L1341">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TensorArraySpec`

Type specification for a <a href="../tf/TensorArray"><code>tf.TensorArray</code></a>.

Inherits From: [`TypeSpec`](../tf/TypeSpec)

### Aliases:

* Class `tf.compat.v1.TensorArraySpec`
* Class `tf.compat.v2.TensorArraySpec`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/tensor_array_ops.py#L1250-L1263">View source</a>

``` python
__init__(
    element_shape=None,
    dtype=tf.dtypes.float32,
    dynamic_size=False,
    infer_shape=True
)
```

Constructs a type specification for a <a href="../tf/TensorArray"><code>tf.TensorArray</code></a>.


#### Args:


* <b>`element_shape`</b>: The shape of each element in the `TensorArray`.
* <b>`dtype`</b>: Data type of the `TensorArray`.
* <b>`dynamic_size`</b>: Whether the `TensorArray` can grow past its initial size.
* <b>`infer_shape`</b>: Whether shape inference is enabled.



## Properties

<h3 id="value_type"><code>value_type</code></h3>






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/type_spec.py#L262-L265">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/type_spec.py#L267-L268">View source</a>

``` python
__ne__(other)
```

Return self!=value.


<h3 id="from_value"><code>from_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/tensor_array_ops.py#L1320-L1330">View source</a>

``` python
@staticmethod
from_value(value)
```




<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/tensor_array_ops.py#L1265-L1274">View source</a>

``` python
is_compatible_with(other)
```

Returns true if `spec_or_value` is compatible with this TypeSpec.


<h3 id="most_specific_compatible_type"><code>most_specific_compatible_type</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/tensor_array_ops.py#L1276-L1284">View source</a>

``` python
most_specific_compatible_type(other)
```

Returns the most specific TypeSpec compatible with `self` and `other`.


#### Args:


* <b>`other`</b>: A `TypeSpec`.


#### Raises:


* <b>`ValueError`</b>: If there is no TypeSpec that is compatible with both `self`
  and `other`.
