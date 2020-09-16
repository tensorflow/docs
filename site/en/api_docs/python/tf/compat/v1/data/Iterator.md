description: Represents the state of iterating through a Dataset.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.data.Iterator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_string_handle"/>
<meta itemprop="property" content="from_structure"/>
<meta itemprop="property" content="get_next"/>
<meta itemprop="property" content="make_initializer"/>
<meta itemprop="property" content="string_handle"/>
</div>

# tf.compat.v1.data.Iterator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L81-L503">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents the state of iterating through a `Dataset`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.data.Iterator(
    iterator_resource, initializer, output_types, output_shapes, output_classes
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`iterator_resource`
</td>
<td>
A <a href="../../../../tf.md#resource"><code>tf.resource</code></a> scalar <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> representing the
iterator.
</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
A <a href="../../../../tf/Operation.md"><code>tf.Operation</code></a> that should be run to initialize this
iterator.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A nested structure of <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> objects corresponding to
each component of an element of this iterator.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
A nested structure of <a href="../../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> objects
corresponding to each component of an element of this iterator.
</td>
</tr><tr>
<td>
`output_classes`
</td>
<td>
A nested structure of Python `type` objects corresponding
to each component of an element of this iterator.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`element_spec`
</td>
<td>

</td>
</tr><tr>
<td>
`initializer`
</td>
<td>
A <a href="../../../../tf/Operation.md"><code>tf.Operation</code></a> that should be run to initialize this iterator.
</td>
</tr><tr>
<td>
`output_classes`
</td>
<td>
Returns the class of each component of an element of this iterator. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/compat/v1/data/get_output_classes.md"><code>tf.compat.v1.data.get_output_classes(iterator)</code></a>.

The expected values are <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> and <a href="../../../../tf/sparse/SparseTensor.md"><code>tf.sparse.SparseTensor</code></a>.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
Returns the shape of each component of an element of this iterator. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/compat/v1/data/get_output_shapes.md"><code>tf.compat.v1.data.get_output_shapes(iterator)</code></a>.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
Returns the type of each component of an element of this iterator. (deprecated)

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Use <a href="../../../../tf/compat/v1/data/get_output_types.md"><code>tf.compat.v1.data.get_output_types(iterator)</code></a>.
</td>
</tr>
</table>



## Methods

<h3 id="from_string_handle"><code>from_string_handle</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L228-L304">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_string_handle(
    string_handle, output_types, output_shapes=None, output_classes=None
)
</code></pre>

Creates a new, uninitialized `Iterator` based on the given handle.

This method allows you to define a "feedable" iterator where you can choose
between concrete iterators by feeding a value in a `tf.Session.run` call.
In that case, `string_handle` would be a <a href="../../../../tf/compat/v1/placeholder.md"><code>tf.compat.v1.placeholder</code></a>, and you
would
feed it with the value of `tf.data.Iterator.string_handle` in each step.

For example, if you had two iterators that marked the current position in
a training dataset and a test dataset, you could choose which to use in
each step as follows:

```python
train_iterator = tf.data.Dataset(...).make_one_shot_iterator()
train_iterator_handle = sess.run(train_iterator.string_handle())

test_iterator = tf.data.Dataset(...).make_one_shot_iterator()
test_iterator_handle = sess.run(test_iterator.string_handle())

handle = tf.compat.v1.placeholder(tf.string, shape=[])
iterator = tf.data.Iterator.from_string_handle(
    handle, train_iterator.output_types)

next_element = iterator.get_next()
loss = f(next_element)

train_loss = sess.run(loss, feed_dict={handle: train_iterator_handle})
test_loss = sess.run(loss, feed_dict={handle: test_iterator_handle})
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`string_handle`
</td>
<td>
A scalar <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> of type <a href="../../../../tf.md#string"><code>tf.string</code></a> that evaluates to
a handle produced by the `Iterator.string_handle()` method.
</td>
</tr><tr>
<td>
`output_types`
</td>
<td>
A nested structure of <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> objects corresponding to
each component of an element of this dataset.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
(Optional.) A nested structure of <a href="../../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> objects
corresponding to each component of an element of this dataset. If
omitted, each component will have an unconstrainted shape.
</td>
</tr><tr>
<td>
`output_classes`
</td>
<td>
(Optional.) A nested structure of Python `type` objects
corresponding to each component of an element of this iterator. If
omitted, each component is assumed to be of type <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Iterator`.
</td>
</tr>

</table>



<h3 id="from_structure"><code>from_structure</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L124-L226">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>from_structure(
    output_types, output_shapes=None, shared_name=None, output_classes=None
)
</code></pre>

Creates a new, uninitialized `Iterator` with the given structure.

This iterator-constructing method can be used to create an iterator that
is reusable with many different datasets.

The returned iterator is not bound to a particular dataset, and it has
no `initializer`. To initialize the iterator, run the operation returned by
`Iterator.make_initializer(dataset)`.

