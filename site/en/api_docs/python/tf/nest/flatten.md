description: Returns a flat list from a given nested structure.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.nest.flatten" />
<meta itemprop="path" content="Stable" />
</div>

# tf.nest.flatten

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/util/nest.py#L274-L338">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns a flat list from a given nested structure.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.nest.flatten`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.nest.flatten(
    structure, expand_composites=(False)
)
</code></pre>



<!-- Placeholder for "Used in" -->

If nest is not a structure , tuple (or a namedtuple), dict, or an attrs class,
then returns a single-element list:
  [nest].

In the case of dict instances, the sequence consists of the values, sorted by
key to ensure deterministic behavior. This is true also for OrderedDict
instances: their sequence order is ignored, the sorting order of keys is used
instead. The same convention is followed in pack_sequence_as. This correctly
repacks dicts and OrderedDicts after they have been flattened, and also allows
flattening an OrderedDict and then repacking it back using a corresponding
plain dict, or vice-versa. Dictionaries with non-sortable keys cannot be
flattened.

Users must not modify any collections used in nest while this function is
running.

#### Examples:



1. Python dict (ordered by key):

```
>>> dict = { "key3": "value3", "key1": "value1", "key2": "value2" }
>>> tf.nest.flatten(dict)
['value1', 'value2', 'value3']
```

2. For a nested python tuple:

```
>>> tuple = ((1.0, 2.0), (3.0, 4.0, 5.0), (6.0))
>>> tf.nest.flatten(tuple)
    [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
```

3. Numpy array (will not flatten):

```
>>> array = np.array([[1, 2], [3, 4]])
>>> tf.nest.flatten(array)
    [array([[1, 2],
            [3, 4]])]
```


4. <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> (will not flatten):

```
>>> tensor = tf.constant([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
>>> tf.nest.flatten(tensor)
    [<tf.Tensor: shape=(3, 3), dtype=float32, numpy=
      array([[1., 2., 3.],
             [4., 5., 6.],
             [7., 8., 9.]], dtype=float32)>]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`structure`
</td>
<td>
an arbitrarily nested structure. Note, numpy arrays are
considered atoms and are not flattened.
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
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A Python list, the flattened version of the input.
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
The nest is or contains a dict with non-sortable keys.
</td>
</tr>
</table>

