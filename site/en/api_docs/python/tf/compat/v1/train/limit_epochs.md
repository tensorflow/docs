page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.limit_epochs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/input.py#L81-L114">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns tensor `num_epochs` times and then raises an `OutOfRange` error. (deprecated)

``` python
tf.compat.v1.train.limit_epochs(
    tensor,
    num_epochs=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data"><code>tf.data</code></a>. Use `tf.data.Dataset.from_tensors(tensor).repeat(num_epochs)`.

Note: creates local counter `epochs`. Use `local_variables_initializer()` to
initialize local variables.

#### Args:


* <b>`tensor`</b>: Any `Tensor`.
* <b>`num_epochs`</b>: A positive integer (optional).  If specified, limits the number
  of steps the output tensor may be evaluated.
* <b>`name`</b>: A name for the operations (optional).


#### Returns:

tensor or `OutOfRange`.



#### Raises:


* <b>`ValueError`</b>: if `num_epochs` is invalid.
