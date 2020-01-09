page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.autograph.to_code


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/autograph/impl/api.py#L730-L755">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Similar to `to_graph`, but returns Python source code as a string.

### Aliases:

* `tf.compat.v2.autograph.to_code`


``` python
tf.autograph.to_code(
    entity,
    recursive=True,
    experimental_optional_features=None
)
```



### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)

### Used in the tutorials:

* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)



Also see: <a href="../../tf/autograph/to_graph"><code>tf.autograph.to_graph</code></a>.

`to_graph` returns the Python source code that can be used to generate a
TensorFlow graph that is functionally identical to the input Python code.

#### Args:


* <b>`entity`</b>: Python callable or class to convert.
* <b>`recursive`</b>: Whether to recursively convert any functions that the converted
  function may call.
* <b>`experimental_optional_features`</b>: `None`, a tuple of, or a single
  <a href="../../tf/autograph/experimental/Feature"><code>tf.autograph.experimental.Feature</code></a> value. Controls the use of optional
  features in the conversion process.


#### Returns:

The converted code as string.
