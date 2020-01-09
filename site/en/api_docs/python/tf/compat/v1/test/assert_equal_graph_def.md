page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.test.assert_equal_graph_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/test_util.py#L159-L181">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Asserts that two `GraphDef`s are (mostly) the same.

``` python
tf.compat.v1.test.assert_equal_graph_def(
    actual,
    expected,
    checkpoint_v2=False,
    hash_table_shared_name=False
)
```



<!-- Placeholder for "Used in" -->

Compares two `GraphDef` protos for equality, ignoring versions and ordering of
nodes, attrs, and control inputs.  Node names are used to match up nodes
between the graphs, so the naming of nodes must be consistent.

#### Args:


* <b>`actual`</b>: The `GraphDef` we have.
* <b>`expected`</b>: The `GraphDef` we expected.
* <b>`checkpoint_v2`</b>: boolean determining whether to ignore randomized attribute
  values that appear in V2 checkpoints.
* <b>`hash_table_shared_name`</b>: boolean determining whether to ignore randomized
  shared_names that appear in HashTableV2 op defs.


#### Raises:


* <b>`AssertionError`</b>: If the `GraphDef`s do not match.
* <b>`TypeError`</b>: If either argument is not a `GraphDef`.
