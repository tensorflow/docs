page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lookup.StaticVocabularyTable

## Class `StaticVocabularyTable`



Inherits From: [`StaticVocabularyTable`](../../tf/compat/v2/lookup/StaticVocabularyTable)

### Aliases:

* Class `tf.compat.v1.lookup.StaticVocabularyTable`
* Class `tf.lookup.StaticVocabularyTable`



Defined in [`python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/lookup_ops.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    initializer,
    num_oov_buckets,
    lookup_key_dtype=None,
    name=None
)
```

Construct a `StaticVocabularyTable` object.


#### Args:


* <b>`initializer`</b>: A TableInitializerBase object that contains the data used to
  initialize the table. If None, then we only use out-of-vocab buckets.
* <b>`num_oov_buckets`</b>: Number of buckets to use for out-of-vocabulary keys. Must
  be greater than zero.
* <b>`lookup_key_dtype`</b>: Data type of keys passed to `lookup`. Defaults to
  `initializer.key_dtype` if `initializer` is specified, otherwise
  <a href="../../tf#string"><code>tf.string</code></a>. Must be string or integer, and must be castable to
  `initializer.key_dtype`.
* <b>`name`</b>: A name for the operation (optional).


#### Raises:


* <b>`ValueError`</b>: when `num_oov_buckets` is not positive.
* <b>`TypeError`</b>: when lookup_key_dtype or initializer.key_dtype are not
  integer or string. Also when initializer.value_dtype != int64.



## Properties

<h3 id="initializer"><code>initializer</code></h3>




<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.


<h3 id="name"><code>name</code></h3>




<h3 id="resource_handle"><code>resource_handle</code></h3>




<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.




## Methods

<h3 id="lookup"><code>lookup</code></h3>

``` python
lookup(
    keys,
    name=None
)
```

Looks up `keys` in the table, outputs the corresponding values.

It assigns out-of-vocabulary keys to buckets based in their hashes.

#### Args:


* <b>`keys`</b>: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
* <b>`name`</b>: Optional name for the op.


#### Returns:

A `SparseTensor` if keys are sparse, otherwise a dense `Tensor`.



#### Raises:


* <b>`TypeError`</b>: when `keys` doesn't match the table key data type.

<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.




