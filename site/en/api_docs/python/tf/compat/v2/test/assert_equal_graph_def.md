page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.test.assert_equal_graph_def

Asserts that two `GraphDef`s are (mostly) the same.

``` python
tf.compat.v2.test.assert_equal_graph_def(
    expected,
    actual
)
```



Defined in [`python/framework/test_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/test_util.py).

<!-- Placeholder for "Used in" -->

Compares two `GraphDef` protos for equality, ignoring versions and ordering of
nodes, attrs, and control inputs.  Node names are used to match up nodes
between the graphs, so the naming of nodes must be consistent. This function
ignores randomized attribute values that may appear in V2 checkpoints.

#### Args:


* <b>`expected`</b>: The `GraphDef` we expected.
* <b>`actual`</b>: The `GraphDef` we have.


#### Raises:


* <b>`AssertionError`</b>: If the `GraphDef`s do not match.
* <b>`TypeError`</b>: If either argument is not a `GraphDef`.