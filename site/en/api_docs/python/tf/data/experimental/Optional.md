page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.Optional


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/optional_ops.py#L36-L121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `Optional`

Wraps a value that may/may not be present at runtime.



### Aliases:

* Class `tf.compat.v1.data.experimental.Optional`
* Class `tf.compat.v2.data.experimental.Optional`


<!-- Placeholder for "Used in" -->

An `Optional` can represent the result of an operation that may fail as a
value, rather than raising an exception and halting execution. For example,
<a href="../../../tf/data/experimental/get_next_as_optional"><code>tf.data.experimental.get_next_as_optional</code></a> returns an `Optional` that either
contains the next value from a <a href="../../../tf/compat/v1/data/Iterator"><code>tf.compat.v1.data.Iterator</code></a> if one exists, or
a "none" value that indicates the end of the sequence has been reached.

`Optional` can only be used by values that are convertible to `Tensor` or
`CompositeTensor`.

## Properties

<h3 id="value_structure"><code>value_structure</code></h3>

The structure of the components of this optional.


#### Returns:

A `Structure` object representing the structure of the components of this
  optional.




## Methods

<h3 id="from_value"><code>from_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/optional_ops.py#L87-L105">View source</a>

``` python
@staticmethod
from_value(value)
```

Returns an `Optional` that wraps the given value.


#### Args:


* <b>`value`</b>: A value to wrap. The value must be convertible to `Tensor` or
  `CompositeTensor`.


#### Returns:

An `Optional` that wraps `value`.


<h3 id="get_value"><code>get_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/optional_ops.py#L61-L75">View source</a>

``` python
get_value(name=None)
```

Returns the value wrapped by this optional.

If this optional does not have a value (i.e. `self.has_value()` evaluates
to `False`), this operation will raise <a href="../../../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a>
at runtime.

#### Args:


* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

The wrapped value.


<h3 id="has_value"><code>has_value</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/optional_ops.py#L49-L59">View source</a>

``` python
has_value(name=None)
```

Returns a tensor that evaluates to `True` if this optional has a value.


#### Args:


* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

A scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of type <a href="../../../tf#bool"><code>tf.bool</code></a>.


<h3 id="none_from_structure"><code>none_from_structure</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/data/ops/optional_ops.py#L107-L121">View source</a>

``` python
@staticmethod
none_from_structure(value_structure)
```

Returns an `Optional` that has no value.

NOTE: This method takes an argument that defines the structure of the value
that would be contained in the returned `Optional` if it had a value.

#### Args:


* <b>`value_structure`</b>: A `Structure` object representing the structure of the
  components of this optional.


#### Returns:

An `Optional` that has no value.
