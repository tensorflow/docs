page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.count_nonzero


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/math_ops.py#L1619-L1692">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes number of nonzero elements across dimensions of a tensor. (deprecated arguments) (deprecated arguments)

### Aliases:

* `tf.compat.v1.math.count_nonzero`


``` python
tf.compat.v1.count_nonzero(
    input_tensor=None,
    axis=None,
    keepdims=None,
    dtype=tf.dtypes.int64,
    name=None,
    reduction_indices=None,
    keep_dims=None,
    input=None
)
```



<!-- Placeholder for "Used in" -->

Warning: SOME ARGUMENTS ARE DEPRECATED: `(keep_dims)`. They will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead

Warning: SOME ARGUMENTS ARE DEPRECATED: `(axis)`. They will be removed in a future version.
Instructions for updating:
reduction_indices is deprecated, use axis instead

Reduces `input_tensor` along the dimensions given in `axis`.
Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
entry in `axis`. If `keepdims` is true, the reduced dimensions
are retained with length 1.

If `axis` has no entries, all dimensions are reduced, and a
tensor with a single element is returned.

**NOTE** Floating point comparison to zero is done by exact floating point
equality check.  Small values are **not** rounded to zero for purposes of
the nonzero check.

#### For example:



```python
x = tf.constant([[0, 1, 0], [1, 1, 0]])
tf.math.count_nonzero(x)  # 3
tf.math.count_nonzero(x, 0)  # [1, 2, 0]
tf.math.count_nonzero(x, 1)  # [1, 2]
tf.math.count_nonzero(x, 1, keepdims=True)  # [[1], [2]]
tf.math.count_nonzero(x, [0, 1])  # 3
```

**NOTE** Strings are compared against zero-length empty string `""`. Any
string with a size greater than zero is already considered as nonzero.

#### For example:


```python
x = tf.constant(["", "a", "  ", "b", ""])
tf.math.count_nonzero(x) # 3, with "a", "  ", and "b" as nonzero strings.
```

#### Args:


* <b>`input_tensor`</b>: The tensor to reduce. Should be of numeric type, `bool`, or
  `string`.
* <b>`axis`</b>: The dimensions to reduce. If `None` (the default), reduces all
  dimensions. Must be in the range `[-rank(input_tensor),
  rank(input_tensor))`.
* <b>`keepdims`</b>: If true, retains reduced dimensions with length 1.
* <b>`dtype`</b>: The output dtype; defaults to <a href="../../../tf#int64"><code>tf.int64</code></a>.
* <b>`name`</b>: A name for the operation (optional).
* <b>`reduction_indices`</b>: The old (deprecated) name for axis.
* <b>`keep_dims`</b>: Deprecated alias for `keepdims`.
* <b>`input`</b>: Overrides input_tensor. For compatibility.


#### Returns:

The reduced tensor (number of nonzero values).
