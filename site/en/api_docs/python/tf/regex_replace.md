page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.regex_replace

### Aliases:

* `tf.regex_replace`
* `tf.strings.regex_replace`

``` python
tf.regex_replace(
    input,
    pattern,
    rewrite,
    replace_global=True,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_string_ops.py`.

Replaces the match of pattern in input with rewrite.

It follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

#### Args:

* <b>`input`</b>: A `Tensor` of type `string`. The text to be processed.
* <b>`pattern`</b>: A `Tensor` of type `string`.
    The regular expression to match the input.
* <b>`rewrite`</b>: A `Tensor` of type `string`.
    The rewrite to be applied to the matched expresion.
* <b>`replace_global`</b>: An optional `bool`. Defaults to `True`.
    If True, the replacement is global, otherwise the replacement
    is done only on the first match.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `string`.