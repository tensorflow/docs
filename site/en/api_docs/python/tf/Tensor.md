


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.Tensor

### `class tf.Tensor`

See the guide: [Building Graphs > Core graph data structures](../../../api_guides/python/framework#Core_graph_data_structures)

Represents one of the outputs of an `Operation`.

A `Tensor` is a symbolic handle to one of the outputs of an
`Operation`. It does not hold the values of that operation's output,
but instead provides a means of computing those values in a
TensorFlow [`tf.Session`](../tf/Session).

This class has two primary purposes:

1. A `Tensor` can be passed as an input to another `Operation`.
   This builds a dataflow connection between operations, which
   enables TensorFlow to execute an entire `Graph` that represents a
   large, multi-step computation.

2. After the graph has been launched in a session, the value of the
   `Tensor` can be computed by passing it to
   [`tf.Session.run`](../tf/Session#run).
   `t.eval()` is a shortcut for calling
   `tf.get_default_session().run(t)`.

In the following example, `c`, `d`, and `e` are symbolic `Tensor`
objects, whereas `result` is a numpy array that stores a concrete
value:

```python
# Build a dataflow graph.
c = tf.constant([[1.0, 2.0], [3.0, 4.0]])
d = tf.constant([[1.0, 1.0], [0.0, 1.0]])
e = tf.matmul(c, d)

# Construct a `Session` to execute the graph.
sess = tf.Session()

# Execute the graph and store the value that `e` represents in `result`.
result = sess.run(e)
```

## Properties

<h3 id="device"><code>device</code></h3>

The name of the device on which this tensor will be produced, or None.

<h3 id="dtype"><code>dtype</code></h3>

The `DType` of elements in this tensor.

<h3 id="graph"><code>graph</code></h3>

The `Graph` that contains this tensor.

<h3 id="name"><code>name</code></h3>

The string name of this tensor.

<h3 id="op"><code>op</code></h3>

The `Operation` that produces this tensor as an output.

<h3 id="shape"><code>shape</code></h3>

Returns the `TensorShape` that represents the shape of this tensor.

The shape is computed using shape inference functions that are
registered in the Op for each `Operation`.  See
[`tf.TensorShape`](../tf/TensorShape)
for more details of what a shape represents.

The inferred shape of a tensor is used to provide shape
information without having to launch the graph in a session. This
can be used for debugging, and providing early error messages. For
example:

```python
c = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

print(c.shape)
==> TensorShape([Dimension(2), Dimension(3)])

d = tf.constant([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, 1.0]])

print(d.shape)
==> TensorShape([Dimension(4), Dimension(2)])

# Raises a ValueError, because `c` and `d` do not have compatible
# inner dimensions.
e = tf.matmul(c, d)

f = tf.matmul(c, d, transpose_a=True, transpose_b=True)

print(f.shape)
==> TensorShape([Dimension(3), Dimension(4)])
```

In some cases, the inferred shape may have unknown dimensions. If
the caller has additional information about the values of these
dimensions, `Tensor.set_shape()` can be used to augment the
inferred shape.

#### Returns:

  A `TensorShape` representing the shape of this tensor.

<h3 id="value_index"><code>value_index</code></h3>

The index of this tensor in the outputs of its `Operation`.



## Methods

<h3 id="__init__"><code>__init__(op, value_index, dtype)</code></h3>

Creates a new `Tensor`.

#### Args:

* <b>`op`</b>: An `Operation`. `Operation` that computes this tensor.
* <b>`value_index`</b>: An `int`. Index of the operation's endpoint that produces
    this tensor.
* <b>`dtype`</b>: A `DType`. Type of elements stored in this tensor.


#### Raises:

* <b>`TypeError`</b>: If the op is not an `Operation`.

<h3 id="consumers"><code>consumers()</code></h3>

Returns a list of `Operation`s that consume this tensor.

#### Returns:

  A list of `Operation`s.

<h3 id="eval"><code>eval(feed_dict=None, session=None)</code></h3>

Evaluates this tensor in a `Session`.

Calling this method will execute all preceding operations that
produce the inputs needed for the operation that produces this
tensor.

*N.B.* Before invoking `Tensor.eval()`, its graph must have been
launched in a session, and either a default session must be
available, or `session` must be specified explicitly.

#### Args:

* <b>`feed_dict`</b>: A dictionary that maps `Tensor` objects to feed values.
    See [`tf.Session.run`](../tf/Session#run) for a
    description of the valid feed values.
* <b>`session`</b>: (Optional.) The `Session` to be used to evaluate this tensor. If
    none, the default session will be used.


#### Returns:

  A numpy array corresponding to the value of this tensor.

<h3 id="get_shape"><code>get_shape()</code></h3>

Alias of Tensor.shape.

<h3 id="set_shape"><code>set_shape(shape)</code></h3>

Updates the shape of this tensor.

This method can be called multiple times, and will merge the given
`shape` with the current shape of this tensor. It can be used to
provide additional information about the shape of this tensor that
cannot be inferred from the graph alone. For example, this can be used
to provide additional information about the shapes of images:

```python
_, image_data = tf.TFRecordReader(...).read(...)
image = tf.image.decode_png(image_data, channels=3)

# The height and width dimensions of `image` are data dependent, and
# cannot be computed without executing the op.
print(image.shape)
==> TensorShape([Dimension(None), Dimension(None), Dimension(3)])

# We know that each image in this dataset is 28 x 28 pixels.
image.set_shape([28, 28, 3])
print(image.shape)
==> TensorShape([Dimension(28), Dimension(28), Dimension(3)])
```

#### Args:

* <b>`shape`</b>: A `TensorShape` representing the shape of this tensor.


#### Raises:

* <b>`ValueError`</b>: If `shape` is not compatible with the current shape of
    this tensor.



## Class Members

<h3 id="OVERLOADABLE_OPERATORS"><code>OVERLOADABLE_OPERATORS</code></h3>



Defined in [`tensorflow/python/framework/ops.py`](https://www.tensorflow.org/code/tensorflow/python/framework/ops.py).

