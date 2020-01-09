page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.GradientTape


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L692-L1245">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `GradientTape`

Record operations for automatic differentiation.



### Aliases:

* Class `tf.compat.v1.GradientTape`
* Class `tf.compat.v2.GradientTape`


### Used in the guide:

* [Better performance with tf.function and AutoGraph](https://www.tensorflow.org/guide/function)
* [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training)
* [Eager execution](https://www.tensorflow.org/guide/eager)
* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)
* [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

### Used in the tutorials:

* [Adversarial example using FGSM](https://www.tensorflow.org/tutorials/generative/adversarial_fgsm)
* [Automatic differentiation and gradient tape](https://www.tensorflow.org/tutorials/customization/autodiff)
* [Better performance with tf.function](https://www.tensorflow.org/tutorials/customization/performance)
* [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)
* [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)
* [Custom training: basics](https://www.tensorflow.org/tutorials/customization/custom_training)
* [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)
* [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)
* [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)
* [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)
* [Neural machine translation with attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention)
* [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer)
* [Pix2Pix](https://www.tensorflow.org/tutorials/generative/pix2pix)
* [TensorFlow 2.0 quickstart for experts](https://www.tensorflow.org/tutorials/quickstart/advanced)
* [Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation)
* [Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer)



Operations are recorded if they are executed within this context manager and
at least one of their inputs is being "watched".

Trainable variables (created by <a href="../tf/Variable"><code>tf.Variable</code></a> or <a href="../tf/compat/v1/get_variable"><code>tf.compat.v1.get_variable</code></a>,
where `trainable=True` is default in both cases) are automatically watched.
Tensors can be manually watched by invoking the `watch` method on this context
manager.

For example, consider the function `y = x * x`. The gradient at `x = 3.0` can
be computed as:

```python
x = tf.constant(3.0)
with tf.GradientTape() as g:
  g.watch(x)
  y = x * x
dy_dx = g.gradient(y, x) # Will compute to 6.0
```

GradientTapes can be nested to compute higher-order derivatives. For example,

```python
x = tf.constant(3.0)
with tf.GradientTape() as g:
  g.watch(x)
  with tf.GradientTape() as gg:
    gg.watch(x)
    y = x * x
  dy_dx = gg.gradient(y, x)     # Will compute to 6.0
d2y_dx2 = g.gradient(dy_dx, x)  # Will compute to 2.0
```

By default, the resources held by a GradientTape are released as soon as
GradientTape.gradient() method is called. To compute multiple gradients over
the same computation, create a persistent gradient tape. This allows multiple
calls to the gradient() method as resources are released when the tape object
is garbage collected. For example:

```python
x = tf.constant(3.0)
with tf.GradientTape(persistent=True) as g:
  g.watch(x)
  y = x * x
  z = y * y
dz_dx = g.gradient(z, x)  # 108.0 (4*x^3 at x = 3)
dy_dx = g.gradient(y, x)  # 6.0
del g  # Drop the reference to the tape
```

By default GradientTape will automatically watch any trainable variables that
are accessed inside the context. If you want fine grained control over which
variables are watched you can disable automatic tracking by passing
`watch_accessed_variables=False` to the tape constructor:

```python
with tf.GradientTape(watch_accessed_variables=False) as tape:
  tape.watch(variable_a)
  y = variable_a ** 2  # Gradients will be available for `variable_a`.
  z = variable_b ** 3  # No gradients will be available since `variable_b` is
                       # not being watched.
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

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L778-L799">View source</a>

``` python
__init__(
    persistent=False,
    watch_accessed_variables=True
)
```

Creates a new GradientTape.


#### Args:


* <b>`persistent`</b>: Boolean controlling whether a persistent gradient tape
  is created. False by default, which means at most one call can
  be made to the gradient() method on this object.
* <b>`watch_accessed_variables`</b>: Boolean controlling whether the tape will
  automatically `watch` any (trainable) variables accessed while the tape
  is active. Defaults to True meaning gradients can be requested from any
  result computed in the tape derived from reading a trainable `Variable`.
  If False users must explicitly `watch` any `Variable`s they want to
  request gradients from.



## Methods

<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L801-L804">View source</a>

``` python
__enter__()
```

Enters a context inside which operations are recorded on this tape.


<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L806-L809">View source</a>

``` python
__exit__(
    typ,
    value,
    traceback
)
```

Exits the recording context, no further operations are traced.


<h3 id="batch_jacobian"><code>batch_jacobian</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L1126-L1245">View source</a>

``` python
batch_jacobian(
    target,
    source,
    unconnected_gradients=tf.UnconnectedGradients.NONE,
    parallel_iterations=None,
    experimental_use_pfor=True
)
```

Computes and stacks per-example jacobians.

See [wikipedia article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant) for the
definition of a Jacobian. This function is essentially an efficient
implementation of the following:

`tf.stack([self.jacobian(y[i], x[i]) for i in range(x.shape[0])])`.

Note that compared to <a href="../tf/GradientTape#jacobian"><code>GradientTape.jacobian</code></a> which computes gradient of
each output value w.r.t each input value, this function is useful when
`target[i,...]` is independent of `source[j,...]` for `j != i`. This
assumption allows more efficient computation as compared to
<a href="../tf/GradientTape#jacobian"><code>GradientTape.jacobian</code></a>. The output, as well as intermediate activations,
are lower dimensional and avoid a bunch of redundant zeros which would
result in the jacobian computation given the independence assumption.

#### Example usage:



```python
with tf.GradientTape() as g:
  x = tf.constant([[1., 2.], [3., 4.]], dtype=tf.float32)
  g.watch(x)
  y = x * x
batch_jacobian = g.batch_jacobian(y, x)
# batch_jacobian is [[[2,  0], [0,  4]], [[6,  0], [0,  8]]]
```

#### Args:


* <b>`target`</b>: A tensor with rank 2 or higher and with shape [b, y1, ..., y_n].
  `target[i,...]` should only depend on `source[i,...]`.
* <b>`source`</b>: A tensor with rank 2 or higher and with shape [b, x1, ..., x_m].
* <b>`unconnected_gradients`</b>: a value which can either hold 'none' or 'zero' and
  alters the value which will be returned if the target and sources are
  unconnected. The possible values and effects are detailed in
  'UnconnectedGradients' and it defaults to 'none'.
* <b>`parallel_iterations`</b>: A knob to control how many iterations are dispatched
  in parallel. This knob can be used to control the total memory usage.
* <b>`experimental_use_pfor`</b>: If true, uses pfor for computing the Jacobian. Else
  uses a tf.while_loop.


#### Returns:

A tensor `t` with shape [b, y_1, ..., y_n, x1, ..., x_m] where `t[i, ...]`
is the jacobian of `target[i, ...]` w.r.t. `source[i, ...]`, i.e. stacked
per-example jacobians.



#### Raises:


* <b>`RuntimeError`</b>: If called on a non-persistent tape with eager execution
  enabled and without enabling experimental_use_pfor.
* <b>`ValueError`</b>: If vectorization of jacobian computation fails or if first
  dimension of `target` and `source` do not match.

<h3 id="gradient"><code>gradient</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L935-L1020">View source</a>

``` python
gradient(
    target,
    sources,
    output_gradients=None,
    unconnected_gradients=tf.UnconnectedGradients.NONE
)
```

Computes the gradient using operations recorded in context of this tape.


#### Args:


* <b>`target`</b>: Tensor (or list of tensors) to be differentiated.
* <b>`sources`</b>: a list or nested structure of Tensors or Variables. `target`
  will be differentiated against elements in `sources`.
* <b>`output_gradients`</b>: a list of gradients, one for each element of
  target. Defaults to None.
* <b>`unconnected_gradients`</b>: a value which can either hold 'none' or 'zero' and
  alters the value which will be returned if the target and sources are
  unconnected. The possible values and effects are detailed in
  'UnconnectedGradients' and it defaults to 'none'.


#### Returns:

a list or nested structure of Tensors (or IndexedSlices, or None),
one for each element in `sources`. Returned structure is the same as
the structure of `sources`.



#### Raises:


* <b>`RuntimeError`</b>: if called inside the context of the tape, or if called more
 than once on a non-persistent tape.
* <b>`ValueError`</b>: if the target is a variable or if unconnected gradients is
 called with an unknown value.

<h3 id="jacobian"><code>jacobian</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L1022-L1124">View source</a>

``` python
jacobian(
    target,
    sources,
    unconnected_gradients=tf.UnconnectedGradients.NONE,
    parallel_iterations=None,
    experimental_use_pfor=True
)
```

Computes the jacobian using operations recorded in context of this tape.

See [wikipedia article](http://en.wikipedia.org/wiki/jacobian_matrix_and_determinant) for the
definition of a Jacobian.

#### Example usage:



```python
with tf.GradientTape() as g:
  x  = tf.constant([1.0, 2.0])
  g.watch(x)
  y = x * x
jacobian = g.jacobian(y, x)
# jacobian value is [[2., 0.], [0., 4.]]
```

#### Args:


* <b>`target`</b>: Tensor to be differentiated.
* <b>`sources`</b>: a list or nested structure of Tensors or Variables. `target`
  will be differentiated against elements in `sources`.
* <b>`unconnected_gradients`</b>: a value which can either hold 'none' or 'zero' and
  alters the value which will be returned if the target and sources are
  unconnected. The possible values and effects are detailed in
  'UnconnectedGradients' and it defaults to 'none'.
* <b>`parallel_iterations`</b>: A knob to control how many iterations are dispatched
  in parallel. This knob can be used to control the total memory usage.
* <b>`experimental_use_pfor`</b>: If true, vectorizes the jacobian computation. Else
  falls back to a sequential while_loop. Vectorization can sometimes fail
  or lead to excessive memory usage. This option can be used to disable
  vectorization in such cases.


#### Returns:

A list or nested structure of Tensors (or None), one for each element in
`sources`. Returned structure is the same as the structure of `sources`.
Note if any gradient is sparse (IndexedSlices), jacobian function
currently makes it dense and returns a Tensor instead. This may change in
the future.




#### Raises:


* <b>`RuntimeError`</b>: If called on a non-persistent tape with eager execution
  enabled and without enabling experimental_use_pfor.
* <b>`ValueError`</b>: If vectorization of jacobian computation fails.

<h3 id="reset"><code>reset</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L895-L929">View source</a>

``` python
reset()
```

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L863-L893">View source</a>

``` python
stop_recording()
```

Temporarily stops recording operations on this tape.

Operations executed while this context manager is active will not be
recorded on the tape. This is useful for reducing the memory used by tracing
all computations.

#### For example:



```
  with tf.GradientTape(persistent=True) as t:
    loss = compute_loss(model)
    with t.stop_recording():
      # The gradient computation below is not traced, saving memory.
      grads = t.gradient(loss, model.variables)
```

#### Yields:

None


#### Raises:


* <b>`RuntimeError`</b>: if the tape is not currently recording.

<h3 id="watch"><code>watch</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L837-L861">View source</a>

``` python
watch(tensor)
```

Ensures that `tensor` is being traced by this tape.


#### Args:


* <b>`tensor`</b>: a Tensor or list of Tensors.


#### Raises:


* <b>`ValueError`</b>: if it encounters something that is not a tensor.

<h3 id="watched_variables"><code>watched_variables</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/eager/backprop.py#L931-L933">View source</a>

``` python
watched_variables()
```

Returns variables watched by this tape in order of construction.
