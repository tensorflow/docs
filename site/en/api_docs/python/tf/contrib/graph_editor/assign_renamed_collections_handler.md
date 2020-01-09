page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.assign_renamed_collections_handler


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L85-L105">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Add the transformed elem to the (renamed) collections of elem.

``` python
tf.contrib.graph_editor.assign_renamed_collections_handler(
    info,
    elem,
    elem_
)
```



<!-- Placeholder for "Used in" -->

A collection is renamed only if is not a known key, as described in
<a href="../../../tf/GraphKeys"><code>tf.compat.v1.GraphKeys</code></a>.

#### Args:


* <b>`info`</b>: Transform._TmpInfo instance.
* <b>`elem`</b>: the original element (<a href="../../../tf/Tensor"><code>tf.Tensor</code></a> or <a href="../../../tf/Operation"><code>tf.Operation</code></a>)
* <b>`elem_`</b>: the transformed element
