page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.RaggedTensorSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/RaggedTensorSpec">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_tensor.py#L1925-L2067">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `RaggedTensorSpec`

Type specification for a <a href="../tf/RaggedTensor"><code>tf.RaggedTensor</code></a>.



### Aliases:

* Class <a href="/api_docs/python/tf/RaggedTensorSpec"><code>tf.compat.v1.RaggedTensorSpec</code></a>
* Class <a href="/api_docs/python/tf/RaggedTensorSpec"><code>tf.compat.v2.RaggedTensorSpec</code></a>


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_tensor.py#L1934-L1963">View source</a>

``` python
__init__(
    shape=None,
    dtype=tf.dtypes.float32,
    ragged_rank=None,
    row_splits_dtype=tf.dtypes.int64
)
```

Constructs a type specification for a <a href="../tf/RaggedTensor"><code>tf.RaggedTensor</code></a>.


#### Args:


* <b>`shape`</b>: The shape of the RaggedTensor, or `None` to allow any shape.  If
  a shape is specified, then all ragged dimensions must have size `None`.
* <b>`dtype`</b>: <a href="../tf/dtypes/DType"><code>tf.DType</code></a> of values in the RaggedTensor.
* <b>`ragged_rank`</b>: Python integer, the ragged rank of the RaggedTensor
  to be described.  Defaults to `shape.ndims - 1`.
* <b>`row_splits_dtype`</b>: `dtype` for the RaggedTensor's `row_splits` tensor.
  One of <a href="../tf#int32"><code>tf.int32</code></a> or <a href="../tf#int64"><code>tf.int64</code></a>.



## Properties

<h3 id="value_type"><code>value_type</code></h3>

The Python type for values that are compatible with this TypeSpec.




## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/type_spec.py#L262-L265">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/type_spec.py#L267-L268">View source</a>

``` python
__ne__(other)
```

Return self!=value.


<h3 id="from_value"><code>from_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_tensor.py#L2062-L2067">View source</a>

``` python
@classmethod
from_value(
    cls,
    value
)
```




<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/type_spec.py#L87-L102">View source</a>

``` python
is_compatible_with(spec_or_value)
```

Returns true if `spec_or_value` is compatible with this TypeSpec.


<h3 id="most_specific_compatible_type"><code>most_specific_compatible_type</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/type_spec.py#L104-L126">View source</a>

``` python
most_specific_compatible_type(other)
```

Returns the most specific TypeSpec compatible with `self` and `other`.


#### Args:


* <b>`other`</b>: A `TypeSpec`.


#### Raises:


* <b>`ValueError`</b>: If there is no TypeSpec that is compatible with both `self`
  and `other`.
