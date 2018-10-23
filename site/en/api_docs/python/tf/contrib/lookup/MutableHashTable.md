

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lookup.MutableHashTable

## Class `MutableHashTable`

Inherits From: [`LookupInterface`](../../../tf/contrib/lookup/LookupInterface)



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/lookup/lookup_ops.py).

A generic mutable hash table implementation.

Data can be inserted by calling the insert method. It does not support
initialization via the init method.

Example usage:

```python
table = tf.contrib.lookup.MutableHashTable(key_dtype=tf.string,
                                           value_dtype=tf.int64,
                                           default_value=-1)
table.insert(keys, values)
out = table.lookup(query_keys)
print(out.eval())
```

## Properties

<h3 id="init"><code>init</code></h3>

The table initialization op.

<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.

<h3 id="name"><code>name</code></h3>

The name of the table.

<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    key_dtype,
    value_dtype,
    default_value,
    shared_name=None,
    name='MutableHashTable',
    checkpoint=True
)
```

Creates an empty `MutableHashTable` object.

Creates a table, the type of its keys and values are specified by key_dtype
and value_dtype, respectively.

#### Args:

* <b>`key_dtype`</b>: the type of the key tensors.
* <b>`value_dtype`</b>: the type of the value tensors.
* <b>`default_value`</b>: The value to use if a key is missing in the table.
* <b>`shared_name`</b>: If non-empty, this table will be shared under
    the given name across multiple sessions.
* <b>`name`</b>: A name for the operation (optional).
* <b>`checkpoint`</b>: if True, the contents of the table are saved to and restored
    from checkpoints. If `shared_name` is empty for a checkpointed table, it
    is shared using the table node name.


#### Returns:

A `MutableHashTable` object.


#### Raises:

* <b>`ValueError`</b>: If checkpoint is True and no name was specified.

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

* <b>`keys`</b>: Keys to insert. Can be a tensor of any shape. Must match the
    table's key type.
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

<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A scalar tensor containing the number of elements in this table.



