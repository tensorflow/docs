page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.unicode_script

``` python
tf.strings.unicode_script(
    input,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_string_ops.py`.

Determine the script codes of a given tensor of Unicode integer code points.

This operation converts Unicode code points to script codes corresponding to
each code point. Script codes correspond to International Components for
Unicode (ICU) UScriptCode values. See http://icu-project.org/apiref/icu4c/uscript_8h.html.
Returns -1 (USCRIPT_INVALID_CODE) for invalid codepoints. Output shape will
match input shape.

#### Args:

* <b>`input`</b>: A `Tensor` of type `int32`. A Tensor of int32 Unicode code points.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int32`.