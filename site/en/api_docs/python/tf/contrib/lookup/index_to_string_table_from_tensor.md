page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lookup.index_to_string_table_from_tensor


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/lookup/lookup_ops.py#L195-L245">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns a lookup table that maps a `Tensor` of indices into strings.

``` python
tf.contrib.lookup.index_to_string_table_from_tensor(
    mapping,
    default_value='UNK',
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation constructs a lookup table to map int64 indices into string
values. The mapping is initialized from a string `mapping` 1-D `Tensor` where
each element is a value and the corresponding index within the tensor is the
key.

Any input which does not have a corresponding index in 'mapping'
(an out-of-vocabulary entry) is assigned the `default_value`

The underlying table must be initialized by calling
`session.run(tf.compat.v1.tables_initializer)` or `session.run(table.init)`
once.

Elements in `mapping` cannot have duplicates, otherwise when executing the
table initializer op, it will throw a `FailedPreconditionError`.

#### Sample Usages:



```python
mapping_string = tf.constant(["emerson", "lake", "palmer"])
indices = tf.constant([1, 5], tf.int64)
table = tf.contrib.lookup.index_to_string_table_from_tensor(
    mapping_string, default_value="UNKNOWN")
values = table.lookup(indices)
...
tf.compat.v1.tables_initializer().run()

values.eval() ==> ["lake", "UNKNOWN"]
```

#### Args:


* <b>`mapping`</b>: A 1-D string `Tensor` that specifies the strings to map from
  indices.
* <b>`default_value`</b>: The value to use for out-of-vocabulary indices.
* <b>`name`</b>: A name for this op (optional).


#### Returns:

The lookup table to map a string values associated to a given index `int64`
`Tensors`.



#### Raises:


* <b>`ValueError`</b>: when `mapping` is not set.
