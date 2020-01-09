page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.swap_ts


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/reroute.py#L208-L230">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



For each tensor's pair, swap the end of (t0,t1).

``` python
tf.contrib.graph_editor.swap_ts(
    ts0,
    ts1,
    can_modify=None,
    cannot_modify=None
)
```



<!-- Placeholder for "Used in" -->

    B0 B1     B0 B1
    |  |    =>  X
    A0 A1     A0 A1

#### Args:


* <b>`ts0`</b>: an object convertible to a list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.
* <b>`ts1`</b>: an object convertible to a list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.
* <b>`can_modify`</b>: iterable of operations which can be modified. Any operation
  outside within_ops will be left untouched by this function.
* <b>`cannot_modify`</b>: iterable of operations which cannot be modified.
  Any operation within cannot_modify will be left untouched by this
  function.

#### Returns:

The number of individual modifications made by the function.


#### Raises:


* <b>`TypeError`</b>: if ts0 or ts1 cannot be converted to a list of tf.Tensor.
* <b>`TypeError`</b>: if can_modify or cannot_modify is not None and cannot be
  converted to a list of tf.Operation.
