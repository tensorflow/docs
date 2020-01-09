page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.graph_replace


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/transform.py#L709-L752">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Create a new graph which compute the targets from the replaced Tensors.

``` python
tf.contrib.graph_editor.graph_replace(
    target_ts,
    replacement_ts,
    dst_scope='',
    src_scope='',
    reuse_dst_scope=False
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`target_ts`</b>: a single tf.Tensor or an iterable of tf.Tensor.
* <b>`replacement_ts`</b>: dictionary mapping from original tensors to replaced tensors
* <b>`dst_scope`</b>: the destination scope.
* <b>`src_scope`</b>: the source scope.
* <b>`reuse_dst_scope`</b>: if True the dst_scope is re-used if it already exists.
  Otherwise, the scope is given a unique name based on the one given
  by appending an underscore followed by a digit (default).

#### Returns:

A single tf.Tensor or a list of target tf.Tensor, depending on
the type of the input argument `target_ts`.
The returned tensors are recomputed using the tensors from replacement_ts.


#### Raises:


* <b>`ValueError`</b>: if the targets are not connected to replacement_ts.
