page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.TensorSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/TensorSpec">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L33-L184">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TensorSpec`

Describes a tf.Tensor.



### Aliases:

* Class <a href="/api_docs/python/tf/TensorSpec"><code>tf.compat.v1.TensorSpec</code></a>
* Class <a href="/api_docs/python/tf/TensorSpec"><code>tf.compat.v2.TensorSpec</code></a>
* Class <a href="/api_docs/python/tf/TensorSpec"><code>tf.contrib.eager.TensorSpec</code></a>
* Class <a href="/api_docs/python/tf/TensorSpec"><code>tf.contrib.framework.TensorSpec</code></a>


<!-- Placeholder for "Used in" -->

Metadata for describing the <a href="../tf/Tensor"><code>tf.Tensor</code></a> objects accepted or returned
by some TensorFlow APIs.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L42-L60">View source</a>

``` python
__init__(
    shape,
    dtype=tf.dtypes.float32,
    name=None
)
```

Creates a TensorSpec.


#### Args:


* <b>`shape`</b>: Value convertible to <a href="../tf/TensorShape"><code>tf.TensorShape</code></a>. The shape of the tensor.
* <b>`dtype`</b>: Value convertible to <a href="../tf/dtypes/DType"><code>tf.DType</code></a>. The type of the tensor values.
* <b>`name`</b>: Optional name for the Tensor.


#### Raises:


* <b>`TypeError`</b>: If shape is not convertible to a <a href="../tf/TensorShape"><code>tf.TensorShape</code></a>, or dtype is
  not convertible to a <a href="../tf/dtypes/DType"><code>tf.DType</code></a>.



## Properties

<h3 id="dtype"><code>dtype</code></h3>

Returns the `dtype` of elements in the tensor.


<h3 id="name"><code>name</code></h3>

Returns the (optionally provided) name of the described tensor.


<h3 id="shape"><code>shape</code></h3>

Returns the `TensorShape` that represents the shape of the tensor.


<h3 id="value_type"><code>value_type</code></h3>






## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L113-L118">View source</a>

``` python
__eq__(other)
```

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L120-L121">View source</a>

``` python
__ne__(other)
```

Return self!=value.


<h3 id="from_spec"><code>from_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L62-L64">View source</a>

``` python
@classmethod
from_spec(
    cls,
    spec,
    name=None
)
```




<h3 id="from_tensor"><code>from_tensor</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L66-L73">View source</a>

``` python
@classmethod
from_tensor(
    cls,
    tensor,
    name=None
)
```




<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L90-L104">View source</a>

``` python
is_compatible_with(spec_or_tensor)
```

Returns True if spec_or_tensor is compatible with this TensorSpec.

Two tensors are considered compatible if they have the same dtype
and their shapes are compatible (see <a href="../tf/TensorShape#is_compatible_with"><code>tf.TensorShape.is_compatible_with</code></a>).

#### Args:


* <b>`spec_or_tensor`</b>: A tf.TensorSpec or a tf.Tensor


#### Returns:

True if spec_or_tensor is compatible with self.


<h3 id="most_specific_compatible_type"><code>most_specific_compatible_type</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/tensor_spec.py#L125-L130">View source</a>

``` python
most_specific_compatible_type(other)
```

Returns the most specific TypeSpec compatible with `self` and `other`.


#### Args:


* <b>`other`</b>: A `TypeSpec`.


#### Raises:


* <b>`ValueError`</b>: If there is no TypeSpec that is compatible with both `self`
  and `other`.
