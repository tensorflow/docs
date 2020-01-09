page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.parallel_stack


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/parallel_stack">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L1048-L1096">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Stacks a list of rank-`R` tensors into one rank-`(R+1)` tensor in parallel.

### Aliases:

* <a href="/api_docs/python/tf/parallel_stack"><code>tf.compat.v1.parallel_stack</code></a>
* <a href="/api_docs/python/tf/parallel_stack"><code>tf.compat.v2.parallel_stack</code></a>


``` python
tf.parallel_stack(
    values,
    name='parallel_stack'
)
```



<!-- Placeholder for "Used in" -->

Requires that the shape of inputs be known at graph construction time.

Packs the list of tensors in `values` into a tensor with rank one higher than
each tensor in `values`, by packing them along the first dimension.
Given a list of length `N` of tensors of shape `(A, B, C)`; the `output`
tensor will have the shape `(N, A, B, C)`.

#### For example:



```python
x = tf.constant([1, 4])
y = tf.constant([2, 5])
z = tf.constant([3, 6])
tf.parallel_stack([x, y, z])  # [[1, 4], [2, 5], [3, 6]]
```

The difference between `stack` and `parallel_stack` is that `stack` requires
all the inputs be computed before the operation will begin but doesn't require
that the input shapes be known during graph construction.

`parallel_stack` will copy pieces of the input into the output as they become
available, in some situations this can provide a performance benefit.

Unlike `stack`, `parallel_stack` does NOT support backpropagation.

This is the opposite of unstack.  The numpy equivalent is

    tf.parallel_stack([x, y, z]) = np.asarray([x, y, z])

#### Args:


* <b>`values`</b>: A list of `Tensor` objects with the same shape and type.
* <b>`name`</b>: A name for this operation (optional).


#### Returns:


* <b>`output`</b>: A stacked `Tensor` with the same type as `values`.
