description: foldr on the list of tensors unpacked from elems on dimension 0. (deprecated argument values)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.foldr" />
<meta itemprop="path" content="Stable" />
</div>

# tf.foldr

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/functional_ops.py#L362-L436">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



foldr on the list of tensors unpacked from `elems` on dimension 0. (deprecated argument values)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.foldr(
    fn, elems, initializer=None, parallel_iterations=10, back_prop=(True),
    swap_memory=(False), name=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENT VALUES ARE DEPRECATED: `(back_prop=False)`. They will be removed in a future version.
Instructions for updating:
back_prop=False is deprecated. Consider using tf.stop_gradient instead.
Instead of:
results = tf.foldr(fn, elems, back_prop=False)
Use:
results = tf.nest.map_structure(tf.stop_gradient, tf.foldr(fn, elems))

This foldr operator repeatedly applies the callable `fn` to a sequence
of elements from last to first. The elements are made of the tensors
unpacked from `elems`. The callable fn takes two tensors as arguments.
The first argument is the accumulated value computed from the preceding
invocation of fn, and the second is the value at the current position of
`elems`. If `initializer` is None, `elems` must contain at least one element,
and its first element is used as the initializer.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape
of the result tensor is `fn(initializer, values[0]).shape`.

This method also allows multi-arity `elems` and output of `fn`.  If `elems`
is a (possibly nested) list or tuple of tensors, then each of these tensors
must have a matching first (unpack) dimension.  The signature of `fn` may
match the structure of `elems`.  That is, if `elems` is
`(t1, [t2, t3, [t4, t5]])`, then an appropriate signature for `fn` is:
`fn = lambda (t1, [t2, t3, [t4, t5]]):`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`fn`
</td>
<td>
The callable to be performed.
</td>
</tr><tr>
<td>
`elems`
</td>
<td>
A tensor or (possibly nested) sequence of tensors, each of which will
be unpacked along their first dimension.  The nested sequence of the
resulting slices will be the first argument to `fn`.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
(optional) A tensor or (possibly nested) sequence of tensors,
as the initial value for the accumulator.
</td>
</tr><tr>
<td>
`parallel_iterations`
</td>
<td>
(optional) The number of iterations allowed to run in
parallel.
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
A tensor or (possibly nested) sequence of tensors, resulting from applying
`fn` consecutively to the list of tensors unpacked from `elems`, from last
to first.
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
if `fn` is not callable.
</td>
</tr>
</table>



#### Example:

```python
elems = [1, 2, 3, 4, 5, 6]
sum = foldr(lambda a, x: a + x, elems)
# sum == 21
```
