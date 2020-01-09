page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.regex_full_match


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/regex_full_match">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/string_ops.py#L48-L73">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Check if the input matches the regex pattern.

### Aliases:

* <a href="/api_docs/python/tf/strings/regex_full_match"><code>tf.compat.v1.strings.regex_full_match</code></a>
* <a href="/api_docs/python/tf/strings/regex_full_match"><code>tf.compat.v2.strings.regex_full_match</code></a>


``` python
tf.strings.regex_full_match(
    input,
    pattern,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The input is a string tensor of any shape. The pattern is a scalar
string tensor which is applied to every element of the input tensor.
The boolean values (True or False) of the output tensor indicate
if the input matches the regex pattern provided.

The pattern follows the re2 syntax (https://github.com/google/re2/wiki/Syntax)

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`.
  A string tensor of the text to be processed.
* <b>`pattern`</b>: A `Tensor` of type `string`.
  A scalar string tensor containing the regular expression to match the input.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `bool`.
