page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.framework.with_shape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/framework/python/framework/tensor_util.py#L232-L299">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Asserts tensor has expected shape.

``` python
tf.contrib.framework.with_shape(
    expected_shape,
    tensor
)
```



<!-- Placeholder for "Used in" -->

If tensor shape and expected_shape, are fully defined, assert they match.
Otherwise, add assert op that will validate the shape when tensor is
evaluated, and set shape on tensor.

#### Args:


* <b>`expected_shape`</b>: Expected shape to assert, as a 1D array of ints, or tensor
    of same.
* <b>`tensor`</b>: Tensor whose shape we're validating.

#### Returns:

tensor, perhaps with a dependent assert operation.


#### Raises:


* <b>`ValueError`</b>: if tensor has an invalid shape.
