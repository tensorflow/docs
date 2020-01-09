page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.hessians


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/gradients_impl.py#L399-L406">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Constructs the Hessian of sum of `ys` with respect to `x` in `xs`.

### Aliases:

* `tf.compat.v2.hessians`


``` python
tf.hessians(
    ys,
    xs,
    gate_gradients=False,
    aggregation_method=None,
    name='hessians'
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
