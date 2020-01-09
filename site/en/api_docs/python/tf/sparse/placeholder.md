page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.sparse.placeholder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2649-L2713">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Inserts a placeholder for a sparse tensor that will be always fed.

### Aliases:

* <a href="/api_docs/python/tf/sparse/placeholder"><code>tf.compat.v1.sparse.placeholder</code></a>
* <a href="/api_docs/python/tf/sparse/placeholder"><code>tf.compat.v1.sparse_placeholder</code></a>
* <a href="/api_docs/python/tf/sparse/placeholder"><code>tf.sparse_placeholder</code></a>


``` python
tf.sparse.placeholder(
    dtype,
    shape=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

**Important**: This sparse tensor will produce an error if evaluated.
Its value must be fed using the `feed_dict` optional argument to
<a href="../../tf/InteractiveSession#run"><code>Session.run()</code></a>, <a href="../../tf/Tensor#eval"><code>Tensor.eval()</code></a>, or <a href="../../tf/Operation#run"><code>Operation.run()</code></a>.

#### For example:



```python
x = tf.compat.v1.sparse.placeholder(tf.float32)
y = tf.sparse.reduce_sum(x)

with tf.compat.v1.Session() as sess:
  print(sess.run(y))  # ERROR: will fail because x was not fed.

  indices = np.array([[3, 2, 0], [4, 5, 1]], dtype=np.int64)
  values = np.array([1.0, 2.0], dtype=np.float32)
  shape = np.array([7, 9, 2], dtype=np.int64)
  print(sess.run(y, feed_dict={
    x: tf.compat.v1.SparseTensorValue(indices, values, shape)}))  # Will
    succeed.
  print(sess.run(y, feed_dict={
    x: (indices, values, shape)}))  # Will succeed.

  sp = tf.SparseTensor(indices=indices, values=values, dense_shape=shape)
  sp_value = sp.eval(session=sess)
  print(sess.run(y, feed_dict={x: sp_value}))  # Will succeed.
```

@compatibility{eager} Placeholders are not compatible with eager execution.

#### Args:


* <b>`dtype`</b>: The type of `values` elements in the tensor to be fed.
* <b>`shape`</b>: The shape of the tensor to be fed (optional). If the shape is not
  specified, you can feed a sparse tensor of any shape.
* <b>`name`</b>: A name for prefixing the operations (optional).


#### Returns:

A `SparseTensor` that may be used as a handle for feeding a value, but not
evaluated directly.



#### Raises:


* <b>`RuntimeError`</b>: if eager execution is enabled
