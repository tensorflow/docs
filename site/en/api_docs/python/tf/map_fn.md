description: map on the list of tensors unpacked from elems on dimension 0. (deprecated argument values)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.map_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.map_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/map_fn.py#L290-L425">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



map on the list of tensors unpacked from `elems` on dimension 0. (deprecated argument values)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.map_fn(
    fn, elems, dtype=None, parallel_iterations=None, back_prop=(True),
    swap_memory=(False), infer_shape=(True), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENT VALUES ARE DEPRECATED: `(back_prop=False)`. They will be removed in a future version.
Instructions for updating:
back_prop=False is deprecated. Consider using tf.stop_gradient instead.
Instead of:
results = tf.map_fn(fn, elems, back_prop=False)
Use:
results = tf.nest.map_structure(tf.stop_gradient, tf.map_fn(fn, elems))

The simplest version of `map_fn` repeatedly applies the callable `fn` to a
sequence of elements from first to last. The elements are made of the
tensors unpacked from `elems`. `dtype` is the data type of the return
value of `fn`. Users must provide `dtype` if it is different from
the data type of `elems`.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
of the result tensor is `[values.shape[0]] + fn(values[0]).shape`.

This method also allows multi-arity `elems` and output of `fn`.  If `elems`
is a (possibly nested) list or tuple of tensors, then each of these tensors
must have a matching first (unpack) dimension.  The signature of `fn` may
match the structure of `elems`.  That is, if `elems` is
`(t1, [t2, t3, [t4, t5]])`, then an appropriate signature for `fn` is:
`fn = lambda (t1, [t2, t3, [t4, t5]]):`.

Furthermore, `fn` may emit a different structure than its input.  For example,
`fn` may look like: `fn = lambda t1: return (t1 + 1, t1 - 1)`.  In this case,
the `dtype` parameter is not optional: `dtype` must be a type or (possibly
nested) tuple of types matching the output of `fn`.

To apply a functional operation to the nonzero elements of a SparseTensor
one of the following methods is recommended. First, if the function is
expressible as TensorFlow ops, use

```python
  result = SparseTensor(input.indices, fn(input.values), input.dense_shape)
```

If, however, the function is not expressible as a TensorFlow op, then use

```python
result = SparseTensor(
  input.indices, map_fn(fn, input.values), input.dense_shape)
```

instead.

When executing eagerly, map_fn does not execute in parallel even if
`parallel_iterations` is set to a value > 1. You can still get the
performance benefits of running a function in parallel by using the
<a href="../tf/function.md"><code>tf.function</code></a> decorator,

```python
# Assume the function being used in map_fn is fn.
# To ensure map_fn calls fn in parallel, use the tf.function decorator.
@tf.function
def func(tensor):
  return tf.map_fn(fn, tensor)
```

Note that if you use the <a href="../tf/function.md"><code>tf.function</code></a> decorator, any non-TensorFlow Python
code that you may have written in your function won't get executed. See
[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) for
more  details. The recommendation would be to debug without <a href="../tf/function.md"><code>tf.function</code></a> but
switch to it to get performance benefits of running `map_fn` in parallel.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`fn`
</td>
<td>
The callable to be performed.  It accepts one argument, which will have
the same (possibly nested) structure as `elems`.  Its output must have the
same structure as `dtype` if one is provided, otherwise it must have the
same structure as `elems`.
</td>
</tr><tr>
<td>
`elems`
</td>
<td>
A tensor or (possibly nested) sequence of tensors, each of which will
be unpacked along their first dimension.  The nested sequence of the
resulting slices will be applied to `fn`.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(optional) The output type(s) of `fn`.  If `fn` returns a structure
of Tensors differing from the structure of `elems`, then `dtype` is not
optional and must have the same structure as the output of `fn`.
</td>
</tr><tr>
<td>
`parallel_iterations`
</td>
<td>
(optional) The number of iterations allowed to run in
parallel. When graph building, the default value is 10. While executing
eagerly, the default value is set to 1.
</td>
</tr><tr>
<td>
`back_prop`
</td>
<td>
(optional) Deprecated. False disables support for back
propagation. Prefer using <a href="../tf/stop_gradient.md"><code>tf.stop_gradient</code></a> instead.
</td>
</tr><tr>
<td>
`swap_memory`
</td>
<td>
(optional) True enables GPU-CPU memory swapping.
</td>
</tr><tr>
<td>
`infer_shape`
</td>
<td>
(optional) False disables tests for consistent output shapes.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(optional) Name prefix for the returned tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor or (possibly nested) sequence of tensors.  Each tensor packs the
results of applying `fn` to tensors unpacked from `elems` along the first
dimension, from first to last.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
if `fn` is not callable or the structure of the output of
`fn` and `dtype` do not match, or if elems is a SparseTensor.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if the lengths of the output of `fn` and `dtype` do not match.
</td>
</tr>
</table>



#### Examples:

```python
elems = np.array([1, 2, 3, 4, 5, 6])
squares = map_fn(lambda x: x * x, elems)
# squares == [1, 4, 9, 16, 25, 36]
```

```python
elems = (np.array([1, 2, 3]), np.array([-1, 1, -1]))
alternate = map_fn(lambda x: x[0] * x[1], elems, dtype=tf.int64)
# alternate == [-1, 2, -3]
```

```python
elems = np.array([1, 2, 3])
alternates = map_fn(lambda x: (x, -x), elems, dtype=(tf.int64, tf.int64))
# alternates[0] == [1, 2, 3]
# alternates[1] == [-1, -2, -3]
```
