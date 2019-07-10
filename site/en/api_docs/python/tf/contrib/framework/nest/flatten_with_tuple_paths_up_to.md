page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.flatten_with_tuple_paths_up_to

Flattens `input_tree` up to `shallow_tree`.

``` python
tf.contrib.framework.nest.flatten_with_tuple_paths_up_to(
    shallow_tree,
    input_tree,
    check_types=True,
    expand_composites=False,
    check_subtrees_length=True
)
```



Defined in [`python/util/nest.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/nest.py).

<!-- Placeholder for "Used in" -->

Any further depth in structure in `input_tree` is retained as elements in the
partially flattened output.

Returns a list of (path, value) pairs, where value a leaf node in the
flattened tree, and path is the tuple path of that leaf in input_tree.

If `shallow_tree` and `input_tree` are not sequences, this returns a
single-element list: `[((), input_tree)]`.

#### Use Case:



Sometimes we may wish to partially flatten a nested sequence, retaining some
of the nested structure. We achieve this by specifying a shallow structure,
`shallow_tree`, we wish to flatten up to.

The input, `input_tree`, can be thought of as having the same structure layout
as `shallow_tree`, but with leaf nodes that are themselves tree structures.

#### Examples:



```python
input_tree = [[[2, 2], [3, 3]], [[4, 9], [5, 5]]]
shallow_tree = [[True, True], [False, True]]

flattened_input_tree = flatten_with_tuple_paths_up_to(shallow_tree,
                                                      input_tree)
flattened_shallow_tree = flatten_with_tuple_paths_up_to(shallow_tree,
                                                        shallow_tree)

# Output is:
# [((0, 0), [2, 2]),
#  ((0, 1), [3, 3]),
#  ((1, 0), [4, 9]),
#  ((1, 1), [5, 5])]
#
# [((0, 0), True),
#  ((0, 1), True),
#  ((1, 0), False),
#  ((1, 1), True)]
```

```python
input_tree = [[('a', 1), [('b', 2), [('c', 3), [('d', 4)]]]]]
shallow_tree = [['level_1', ['level_2', ['level_3', ['level_4']]]]]

input_tree_flattened_as_shallow_tree = flatten_up_to(shallow_tree, input_tree)
input_tree_flattened = flatten(input_tree)

# Output is:
# [((0, 0), ('a', 1)),
#  ((0, 1, 0), ('b', 2)),
#  ((0, 1, 1, 0), ('c', 3)),
#  ((0, 1, 1, 1), ('d', 4))]
# ['a', 1, 'b', 2, 'c', 3, 'd', 4]
```

Non-Sequence Edge Cases:

```python
flatten_with_tuple_paths_up_to(0, 0)  # Output: [(), 0]

flatten_with_tuple_paths_up_to(0, [0, 1, 2])  # Output: [(), [0, 1, 2]]

flatten_with_tuple_paths_up_to([0, 1, 2], 0)  # Output: TypeError

flatten_with_tuple_paths_up_to([0, 1, 2], [0, 1, 2])
# Output: [((0,) 0), ((1,), 1), ((2,), 2)]
```

#### Args:


* <b>`shallow_tree`</b>: a possibly pruned structure of input_tree.
* <b>`input_tree`</b>: an arbitrarily nested structure or a scalar object.
  Note, numpy arrays are considered scalars.
* <b>`check_types`</b>: bool. If True, check that each node in shallow_tree has the
  same type as the corresponding node in input_tree.
* <b>`expand_composites`</b>: If true, then composite tensors such as tf.SparseTensor
   and tf.RaggedTensor are expanded into their component tensors.
* <b>`check_subtrees_length`</b>: if `True` (default) the subtrees `shallow_tree` and
  `input_tree` have to be the same length. If `False` sequences are treated
  as key-value like mappings allowing them to be considered as valid
  subtrees. Note that this may drop parts of the `input_tree`.


#### Returns:

A Python list, the partially flattened version of `input_tree` according to
the structure of `shallow_tree`.



#### Raises:


* <b>`TypeError`</b>: If `shallow_tree` is a sequence but `input_tree` is not.
* <b>`TypeError`</b>: If the sequence types of `shallow_tree` are different from
  `input_tree`.
* <b>`ValueError`</b>: If the sequence lengths of `shallow_tree` are different from
  `input_tree`.