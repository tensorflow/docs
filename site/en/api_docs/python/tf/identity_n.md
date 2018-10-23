

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.identity_n

``` python
tf.identity_n(
    input,
    name=None
)
```



Defined in `tensorflow/python/ops/gen_array_ops.py`.

Returns a list of tensors with the same shapes and contents as the input

tensors.

This op can be used to override the gradient for complicated functions. For
example, suppose y = f(x) and we wish to apply a custom function g for backprop
such that dx = g(dy). In Python,

```python
with tf.get_default_graph().gradient_override_map(
    {'IdentityN': 'OverrideGradientWithG'}):
  y, _ = identity_n([f(x), x])

@tf.RegisterGradient('OverrideGradientWithG')
def ApplyG(op, dy, _):
  return [None, g(dy)]  # Do not backprop to f(x).
```

#### Args:

* <b>`input`</b>: A list of `Tensor` objects.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A list of `Tensor` objects. Has the same type as `input`.