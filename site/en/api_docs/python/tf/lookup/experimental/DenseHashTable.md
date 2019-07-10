page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lookup.experimental.DenseHashTable

## Class `DenseHashTable`

A generic mutable hash table implementation using tensors as backing store.

Inherits From: [`LookupInterface`](../../../tf/contrib/lookup/LookupInterface)

### Aliases:

* Class `tf.compat.v1.lookup.experimental.DenseHashTable`
* Class `tf.compat.v2.lookup.experimental.DenseHashTable`
* Class `tf.contrib.lookup.MutableDenseHashTable`
* Class `tf.lookup.experimental.DenseHashTable`



Defined in [`python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/lookup_ops.py).

<!-- Placeholder for "Used in" -->

Data can be inserted by calling the insert method and removed by calling the
remove method. It does not support initialization via the init method.

It uses "open addressing" with quadratic reprobing to resolve collisions.
Compared to `MutableHashTable` the insert, remove and lookup operations in a
`DenseHashTable` are typically faster, but memory usage can be higher.
However, `DenseHashTable` does not require additional memory for
temporary tensors created during checkpointing and restore operations.

#### Example usage:



```python
table = tf.lookup.DenseHashTable(key_dtype=tf.int64,
                                 value_dtype=tf.int64,
                                 default_value=-1,
                                 empty_key=0,
                                 deleted_key=-1)

sess.run(table.insert(keys, values))
out = table.lookup(query_keys)
print(out.eval())
```

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    key_dtype,
    value_dtype,
    default_value,
    empty_key,
    deleted_key,
    initial_num_buckets=None,
    name='MutableDenseHashTable',
    checkpoint=True
)
```

Creates an empty `DenseHashTable` object.

Creates a table, the type of its keys and values are specified by key_dtype
and value_dtype, respectively.

#### Args:


* <b>`key_dtype`</b>: the type of the key tensors.
* <b>`value_dtype`</b>: the type of the value tensors.
* <b>`default_value`</b>: The value to use if a key is missing in the table.
* <b>`empty_key`</b>: the key to use to represent empty buckets internally. Must not
  be used in insert, remove or lookup operations.
* <b>`deleted_key`</b>: the key to use to represent deleted buckets internally. Must
  not be used in insert, remove or lookup operations and be different from
  the empty_key.
* <b>`initial_num_buckets`</b>: the initial number of buckets.
* <b>`name`</b>: A name for the operation (optional).
* <b>`checkpoint`</b>: if True, the contents of the table are saved to and restored
  from checkpoints. If `shared_name` is empty for a checkpointed table, it
  is shared using the table node name.


#### Returns:

A `DenseHashTable` object.



#### Raises:


* <b>`ValueError`</b>: If checkpoint is True and no name was specified.



## Properties

<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.


<h3 id="name"><code>name</code></h3>




<h3 id="resource_handle"><code>resource_handle</code></h3>

Returns the resource handle associated with this Resource.


<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.




## Methods

<h3 id="erase"><code>erase</code></h3>

``` python
erase(
    keys,
    name=None
)
```

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

#### Args:


* <b>`keys`</b>: Keys to remove. Can be a tensor of any shape. Must match the table's
  key type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.



#### Raises:


* <b>`TypeError`</b>: when `keys` do not match the table data types.

<h3 id="export"><code>export</code></h3>

``` python
export(name=None)
```

Returns tensors of all keys and values in the table.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A pair of tensors with the first tensor containing all keys and the
  second tensors containing all values in the table.


<h3 id="insert"><code>insert</code></h3>

``` python
insert(
    keys,
    values,
    name=None
)
```

Associates `keys` with `values`.


#### Args:


* <b>`keys`</b>: Keys to insert. Can be a tensor of any shape. Must match the table's
  key type.
* <b>`values`</b>: Values to be associated with keys. Must be a tensor of the same
  shape as `keys` and match the table's value type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.



#### Raises:


* <b>`TypeError`</b>: when `keys` or `values` doesn't match the table data
  types.

<h3 id="insert_or_assign"><code>insert_or_assign</code></h3>

``` python
insert_or_assign(
    keys,
    values,
    name=None
)
```

Associates `keys` with `values`.


#### Args:


* <b>`keys`</b>: Keys to insert. Can be a tensor of any shape. Must match the table's
  key type.
* <b>`values`</b>: Values to be associated with keys. Must be a tensor of the same
  shape as `keys` and match the table's value type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.



#### Raises:


* <b>`TypeError`</b>: when `keys` or `values` doesn't match the table data
  types.

<h3 id="lookup"><code>lookup</code></h3>

``` python
lookup(
    keys,
    name=None
)
```

Looks up `keys` in a table, outputs the corresponding values.

The `default_value` is used for keys not present in the table.

#### Args:


* <b>`keys`</b>: Keys to look up. Can be a tensor of any shape. Must match the
  table's key_dtype.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tensor containing the values in the same shape as `keys` using the
  table's value type.



#### Raises:


* <b>`TypeError`</b>: when `keys` do not match the table data types.

<h3 id="remove"><code>remove</code></h3>

``` python
remove(
    keys,
    name=None
)
```

Removes `keys` and its associated values from the table.

If a key is not present in the table, it is silently ignored.

#### Args:


* <b>`keys`</b>: Keys to remove. Can be a tensor of any shape. Must match the table's
  key type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The created Operation.



#### Raises:


* <b>`TypeError`</b>: when `keys` do not match the table data types.

<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.


#### Args:


* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar tensor containing the number of elements in this table.




