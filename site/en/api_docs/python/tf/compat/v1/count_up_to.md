page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.count_up_to


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/state_ops.py#L231-L252">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Increments 'ref' until it reaches 'limit'. (deprecated)

``` python
tf.compat.v1.count_up_to(
    ref,
    limit,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Prefer Dataset.range instead.

#### Args:


* <b>`ref`</b>: A Variable. Must be one of the following types: `int32`, `int64`.
  Should be from a scalar `Variable` node.
* <b>`limit`</b>: An `int`.
  If incrementing ref would bring it above limit, instead generates an
  'OutOfRange' error.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `ref`.
A copy of the input before increment. If nothing else modifies the
input, the values produced will all be distinct.
