page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.eager.implicit_gradients

``` python
tf.contrib.eager.implicit_gradients(f)
```



Defined in [`tensorflow/python/eager/backprop.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/eager/backprop.py).

Returns a function which differentiates f with respect to variables.

The wrapped function returns the gradient of f when called with the same
arguments. The gradient is with respect to all trainable TFE variables
accessed by `f`.

This function is useful when the exact set of variables to differentiate with
is not known ahead of time.

Example:

```python
dense_layer = tf.layers.Dense(1)
def loss(x, y):
  return tf.reduce_sum(tf.square(dense_layer(x) - y))

# Obtain the gradient function.
grad_fn = tfe.implicit_gradients(loss)

# Invoke the gradient function with concrete values of x and y.
x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
y = tf.constant([[10.0], [20.0]])
grads_and_vars = grad_fn(x, y)

# Apply the gradients to Variables.
optimizer = tf.train.GradientDescentOptimizer(0.1)
optimizer.apply_gradients(grads_and_vars)
```

#### Args:

* <b>`f`</b>: function to be differentiated. If `f` returns a scalar, this scalar will
    be differentiated. If `f` returns a tensor or list of tensors, by default
    a scalar will be computed by adding all their values to produce a single
    scalar.


#### Returns:

A function which, when called, returns a list of (gradient, variable) pairs.