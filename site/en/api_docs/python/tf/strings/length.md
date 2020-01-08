page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.length

``` python
tf.strings.length(
    input,
    name=None,
    unit='BYTE'
)
```



Defined in [`tensorflow/python/ops/string_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/string_ops.py).

String lengths of `input`.

Computes the length of each string given in the input tensor.

#### Args:

* <b>`input`</b>: A `Tensor` of type `string`.
    The string for which to compute the length.
* <b>`unit`</b>: An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`.
    The unit that is counted to compute string length.  One of: `"BYTE"` (for
    the number of bytes in each string) or `"UTF8_CHAR"` (for the number of UTF-8
    encoded Unicode code points in each string).  Results are undefined
    if `unit=UTF8_CHAR` and the `input` strings do not contain structurally
    valid UTF-8.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int32`.