page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.scan


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/scan">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/functional_ops.py#L280-L529">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



scan on the list of tensors unpacked from `elems` on dimension 0.

### Aliases:

* <a href="/api_docs/python/tf/scan"><code>tf.compat.v1.scan</code></a>
* <a href="/api_docs/python/tf/scan"><code>tf.compat.v2.scan</code></a>


``` python
tf.scan(
    fn,
    elems,
    initializer=None,
    parallel_iterations=10,
    back_prop=True,
    swap_memory=False,
    infer_shape=True,
    reverse=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

The simplest version of `scan` repeatedly applies the callable `fn` to a
sequence of elements from first to last. The elements are made of the tensors
unpacked from `elems` on dimension 0. The callable fn takes two tensors as
arguments. The first argument is the accumulated value computed from the
preceding invocation of fn, and the second is the value at the current
position of `elems`. If `initializer` is None, `elems` must contain at least
one element, and its first element is used as the initializer.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
of the result tensor is `[len(values)] + fn(initializer, values[0]).shape`.
If reverse=True, it's fn(initializer, values[-1]).shape.

This method also allows multi-arity `elems` and accumulator.  If `elems`
is a (possibly nested) list or tuple of tensors, then each of these tensors
must have a matching first (unpack) dimension.  The second argument of
`fn` must match the structure of `elems`.

If no `initializer` is provided, the output structure and dtypes of `fn`
are assumed to be the same as its input; and in this case, the first
argument of `fn` must match the structure of `elems`.

If an `initializer` is provided, then the output of `fn` must have the same
structure as `initializer`; and the first argument of `fn` must match
this structure.

For example, if `elems` is `(t1, [t2, t3])` and `initializer` is
`[i1, i2]` then an appropriate signature for `fn` in `python2` is:
`fn = lambda (acc_p1, acc_p2), (t1, [t2, t3]):` and `fn` must return a list,
`[acc_n1, acc_n2]`.  An alternative correct signature for `fn`, and the
 one that works in `python3`, is:
`fn = lambda a, t:`, where `a` and `t` correspond to the input tuples.

#### Args:


* <b>`fn`</b>: The callable to be performed.  It accepts two arguments.  The first will
  have the same structure as `initializer` if one is provided, otherwise it
  will have the same structure as `elems`.  The second will have the same
  (possibly nested) structure as `elems`.  Its output must have the same
  structure as `initializer` if one is provided, otherwise it must have the
  same structure as `elems`.
* <b>`elems`</b>: A tensor or (possibly nested) sequence of tensors, each of which will
  be unpacked along their first dimension.  The nested sequence of the
  resulting slices will be the first argument to `fn`.
* <b>`initializer`</b>: (optional) A tensor or (possibly nested) sequence of tensors,
  initial value for the accumulator, and the expected output type of `fn`.
* <b>`parallel_iterations`</b>: (optional) The number of iterations allowed to run in
  parallel.
* <b>`back_prop`</b>: (optional) True enables support for back propagation.
* <b>`swap_memory`</b>: (optional) True enables GPU-CPU memory swapping.
* <b>`infer_shape`</b>: (optional) False disables tests for consistent output shapes.
* <b>`reverse`</b>: (optional) True scans the tensor last to first (instead of first to
  last).
* <b>`name`</b>: (optional) Name prefix for the returned tensors.


#### Returns:

A tensor or (possibly nested) sequence of tensors.  Each tensor packs the
results of applying `fn` to tensors unpacked from `elems` along the first
dimension, and the previous accumulator value(s), from first to last (or
last to first, if `reverse=True`).



#### Raises:


* <b>`TypeError`</b>: if `fn` is not callable or the structure of the output of
  `fn` and `initializer` do not match.
* <b>`ValueError`</b>: if the lengths of the output of `fn` and `initializer`
  do not match.


#### Examples:

```python
elems = np.array([1, 2, 3, 4, 5, 6])
sum = scan(lambda a, x: a + x, elems)
# sum == [1, 3, 6, 10, 15, 21]
sum = scan(lambda a, x: a + x, elems, reverse=True)
# sum == [21, 20, 18, 15, 11, 6]
```

```python
elems = np.array([1, 2, 3, 4, 5, 6])
initializer = np.array(0)
sum_one = scan(
    lambda a, x: x[0] - x[1] + a, (elems + 1, elems), initializer)
# sum_one == [1, 2, 3, 4, 5, 6]
```

```python
elems = np.array([1, 0, 0, 0, 0, 0])
initializer = (np.array(0), np.array(1))
fibonaccis = scan(lambda a, _: (a[1], a[0] + a[1]), elems, initializer)
# fibonaccis == ([1, 1, 2, 3, 5, 8], [1, 2, 3, 5, 8, 13])
```
