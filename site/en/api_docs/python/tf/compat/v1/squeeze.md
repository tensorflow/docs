page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.squeeze


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L3597-L3649">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Removes dimensions of size 1 from the shape of a tensor. (deprecated arguments)

``` python
tf.compat.v1.squeeze(
    input,
    axis=None,
    name=None,
    squeeze_dims=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(squeeze_dims)`. They will be removed in a future version.
Instructions for updating:
Use the `axis` argument instead

Given a tensor `input`, this operation returns a tensor of the same type with
all dimensions of size 1 removed. If you don't want to remove all size 1
dimensions, you can remove specific size 1 dimensions by specifying
`axis`.

#### For example:



```python
# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
tf.shape(tf.squeeze(t))  # [2, 3]
```

Or, to remove specific size 1 dimensions:

```python
# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
tf.shape(tf.squeeze(t, [2, 4]))  # [1, 2, 3, 1]
```

Note: if `input` is a <a href="../../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a>, then this operation takes `O(N)`
time, where `N` is the number of elements in the squeezed dimensions.

#### Args:


* <b>`input`</b>: A `Tensor`. The `input` to squeeze.
* <b>`axis`</b>: An optional list of `ints`. Defaults to `[]`. If specified, only
  squeezes the dimensions listed. The dimension index starts at 0. It is an
  error to squeeze a dimension that is not 1. Must be in the range
  `[-rank(input), rank(input))`.
  Must be specified if `input` is a `RaggedTensor`.
* <b>`name`</b>: A name for the operation (optional).
* <b>`squeeze_dims`</b>: Deprecated keyword argument that is now axis.


#### Returns:

A `Tensor`. Has the same type as `input`.
Contains the same data as `input`, but has one or more dimensions of
size 1 removed.



#### Raises:


* <b>`ValueError`</b>: When both `squeeze_dims` and `axis` are specified.
