page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.make_placeholder_from_tensor

Create a <a href="../../../tf/placeholder"><code>tf.compat.v1.placeholder</code></a> for the Graph Editor.

``` python
tf.contrib.graph_editor.make_placeholder_from_tensor(
    t,
    scope=None,
    prefix=_DEFAULT_PLACEHOLDER_PREFIX
)
```



Defined in [`contrib/graph_editor/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/util.py).

<!-- Placeholder for "Used in" -->

Note that the correct graph scope must be set by the calling function.

#### Args:


* <b>`t`</b>: a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a> whose name will be used to create the placeholder (see
  function placeholder_name).
* <b>`scope`</b>: absolute scope within which to create the placeholder. None means
  that the scope of `t` is preserved. `""` means the root scope.
* <b>`prefix`</b>: placeholder name prefix.


#### Returns:

A newly created <a href="../../../tf/placeholder"><code>tf.compat.v1.placeholder</code></a>.


#### Raises:


* <b>`TypeError`</b>: if `t` is not `None` or a <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.