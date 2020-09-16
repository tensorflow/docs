description: A TensorFlow Session for use in interactive contexts, such as a shell.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.InteractiveSession" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="as_default"/>
<meta itemprop="property" content="close"/>
<meta itemprop="property" content="list_devices"/>
<meta itemprop="property" content="make_callable"/>
<meta itemprop="property" content="partial_run"/>
<meta itemprop="property" content="partial_run_setup"/>
<meta itemprop="property" content="run"/>
</div>

# tf.compat.v1.InteractiveSession

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L1679-L1784">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A TensorFlow `Session` for use in interactive contexts, such as a shell.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.InteractiveSession(
    target='', graph=None, config=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

The only difference with a regular `Session` is that an `InteractiveSession`
installs itself as the default session on construction.
The methods <a href="../../../tf/Tensor.md#eval"><code>tf.Tensor.eval</code></a>
and <a href="../../../tf/Operation.md#run"><code>tf.Operation.run</code></a>
will use that session to run ops.

This is convenient in interactive shells and [IPython
notebooks](http://ipython.org), as it avoids having to pass an explicit
`Session` object to run ops.

#### For example:



```python
sess = tf.compat.v1.InteractiveSession()
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b
# We can just use 'c.eval()' without passing 'sess'
print(c.eval())
sess.close()
```

Note that a regular session installs itself as the default session when it
is created in a `with` statement.  The common usage in non-interactive
programs is to follow that pattern:

```python
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b
with tf.compat.v1.Session():
  # We can also use 'c.eval()' here.
  print(c.eval())
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`target`
</td>
<td>
(Optional.) The execution engine to connect to. Defaults to using
an in-process engine.
</td>
</tr><tr>
<td>
`graph`
</td>
<td>
(Optional.) The `Graph` to be launched (described above).
</td>
</tr><tr>
<td>
`config`
</td>
<td>
(Optional) `ConfigProto` proto used to configure the session.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`graph`
</td>
<td>
The graph that was launched in this session.
</td>
</tr><tr>
<td>
`graph_def`
</td>
<td>
A serializable version of the underlying TensorFlow graph.
</td>
</tr><tr>
<td>
`sess_str`
</td>
<td>
The TensorFlow process to which this session will connect.
</td>
</tr>
</table>



## Methods

<h3 id="as_default"><code>as_default</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L793-L846">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_default()
</code></pre>

Returns a context manager that makes this object the default session.

Use with the `with` keyword to specify that calls to
<a href="../../../tf/Operation.md#run"><code>tf.Operation.run</code></a> or <a href="../../../tf/Tensor.md#eval"><code>tf.Tensor.eval</code></a> should be executed in
this session.

```python
c = tf.constant(..)
sess = tf.compat.v1.Session()

with sess.as_default():
  assert tf.compat.v1.get_default_session() is sess
  print(c.eval())
```

To get the current default session, use <a href="../../../tf/compat/v1/get_default_session.md"><code>tf.compat.v1.get_default_session</code></a>.

*N.B.* The `as_default` context manager *does not* close the
session when you exit the context, and you must close the session
explicitly.

```python
c = tf.constant(...)
sess = tf.compat.v1.Session()
with sess.as_default():
  print(c.eval())
# ...
with sess.as_default():
  print(c.eval())

sess.close()
```

Alternatively, you can use `with tf.compat.v1.Session():` to create a
session that is automatically closed on exiting the context,
including when an uncaught exception is raised.

*N.B.* The default session is a property of the current thread. If you
create a new thread, and wish to use the default session in that
thread, you must explicitly add a `with sess.as_default():` in that
thread's function.

*N.B.* Entering a `with sess.as_default():` block does not affect
the current default graph. If you are using multiple graphs, and
`sess.graph` is different from the value of
<a href="../../../tf/compat/v1/get_default_graph.md"><code>tf.compat.v1.get_default_graph</code></a>, you must explicitly enter a
`with sess.graph.as_default():` block to make `sess.graph` the default
graph.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A context manager using this session as the default session.
</td>
</tr>

</table>



<h3 id="close"><code>close</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L1771-L1784">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>close()
</code></pre>

Closes an `InteractiveSession`.


<h3 id="list_devices"><code>list_devices</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L706-L742">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>list_devices()
</code></pre>

Lists available devices in this session.

```python
devices = sess.list_devices()
for d in devices:
  print(d.name)
```

#### Where:

Each element in the list has the following properties

* <b>`name`</b>: A string with the full name of the device. ex:
    `/job:worker/replica:0/task:3/device:CPU:0`
* <b>`device_type`</b>: The type of the device (e.g. `CPU`, `GPU`, `TPU`.)
* <b>`memory_limit`</b>: The maximum amount of memory available on the device.
    Note: depending on the device, it is possible the usable memory could
    be substantially less.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
If it encounters an error (e.g. session is in an
invalid state, or network errors occur).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of devices in the session.
</td>
</tr>

</table>



<h3 id="make_callable"><code>make_callable</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L1186-L1309">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>make_callable(
    fetches, feed_list=None, accept_options=(False)
)
</code></pre>

Returns a Python callable that runs a particular step.

The returned callable will take `len(feed_list)` arguments whose types
must be compatible feed values for the respective elements of `feed_list`.
For example, if element `i` of `feed_list` is a <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, the `i`th
argument to the returned callable must be a numpy ndarray (or something
convertible to an ndarray) with matching element type and shape. See
`tf.Session.run` for details of the allowable feed key and value types.

The returned callable will have the same return type as
`tf.Session.run(fetches, ...)`. For example, if `fetches` is a <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>,
the callable will return a numpy ndarray; if `fetches` is a <a href="../../../tf/Operation.md"><code>tf.Operation</code></a>,
it will return `None`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fetches`
</td>
<td>
A value or list of values to fetch. See `tf.Session.run` for
details of the allowable fetch types.
</td>
</tr><tr>
<td>
`feed_list`
</td>
<td>
(Optional.) A list of `feed_dict` keys. See `tf.Session.run`
for details of the allowable feed key types.
</td>
</tr><tr>
<td>
`accept_options`
</td>
<td>
(Optional.) If `True`, the returned `Callable` will be
able to accept <a href="../../../tf/compat/v1/RunOptions.md"><code>tf.compat.v1.RunOptions</code></a> and <a href="../../../tf/compat/v1/RunMetadata.md"><code>tf.compat.v1.RunMetadata</code></a>
as optional keyword arguments `options` and `run_metadata`,
respectively, with the same syntax and semantics as `tf.Session.run`,
which is useful for certain use cases (profiling and debugging) but will
result in measurable slowdown of the `Callable`'s
performance. Default: `False`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A function that when called will execute the step defined by
`feed_list` and `fetches` in this session.
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
If `fetches` or `feed_list` cannot be interpreted
as arguments to `tf.Session.run`.
</td>
</tr>
</table>



<h3 id="partial_run"><code>partial_run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L969-L1014">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>partial_run(
    handle, fetches, feed_dict=None
)
</code></pre>

