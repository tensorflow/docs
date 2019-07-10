page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.assert_equal_graph_def

Asserts that two `GraphDef`s are (mostly) the same.

### Aliases:

* `tf.compat.v1.test.assert_equal_graph_def`
* `tf.test.assert_equal_graph_def`

``` python
tf.test.assert_equal_graph_def(
    actual,
    expected,
    checkpoint_v2=False
)
```



Defined in [`python/framework/test_util.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/test_util.py).

<!-- Placeholder for "Used in" -->

Compares two `GraphDef` protos for equality, ignoring versions and ordering of
nodes, attrs, and control inputs.  Node names are used to match up nodes
between the graphs, so the naming of nodes must be consistent.

#### Args:


* <b>`actual`</b>: The `GraphDef` we have.
* <b>`expected`</b>: The `GraphDef` we expected.
* <b>`checkpoint_v2`</b>: boolean determining whether to ignore randomized attribute
  values that appear in V2 checkpoints.


#### Raises:


* <b>`AssertionError`</b>: If the `GraphDef`s do not match.
* <b>`TypeError`</b>: If either argument is not a `GraphDef`.