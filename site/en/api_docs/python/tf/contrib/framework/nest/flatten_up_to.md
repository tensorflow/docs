

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.flatten_up_to

``` python
tf.contrib.framework.nest.flatten_up_to(
    shallow_tree,
    input_tree
)
```



Defined in [`tensorflow/python/util/nest.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/util/nest.py).

Flattens `input_tree` up to `shallow_tree`.

Any further depth in structure in `input_tree` is retained as elements in the
partially flatten output.

If `shallow_tree` and `input_tree` are not sequences, this returns a
single-element list: `[input_tree]`.

Use Case:

Sometimes we may wish to partially flatten a nested sequence, retaining some
of the nested structure. We achieve this by specifying a shallow structure,
`shallow_tree`, we wish to flatten up to.

The input, `input_tree`, can be thought of as having the same structure as
`shallow_tree`, but with leaf nodes that are themselves tree structures.

Examples:

```python
input_tree = [[[2, 2], [3, 3]], [[4, 9], [5, 5]]]
shallow_tree = [[True, True], [False, True]]

flattened_input_tree = flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = flatten_up_to(shallow_tree, shallow_tree)

# Output is:
# [[2, 2], [3, 3], [4, 9], [5, 5]]
# [True, True, False, True]
```

```python
input_tree = [[('a', 1), [('b', 2), [('c', 3), [('d', 4)]]]]]
shallow_tree = [['level_1', ['level_2', ['level_3', ['level_4']]]]]

input_tree_flattened_as_shallow_tree = flatten_up_to(shallow_tree, input_tree)
input_tree_flattened = flatten(input_tree)

# Output is:
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
# ['a', 1, 'b', 2, 'c', 3, 'd', 4]
```

Non-Sequence Edge Cases:

```python
flatten_up_to(0, 0)  # Output: [0]
flatten_up_to(0, [0, 1, 2])  # Output: [[0, 1, 2]]
flatten_up_to([0, 1, 2], 0)  # Output: TypeError
flatten_up_to([0, 1, 2], [0, 1, 2])  # Output: [0, 1, 2]
```

#### Args:

* <b>`shallow_tree`</b>: a possibly pruned structure of input_tree.
* <b>`input_tree`</b>: an arbitrarily nested structure or a scalar object.
    Note, numpy arrays are considered scalars.


#### Returns:

A Python list, the partially flattened version of `input_tree` according to
the structure of `shallow_tree`.


#### Raises:

* <b>`TypeError`</b>: If `shallow_tree` is a sequence but `input_tree` is not.
* <b>`TypeError`</b>: If the sequence types of `shallow_tree` are different from
    `input_tree`.
* <b>`ValueError`</b>: If the sequence lengths of `shallow_tree` are different from
    `input_tree`.