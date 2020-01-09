page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.dimension_at_index


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/framework/tensor_shape.py#L131-L177">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Compatibility utility required to allow for both V1 and V2 behavior in TF.

### Aliases:

* `tf.compat.v1.compat.dimension_at_index`
* `tf.compat.v1.dimension_at_index`
* `tf.compat.v2.compat.dimension_at_index`


``` python
tf.compat.dimension_at_index(
    shape,
    index
)
```



<!-- Placeholder for "Used in" -->

Until the release of TF 2.0, we need the legacy behavior of `TensorShape` to
coexist with the new behavior. This utility is a bridge between the two.

If you want to retrieve the Dimension instance corresponding to a certain
index in a TensorShape instance, use this utility, like this:

```
# If you had this in your V1 code:
dim = tensor_shape[i]

# Use `dimension_at_index` as direct replacement compatible with both V1 & V2:
dim = dimension_at_index(tensor_shape, i)

# Another possibility would be this, but WARNING: it only works if the
# tensor_shape instance has a defined rank.
dim = tensor_shape.dims[i]  # `dims` may be None if the rank is undefined!

# In native V2 code, we recommend instead being more explicit:
if tensor_shape.rank is None:
  dim = Dimension(None)
else:
  dim = tensor_shape.dims[i]

# Being more explicit will save you from the following trap (present in V1):
# you might do in-place modifications to `dim` and expect them to be reflected
# in `tensor_shape[i]`, but they would not be (as the Dimension object was
# instantiated on the fly.
```

#### Arguments:


* <b>`shape`</b>: A TensorShape instance.
* <b>`index`</b>: An integer index.


#### Returns:

A dimension object.
