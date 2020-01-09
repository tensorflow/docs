page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.enable_v2_tensorshape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/tensor_shape.py#L35-L84">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



In TensorFlow 2.0, iterating over a TensorShape instance returns values.

``` python
tf.compat.v1.enable_v2_tensorshape()
```



<!-- Placeholder for "Used in" -->

This enables the new behavior.

Concretely, `tensor_shape[i]` returned a Dimension instance in V1, but
it V2 it returns either an integer, or None.

#### Examples:



```
#######################
# If you had this in V1:
value = tensor_shape[i].value

# Do this in V2 instead:
value = tensor_shape[i]

#######################
# If you had this in V1:
for dim in tensor_shape:
  value = dim.value
  print(value)

# Do this in V2 instead:
for value in tensor_shape:
  print(value)

#######################
# If you had this in V1:
dim = tensor_shape[i]
dim.assert_is_compatible_with(other_shape)  # or using any other shape method

# Do this in V2 instead:
if tensor_shape.rank is None:
  dim = Dimension(None)
else:
  dim = tensor_shape.dims[i]
dim.assert_is_compatible_with(other_shape)  # or using any other shape method

# The V2 suggestion above is more explicit, which will save you from
# the following trap (present in V1):
# you might do in-place modifications to `dim` and expect them to be reflected
# in `tensor_shape[i]`, but they would not be.
```
