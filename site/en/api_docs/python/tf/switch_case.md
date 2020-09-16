description: Create a switch/case operation, i.e. an integer-indexed conditional.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.switch_case" />
<meta itemprop="path" content="Stable" />
</div>

# tf.switch_case

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/ops/control_flow_ops.py#L3506-L3579">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Create a switch/case operation, i.e. an integer-indexed conditional.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.switch_case`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.switch_case(
    branch_index, branch_fns, default=None, name='switch_case'
)
</code></pre>



<!-- Placeholder for "Used in" -->

See also <a href="../tf/case.md"><code>tf.case</code></a>.

This op can be substantially more efficient than <a href="../tf/case.md"><code>tf.case</code></a> when exactly one
branch will be selected. <a href="../tf/switch_case.md"><code>tf.switch_case</code></a> is more like a C++ switch/case
statement than <a href="../tf/case.md"><code>tf.case</code></a>, which is more like an if/elif/elif/else chain.

The `branch_fns` parameter is either a dict from `int` to callables, or list
of (`int`, callable) pairs, or simply a list of callables (in which case the
index is implicitly the key). The `branch_index` `Tensor` is used to select an
element in `branch_fns` with matching `int` key, falling back to `default`
if none match, or `max(keys)` if no `default` is provided. The keys must form
a contiguous set from `0` to `len(branch_fns) - 1`.

<a href="../tf/switch_case.md"><code>tf.switch_case</code></a> supports nested structures as implemented in <a href="../tf/nest.md"><code>tf.nest</code></a>. All
callables must return the same (possibly nested) value structure of lists,
tuples, and/or named tuples.

**Example:**

#### Pseudocode:



```c++
switch (branch_index) {  // c-style switch
  case 0: return 17;
  case 1: return 31;
  default: return -1;
}
```
or
```python
branches = {0: lambda: 17, 1: lambda: 31}
branches.get(branch_index, lambda: -1)()
```

#### Expressions:



```python
def f1(): return tf.constant(17)
def f2(): return tf.constant(31)
def f3(): return tf.constant(-1)
r = tf.switch_case(branch_index, branch_fns={0: f1, 1: f2}, default=f3)
# Equivalent: tf.switch_case(branch_index, branch_fns={0: f1, 1: f2, 2: f3})
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`branch_index`
</td>
<td>
An int Tensor specifying which of `branch_fns` should be
executed.
</td>
</tr><tr>
<td>
`branch_fns`
</td>
<td>
A `dict` mapping `int`s to callables, or a `list` of
(`int`, callable) pairs, or simply a list of callables (in which case the
index serves as the key). Each callable must return a matching structure
of tensors.
</td>
</tr><tr>
<td>
`default`
</td>
<td>
Optional callable that returns a structure of tensors.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
A name for this operation (optional).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
The tensors returned by the callable identified by `branch_index`, or those
returned by `default` if no key matches and `default` was provided, or those
returned by the max-keyed `branch_fn` if no `default` is provided.
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
If `branch_fns` is not a list/dictionary.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If `branch_fns` is a list but does not contain 2-tuples or
callables.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If `fns[i]` is not callable for any i, or `default` is not
callable.
</td>
</tr>
</table>

