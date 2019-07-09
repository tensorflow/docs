

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.as_string

### Aliases:

* `tf.as_string`
* `tf.dtypes.as_string`

``` python
tf.as_string(
    input,
    precision=-1,
    scientific=False,
    shortest=False,
    width=-1,
    fill='',
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_string_ops.py`.

See the guide: [Strings > Conversion](../../../api_guides/python/string_ops#Conversion)

Converts each entry in the given tensor to strings.  Supports many numeric

types and boolean.

#### Args:

* <b>`input`</b>: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `complex64`, `float32`, `float64`, `bool`.
* <b>`precision`</b>: An optional `int`. Defaults to `-1`.
    The post-decimal precision to use for floating point numbers.
    Only used if precision > -1.
* <b>`scientific`</b>: An optional `bool`. Defaults to `False`.
    Use scientific notation for floating point numbers.
* <b>`shortest`</b>: An optional `bool`. Defaults to `False`.
    Use shortest representation (either scientific or standard) for
    floating point numbers.
* <b>`width`</b>: An optional `int`. Defaults to `-1`.
    Pad pre-decimal numbers to this width.
    Applies to both floating point and integer numbers.
    Only used if width > -1.
* <b>`fill`</b>: An optional `string`. Defaults to `""`.
    The value to pad if width > -1.  If empty, pads with spaces.
    Another typical value is '0'.  String cannot be longer than 1 character.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.