page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.hessians


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/hessians">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/gradients_impl.py#L332-L396">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.

### Aliases:

* <a href="/api_docs/python/tf/hessians"><code>tf.compat.v1.hessians</code></a>


``` python
tf.hessians(
    ys,
    xs,
    name='hessians',
    colocate_gradients_with_ops=False,
    gate_gradients=False,
    aggregation_method=None
)
```



<!-- Placeholder for "Used in" -->

`hessians()` adds ops to the graph to output the Hessian matrix of `ys`
with respect to `xs`.  It returns a list of `Tensor` of length `len(xs)`
where each tensor is the Hessian of `sum(ys)`.

The Hessian is a matrix of second-order partial derivatives of a scalar
tensor (see https://en.wikipedia.org/wiki/Hessian_matrix for more details).

#### Args:


* <b>`ys`</b>: A `Tensor` or list of tensors to be differentiated.
* <b>`xs`</b>: A `Tensor` or list of tensors to be used for differentiation.
* <b>`name`</b>: Optional name to use for grouping all the gradient ops together.
  defaults to 'hessians'.
* <b>`colocate_gradients_with_ops`</b>: See `gradients()` documentation for details.
* <b>`gate_gradients`</b>: See `gradients()` documentation for details.
* <b>`aggregation_method`</b>: See `gradients()` documentation for details.


#### Returns:

A list of Hessian matrices of `sum(ys)` for each `x` in `xs`.



#### Raises:


* <b>`LookupError`</b>: if one of the operations between `xs` and `ys` does not
  have a registered gradient function.
