page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.scatter_sub


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/state_ops.py#L486-L537">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Subtracts sparse updates to a variable reference.

### Aliases:

* <a href="/api_docs/python/tf/scatter_sub"><code>tf.compat.v1.scatter_sub</code></a>


``` python
tf.scatter_sub(
    ref,
    indices,
    updates,
    use_locking=False,
    name=None
)
```



<!-- Placeholder for "Used in" -->

```python
    # Scalar indices
    ref[indices, ...] -= updates[...]

    # Vector indices (for each i)
    ref[indices[i], ...] -= updates[i, ...]

    # High rank indices (for each i, ..., j)
    ref[indices[i, ..., j], ...] -= updates[i, ..., j, ...]
```

This operation outputs `ref` after the update is done.
This makes it easier to chain operations that need to use the reset value.

Duplicate entries are handled correctly: if multiple `indices` reference
the same location, their (negated) contributions add.

Requires `updates.shape = indices.shape + ref.shape[1:]` or
`updates.shape = []`.

<div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
<img style="width:100%"
     src="https://www.tensorflow.org/images/ScatterSub.png" alt>
</div>

#### Args:


* <b>`ref`</b>: A mutable `Tensor`. Must be one of the following types: `float32`,
  `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`,
  `qint8`, `quint8`, `qint32`, `bfloat16`, `uint16`, `complex128`, `half`,
  `uint32`, `uint64`. Should be from a `Variable` node.
* <b>`indices`</b>: A `Tensor`. Must be one of the following types: `int32`, `int64`.
  A tensor of indices into the first dimension of `ref`.
* <b>`updates`</b>: A `Tensor`. Must have the same type as `ref`.
  A tensor of updated values to subtract from `ref`.
* <b>`use_locking`</b>: An optional `bool`. Defaults to `False`.
  If True, the subtraction will be protected by a lock;
  otherwise the behavior is undefined, but may exhibit less contention.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A mutable `Tensor`. Has the same type as `ref`.
