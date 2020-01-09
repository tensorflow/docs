page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.graph_editor.get_generating_ops


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/graph_editor/util.py#L305-L316">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Return all the generating ops of the tensors in `ts`.

``` python
tf.contrib.graph_editor.get_generating_ops(ts)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`ts`</b>: a list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>

#### Returns:

A list of all the generating <a href="../../../tf/Operation"><code>tf.Operation</code></a> of the tensors in `ts`.


#### Raises:


* <b>`TypeError`</b>: if `ts` cannot be converted to a list of <a href="../../../tf/Tensor"><code>tf.Tensor</code></a>.
