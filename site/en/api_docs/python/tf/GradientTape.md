description: Record operations for automatic differentiation.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.GradientTape" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="batch_jacobian"/>
<meta itemprop="property" content="gradient"/>
<meta itemprop="property" content="jacobian"/>
<meta itemprop="property" content="reset"/>
<meta itemprop="property" content="stop_recording"/>
<meta itemprop="property" content="watch"/>
<meta itemprop="property" content="watched_variables"/>
</div>

# tf.GradientTape

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L736-L1360">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Record operations for automatic differentiation.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`tf.autodiff.GradientTape`</p>

<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.GradientTape`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.GradientTape(
    persistent=(False), watch_accessed_variables=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

Operations are recorded if they are executed within this context manager and
at least one of their inputs is being "watched".

Trainable variables (created by <a href="../tf/Variable.md"><code>tf.Variable</code></a> or <a href="../tf/compat/v1/get_variable.md"><code>tf.compat.v1.get_variable</code></a>,
where `trainable=True` is default in both cases) are automatically watched.
Tensors can be manually watched by invoking the `watch` method on this context
manager.

For example, consider the function `y = x * x`. The gradient at `x = 3.0` can
be computed as:

```
>>> x = tf.constant(3.0)
>>> with tf.GradientTape() as g:
...   g.watch(x)
...   y = x * x
>>> dy_dx = g.gradient(y, x)
>>> print(dy_dx)
tf.Tensor(6.0, shape=(), dtype=float32)
```

GradientTapes can be nested to compute higher-order derivatives. For example,

```
>>> x = tf.constant(5.0)
>>> with tf.GradientTape() as g:
...   g.watch(x)
...   with tf.GradientTape() as gg:
...     gg.watch(x)
...     y = x * x
...   dy_dx = gg.gradient(y, x)  # dy_dx = 2 * x
>>> d2y_dx2 = g.gradient(dy_dx, x)  # d2y_dx2 = 2
>>> print(dy_dx)
tf.Tensor(10.0, shape=(), dtype=float32)
>>> print(d2y_dx2)
tf.Tensor(2.0, shape=(), dtype=float32)
```

By default, the resources held by a GradientTape are released as soon as
GradientTape.gradient() method is called. To compute multiple gradients over
the same computation, create a persistent gradient tape. This allows multiple
calls to the gradient() method as resources are released when the tape object
is garbage collected. For example:

```
>>> x = tf.constant(3.0)
>>> with tf.GradientTape(persistent=True) as g:
...   g.watch(x)
...   y = x * x
...   z = y * y
>>> dz_dx = g.gradient(z, x)  # (4*x^3 at x = 3)
>>> print(dz_dx)
tf.Tensor(108.0, shape=(), dtype=float32)
>>> dy_dx = g.gradient(y, x)
>>> print(dy_dx)
tf.Tensor(6.0, shape=(), dtype=float32)
```

By default GradientTape will automatically watch any trainable variables that
are accessed inside the context. If you want fine grained control over which
variables are watched you can disable automatic tracking by passing
`watch_accessed_variables=False` to the tape constructor:

```
>>> x = tf.Variable(2.0)
>>> w = tf.Variable(5.0)
>>> with tf.GradientTape(
...     watch_accessed_variables=False, persistent=True) as tape:
...   tape.watch(x)
...   y = x ** 2  # Gradients will be available for `x`.
...   z = w ** 3  # No gradients will be available as `w` isn't being watched.
>>> dy_dx = tape.gradient(y, x)
>>> print(dy_dx)
tf.Tensor(4.0, shape=(), dtype=float32)
>>> # No gradients will be available as `w` isn't being watched.
>>> dz_dy = tape.gradient(z, w)
>>> print(dz_dy)
None
```

Note that when using models you should ensure that your variables exist when
using `watch_accessed_variables=False`. Otherwise it's quite easy to make your
first iteration not have any gradients:

```python
a = tf.keras.layers.Dense(32)
b = tf.keras.layers.Dense(32)

with tf.GradientTape(watch_accessed_variables=False) as tape:
  tape.watch(a.variables)  # Since `a.build` has not been called at this point
                           # `a.variables` will return an empty list and the
                           # tape will not be watching anything.
  result = b(a(inputs))
  tape.gradient(result, a.variables)  # The result of this computation will be
                                      # a list of `None`s since a's variables
                                      # are not being watched.
