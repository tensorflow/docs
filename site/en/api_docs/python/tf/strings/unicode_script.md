page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.unicode_script


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

Defined in generated file: `python/ops/gen_string_ops.py`



Determine the script codes of a given tensor of Unicode integer code points.

### Aliases:

* `tf.compat.v1.strings.unicode_script`
* `tf.compat.v2.strings.unicode_script`


``` python
tf.strings.unicode_script(
    input,
    name=None
)
```



### Used in the tutorials:

* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



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
