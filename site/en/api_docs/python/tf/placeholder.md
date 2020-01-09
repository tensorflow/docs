page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.placeholder


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/array_ops.py#L2577-L2619">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Inserts a placeholder for a tensor that will be always fed.

### Aliases:

* <a href="/api_docs/python/tf/placeholder"><code>tf.compat.v1.placeholder</code></a>


``` python
tf.placeholder(
    dtype,
    shape=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

**Important**: This tensor will produce an error if evaluated. Its value must
be fed using the `feed_dict` optional argument to <a href="../tf/InteractiveSession#run"><code>Session.run()</code></a>,
<a href="../tf/Tensor#eval"><code>Tensor.eval()</code></a>, or <a href="../tf/Operation#run"><code>Operation.run()</code></a>.

#### For example:



```python
x = tf.compat.v1.placeholder(tf.float32, shape=(1024, 1024))
y = tf.matmul(x, x)

with tf.compat.v1.Session() as sess:
  print(sess.run(y))  # ERROR: will fail because x was not fed.

  rand_array = np.random.rand(1024, 1024)
  print(sess.run(y, feed_dict={x: rand_array}))  # Will succeed.
```



#### Args:


* <b>`dtype`</b>: The type of elements in the tensor to be fed.
* <b>`shape`</b>: The shape of the tensor to be fed (optional). If the shape is not
  specified, you can feed a tensor of any shape.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` that may be used as a handle for feeding a value, but not
evaluated directly.



#### Raises:


* <b>`RuntimeError`</b>: if eager execution is enabled

#### Eager Compatibility
Placeholders are not compatible with eager execution.
