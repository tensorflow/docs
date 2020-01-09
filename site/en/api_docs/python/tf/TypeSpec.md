page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.TypeSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/TypeSpec">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/type_spec.py#L47-L414">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TypeSpec`

Specifies a TensorFlow value type.



### Aliases:

* Class <a href="/api_docs/python/tf/TypeSpec"><code>tf.compat.v1.TypeSpec</code></a>
* Class <a href="/api_docs/python/tf/TypeSpec"><code>tf.compat.v1.data.experimental.Structure</code></a>
* Class <a href="/api_docs/python/tf/TypeSpec"><code>tf.compat.v2.TypeSpec</code></a>
* Class <a href="/api_docs/python/tf/TypeSpec"><code>tf.data.experimental.Structure</code></a>


<!-- Placeholder for "Used in" -->

A <a href="../tf/TypeSpec"><code>tf.TypeSpec</code></a> provides metadata describing an object accepted or returned
by TensorFlow APIs.  Concrete subclasses, such as <a href="../tf/TensorSpec"><code>tf.TensorSpec</code></a> and
<a href="../tf/RaggedTensorSpec"><code>tf.RaggedTensorSpec</code></a>, are used to describe different value types.

For example, <a href="../tf/function"><code>tf.function</code></a>'s `input_signature` argument accepts a list
(or nested structure) of `TypeSpec`s.

Creating new subclasses of TypeSpec (outside of TensorFlow core) is not
currently supported.  In particular, we may make breaking changes to the
private methods and properties defined by this base class.

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
