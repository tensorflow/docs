page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.math.add_n

Adds all input tensors element-wise.

### Aliases:

* `tf.add_n`
* `tf.compat.v1.add_n`
* `tf.compat.v1.math.add_n`
* `tf.compat.v2.add_n`
* `tf.compat.v2.math.add_n`
* `tf.math.add_n`

``` python
tf.math.add_n(
    inputs,
    name=None
)
```



Defined in [`python/ops/math_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/math_ops.py).

<!-- Placeholder for "Used in" -->

Converts `IndexedSlices` objects into dense tensors prior to adding.

<a href="../../tf/math/add_n"><code>tf.math.add_n</code></a> performs the same operation as <a href="../../tf/math/accumulate_n"><code>tf.math.accumulate_n</code></a>, but it
waits for all of its inputs to be ready before beginning to sum.
This buffering can result in higher memory consumption when inputs are ready
at different times, since the minimum temporary storage required is
proportional to the input size rather than the output size.

This op does not [broadcast](
https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html)
its inputs. If you need broadcasting, use <a href="../../tf/math/add"><code>tf.math.add</code></a> (or the `+` operator)
instead.

#### For example:



```python
a = tf.constant([[3, 5], [4, 8]])
b = tf.constant([[1, 6], [2, 9]])
tf.math.add_n([a, b, a])  # [[7, 16], [10, 25]]
```

#### Args:


* <b>`inputs`</b>: A list of <a href="../../tf/Tensor"><code>tf.Tensor</code></a> or <a href="../../tf/IndexedSlices"><code>tf.IndexedSlices</code></a> objects, each with same
  shape and type.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of same shape and type as the elements of `inputs`.



#### Raises:


* <b>`ValueError`</b>: If `inputs` don't all have same shape and dtype or the shape
cannot be inferred.