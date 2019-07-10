page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.filter_ts

Get all the tensors which are input or output of an op in ops.

``` python
tf.contrib.graph_editor.filter_ts(
    ops,
    positive_filter
)
```



Defined in [`contrib/graph_editor/select.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/select.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ops`</b>: an object convertible to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
* <b>`positive_filter`</b>: a function deciding whether to keep a tensor or not.
  If `True`, all the tensors are returned.

#### Returns:

A list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.


#### Raises:


* <b>`TypeError`</b>: if ops cannot be converted to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.