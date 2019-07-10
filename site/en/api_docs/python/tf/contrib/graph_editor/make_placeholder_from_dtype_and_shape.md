page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_placeholder_from_dtype_and_shape

### Aliases:

* `tf.contrib.graph_editor.make_placeholder_from_dtype_and_shape`
* `tf.contrib.graph_editor.ph`

``` python
tf.contrib.graph_editor.make_placeholder_from_dtype_and_shape(
    dtype,
    shape=None,
    scope=None,
    prefix=_DEFAULT_PLACEHOLDER_PREFIX
)
```



Defined in [`tensorflow/contrib/graph_editor/util.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/graph_editor/util.py).

Create a tf.placeholder for the Graph Editor.

Note that the correct graph scope must be set by the calling function.
The placeholder is named using the function placeholder_name (with no
tensor argument).

#### Args:

* <b>`dtype`</b>: the tensor type.
* <b>`shape`</b>: the tensor shape (optional).
* <b>`scope`</b>: absolute scope within which to create the placeholder. None
    means that the scope of t is preserved. "" means the root scope.
* <b>`prefix`</b>: placeholder name prefix.

#### Returns:

A newly created tf.placeholder.