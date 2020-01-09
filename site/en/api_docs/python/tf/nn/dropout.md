page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.dropout


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/nn_ops.py#L4232-L4317">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes dropout.

### Aliases:

* `tf.compat.v2.nn.dropout`


``` python
tf.nn.dropout(
    x,
    rate,
    noise_shape=None,
    seed=None,
    name=None
)
```



### Used in the guide:

* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)



With probability `rate`, drops elements of `x`. Input that are kept are
scaled up by `1 / (1 - rate)`, otherwise outputs `0`.  The scaling is so that
the expected sum is unchanged.

**Note:** The behavior of dropout has changed between TensorFlow 1.x and 2.x.
When converting 1.x code, please use named arguments to ensure behavior stays
consistent.

By default, each element is kept or dropped independently.  If `noise_shape`
is specified, it must be
[broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
will make independent decisions.  For example, if `shape(x) = [k, l, m, n]`
and `noise_shape = [k, 1, 1, n]`, each batch and channel component will be
kept independently and each row and column will be kept or not kept together.

#### Args:


* <b>`x`</b>: A floating point tensor.
* <b>`rate`</b>: A scalar `Tensor` with the same type as x. The probability
  that each element is dropped. For example, setting rate=0.1 would drop
  10% of input elements.
* <b>`noise_shape`</b>: A 1-D `Tensor` of type `int32`, representing the
  shape for randomly generated keep/drop flags.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
  <a href="../../tf/compat/v1/set_random_seed"><code>tf.compat.v1.set_random_seed</code></a> for behavior.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:

A Tensor of the same shape of `x`.



#### Raises:


* <b>`ValueError`</b>: If `rate` is not in `(0, 1]` or if `x` is not a floating point
  tensor.