Continues the execution with more feeds and fetches.

This is EXPERIMENTAL and subject to change.

To use partial execution, a user first calls `partial_run_setup()` and
then a sequence of `partial_run()`. `partial_run_setup` specifies the
list of feeds and fetches that will be used in the subsequent
`partial_run` calls.

The optional `feed_dict` argument allows the caller to override
the value of tensors in the graph. See run() for more information.

Below is a simple example:

```python
a = array_ops.placeholder(dtypes.float32, shape=[])
b = array_ops.placeholder(dtypes.float32, shape=[])
c = array_ops.placeholder(dtypes.float32, shape=[])
r1 = math_ops.add(a, b)
r2 = math_ops.multiply(r1, c)

h = sess.partial_run_setup([r1, r2], [a, b, c])
res = sess.partial_run(h, r1, feed_dict={a: 1, b: 2})
res = sess.partial_run(h, r2, feed_dict={c: res})
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`handle`
</td>
<td>
A handle for a sequence of partial runs.
</td>
</tr><tr>
<td>
`fetches`
</td>
<td>
A single graph element, a list of graph elements, or a dictionary
whose values are graph elements or lists of graph elements (see
documentation for `run`).
</td>
</tr><tr>
<td>
`feed_dict`
</td>
<td>
A dictionary that maps graph elements to values (described
above).
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Either a single value if `fetches` is a single graph element, or
a list of values if `fetches` is a list, or a dictionary with the
same keys as `fetches` if that is a dictionary
(see documentation for `run`).
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses on error.
</td>
</tr>
</table>



<h3 id="partial_run_setup"><code>partial_run_setup</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L1016-L1090">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>partial_run_setup(
    fetches, feeds=None
)
</code></pre>

Sets up a graph with feeds and fetches for partial run.

This is EXPERIMENTAL and subject to change.

Note that contrary to `run`, `feeds` only specifies the graph elements.
The tensors will be supplied by the subsequent `partial_run` calls.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fetches`
</td>
<td>
A single graph element, or a list of graph elements.
</td>
</tr><tr>
<td>
`feeds`
</td>
<td>
A single graph element, or a list of graph elements.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A handle for partial run.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If this `Session` is in an invalid state (e.g. has been
closed).
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If `fetches` or `feed_dict` keys are of an inappropriate type.
</td>
</tr><tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if a TensorFlow error happens.
</td>
</tr>
</table>



