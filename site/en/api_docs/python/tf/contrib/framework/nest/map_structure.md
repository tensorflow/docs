

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.map_structure

``` python
tf.contrib.framework.nest.map_structure(
    func,
    *structure,
    **check_types_dict
)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/util/nest.py).

Applies `func` to each entry in `structure` and returns a new structure.

Applies `func(x[0], x[1], ...)` where x[i] is an entry in
`structure[i]`.  All structures in `structure` must have the same arity,
and the return value will contain the results in the same structure.

#### Args:

* <b>`func`</b>: A callable that accepts as many arguments as there are structures.
* <b>`*structure`</b>: scalar, or tuple or list of constructed scalars and/or other
    tuples/lists, or scalars.  Note: numpy arrays are considered as scalars.
* <b>`**check_types_dict`</b>: only valid keyword argument is `check_types`. If set to
    `True` (default) the types of iterables within the structures have to be
    same (e.g. `map_structure(func, [1], (1,))` raises a `TypeError`
    exception). To allow this set this argument to `False`.
    Note that namedtuples with identical name and fields are always
    considered to have the same shallow structure.


#### Returns:

A new structure with the same arity as `structure`, whose values correspond
to `func(x[0], x[1], ...)` where `x[i]` is a value in the corresponding
location in `structure[i]`. If there are different sequence types and
`check_types` is `False` the sequence types of the first structure will be
used.


#### Raises:

* <b>`TypeError`</b>: If `func` is not callable or if the structures do not match
    each other by depth tree.
* <b>`ValueError`</b>: If no structure is provided or if the structures do not match
    each other by type.
* <b>`ValueError`</b>: If wrong keyword arguments are provided.