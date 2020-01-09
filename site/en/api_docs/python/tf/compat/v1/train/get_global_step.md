page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.get_global_step


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/training_util.py#L71-L103">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Get the global step tensor.

``` python
tf.compat.v1.train.get_global_step(graph=None)
```



### Used in the guide:

* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)



The global step tensor must be an integer variable. We first try to find it
in the collection `GLOBAL_STEP`, or by name `global_step:0`.

#### Args:


* <b>`graph`</b>: The graph to find the global step in. If missing, use default graph.


#### Returns:

The global step variable, or `None` if none was found.



#### Raises:


* <b>`TypeError`</b>: If the global step tensor has a non-integer type, or if it is not
  a `Variable`.
