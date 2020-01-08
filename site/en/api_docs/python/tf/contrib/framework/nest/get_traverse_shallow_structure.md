page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.get_traverse_shallow_structure

``` python
tf.contrib.framework.nest.get_traverse_shallow_structure(
    traverse_fn,
    structure
)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.11/tensorflow/python/util/nest.py).

Generates a shallow structure from a `traverse_fn` and `structure`.

`traverse_fn` must accept any possible subtree of `structure` and return
a depth=1 structure containing `True` or `False` values, describing which
of the top-level subtrees may be traversed.  It may also
return scalar `True` or `False` "traversal is OK / not OK for all subtrees."

Examples are available in the unit tests (nest_test.py).

#### Args:

* <b>`traverse_fn`</b>: Function taking a substructure and returning either a scalar
    `bool` (whether to traverse that substructure or not) or a depth=1
    shallow structure of the same type, describing which parts of the
    substructure to traverse.
* <b>`structure`</b>: The structure to traverse.


#### Returns:

A shallow structure containing python bools, which can be passed to
`map_structure_up_to` and `flatten_up_to`.


#### Raises:

* <b>`TypeError`</b>: if `traverse_fn` returns a sequence for a non-sequence input,
    or a structure with depth higher than 1 for a sequence input,
    or if any leaf values in the returned structure or scalar are not type
    `bool`.