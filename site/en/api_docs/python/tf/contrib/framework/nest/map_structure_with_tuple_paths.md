page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.map_structure_with_tuple_paths


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/nest.py#L582-L618">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Applies `func` to each entry in `structure` and returns a new structure.

``` python
tf.contrib.framework.nest.map_structure_with_tuple_paths(
    func,
    *structure,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

Applies `func(tuple_path, x[0], x[1], ..., **kwargs)` where `x[i]` is an entry
in `structure[i]` and `tuple_path` is a tuple of indices and/or dictionary
keys (as returned by `nest.yield_flat_paths`), which uniquely specifies the
common path to x[i] in the structures. All structures in `structure` must have
the same arity, and the return value will contain the results in the same
structure. Special kwarg `check_types` determines whether the types of
iterables within the structure must be the same-- see **kwargs definition
below.

#### Args:


* <b>`func`</b>: A callable with the signature `func(tuple_path, *values, **kwargs)`
  that is evaluated on the leaves of the structure.
* <b>`*structure`</b>: A variable number of compatible structures to process.
* <b>`**kwargs`</b>: Optional kwargs to be passed through to func. Special kwarg
  `check_types` is not passed to func, but instead determines whether the
  types of iterables within the structures have to be same (e.g.
  `map_structure(func, [1], (1,))` raises a `TypeError` exception). To allow
  this set this argument to `False`.


#### Returns:

A structure of the same form as the input structures whose leaves are the
result of evaluating func on corresponding leaves of the input structures.



#### Raises:


* <b>`TypeError`</b>: If `func` is not callable or if the structures do not match
  each other by depth tree.
* <b>`TypeError`</b>: If `check_types` is not `False` and the two structures differ in
  the type of sequence in any of their substructures.
* <b>`ValueError`</b>: If no structures are provided.
