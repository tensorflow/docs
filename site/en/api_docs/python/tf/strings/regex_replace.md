page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.regex_replace


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/strings/regex_replace">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/string_ops.py#L78-L111">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Replace elements of `input` matching regex `pattern` with `rewrite`.

### Aliases:

* <a href="/api_docs/python/tf/strings/regex_replace"><code>tf.compat.v1.regex_replace</code></a>
* <a href="/api_docs/python/tf/strings/regex_replace"><code>tf.compat.v1.strings.regex_replace</code></a>
* <a href="/api_docs/python/tf/strings/regex_replace"><code>tf.compat.v2.strings.regex_replace</code></a>
* <a href="/api_docs/python/tf/strings/regex_replace"><code>tf.regex_replace</code></a>


``` python
tf.strings.regex_replace(
    input,
    pattern,
    rewrite,
    replace_global=True,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: string `Tensor`, the source strings to process.
* <b>`pattern`</b>: string or scalar string `Tensor`, regular expression to use,
  see more details at https://github.com/google/re2/wiki/Syntax
* <b>`rewrite`</b>: string or scalar string `Tensor`, value to use in match
  replacement, supports backslash-escaped digits (\1 to \9) can be to insert
  text matching corresponding parenthesized group.
* <b>`replace_global`</b>: `bool`, if `True` replace all non-overlapping matches,
  else replace only the first match.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

string `Tensor` of the same shape as `input` with specified replacements.