<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/client/session.py#L848-L967">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    fetches, feed_dict=None, options=None, run_metadata=None
)
</code></pre>

Runs operations and evaluates tensors in `fetches`.

This method runs one "step" of TensorFlow computation, by
running the necessary graph fragment to execute every `Operation`
and evaluate every `Tensor` in `fetches`, substituting the values in
`feed_dict` for the corresponding input values.

The `fetches` argument may be a single graph element, or an arbitrarily
nested list, tuple, namedtuple, dict, or OrderedDict containing graph
elements at its leaves.  A graph element can be one of the following types:

* A <a href="../../../tf/Operation.md"><code>tf.Operation</code></a>.
  The corresponding fetched value will be `None`.
* A <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>.
  The corresponding fetched value will be a numpy ndarray containing the
  value of that tensor.
* A <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>.
  The corresponding fetched value will be a
  <a href="../../../tf/compat/v1/SparseTensorValue.md"><code>tf.compat.v1.SparseTensorValue</code></a>
  containing the value of that sparse tensor.
* A `get_tensor_handle` op.  The corresponding fetched value will be a
  numpy ndarray containing the handle of that tensor.
* A `string` which is the name of a tensor or operation in the graph.

The value returned by `run()` has the same shape as the `fetches` argument,
where the leaves are replaced by the corresponding values returned by
TensorFlow.

#### Example:



```python
   a = tf.constant([10, 20])
   b = tf.constant([1.0, 2.0])
   # 'fetches' can be a singleton
   v = session.run(a)
   # v is the numpy array [10, 20]
   # 'fetches' can be a list.
   v = session.run([a, b])
   # v is a Python list with 2 numpy arrays: the 1-D array [10, 20] and the
   # 1-D array [1.0, 2.0]
   # 'fetches' can be arbitrary lists, tuples, namedtuple, dicts:
   MyData = collections.namedtuple('MyData', ['a', 'b'])
   v = session.run({'k1': MyData(a, b), 'k2': [b, a]})
   # v is a dict with
   # v['k1'] is a MyData namedtuple with 'a' (the numpy array [10, 20]) and
   # 'b' (the numpy array [1.0, 2.0])
   # v['k2'] is a list with the numpy array [1.0, 2.0] and the numpy array
   # [10, 20].
```

The optional `feed_dict` argument allows the caller to override
the value of tensors in the graph. Each key in `feed_dict` can be
one of the following types:

* If the key is a <a href="../../../tf/Tensor.md"><code>tf.Tensor</code></a>, the
  value may be a Python scalar, string, list, or numpy ndarray
  that can be converted to the same `dtype` as that
  tensor. Additionally, if the key is a
  <a href="../../../tf/compat/v1/placeholder.md"><code>tf.compat.v1.placeholder</code></a>, the shape of
  the value will be checked for compatibility with the placeholder.
* If the key is a
  <a href="../../../tf/sparse/SparseTensor.md"><code>tf.SparseTensor</code></a>,
  the value should be a
  <a href="../../../tf/compat/v1/SparseTensorValue.md"><code>tf.compat.v1.SparseTensorValue</code></a>.
* If the key is a nested tuple of `Tensor`s or `SparseTensor`s, the value
  should be a nested tuple with the same structure that maps to their
  corresponding values as above.

Each value in `feed_dict` must be convertible to a numpy array of the dtype
of the corresponding key.

The optional `options` argument expects a [`RunOptions`] proto. The options
allow controlling the behavior of this particular step (e.g. turning tracing
on).

The optional `run_metadata` argument expects a [`RunMetadata`] proto. When
appropriate, the non-Tensor output of this step will be collected there. For
example, when users turn on tracing in `options`, the profiled info will be
collected into this argument and passed back.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`fetches`
</td>
<td>
A single graph element, a list of graph elements, or a dictionary
whose values are graph elements or lists of graph elements (described
above).
</td>
</tr><tr>
<td>
`feed_dict`
</td>
<td>
A dictionary that maps graph elements to values (described
above).
</td>
</tr><tr>
<td>
`options`
</td>
<td>
A [`RunOptions`] protocol buffer
</td>
</tr><tr>
<td>
`run_metadata`
</td>
<td>
A [`RunMetadata`] protocol buffer
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
Either a single value if `fetches` is a single graph element, or
a list of values if `fetches` is a list, or a dictionary with the
same keys as `fetches` if that is a dictionary (described above).
Order in which `fetches` operations are evaluated inside the call
is undefined.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If this `Session` is in an invalid state (e.g. has been
closed).
</td>
</tr><tr>
<td>
`TypeError`
</td>
<td>
If `fetches` or `feed_dict` keys are of an inappropriate type.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If `fetches` or `feed_dict` keys are invalid or refer to a
`Tensor` that doesn't exist.
</td>
</tr>
</table>





