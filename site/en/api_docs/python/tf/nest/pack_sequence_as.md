page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nest.pack_sequence_as

Returns a given flattened sequence packed into a given structure.

### Aliases:

* `tf.compat.v1.nest.pack_sequence_as`
* `tf.compat.v2.nest.pack_sequence_as`
* `tf.contrib.framework.nest.pack_sequence_as`
* `tf.nest.pack_sequence_as`

``` python
tf.nest.pack_sequence_as(
    structure,
    flat_sequence,
    expand_composites=False
)
```



Defined in [`python/util/nest.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/nest.py).

<!-- Placeholder for "Used in" -->

If `structure` is a scalar, `flat_sequence` must be a single-element list;
in this case the return value is `flat_sequence[0]`.

If `structure` is or contains a dict instance, the keys will be sorted to
pack the flat sequence in deterministic order. This is true also for
`OrderedDict` instances: their sequence order is ignored, the sorting order of
keys is used instead. The same convention is followed in `flatten`.
This correctly repacks dicts and `OrderedDict`s after they have been
flattened, and also allows flattening an `OrderedDict` and then repacking it
back using a corresponding plain dict, or vice-versa.
Dictionaries with non-sortable keys cannot be flattened.

#### Args:


* <b>`structure`</b>: Nested structure, whose structure is given by nested lists,
    tuples, and dicts. Note: numpy arrays and strings are considered
    scalars.
* <b>`flat_sequence`</b>: flat sequence to pack.
* <b>`expand_composites`</b>: If true, then composite tensors such as <a href="../../tf/sparse/SparseTensor"><code>tf.SparseTensor</code></a>
    and <a href="../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a> are expanded into their component tensors.


#### Returns:


* <b>`packed`</b>: `flat_sequence` converted to have the same recursive structure as
  `structure`.


#### Raises:


* <b>`ValueError`</b>: If `flat_sequence` and `structure` have different
  element counts.
* <b>`TypeError`</b>: `structure` is or contains a dict with non-sortable keys.