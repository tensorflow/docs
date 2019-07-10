page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.Optional

## Class `Optional`



### Aliases:

* Class `tf.contrib.data.Optional`
* Class `tf.data.experimental.Optional`



Defined in [`tensorflow/python/data/ops/optional_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/ops/optional_ops.py).

Wraps a nested structure of tensors that may/may not be present at runtime.

An `Optional` can represent the result of an operation that may fail as a
value, rather than raising an exception and halting execution. For example,
<a href="../../../tf/data/experimental/get_next_as_optional"><code>tf.data.experimental.get_next_as_optional</code></a> returns an `Optional` that either
contains the next value from a <a href="../../../tf/data/Iterator"><code>tf.data.Iterator</code></a> if one exists, or a "none"
value that indicates the end of the sequence has been reached.

## Properties

<h3 id="value_structure"><code>value_structure</code></h3>

The structure of the components of this optional.

#### Returns:

A `Structure` object representing the structure of the components of this
  optional.



## Methods

<h3 id="from_value"><code>from_value</code></h3>

``` python
@staticmethod
from_value(value)
```

Returns an `Optional` that wraps the given value.

#### Args:

* <b>`value`</b>: A nested structure of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> and/or <a href="../../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a> objects.


#### Returns:

An `Optional` that wraps `value`.

<h3 id="get_value"><code>get_value</code></h3>

``` python
get_value(name=None)
```

Returns a nested structure of values wrapped by this optional.

If this optional does not have a value (i.e. `self.has_value()` evaluates
to `False`), this operation will raise <a href="../../../tf/errors/InvalidArgumentError"><code>tf.errors.InvalidArgumentError</code></a>
at runtime.

#### Args:

* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

A nested structure of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> and/or <a href="../../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a> objects.

<h3 id="has_value"><code>has_value</code></h3>

``` python
has_value(name=None)
```

Returns a tensor that evaluates to `True` if this optional has a value.

#### Args:

* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

A scalar <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> of type <a href="../../../tf/dtypes#bool"><code>tf.bool</code></a>.

<h3 id="none_from_structure"><code>none_from_structure</code></h3>

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