```

Note that only tensors with real or complex dtypes are differentiable.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`persistent`
</td>
<td>
Boolean controlling whether a persistent gradient tape
is created. False by default, which means at most one call can
be made to the gradient() method on this object.
</td>
</tr><tr>
<td>
`watch_accessed_variables`
</td>
<td>
Boolean controlling whether the tape will
automatically `watch` any (trainable) variables accessed while the tape
is active. Defaults to True meaning gradients can be requested from any
result computed in the tape derived from reading a trainable `Variable`.
If False users must explicitly `watch` any `Variable`s they want to
request gradients from.
</td>
</tr>
</table>



## Methods

<h3 id="batch_jacobian"><code>batch_jacobian</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L1221-L1360">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>batch_jacobian(
    target, source, unconnected_gradients=tf.UnconnectedGradients.NONE,
    parallel_iterations=None, experimental_use_pfor=(True)
)
</code></pre>

Computes and stacks per-example jacobians.

See [wikipedia article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant)
for the definition of a Jacobian. This function is essentially an efficient
implementation of the following:

`tf.stack([self.jacobian(y[i], x[i]) for i in range(x.shape[0])])`.

Note that compared to <a href="../tf/GradientTape.md#jacobian"><code>GradientTape.jacobian</code></a> which computes gradient of
each output value w.r.t each input value, this function is useful when
`target[i,...]` is independent of `source[j,...]` for `j != i`. This
assumption allows more efficient computation as compared to
<a href="../tf/GradientTape.md#jacobian"><code>GradientTape.jacobian</code></a>. The output, as well as intermediate activations,
are lower dimensional and avoid a bunch of redundant zeros which would
result in the jacobian computation given the independence assumption.

Note: Unless you set `persistent=True` a GradientTape can only be used to
compute one set of gradients (or jacobians).

#### Example usage:



```python
with tf.GradientTape() as g:
  x = tf.constant([[1., 2.], [3., 4.]], dtype=tf.float32)
  g.watch(x)
  y = x * x
batch_jacobian = g.batch_jacobian(y, x)
# batch_jacobian is [[[2,  0], [0,  4]], [[6,  0], [0,  8]]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
A tensor with rank 2 or higher and with shape [b, y1, ..., y_n].
`target[i,...]` should only depend on `source[i,...]`.
</td>
</tr><tr>
<td>
`source`
</td>
<td>
A tensor with rank 2 or higher and with shape [b, x1, ..., x_m].
</td>
</tr><tr>
<td>
`unconnected_gradients`
</td>
<td>
a value which can either hold 'none' or 'zero' and
alters the value which will be returned if the target and sources are
unconnected. The possible values and effects are detailed in
'UnconnectedGradients' and it defaults to 'none'.
</td>
</tr><tr>
<td>
`parallel_iterations`
</td>
<td>
A knob to control how many iterations are dispatched
in parallel. This knob can be used to control the total memory usage.
</td>
</tr><tr>
<td>
`experimental_use_pfor`
</td>
<td>
If true, uses pfor for computing the Jacobian. Else
uses a tf.while_loop.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A tensor `t` with shape [b, y_1, ..., y_n, x1, ..., x_m] where `t[i, ...]`
is the jacobian of `target[i, ...]` w.r.t. `source[i, ...]`, i.e. stacked
per-example jacobians.
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
If called on a used, non-persistent tape.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called on a non-persistent tape with eager execution
enabled and without enabling experimental_use_pfor.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If vectorization of jacobian computation fails or if first
dimension of `target` and `source` do not match.
</td>
</tr>
</table>



<h3 id="gradient"><code>gradient</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L993-L1101">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>gradient(
    target, sources, output_gradients=None,
    unconnected_gradients=tf.UnconnectedGradients.NONE
)
</code></pre>

Computes the gradient using operations recorded in context of this tape.

Note: Unless you set `persistent=True` a GradientTape can only be used to
compute one set of gradients (or jacobians).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
a list or nested structure of Tensors or Variables to be
differentiated.
</td>
</tr><tr>
<td>
`sources`
</td>
<td>
a list or nested structure of Tensors or Variables. `target`
will be differentiated against elements in `sources`.
</td>
</tr><tr>
<td>
`output_gradients`
</td>
<td>
a list of gradients, one for each element of
target. Defaults to None.
</td>
</tr><tr>
<td>
`unconnected_gradients`
</td>
<td>
a value which can either hold 'none' or 'zero' and
alters the value which will be returned if the target and sources are
unconnected. The possible values and effects are detailed in
'UnconnectedGradients' and it defaults to 'none'.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a list or nested structure of Tensors (or IndexedSlices, or None),
one for each element in `sources`. Returned structure is the same as
the structure of `sources`.
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
If called on a used, non-persistent tape.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called inside the context of the tape.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If the target is a variable or if unconnected gradients is
called with an unknown value.
</td>
</tr>
</table>



