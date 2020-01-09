page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.ragged.placeholder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/ragged/ragged_factory_ops.py#L316-L349">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Creates a placeholder for a <a href="../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a> that will always be fed.

### Aliases:

* <a href="/api_docs/python/tf/ragged/placeholder"><code>tf.compat.v1.ragged.placeholder</code></a>


``` python
tf.ragged.placeholder(
    dtype,
    ragged_rank,
    value_shape=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

**Important**: This ragged tensor will produce an error if evaluated.
Its value must be fed using the `feed_dict` optional argument to
<a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a>, <a href="../../tf/Tensor#eval"><code>Tensor.eval()</code></a>, or <a href="../../tf/Operation#run"><code>Operation.run()</code></a>.

@compatibility{eager} Placeholders are not compatible with eager execution.

#### Args:


* <b>`dtype`</b>: The data type for the `RaggedTensor`.
* <b>`ragged_rank`</b>: The ragged rank for the `RaggedTensor`
* <b>`value_shape`</b>: The shape for individual flat values in the `RaggedTensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `RaggedTensor` that may be used as a handle for feeding a value, but
not evaluated directly.



#### Raises:


* <b>`RuntimeError`</b>: if eager execution is enabled
