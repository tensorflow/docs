page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.io.decode_csv


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/parsing_ops.py#L1970-L2026">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convert CSV records to tensors. Each column maps to one tensor.

### Aliases:

* `tf.compat.v2.io.decode_csv`


``` python
tf.io.decode_csv(
    records,
    record_defaults,
    field_delim=',',
    use_quote_delim=True,
    na_value='',
    select_cols=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

RFC 4180 format is expected for the CSV records.
(https://tools.ietf.org/html/rfc4180)
Note that we allow leading and trailing spaces with int or float field.

#### Args:


* <b>`records`</b>: A `Tensor` of type `string`.
  Each string is a record/row in the csv and all records should have
  the same format.
* <b>`record_defaults`</b>: A list of `Tensor` objects with specific types.
  Acceptable types are `float32`, `float64`, `int32`, `int64`, `string`.
  One tensor per column of the input record, with either a
  scalar default value for that column or an empty vector if the column is
  required.
* <b>`field_delim`</b>: An optional `string`. Defaults to `","`.
  char delimiter to separate fields in a record.
* <b>`use_quote_delim`</b>: An optional `bool`. Defaults to `True`.
  If false, treats double quotation marks as regular
  characters inside of the string fields (ignoring RFC 4180, Section 2,
  Bullet 5).
* <b>`na_value`</b>: Additional string to recognize as NA/NaN.
* <b>`select_cols`</b>: Optional sorted list of column indices to select. If specified,
  only this subset of columns will be parsed and returned.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` objects. Has the same type as `record_defaults`.
Each tensor will have the same shape as records.



#### Raises:


* <b>`ValueError`</b>: If any of the arguments is malformed.
