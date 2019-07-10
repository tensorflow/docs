page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.no_gradient

Specifies that ops of type `op_type` is not differentiable.

### Aliases:

* `tf.NoGradient`
* `tf.NotDifferentiable`
* `tf.compat.v1.NoGradient`
* `tf.compat.v1.NotDifferentiable`
* `tf.compat.v1.no_gradient`
* `tf.compat.v2.no_gradient`
* `tf.no_gradient`

``` python
tf.no_gradient(op_type)
```



Defined in [`python/framework/ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/ops.py).

<!-- Placeholder for "Used in" -->

This function should *not* be used for operations that have a
well-defined gradient that is not yet implemented.

This function is only used when defining a new op type. It may be
used for ops such as <a href="../tf/size"><code>tf.size()</code></a> that are not differentiable.  For
example:

```python
tf.no_gradient("Size")
```

The gradient computed for 'op_type' will then propagate zeros.

For ops that have a well-defined gradient but are not yet implemented,
no declaration should be made, and an error *must* be thrown if
an attempt to request its gradient is made.

#### Args:


* <b>`op_type`</b>: The string type of an operation. This corresponds to the
  `OpDef.name` field for the proto that defines the operation.


#### Raises:


* <b>`TypeError`</b>: If `op_type` is not a string.