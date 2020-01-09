page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.IndexedSlicesSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/IndexedSlicesSpec">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L183-L246">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `IndexedSlicesSpec`

Type specification for a <a href="../tf/IndexedSlices"><code>tf.IndexedSlices</code></a>.

Inherits From: [`TypeSpec`](../tf/TypeSpec)

### Aliases:

* Class <a href="/api_docs/python/tf/IndexedSlicesSpec"><code>tf.compat.v1.IndexedSlicesSpec</code></a>
* Class <a href="/api_docs/python/tf/IndexedSlicesSpec"><code>tf.compat.v2.IndexedSlicesSpec</code></a>


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/indexed_slices.py#L191-L215">View source</a>

``` python
__init__(
    shape=None,
    dtype=tf.dtypes.float32,
    indices_dtype=tf.dtypes.int64,
    dense_shape_dtype=None,
    indices_shape=None
)
```

Constructs a type specification for a <a href="../tf/IndexedSlices"><code>tf.IndexedSlices</code></a>.


#### Args:


* <b>`shape`</b>: The dense shape of the `IndexedSlices`, or `None` to allow any
  dense shape.
* <b>`dtype`</b>: <a href="../tf/dtypes/DType"><code>tf.DType</code></a> of values in the `IndexedSlices`.
* <b>`indices_dtype`</b>: <a href="../tf/dtypes/DType"><code>tf.DType</code></a> of the `indices` in the `IndexedSlices`.  One
  of <a href="../tf#int32"><code>tf.int32</code></a> or <a href="../tf#int64"><code>tf.int64</code></a>.
* <b>`dense_shape_dtype`</b>: <a href="../tf/dtypes/DType"><code>tf.DType</code></a> of the `dense_shape` in the `IndexedSlices`.
  One of <a href="../tf#int32"><code>tf.int32</code></a>, <a href="../tf#int64"><code>tf.int64</code></a>, or `None` (if the `IndexedSlices` has
  no `dense_shape` tensor).
* <b>`indices_shape`</b>: The shape of the `indices` component, which indicates
  how many slices are in the `IndexedSlices`.



## Properties

<h3 id="value_type"><code>value_type</code></h3>






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
