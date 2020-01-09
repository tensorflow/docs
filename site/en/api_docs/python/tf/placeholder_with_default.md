page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.placeholder_with_default


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2622-L2635">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



A placeholder op that passes through `input` when its output is not fed.

### Aliases:

* <a href="/api_docs/python/tf/placeholder_with_default"><code>tf.compat.v1.placeholder_with_default</code></a>


``` python
tf.placeholder_with_default(
    input,
    shape,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`input`</b>: A `Tensor`. The default value to produce when output is not fed.
* <b>`shape`</b>: A <a href="../tf/TensorShape"><code>tf.TensorShape</code></a> or list of `int`s. The (possibly partial) shape of
  the tensor.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
