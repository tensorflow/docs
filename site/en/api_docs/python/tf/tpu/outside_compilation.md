page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.tpu.outside_compilation


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/tpu/tpu.py#L535-L575">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Builds part of a computation outside any current TPU replicate scope.

### Aliases:

* <a href="/api_docs/python/tf/tpu/outside_compilation"><code>tf.compat.v1.tpu.outside_compilation</code></a>
* <a href="/api_docs/python/tf/tpu/outside_compilation"><code>tf.contrib.tpu.outside_compilation</code></a>


``` python
tf.tpu.outside_compilation(
    computation,
    *args,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`computation`</b>: A Python function that builds the computation to
  place on the host.
* <b>`*args`</b>: the positional arguments for the computation.
* <b>`**kwargs`</b>: the keyword arguments for the computation.


#### Returns:

The Tensors returned by computation.
