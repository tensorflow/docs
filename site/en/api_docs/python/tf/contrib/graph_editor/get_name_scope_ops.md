page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_name_scope_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/select.py#L193-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get all the operations under the given scope path.

``` python
tf.contrib.graph_editor.get_name_scope_ops(
    ops,
    scope
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of tf.Operation.
* <b>`scope`</b>: a scope path.

#### Returns:

A list of tf.Operation.


#### Raises:


* <b>`TypeError`</b>: if ops cannot be converted to a list of tf.Operation.
