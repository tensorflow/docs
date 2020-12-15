description: Asserts that two structures are nested in the same way.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nest.assert_same_structure" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nest.assert_same_structure

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/util/nest.py#L357-L402">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Asserts that two structures are nested in the same way.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nest.assert_same_structure`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nest.assert_same_structure(
    nest1, nest2, check_types=(True), expand_composites=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Note that namedtuples with identical name and fields are always considered
to have the same shallow structure (even with `check_types=True`).
For instance, this code will print `True`:

```python
def nt(a, b):
  return collections.namedtuple('foo', 'a b')(a, b)
print(assert_same_structure(nt(0, 1), nt(2, 3)))
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`nest1`
</td>
<td>
an arbitrarily nested structure.
</td>
</tr><tr>
<td>
`nest2`
</td>
<td>
an arbitrarily nested structure.
</td>
</tr><tr>
<td>
`check_types`
</td>
<td>
if `True` (default) types of sequences are checked as well,
including the keys of dictionaries. If set to `False`, for example a
list and a tuple of objects will look the same if they have the same
size. Note that namedtuples with identical name and fields are always
considered to have the same shallow structure. Two types will also be
considered the same if they are both list subtypes (which allows "list"
and "_ListWrapper" from trackable dependency tracking to compare
equal).
</td>
</tr><tr>
<td>
`expand_composites`
</td>
<td>
If true, then composite tensors such as
<a href="../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a> and <a href="../../tf/RaggedTensor.md"><code>tf.RaggedTensor</code></a> are expanded into their
component tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If the two structures do not have the same number of elements or
if the two structures are not nested in the same way.
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If the two structures differ in the type of sequence in any of
their substructures. Only possible if `check_types` is `True`.
</td>
</tr>
</table>

