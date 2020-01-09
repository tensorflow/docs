page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.unique


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/array_ops.py#L1618-L1624">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Finds unique elements in a 1-D tensor.

### Aliases:

* `tf.compat.v1.unique`
* `tf.compat.v2.unique`


``` python
tf.unique(
    x,
    out_idx=tf.dtypes.int32,
    name=None
)
```



<!-- Placeholder for "Used in" -->

This operation returns a tensor `y` containing all of the unique elements of `x`
sorted in the same order that they occur in `x`. This operation also returns a
tensor `idx` the same size as `x` that contains the index of each value of `x`
in the unique output `y`. In other words:

`y[idx[i]] = x[i] for i in [0, 1,...,rank(x) - 1]`

#### For example:



```
# tensor 'x' is [1, 1, 2, 4, 4, 4, 7, 8, 8]
y, idx = unique(x)
y ==> [1, 2, 4, 7, 8]
idx ==> [0, 0, 1, 2, 2, 2, 3, 4, 4]
```

#### Args:


* <b>`x`</b>: A `Tensor`. 1-D.
* <b>`out_idx`</b>: An optional <a href="../tf/dtypes/DType"><code>tf.DType</code></a> from: `tf.int32, tf.int64`. Defaults to <a href="../tf#int32"><code>tf.int32</code></a>.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `Tensor` objects (y, idx).


* <b>`y`</b>: A `Tensor`. Has the same type as `x`.
* <b>`idx`</b>: A `Tensor` of type `out_idx`.
