page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.unravel_index


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/unravel_index">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>

Defined in generated file: `python/ops/gen_array_ops.py`



Converts an array of flat indices into a tuple of coordinate arrays.

### Aliases:

* <a href="/api_docs/python/tf/unravel_index"><code>tf.compat.v1.unravel_index</code></a>
* <a href="/api_docs/python/tf/unravel_index"><code>tf.compat.v2.unravel_index</code></a>


``` python
tf.unravel_index(
    indices,
    dims,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Example:



```
y = tf.unravel_index(indices=[2, 5, 7], dims=[3, 3])
# 'dims' represent a hypothetical (3, 3) tensor of indices:
# [[0, 1, *2*],
#  [3, 4, *5*],
#  [6, *7*, 8]]
# For each entry from 'indices', this operation returns
# its coordinates (marked with '*'), such as
# 2 ==> (0, 2)
# 5 ==> (1, 2)
# 7 ==> (2, 1)
y ==> [[0, 1, 2], [2, 2, 1]]
```



#### Args:


* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  An 0-D or 1-D `int` Tensor whose elements are indices into the
  flattened version of an array of dimensions dims.
* <b>`dims`</b>: A `Tensor`. Must have the same type as `indices`.
  An 1-D `int` Tensor. The shape of the array to use for unraveling
  indices.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `indices`.


#### Numpy Compatibility
Equivalent to np.unravel_index
