page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.data.experimental.SparseTensorStructure

## Class `SparseTensorStructure`

Inherits From: [`Structure`](../../../tf/data/experimental/Structure)



Defined in [`tensorflow/python/data/util/structure.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/data/util/structure.py).

Represents structural information about a <a href="../../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    dtype,
    dense_shape
)
```

Initialize self.  See help(type(self)) for accurate signature.



## Methods

<h3 id="from_value"><code>from_value</code></h3>

``` python
@staticmethod
from_value(value)
```

Returns a `Structure` that represents the given `value`.

#### Args:

* <b>`value`</b>: A potentially structured value.


#### Returns:

A `Structure` that is compatible with `value`.


#### Raises:

* <b>`TypeError`</b>: If a structure cannot be built for `value`, because its type
    or one of its component types is not supported.

<h3 id="is_compatible_with"><code>is_compatible_with</code></h3>

``` python
is_compatible_with(other)
```

Returns `True` if `other` is compatible with this structure.

A structure `t` is a "subtype" of `s` if:

* `s` and `t` are instances of the same `Structure` subclass.
* The nested structures (if any) of `s` and `t` are the same, according to
  <a href="../../../tf/contrib/framework/nest/assert_same_structure"><code>tf.contrib.framework.nest.assert_same_structure</code></a>, and each nested
  structure of `t` is a "subtype" of the corresponding nested structure of
  `s`.
* Any <a href="../../../tf/dtypes/DType"><code>tf.DType</code></a> components of `t` are the same as the corresponding
  components in `s`.
* Any <a href="../../../tf/TensorShape"><code>tf.TensorShape</code></a> components of `t` are compatible with the
  corresponding components in `s`, according to
  <a href="../../../tf/TensorShape#is_compatible_with"><code>tf.TensorShape.is_compatible_with</code></a>.

#### Args:

* <b>`other`</b>: A `Structure`.


#### Returns:

`True` if `other` is a subtype of this structure, otherwise `False`.



