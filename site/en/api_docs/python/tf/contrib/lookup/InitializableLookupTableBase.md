

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.lookup.InitializableLookupTableBase

### `class tf.contrib.lookup.InitializableLookupTableBase`



Defined in [`tensorflow/contrib/lookup/lookup_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/contrib/lookup/lookup_ops.py).

Initializable lookup table interface.

An initializable lookup tables persist across different steps.

## Properties

<h3 id="default_value"><code>default_value</code></h3>

The default value of the table.

<h3 id="init"><code>init</code></h3>

The table initialization op.

<h3 id="key_dtype"><code>key_dtype</code></h3>

The table key dtype.

<h3 id="name"><code>name</code></h3>

The name of the table.

<h3 id="table_ref"><code>table_ref</code></h3>

Get the underlying table reference.

<h3 id="value_dtype"><code>value_dtype</code></h3>

The table value dtype.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    table_ref,
    default_value,
    initializer
)
```

Construct a table object from a table reference.

If requires a table initializer object (subclass of `TableInitializerBase`).
It provides the table key and value types, as well as the op to initialize
the table. The caller is responsible to execute the initialization op.

#### Args:

* <b>`table_ref`</b>: The table reference, i.e. the output of the lookup table ops.
* <b>`default_value`</b>: The value to use if a key is missing in the table.
* <b>`initializer`</b>: The table initializer to use.

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

The `default_value` is used for keys not present in the table.

#### Args:

* <b>`keys`</b>: Keys to look up. May be either a `SparseTensor` or dense `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `SparseTensor` if keys are sparse, otherwise a dense `Tensor`.


#### Raises:

* <b>`TypeError`</b>: when `keys` or `default_value` doesn't match the table data
    types.

<h3 id="size"><code>size</code></h3>

``` python
size(name=None)
```

Compute the number of elements in this table.

#### Args:

* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A scalar tensor containing the number of elements in this table.



