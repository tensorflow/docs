page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.test.assert_equal_graph_def


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/test_util.py#L138-L156">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Asserts that two `GraphDef`s are (mostly) the same.

### Aliases:

* `tf.compat.v2.test.assert_equal_graph_def`


``` python
tf.test.assert_equal_graph_def(
    expected,
    actual
)
```



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
