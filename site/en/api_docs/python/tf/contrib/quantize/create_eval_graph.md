page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.quantize.create_eval_graph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/quantize/python/quantize_graph.py#L125-L143">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Rewrites an eval input_graph in place for simulated quantization.

``` python
tf.contrib.quantize.create_eval_graph(input_graph=None)
```



<!-- Placeholder for "Used in" -->

Variables added by the rewrite get added to the global variables collection.

The graph has fake quantization ops inserted to simulate the error
introduced by quantization. Since the graph is transformed in place,
the expected behavior of previously held references to nodes and tensors may
change.

#### Args:


* <b>`input_graph`</b>: The tf.Graph to be transformed, if None then defaults to the
  default graph.


#### Raises:


* <b>`ValueError`</b>: If elements contains an element that isn't a tf.Tensor or
  tf.Operation.
