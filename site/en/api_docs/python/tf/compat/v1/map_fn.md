description: Transforms elems by applying fn to each element unstacked on axis 0. (deprecated arguments)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.map_fn" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.map_fn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/map_fn.py#L51-L532">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Transforms `elems` by applying `fn` to each element unstacked on axis 0. (deprecated arguments)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.map_fn(
    fn, elems, dtype=None, parallel_iterations=None, back_prop=(True),
    swap_memory=(False), infer_shape=(True), name=None, fn_output_signature=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(dtype)`. They will be removed in a future version.
Instructions for updating:
Use fn_output_signature instead

See also <a href="../../../tf/scan.md"><code>tf.scan</code></a>.

`map_fn` unstacks `elems` on axis 0 to obtain a sequence of elements;
calls `fn` to transform each element; and then stacks the transformed
values back together.

#### Mapping functions with single-Tensor inputs and outputs

If `elems` is a single tensor and `fn`'s signature is `tf.Tensor->tf.Tensor`,
then `map_fn(fn, elems)` is equivalent to
`tf.stack([fn(elem) for elem in tf.unstack(elems)])`.  E.g.:

```
>>> tf.map_fn(fn=lambda t: tf.range(t, t + 3), elems=tf.constant([3, 5, 2]))
<tf.Tensor: shape=(3, 3), dtype=int32, numpy=
  array([[3, 4, 5],
         [5, 6, 7],
         [2, 3, 4]], dtype=int32)>
```

`map_fn(fn, elems).shape = [elems.shape[0]] + fn(elems[0]).shape`.

#### Mapping functions with multi-arity inputs and outputs

`map_fn` also supports functions with multi-arity inputs and outputs:

* If `elems` is a tuple (or nested structure) of tensors, then those tensors
  must all have the same outer-dimension size (`num_elems`); and `fn` is
  used to transform each tuple (or structure) of corresponding slices from
  `elems`.  E.g., if `elems` is a tuple `(t1, t2, t3)`, then `fn` is used to
  transform each tuple of slices `(t1[i], t2[i], t3[i])`
  (where `0 <= i < num_elems`).

* If `fn` returns a tuple (or nested structure) of tensors, then the
  result is formed by stacking corresponding elements from those structures.

#### Specifying `fn`'s output signature

If `fn`'s input and output signatures are different, then the output
signature must be specified using `fn_output_signature`.  (The input and
output signatures are differ if their structures, dtypes, or tensor types do
not match).  E.g.:

```
>>> tf.map_fn(fn=tf.strings.length,  # input & output have different dtypes
...           elems=tf.constant(["hello", "moon"]),
...           fn_output_signature=tf.int32)
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([5, 4], dtype=int32)>
>>> tf.map_fn(fn=tf.strings.join,  # input & output have different structures
...           elems=[tf.constant(['The', 'A']), tf.constant(['Dog', 'Cat'])],
...           fn_output_signature=tf.string)
<tf.Tensor: shape=(2,), dtype=string,
 numpy=array([b'TheDog', b'ACat'], dtype=object)>
```

`fn_output_signature` can be specified using any of the following:

* A <a href="../../../tf/dtypes/DType.md"><code>tf.DType</code></a> or <a href="../../../tf/TensorSpec.md"><code>tf.TensorSpec</code></a> (to describe a <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>)
* A <a href="../../../tf/RaggedTensorSpec.md"><code>tf.RaggedTensorSpec</code></a> (to describe a <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>)
* A <a href="../../../tf/SparseTensorSpec.md"><code>tf.SparseTensorSpec</code></a> (to describe a <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>)
* A (possibly nested) tuple, list, or dict containing the above types.

#### RaggedTensors

`map_fn` supports <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> inputs and outputs.  In particular:

* If `elems` is a `RaggedTensor`, then `fn` will be called with each
  row of that ragged tensor.
  * If `elems` has only one ragged dimension, then the values passed to
    `fn` will be <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>s.
  * If `elems` has multiple ragged dimensions, then the values passed to
    `fn` will be <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s with one fewer ragged dimension.

* If the result of `map_fn` should be a `RaggedTensor`, then use a
  <a href="../../../tf/RaggedTensorSpec.md"><code>tf.RaggedTensorSpec</code></a> to specify `fn_output_signature`.
  * If `fn` returns <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>s with varying sizes, then use a
    <a href="../../../tf/RaggedTensorSpec.md"><code>tf.RaggedTensorSpec</code></a> with `ragged_rank=0` to combine them into a
    single ragged tensor (which will have ragged_rank=1).
  * If `fn` returns <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>s, then use a <a href="../../../tf/RaggedTensorSpec.md"><code>tf.RaggedTensorSpec</code></a>
    with the same `ragged_rank`.

```
>>> # Example: RaggedTensor input
>>> rt = tf.ragged.constant([[1, 2, 3], [], [4, 5], [6]])
>>> tf.map_fn(tf.reduce_sum, rt, fn_output_signature=tf.int32)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([6, 0, 9, 6], dtype=int32)>
```

```
>>> # Example: RaggedTensor output
>>> elems = tf.constant([3, 5, 0, 2])
>>> tf.map_fn(tf.range, elems,
...           fn_output_signature=tf.RaggedTensorSpec(shape=[None],
...                                                   dtype=tf.int32))
<tf.RaggedTensor [[0, 1, 2], [0, 1, 2, 3, 4], [], [0, 1]]>
```

Note: `map_fn` should only be used if you need to map a function over the
*rows* of a `RaggedTensor`.  If you wish to map a function over the
individual values, then you should use:

* <a href="../../../tf/ragged/map_flat_values.md"><code>tf.ragged.map_flat_values(fn, rt)</code></a>
  (if fn is expressible as TensorFlow ops)
* `rt.with_flat_values(map_fn(fn, rt.flat_values))`
  (otherwise)

E.g.:

```
>>> rt = tf.ragged.constant([[1, 2, 3], [], [4, 5], [6]])
>>> tf.ragged.map_flat_values(lambda x: x + 2, rt)
<tf.RaggedTensor [[3, 4, 5], [], [6, 7], [8]]>
```

#### SparseTensors

`map_fn` supports <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> inputs and outputs.  In particular:

* If `elems` is a `SparseTensor`, then `fn` will be called with each row
  of that sparse tensor. In particular, the value passed to `fn` will be a
  <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> with one fewer dimension than `elems`.

* If the result of `map_fn` should be a `SparseTensor`, then use a
  <a href="../../../tf/SparseTensorSpec.md"><code>tf.SparseTensorSpec</code></a> to specify `fn_output_signature`.  The individual
  `SparseTensor`s returned by `fn` will be stacked into a single
  `SparseTensor` with one more dimension.

```
>>> # Example: SparseTensor input
>>> st = tf.sparse.SparseTensor([[0, 0], [2, 0], [2, 1]], [2, 3, 4], [4, 4])
>>> tf.map_fn(tf.sparse.reduce_sum, st, fn_output_signature=tf.int32)
<tf.Tensor: shape=(4,), dtype=int32, numpy=array([2, 0, 7, 0], dtype=int32)>
```

```
>>> # Example: SparseTensor output
>>> tf.sparse.to_dense(
...     tf.map_fn(tf.sparse.eye, tf.constant([2, 3]),
...               fn_output_signature=tf.SparseTensorSpec(None, tf.float32)))
<tf.Tensor: shape=(2, 3, 3), dtype=float32, numpy=
  array([[[1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 0.]],
         [[1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 1.]]], dtype=float32)>
```

Note: `map_fn` should only be used if you need to map a function over the
*rows* of a `SparseTensor`.  If you wish to map a function over the nonzero
values, then you should use:

* If the function is expressible as TensorFlow ops, use:
  ```python
  tf.sparse.SparseTensor(st.indices, fn(st.values), st.dense_shape)
  ```
* Otherwise, use:
  ```python
  tf.sparse.SparseTensor(st.indices, tf.map_fn(fn, st.values),
                         st.dense_shape)
  ```

#### `map_fn` vs. vectorized operations

`map_fn` will apply the operations used by `fn` to each element of `elems`,
resulting in `O(elems.shape[0])` total operations.  This is somewhat
mitigated by the fact that `map_fn` can process elements in parallel.
However, a transform expressed using `map_fn` is still typically less
efficient than an equivalent transform expressed using vectorized operations.

`map_fn` should typically only be used if one of the following is true:

* It is difficult or expensive to express the desired transform with
  vectorized operations.
* `fn` creates large intermediate values, so an equivalent vectorized
  transform would take too much memory.
* Processing elements in parallel is more efficient than an equivalent
  vectorized transform.
* Efficiency of the transform is not critical, and using `map_fn` is
  more readable.

E.g., the example given above that maps `fn=lambda t: tf.range(t, t + 3)`
across `elems` could be rewritten more efficiently using vectorized ops:

```
>>> elems = tf.constant([3, 5, 2])
>>> tf.range(3) + tf.expand_dims(elems, 1)
<tf.Tensor: shape=(3, 3), dtype=int32, numpy=
  array([[3, 4, 5],
         [5, 6, 7],
         [2, 3, 4]], dtype=int32)>
```

In some cases, <a href="../../../tf/vectorized_map.md"><code>tf.vectorized_map</code></a> can be used to automatically convert a
function to a vectorized eqivalent.

#### Eager execution

When executing eagerly, `map_fn` does not execute in parallel even if
`parallel_iterations` is set to a value > 1. You can still get the
performance benefits of running a function in parallel by using the
<a href="../../../tf/function.md"><code>tf.function</code></a> decorator:

```
>>> fn=lambda t: tf.range(t, t + 3)
>>> @tf.function
... def func(elems):
...   return tf.map_fn(fn, elems, parallel_iterations=3)
>>> func(tf.constant([3, 5, 2]))
<tf.Tensor: shape=(3, 3), dtype=int32, numpy=
  array([[3, 4, 5],
         [5, 6, 7],
         [2, 3, 4]], dtype=int32)>
```


Note: if you use the <a href="../../../tf/function.md"><code>tf.function</code></a> decorator, any non-TensorFlow Python
code that you may have written in your function won't get executed. See
<a href="../../../tf/function.md"><code>tf.function</code></a> for more  details. The recommendation would be to debug without
<a href="../../../tf/function.md"><code>tf.function</code></a> but switch to it to get performance benefits of running `map_fn`
in parallel.

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
same structure as `fn_output_signature` if one is provided; otherwise it
must have the same structure as `elems`.
</td>
</tr><tr>
<td>
`elems`
</td>
<td>
A tensor or (possibly nested) sequence of tensors, each of which will
be unstacked along their first dimension.  `fn` will be applied to the
nested sequence of the resulting slices.  `elems` may include ragged and
sparse tensors. `elems` must consist of at least one tensor.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
Deprecated: Equivalent to `fn_output_signature`.
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
(optional) False disables support for back propagation.
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
</tr><tr>
<td>
`fn_output_signature`
</td>
<td>
The output signature of `fn`. Must be specified if
`fn`'s input and output signatures are different (i.e., if their
structures, dtypes, or tensor types do not match).
`fn_output_signature` can be specified using any of the following:

* A <a href="../../../tf/dtypes/DType.md"><code>tf.DType</code></a> or <a href="../../../tf/TensorSpec.md"><code>tf.TensorSpec</code></a> (to describe a <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>)
* A <a href="../../../tf/RaggedTensorSpec.md"><code>tf.RaggedTensorSpec</code></a> (to describe a <a href="../../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a>)
* A <a href="../../../tf/SparseTensorSpec.md"><code>tf.SparseTensorSpec</code></a> (to describe a <a href="../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>)
* A (possibly nested) tuple, list, or dict containing the above types.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tensor or (possibly nested) sequence of tensors.  Each tensor stacks the
results of applying `fn` to tensors unstacked from `elems` along the first
dimension, from first to last.  The result may include ragged and sparse
tensors.
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
`fn` and `fn_output_signature` do not match.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
if the lengths of the output of `fn` and `fn_output_signature`
do not match, or if the `elems` does not contain any tensor.
</td>
</tr>
</table>



#### Examples:


```
>>> elems = np.array([1, 2, 3, 4, 5, 6])
>>> tf.map_fn(lambda x: x * x, elems)
<tf.Tensor: shape=(6,), dtype=int64, numpy=array([ 1,  4,  9, 16, 25, 36])>
```

```
>>> elems = (np.array([1, 2, 3]), np.array([-1, 1, -1]))
>>> tf.map_fn(lambda x: x[0] * x[1], elems, fn_output_signature=tf.int64)
<tf.Tensor: shape=(3,), dtype=int64, numpy=array([-1,  2, -3])>
```

```
>>> elems = np.array([1, 2, 3])
>>> tf.map_fn(lambda x: (x, -x), elems,
...          fn_output_signature=(tf.int64, tf.int64))
(<tf.Tensor: shape=(3,), dtype=int64, numpy=array([1, 2, 3])>,
 <tf.Tensor: shape=(3,), dtype=int64, numpy=array([-1, -2, -3])>)
```
