page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.reduce_logsumexp

Computes log(sum(exp(elements across dimensions of a tensor))).

### Aliases:

* `tf.compat.v2.math.reduce_logsumexp`
* `tf.compat.v2.reduce_logsumexp`

``` python
tf.compat.v2.reduce_logsumexp(
    input_tensor,
    axis=None,
    keepdims=False,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a
tensor with a single element is returned.

This function is more numerically stable than log(sum(exp(input))). It avoids
overflows caused by taking the exp of large inputs and underflows caused by
taking the log of small inputs.

#### For example:



```python
x = tf.constant([[0., 0., 0.], [0., 0., 0.]])
tf.reduce_logsumexp(x)  # log(6)
tf.reduce_logsumexp(x, 0)  # [log(2), log(2), log(2)]
tf.reduce_logsumexp(x, 1)  # [log(3), log(3)]
tf.reduce_logsumexp(x, 1, keepdims=True)  # [[log(3)], [log(3)]]
tf.reduce_logsumexp(x, [0, 1])  # log(6)
```

#### Args:


* <b>`input_tensor`</b>: The tensor to reduce. Should have numeric type.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default), reduces all
  dimensions. Must be in the range `[-rank(input_tensor),
  rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

The reduced tensor.
