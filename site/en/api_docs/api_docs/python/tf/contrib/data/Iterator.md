

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.data.Iterator

## Class `Iterator`





Defined in [`tensorflow/contrib/data/python/ops/dataset_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/data/python/ops/dataset_ops.py).

Represents the state of iterating through a `Dataset`.

## Properties

<h3 id="initializer"><code>initializer</code></h3>

A `tf.Operation` that should be run to initialize this iterator.

#### Returns:

  A `tf.Operation` that should be run to initialize this iterator


#### Raises:

* <b>`ValueError`</b>: If this iterator initializes itself automatically.

<h3 id="output_shapes"><code>output_shapes</code></h3>

Returns the shape of each component of an element of this iterator.

#### Returns:

  A nested structure of `tf.TensorShape` objects corresponding to each
  component of an element of this iterator.

<h3 id="output_types"><code>output_types</code></h3>

Returns the type of each component of an element of this iterator.

#### Returns:

  A nested structure of `tf.DType` objects corresponding to each component
  of an element of this iterator.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    iterator_resource,
    initializer,
    output_types,
    output_shapes
)
```

Creates a new iterator from the given iterator resource.

NOTE(mrry): Most users will not call this initializer directly, and will
instead use `Iterator.from_dataset()` or `Dataset.make_one_shot_iterator()`.

#### Args:

* <b>`iterator_resource`</b>: A `tf.resource` scalar `tf.Tensor` representing the
    iterator.
* <b>`initializer`</b>: A `tf.Operation` that should be run to initialize this
    iterator.
* <b>`output_types`</b>: A nested structure of `tf.DType` objects corresponding to
    each component of an element of this iterator.
* <b>`output_shapes`</b>: A nested structure of `tf.TensorShape` objects
    corresponding to each component of an element of this dataset.

<h3 id="dispose_op"><code>dispose_op</code></h3>

``` python
dispose_op(name=None)
```

Returns a `tf.Operation` that destroys this iterator.

The returned operation may be used to release any resources consumed by
this iterator without closing the session.

#### Args:

* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

  A `tf.Operation`.

<h3 id="from_dataset"><code>from_dataset</code></h3>

``` python
from_dataset(
    dataset,
    shared_name=None
)
```

Creates a new, uninitialized `Iterator` from the given `Dataset`.

To initialize this iterator, you must run its `initializer`:

```python
dataset = ...
iterator = Iterator.from_dataset(dataset)
# ...
sess.run(iterator.initializer)
```

#### Args:

* <b>`dataset`</b>: A `Dataset` object.
* <b>`shared_name`</b>: (Optional.) If non-empty, this iterator will be shared under
    the given name across multiple sessions that share the same devices
    (e.g. when using a remote server).


#### Returns:

  An `Iterator`.

<h3 id="from_string_handle"><code>from_string_handle</code></h3>

``` python
from_string_handle(
    string_handle,
    output_types,
    output_shapes=None
)
```

Creates a new, uninitialized `Iterator` based on the given handle.

This method allows you to define a "feedable" iterator where you can choose
between concrete iterators by feeding a value in a [`tf.Session.run`](../../../tf/Session#run) call.
In that case, `string_handle` would a [`tf.placeholder`](../../../tf/placeholder), and you would feed
it with the value of [`tf.contrib.data.Iterator.string_handle`](../../../tf/contrib/data/Iterator#string_handle) in each step.

For example, if you had two iterators that marked the current position in
a training dataset and a test dataset, you could choose which to use in
each step as follows:

```python
train_iterator = tf.contrib.data.Dataset(...).make_one_shot_iterator()
train_iterator_handle = sess.run(train_iterator.string_handle())

test_iterator = tf.contrib.data.Dataset(...).make_one_shot_iterator()
test_iterator_handle = sess.run(test_iterator.string_handle())

handle = tf.placeholder(tf.string, shape=[])
iterator = tf.contrib.data.Iterator.from_string_handle(
    handle, train_iterator.output_types)

next_element = iterator.get_next()
loss = f(next_element)

train_loss = sess.run(loss, feed_dict={handle: train_iterator_handle})
test_loss = sess.run(loss, feed_dict={handle: test_iterator_handle})
```

#### Args:

* <b>`string_handle`</b>: A scalar `tf.Tensor` of type `tf.string` that evaluates
    to a handle produced by the `Iterator.string_handle()` method.
* <b>`output_types`</b>: A nested structure of `tf.DType` objects corresponding to
    each component of an element of this iterator.
* <b>`output_shapes`</b>: (Optional.) A nested structure of `tf.TensorShape` objects
    corresponding to each component of an element of this dataset. If
    omitted, each component will have an unconstrainted shape.


#### Returns:

  An `Iterator`.

<h3 id="from_structure"><code>from_structure</code></h3>

``` python
from_structure(
    output_types,
    output_shapes=None,
    shared_name=None
)
```

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

#### Args:

* <b>`output_types`</b>: A nested structure of `tf.DType` objects corresponding to
    each component of an element of this iterator.
* <b>`output_shapes`</b>: (Optional.) A nested structure of `tf.TensorShape` objects
    corresponding to each component of an element of this dataset. If
    omitted, each component will have an unconstrainted shape.
* <b>`shared_name`</b>: (Optional.) If non-empty, this iterator will be shared under
    the given name across multiple sessions that share the same devices
    (e.g. when using a remote server).


#### Returns:

  An `Iterator`.


#### Raises:

* <b>`TypeError`</b>: If the structures of `output_shapes` and `output_types` are
    not the same.

<h3 id="get_next"><code>get_next</code></h3>

``` python
get_next(name=None)
```

Returns a nested structure of `tf.Tensor`s containing the next element.

#### Args:

* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

  A nested structure of `tf.Tensor` objects.

<h3 id="make_initializer"><code>make_initializer</code></h3>

``` python
make_initializer(dataset)
```

Returns a `tf.Operation` that initializes this iterator on `dataset`.

#### Args:

* <b>`dataset`</b>: A `Dataset` with compatible structure to this iterator.


#### Returns:

  A `tf.Operation` that can be run to initialize this iterator on the given
  `dataset`.


#### Raises:

* <b>`TypeError`</b>: If `dataset` and this iterator do not have a compatible
    element structure.

<h3 id="string_handle"><code>string_handle</code></h3>

``` python
string_handle(name=None)
```

Returns a string-valued `tf.Tensor` that represents this iterator.

#### Args:

* <b>`name`</b>: (Optional.) A name for the created operation.


#### Returns:

  A scalar `tf.Tensor` of type `tf.string`.



