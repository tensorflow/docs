page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.cond

``` python
tf.cond(
    pred,
    true_fn=None,
    false_fn=None,
    strict=False,
    name=None,
    fn1=None,
    fn2=None
)
```



Defined in [`tensorflow/python/ops/control_flow_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/ops/control_flow_ops.py).

Return `true_fn()` if the predicate `pred` is true else `false_fn()`. (deprecated arguments)

SOME ARGUMENTS ARE DEPRECATED. They will be removed in a future version.
Instructions for updating:
fn1/fn2 are deprecated in favor of the true_fn/false_fn arguments.

`true_fn` and `false_fn` both return lists of output tensors. `true_fn` and
`false_fn` must have the same non-zero number and type of outputs.

**WARNING**: Any Tensors or Operations created outside of `true_fn` and
`false_fn` will be executed regardless of which branch is selected at runtime.

Although this behavior is consistent with the dataflow model of TensorFlow,
it has frequently surprised users who expected a lazier semantics.
Consider the following simple program:

```python
z = tf.multiply(a, b)
result = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))
```

If `x < y`, the <a href="../tf/math/add"><code>tf.add</code></a> operation will be executed and <a href="../tf/math/square"><code>tf.square</code></a>
operation will not be executed. Since `z` is needed for at least one
branch of the `cond`, the <a href="../tf/math/multiply"><code>tf.multiply</code></a> operation is always executed,
unconditionally.

Note that `cond` calls `true_fn` and `false_fn` *exactly once* (inside the
call to `cond`, and not at all during `Session.run()`). `cond`
stitches together the graph fragments created during the `true_fn` and
`false_fn` calls with some additional graph nodes to ensure that the right
branch gets executed depending on the value of `pred`.

<a href="../tf/cond"><code>tf.cond</code></a> supports nested structures as implemented in
`tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the
same (possibly nested) value structure of lists, tuples, and/or named tuples.
Singleton lists and tuples form the only exceptions to this: when returned by
`true_fn` and/or `false_fn`, they are implicitly unpacked to single values.
This behavior is disabled by passing `strict=True`.

#### Args:

* <b>`pred`</b>: A scalar determining whether to return the result of `true_fn` or
    `false_fn`.
* <b>`true_fn`</b>: The callable to be performed if pred is true.
* <b>`false_fn`</b>: The callable to be performed if pred is false.
* <b>`strict`</b>: A boolean that enables/disables 'strict' mode; see above.
* <b>`name`</b>: Optional name prefix for the returned tensors.


#### Returns:

Tensors returned by the call to either `true_fn` or `false_fn`. If the
callables return a singleton list, the element is extracted from the list.


#### Raises:

* <b>`TypeError`</b>: if `true_fn` or `false_fn` is not callable.
* <b>`ValueError`</b>: if `true_fn` and `false_fn` do not return the same number of
    tensors, or return tensors of different types.

Example:

```python
x = tf.constant(2)
y = tf.constant(5)
def f1(): return tf.multiply(x, 17)
def f2(): return tf.add(y, 23)
r = tf.cond(tf.less(x, y), f1, f2)
# r is set to f1().
# Operations in f2 (e.g., tf.add) are not executed.
```