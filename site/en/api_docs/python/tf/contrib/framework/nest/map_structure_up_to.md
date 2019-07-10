page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.map_structure_up_to

Applies a function or op to a number of partially flattened inputs.

``` python
tf.contrib.framework.nest.map_structure_up_to(
    shallow_tree,
    func,
    *inputs,
    **kwargs
)
```



Defined in [`python/util/nest.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/util/nest.py).

<!-- Placeholder for "Used in" -->

The `inputs` are flattened up to `shallow_tree` before being mapped.

#### Use Case:



Sometimes we wish to apply a function to a partially flattened
sequence (for example when the function itself takes sequence inputs). We
achieve this by specifying a shallow structure, `shallow_tree` we wish to
flatten up to.

The `inputs`, can be thought of as having the same structure layout as
`shallow_tree`, but with leaf nodes that are themselves tree structures.

This function therefore will return something with the same base structure as
`shallow_tree`.

#### Examples:



```python
shallow_tree = [None, None]
inp_val = [1, 2, 3]
out = map_structure_up_to(shallow_tree, lambda x: 2 * x, inp_val)

# Output is: [2, 4]
```

```python
ab_tuple = collections.namedtuple("ab_tuple", "a, b")
op_tuple = collections.namedtuple("op_tuple", "add, mul")
inp_val = ab_tuple(a=2, b=3)
inp_ops = ab_tuple(a=op_tuple(add=1, mul=2), b=op_tuple(add=2, mul=3))
out = map_structure_up_to(inp_val, lambda val, ops: (val + ops.add) * ops.mul,
                          inp_val, inp_ops)

# Output is: ab_tuple(a=6, b=15)
```

```python
data_list = [[2, 4, 6, 8], [[1, 3, 5, 7, 9], [3, 5, 7]]]
name_list = ['evens', ['odds', 'primes']]
out = map_structure_up_to(
    name_list,
    lambda name, sec: "first_{}_{}".format(len(sec), name),
    name_list, data_list)

# Output is: ['first_4_evens', ['first_5_odds', 'first_3_primes']]
```

#### Args:


* <b>`shallow_tree`</b>: a shallow tree, common to all the inputs.
* <b>`func`</b>: callable which will be applied to each input individually.
* <b>`*inputs`</b>: arbitrarily nested combination of objects that are compatible with
    shallow_tree. The function `func` is applied to corresponding
    partially flattened elements of each input, so the function must support
    arity of `len(inputs)`.
* <b>`**kwargs`</b>: kwargs to feed to func(). Special kwarg
  `check_types` is not passed to func, but instead determines whether the
  types of iterables within the structures have to be same (e.g.
  `map_structure(func, [1], (1,))` raises a `TypeError` exception). To allow
  this set this argument to `False`.


#### Raises:


* <b>`TypeError`</b>: If `shallow_tree` is a sequence but `input_tree` is not.
* <b>`TypeError`</b>: If the sequence types of `shallow_tree` are different from
  `input_tree`.
* <b>`ValueError`</b>: If the sequence lengths of `shallow_tree` are different from
  `input_tree`.


#### Returns:

result of repeatedly applying `func`, with the same structure layout as
`shallow_tree`.
