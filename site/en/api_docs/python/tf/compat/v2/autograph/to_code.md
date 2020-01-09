page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.autograph.to_code


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/autograph/impl/api.py#L730-L755">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Similar to `to_graph`, but returns Python source code as a string.

### Aliases:

* <a href="/api_docs/python/tf/compat/v2/autograph/to_code"><code>tf.contrib.autograph.to_code</code></a>


``` python
tf.compat.v2.autograph.to_code(
    entity,
    recursive=True,
    experimental_optional_features=None
)
```



<!-- Placeholder for "Used in" -->

Also see: <a href="../../../../tf/autograph/to_graph"><code>tf.autograph.to_graph</code></a>.

`to_graph` returns the Python source code that can be used to generate a
TensorFlow graph that is functionally identical to the input Python code.

#### Args:


* <b>`entity`</b>: Python callable or class to convert.
* <b>`recursive`</b>: Whether to recursively convert any functions that the converted
  function may call.
* <b>`experimental_optional_features`</b>: `None`, a tuple of, or a single
  <a href="../../../../tf/autograph/experimental/Feature"><code>tf.autograph.experimental.Feature</code></a> value. Controls the use of optional
  features in the conversion process.


#### Returns:

The converted code as string.
