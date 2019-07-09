page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.regex_full_match

``` python
tf.strings.regex_full_match(
    input,
    pattern,
    name=None
)
```



Defined in generated file: `tensorflow/python/ops/gen_string_ops.py`.

Check if the input matches the regex pattern.

The input is a string tensor of any shape. The pattern is a scalar
string tensor which is applied to every element of the input tensor.
The boolean values (True or False) of the output tensor indicate
if the input matches the regex pattern provided.

The pattern follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

#### Args:

* <b>`input`</b>: A `Tensor` of type `string`.
    A string tensor of the text to be processed.
* <b>`pattern`</b>: A `Tensor` of type `string`.
    A 1-D string tensor of the regular expression to match the input.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.