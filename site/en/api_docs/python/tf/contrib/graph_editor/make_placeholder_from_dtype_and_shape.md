page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_placeholder_from_dtype_and_shape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L474-L494">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create a tf.compat.v1.placeholder for the Graph Editor.

### Aliases:

* <a href="/api_docs/python/tf/contrib/graph_editor/make_placeholder_from_dtype_and_shape"><code>tf.contrib.graph_editor.ph</code></a>


``` python
tf.contrib.graph_editor.make_placeholder_from_dtype_and_shape(
    dtype,
    shape=None,
    scope=None,
    prefix=_DEFAULT_PLACEHOLDER_PREFIX
)
```



<!-- Placeholder for "Used in" -->

Note that the correct graph scope must be set by the calling function.
The placeholder is named using the function placeholder_name (with no
tensor argument).

#### Args:


* <b>`dtype`</b>: the tensor type.
* <b>`shape`</b>: the tensor shape (optional).
* <b>`scope`</b>: absolute scope within which to create the placeholder. None means
  that the scope of t is preserved. "" means the root scope.
* <b>`prefix`</b>: placeholder name prefix.


#### Returns:

A newly created tf.placeholder.