<h3 id="jacobian"><code>jacobian</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L1103-L1219">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>jacobian(
    target, sources, unconnected_gradients=tf.UnconnectedGradients.NONE,
    parallel_iterations=None, experimental_use_pfor=(True)
)
</code></pre>

Computes the jacobian using operations recorded in context of this tape.

Note: Unless you set `persistent=True` a GradientTape can only be used to
compute one set of gradients (or jacobians).

See[wikipedia article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant)
for the definition of a Jacobian.

#### Example usage:



```python
with tf.GradientTape() as g:
  x  = tf.constant([1.0, 2.0])
  g.watch(x)
  y = x * x
jacobian = g.jacobian(y, x)
# jacobian value is [[2., 0.], [0., 4.]]
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`target`
</td>
<td>
Tensor to be differentiated.
</td>
</tr><tr>
<td>
`sources`
</td>
<td>
a list or nested structure of Tensors or Variables. `target`
will be differentiated against elements in `sources`.
</td>
</tr><tr>
<td>
`unconnected_gradients`
</td>
<td>
a value which can either hold 'none' or 'zero' and
alters the value which will be returned if the target and sources are
unconnected. The possible values and effects are detailed in
'UnconnectedGradients' and it defaults to 'none'.
</td>
</tr><tr>
<td>
`parallel_iterations`
</td>
<td>
A knob to control how many iterations are dispatched
in parallel. This knob can be used to control the total memory usage.
</td>
</tr><tr>
<td>
`experimental_use_pfor`
</td>
<td>
If true, vectorizes the jacobian computation. Else
falls back to a sequential while_loop. Vectorization can sometimes fail
or lead to excessive memory usage. This option can be used to disable
vectorization in such cases.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list or nested structure of Tensors (or None), one for each element in
`sources`. Returned structure is the same as the structure of `sources`.
Note if any gradient is sparse (IndexedSlices), jacobian function
currently makes it dense and returns a Tensor instead. This may change in
the future.
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
If called on a used, non-persistent tape.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If called on a non-persistent tape with eager execution
enabled and without enabling experimental_use_pfor.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If vectorization of jacobian computation fails.
</td>
</tr>
</table>



<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L951-L985">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reset()
</code></pre>

Clears all information stored in this tape.

Equivalent to exiting and reentering the tape context manager with a new
tape. For example, the two following code blocks are equivalent:

```
with tf.GradientTape() as t:
  loss = loss_fn()
with tf.GradientTape() as t:
  loss += other_loss_fn()
t.gradient(loss, ...)  # Only differentiates other_loss_fn, not loss_fn


# The following is equivalent to the above
with tf.GradientTape() as t:
  loss = loss_fn()
  t.reset()
  loss += other_loss_fn()
t.gradient(loss, ...)  # Only differentiates other_loss_fn, not loss_fn
```

This is useful if you don't want to exit the context manager for the tape,
or can't because the desired reset point is inside a control flow construct:

```
with tf.GradientTape() as t:
  loss = ...
  if loss > k:
    t.reset()
```

<h3 id="stop_recording"><code>stop_recording</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L919-L949">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@tf_contextlib.contextmanager</code>
<code>stop_recording()
</code></pre>

Temporarily stops recording operations on this tape.

Operations executed while this context manager is active will not be
recorded on the tape. This is useful for reducing the memory used by tracing
all computations.

#### For example:



```
>>> x = tf.constant(4.0)
>>> with tf.GradientTape() as tape:
...   with tape.stop_recording():
...     y = x ** 2
>>> dy_dx = tape.gradient(y, x)
>>> print(dy_dx)
None
```

#### Yields:

None


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
if the tape is not currently recording.
</td>
</tr>
</table>



<h3 id="watch"><code>watch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L894-L917">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>watch(
    tensor
)
</code></pre>

Ensures that `tensor` is being traced by this tape.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`tensor`
</td>
<td>
a Tensor or list of Tensors.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if it encounters something that is not a tensor.
</td>
</tr>
</table>



<h3 id="watched_variables"><code>watched_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L987-L991">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>watched_variables()
</code></pre>

Returns variables watched by this tape in order of construction.


<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L856-L859">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>

Enters a context inside which operations are recorded on this tape.


<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/eager/backprop.py#L861-L864">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    typ, value, traceback
)
</code></pre>

Exits the recording context, no further operations are traced.




