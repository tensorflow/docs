page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lite.OpHint.OpHintArgumentTracker

## Class `OpHintArgumentTracker`

Conceptually tracks indices of arguments of "OpHint functions".



### Aliases:

* Class `tf.compat.v1.lite.OpHint.OpHintArgumentTracker`
* Class `tf.lite.OpHint.OpHintArgumentTracker`



Defined in [`lite/python/op_hint.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/python/op_hint.py).

<!-- Placeholder for "Used in" -->

The inputs and arguments of these functions both use an instance
of the class so they can have independent numbering.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    function_name,
    unique_function_id,
    node_name_prefix,
    attr_name,
    level=1,
    children_inputs_mappings=None
)
```

Initialize ophint argument.


#### Args:


* <b>`function_name`</b>: Name of the function that this tracks arguments for.
* <b>`unique_function_id`</b>: UUID of function that this tracks arguments for.
* <b>`node_name_prefix`</b>: How identities that are created are named.
* <b>`attr_name`</b>: Name of attribute to use to store the index for this hint.
  i.e. FUNCTION_INPUT_INDEX or FUNCTION_OUTPUT_INDEX
* <b>`level`</b>: Hierarchical level of the Ophint node, a number.
* <b>`children_inputs_mappings`</b>: Inputs/Outputs mapping for children hints.



## Methods

<h3 id="add"><code>add</code></h3>

``` python
add(
    arg,
    tag=None,
    name=None,
    aggregate=None,
    index_override=None
)
```

Return a wrapped tensor of an input tensor as an argument.


#### Args:


* <b>`arg`</b>: A TensorFlow tensor that should be considered an argument.
* <b>`tag`</b>: String tag to identify arguments that should be packed.
* <b>`name`</b>: Name of argument. This is included in the Identity hint op names.
* <b>`aggregate`</b>: Strategy to aggregate.
Acceptable values are OpHint.AGGREGATE_FIRST, OpHint.AGGREGATE_LAST,
  and OpHint.AGGREGATE_STACK.
  Note, aggregate is only valid if tag is specified.
* <b>`index_override`</b>: Specify what input/output index should this be in the
  final stub. i.e. add(arg0, index=1); add(arg1, index=0) will make the
  final stub be as stub_func(inputs[arg1, arg0], outputs=[]) rather than
  the default call order based ordering.


#### Returns:

A tensor representing the wrapped argument.



#### Raises:


* <b>`ValueError`</b>: When indices are not consistent.



