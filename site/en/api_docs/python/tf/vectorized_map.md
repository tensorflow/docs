page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.vectorized_map


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/parallel_for/control_flow_ops.py#L308-L390">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Parallel map on the list of tensors unpacked from `elems` on dimension 0.

### Aliases:

* `tf.compat.v1.vectorized_map`
* `tf.compat.v2.vectorized_map`


``` python
tf.vectorized_map(
    fn,
    elems
)
```



<!-- Placeholder for "Used in" -->


This method works similar to tf.map_fn but is optimized to run much faster,
possibly with a much larger memory footprint. The speedups are obtained by
vectorization (see https://arxiv.org/pdf/1903.04243.pdf). The idea behind
vectorization is to semantically launch all the invocations of `fn` in
parallel and fuse corresponding operations across all these invocations. This
fusion is done statically at graph generation time and the generated code is
often similar in performance to a manually fused version.

Because <a href="../tf/vectorized_map"><code>tf.vectorized_map</code></a> fully parallelizes the batch, this method will
generally be significantly faster than using <a href="../tf/map_fn"><code>tf.map_fn</code></a>, especially in eager
mode. However this is an experimental feature and currently has a lot of
limitations:
  - There should be no data dependency between the different semantic
    invocations of `fn`, i.e. it should be safe to map the elements of the
    inputs in any order.
  - Stateful kernels may mostly not be supported since these often imply a
    data dependency. We do support a limited set of such stateful kernels
    though (like RandomFoo, Variable operations like reads, etc).
  - `fn` has limited support for control flow operations. <a href="../tf/cond"><code>tf.cond</code></a> in
    particular is not supported.
  - `fn` should return nested structure of Tensors or Operations. However
    if an Operation is returned, it should have zero outputs.
  - The shape and dtype of any intermediate or output tensors in the
    computation of `fn` should not depend on the input to `fn`.

#### Args:


* <b>`fn`</b>: The callable to be performed. It accepts one argument, which will have
  the same (possibly nested) structure as `elems`, and returns a possibly
  nested structure of Tensors and Operations, which may be different than
  the structure of `elems`.
* <b>`elems`</b>: A tensor or (possibly nested) sequence of tensors, each of which will
  be unpacked along their first dimension. The nested sequence of the
  resulting slices will be mapped over by `fn`.


#### Returns:

A tensor or (possibly nested) sequence of tensors. Each tensor packs the
results of applying fn to tensors unpacked from elems along the first
dimension, from first to last.



#### Examples:


```python
def outer_product(a):
  return tf.tensordot(a, a, 0)

batch_size = 100
a = tf.ones((batch_size, 32, 32))
c = tf.vectorized_map(outer_product, a)
assert c.shape == (batch_size, 32, 32, 32, 32)
```

```python
# Computing per-example gradients

batch_size = 10
num_features = 32
layer = tf.keras.layers.Dense(1)

def model_fn(arg):
  with tf.GradientTape() as g:
    inp, label = arg
    inp = tf.expand_dims(inp, 0)
    label = tf.expand_dims(label, 0)
    prediction = layer(inp)
    loss = tf.nn.l2_loss(label - prediction)
  return g.gradient(loss, (layer.kernel, layer.bias))

inputs = tf.random_uniform([batch_size, num_features])
labels = tf.random_uniform([batch_size, 1])
per_example_gradients = tf.vectorized_map(model_fn, (inputs, labels))
assert per_example_gradients[0].shape == (batch_size, num_features, 1)
assert per_example_gradients[1].shape == (batch_size, 1)
```
