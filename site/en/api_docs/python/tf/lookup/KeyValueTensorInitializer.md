page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lookup.KeyValueTensorInitializer


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/lookup_ops.py#L415-L473">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `KeyValueTensorInitializer`

Table initializers given `keys` and `values` tensors.



### Aliases:

* Class `tf.compat.v1.lookup.KeyValueTensorInitializer`
* Class `tf.compat.v2.lookup.KeyValueTensorInitializer`


<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/lookup_ops.py#L418-L446">View source</a>

``` python
__init__(
    keys,
    values,
    key_dtype=None,
    value_dtype=None,
    name=None
)
```

Constructs a table initializer object based on keys and values tensors.


#### Args:


* <b>`keys`</b>: The tensor for the keys.
* <b>`values`</b>: The tensor for the values.
* <b>`key_dtype`</b>: The `keys` data type. Used when `keys` is a python array.
* <b>`value_dtype`</b>: The `values` data type. Used when `values` is a python array.
* <b>`name`</b>: A name for the operation (optional).



## Properties

<h3 id="key_dtype"><code>key_dtype</code></h3>

The expected table key dtype.


<h3 id="value_dtype"><code>value_dtype</code></h3>

The expected table value dtype.




## Methods

<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/lookup_ops.py#L448-L473">View source</a>

``` python
initialize(table)
```

Initializes the given `table` with `keys` and `values` tensors.


#### Args:


* <b>`table`</b>: The table to initialize.


#### Returns:

The operation that initializes the table.



#### Raises:


* <b>`TypeError`</b>: when the keys and values data types do not match the table
key and value data types.