The following is an example

```python
iterator = Iterator.from_structure(tf.int64, tf.TensorShape([]))

dataset_range = Dataset.range(10)
range_initializer = iterator.make_initializer(dataset_range)

dataset_evens = dataset_range.filter(lambda x: x % 2 == 0)
evens_initializer = iterator.make_initializer(dataset_evens)

# Define a model based on the iterator; in this example, the model_fn
# is expected to take scalar tf.int64 Tensors as input (see
# the definition of 'iterator' above).
prediction, loss = model_fn(iterator.get_next())

# Train for `num_epochs`, where for each epoch, we first iterate over
# dataset_range, and then iterate over dataset_evens.
for _ in range(num_epochs):
  # Initialize the iterator to `dataset_range`
  sess.run(range_initializer)
  while True:
    try:
      pred, loss_val = sess.run([prediction, loss])
    except tf.errors.OutOfRangeError:
      break

  # Initialize the iterator to `dataset_evens`
  sess.run(evens_initializer)
  while True:
    try:
      pred, loss_val = sess.run([prediction, loss])
    except tf.errors.OutOfRangeError:
      break
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`output_types`
</td>
<td>
A nested structure of <a href="../../../../tf/dtypes/DType.md"><code>tf.DType</code></a> objects corresponding to
each component of an element of this dataset.
</td>
</tr><tr>
<td>
`output_shapes`
</td>
<td>
(Optional.) A nested structure of <a href="../../../../tf/TensorShape.md"><code>tf.TensorShape</code></a> objects
corresponding to each component of an element of this dataset. If
omitted, each component will have an unconstrainted shape.
</td>
</tr><tr>
<td>
`shared_name`
</td>
<td>
(Optional.) If non-empty, this iterator will be shared under
the given name across multiple sessions that share the same devices
(e.g. when using a remote server).
</td>
</tr><tr>
<td>
`output_classes`
</td>
<td>
(Optional.) A nested structure of Python `type` objects
corresponding to each component of an element of this iterator. If
omitted, each component is assumed to be of type <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
An `Iterator`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If the structures of `output_shapes` and `output_types` are
not the same.
</td>
</tr>
</table>



<h3 id="get_next"><code>get_next</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L379-L433">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_next(
    name=None
)
</code></pre>

Returns a nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a>s representing the next element.

In graph mode, you should typically call this method *once* and use its
result as the input to another computation. A typical loop will then call
`tf.Session.run` on the result of that computation. The loop will terminate
when the `Iterator.get_next()` operation raises
<a href="../../../../tf/errors/OutOfRangeError.md"><code>tf.errors.OutOfRangeError</code></a>. The following skeleton shows how to use
this method when building a training loop:

```python
dataset = ...  # A `tf.data.Dataset` object.
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

# Build a TensorFlow graph that does something with each element.
loss = model_function(next_element)
optimizer = ...  # A `tf.compat.v1.train.Optimizer` object.
train_op = optimizer.minimize(loss)

with tf.compat.v1.Session() as sess:
  try:
    while True:
      sess.run(train_op)
  except tf.errors.OutOfRangeError:
    pass
```

NOTE: It is legitimate to call `Iterator.get_next()` multiple times, e.g.
when you are distributing different elements to multiple devices in a single
step. However, a common pitfall arises when users call `Iterator.get_next()`
in each iteration of their training loop. `Iterator.get_next()` adds ops to
the graph, and executing each op allocates resources (including threads); as
a consequence, invoking it in every iteration of a training loop causes
slowdown and eventual resource exhaustion. To guard against this outcome, we
log a warning when the number of uses crosses a fixed threshold of
suspiciousness.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
(Optional.) A name for the created operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A nested structure of <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> objects.
</td>
</tr>

</table>



<h3 id="make_initializer"><code>make_initializer</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L323-L377">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_initializer(
    dataset, name=None
)
</code></pre>

Returns a <a href="../../../../tf/Operation.md"><code>tf.Operation</code></a> that initializes this iterator on `dataset`.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`dataset`
</td>
<td>
A `Dataset` with compatible structure to this iterator.
</td>
</tr><tr>
<td>
`name`
</td>
<td>
(Optional.) A name for the created operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../../tf/Operation.md"><code>tf.Operation</code></a> that can be run to initialize this iterator on the given
`dataset`.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `dataset` and this iterator do not have a compatible
element structure.
</td>
</tr>
</table>



<h3 id="string_handle"><code>string_handle</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/data/ops/iterator_ops.py#L435-L448">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>string_handle(
    name=None
)
</code></pre>

Returns a string-valued <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> that represents this iterator.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`name`
</td>
<td>
(Optional.) A name for the created operation.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A scalar <a href="../../../../tf/Tensor.md"><code>tf.Tensor</code></a> of type <a href="../../../../tf.md#string"><code>tf.string</code></a>.
</td>
</tr>

</table>





