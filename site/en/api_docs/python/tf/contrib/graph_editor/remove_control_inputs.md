page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.remove_control_inputs

``` python
tf.contrib.graph_editor.remove_control_inputs(
    op,
    cops
)
```



Defined in [`tensorflow/contrib/graph_editor/reroute.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/graph_editor/reroute.py).

See the guide: [Graph Editor (contrib) > Module: reroute](../../../../../api_guides/python/contrib.graph_editor#Module_reroute)

Remove the control inputs cops from co.

Warning: this function is directly manipulating the internals of the
<a href="../../../tf/Graph"><code>tf.Graph</code></a>.

#### Args:

* <b>`op`</b>: a <a href="../../../tf/Operation"><code>tf.Operation</code></a> from which to remove the control inputs.
* <b>`cops`</b>: an object convertible to a list of <a href="../../../tf/Operation"><code>tf.Operation</code></a>.

#### Raises:

* <b>`TypeError`</b>: if op is not a <a href="../../../tf/Operation"><code>tf.Operation</code></a>.
* <b>`ValueError`</b>: if any cop in cops is not a control input of op.