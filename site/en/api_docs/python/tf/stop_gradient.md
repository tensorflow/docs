page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.stop_gradient

Stops gradient computation.

### Aliases:

* `tf.compat.v1.stop_gradient`
* `tf.compat.v2.stop_gradient`
* `tf.stop_gradient`

``` python
tf.stop_gradient(
    input,
    name=None
)
```



Defined in generated file: `python/ops/gen_array_ops.py`.

<!-- Placeholder for "Used in" -->

When executed in a graph, this op outputs its input tensor as-is.

When building ops to compute gradients, this op prevents the contribution of
its inputs to be taken into account.  Normally, the gradient generator adds ops
to a graph to compute the derivatives of a specified 'loss' by recursively
finding out inputs that contributed to its computation.  If you insert this op
in the graph it inputs are masked from the gradient generator.  They are not
taken into account for computing gradients.

This is useful any time you want to compute a value with TensorFlow but need
to pretend that the value was a constant. Some examples include:

*  The *EM* algorithm where the *M-step* should not involve backpropagation
   through the output of the *E-step*.
*  Contrastive divergence training of Boltzmann machines where, when
   differentiating the energy function, the training must not backpropagate
   through the graph that generated the samples from the model.
*  Adversarial training, where no backprop should happen through the adversarial
   example generation process.

#### Args:


* <b>`input`</b>: A `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
