page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_consuming_ops

Return all the consuming ops of the tensors in ts.

``` python
tf.contrib.graph_editor.get_consuming_ops(ts)
```



Defined in [`contrib/graph_editor/util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/graph_editor/util.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ts`</b>: a list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>

#### Returns:

A list of all the consuming <a href="../../../tf/Operation"><code>tf.Operation</code></a> of the tensors in `ts`.


#### Raises:


* <b>`TypeError`</b>: if ts cannot be converted to a list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.