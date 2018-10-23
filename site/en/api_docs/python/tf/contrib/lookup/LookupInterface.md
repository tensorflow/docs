

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.lookup.LookupInterface

### `class tf.contrib.lookup.LookupInterface`



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/lookup/lookup_ops.py).

Represent a lookup table that persists across different steps.

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
    name
)
```

Construct a lookup table interface.

#### Args:

* <b>`key_dtype`</b>: The table key type.
* <b>`value_dtype`</b>: The table value type.
* <b>`name`</b>: A name for the operation (optional).

<h3 id="check_table_dtypes"><code>check_table_dtypes</code></h3>

``` python
check_table_dtypes(
    key_dtype,
    value_dtype
)
```

Check that the given key_dtype and value_dtype matches the table dtypes.

#### Args:

* <b>`key_dtype`</b>: The key data type to check.
* <b>`value_dtype`</b>: The value data type to check.


#### Raises:

* <b>`TypeError`</b>: when 'key_dtype' or 'value_dtype' doesn't match the table data
    types.

<h3 id="lookup"><code>lookup</code></h3>

``` python
lookup(
    keys,
    name=None
)
```

Looks up `keys` in a table, outputs the corresponding values.

<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.



