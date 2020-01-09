page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.to_code


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/autograph/to_code">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L693-L727">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Similar to `to_graph`, but returns Python source code as a string.

### Aliases:

* <a href="/api_docs/python/tf/autograph/to_code"><code>tf.compat.v1.autograph.to_code</code></a>


``` python
tf.autograph.to_code(
    entity,
    recursive=True,
    arg_values=None,
    arg_types=None,
    indentation='  ',
    experimental_optional_features=None
)
```



<!-- Placeholder for "Used in" -->

Also see: <a href="../../tf/autograph/to_graph"><code>tf.autograph.to_graph</code></a>.

`to_graph` returns the Python source code that can be used to generate a
TensorFlow graph that is functionally identical to the input Python code.

#### Args:


* <b>`entity`</b>: Python callable or class to convert.
* <b>`recursive`</b>: Whether to recursively convert any functions that the converted
  function may call.
* <b>`arg_values`</b>: Deprecated.
* <b>`arg_types`</b>: Deprecated.
* <b>`indentation`</b>: Deprecated.
* <b>`experimental_optional_features`</b>: `None`, a tuple of, or a single
  <a href="../../tf/autograph/experimental/Feature"><code>tf.autograph.experimental.Feature</code></a> value. Controls the use of optional
  features in the conversion process.


#### Returns:

The converted code as string.
