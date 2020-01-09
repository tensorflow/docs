page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.nest.map_structure_with_tuple_paths_up_to


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/util/nest.py#L1072-L1168">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Applies a function or op to a number of partially flattened inputs.

``` python
tf.contrib.framework.nest.map_structure_with_tuple_paths_up_to(
    shallow_tree,
    func,
    *inputs,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

Like map_structure_up_to(), except that the 'func' argument takes a path
tuple as its first argument, followed by the corresponding values from
*inputs.

#### Example:



lowercase = {'a': 'a', 'b': ('b0', 'b1')}
uppercase = {'a': 'A', 'b': ('B0', 'B1')}

def print_path_and_values(path, *values):
  print("path: {}, values: {}".format(path, values))

shallow_tree = {'a': None}
map_structure_with_tuple_paths_up_to(shallow_tree,
                                     print_path_and_values,
                                     lowercase,
                                     uppercase)
>>> path: ('a',), values: ('a', 'A')
>>> path: ('b', 0), values: ('b0', 'B0')
>>> path: ('b', 1), values: ('b1', 'B1')

shallow_tree = {'b': None}
map_structure_with_tuple_paths_up_to(shallow_tree,
                                     print_path_and_values,
                                     lowercase,
                                     uppercase,
                                     check_types=False)
>>> path: ('b', 1), values: (('bo', 'b1'), ('B0', 'B1'))

shallow_tree = {'a': None, 'b': {1: None}}
map_structure_with_tuple_paths_up_to(shallow_tree,
                                     print_path_and_values,
                                     lowercase,
                                     uppercase,
                                     check_types=False)
>>> path: ('a',), values: ('a', 'A')
>>> path: ('b', 1), values: ('b1', B1')

#### Args:


* <b>`shallow_tree`</b>: a shallow tree, common to all the inputs.
* <b>`func`</b>: callable that takes args (path, inputs_0_value, ... , inputs_N_value),
  where path is a tuple path to a leaf node in shallow_tree, and
  inputs_i_value is the corresponding value from inputs[i].
* <b>`*inputs`</b>: nested structures that are all structurally compatible with
    shallow_tree.
* <b>`**kwargs`</b>: kwargs to feed to func(). Special kwarg
  `check_types` is not passed to func, but instead determines whether the
  types of iterables within the structures have to be same (e.g.
  `map_structure(func, [1], (1,))` raises a `TypeError` exception). To allow
  this set this argument to `False`.


#### Raises:


* <b>`TypeError`</b>: If `shallow_tree` is a sequence but one of `*inputs` is not.
* <b>`TypeError`</b>: If the sequence types of `shallow_tree` are different from
  `input_tree`.
* <b>`ValueError`</b>: If the sequence lengths of `shallow_tree` are different from
  `input_tree`.


#### Returns:

Result of repeatedly applying `func`. Has the same structure layout as
`shallow_tree`.
