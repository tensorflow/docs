

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.GradientTape

## Class `GradientTape`



### Aliases:

* Class `tf.GradientTape`
* Class `tf.contrib.eager.GradientTape`



Defined in [`tensorflow/python/eager/backprop.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/eager/backprop.py).

Record operations for automatic differentiation.

Operations are recorded if they are executed within this context manager and
at least one of their inputs is being "watched".

Trainable variables (created by <a href="../tf/contrib/eager/Variable"><code>tf.contrib.eager.Variable</code></a> or
<a href="../tf/get_variable"><code>tf.get_variable</code></a>, trainable=True is default in both cases) are automatically
watched. Tensors can be manually watched by invoking the `watch` method on
this context manager.

For example, consider the function `y = x * x`. The gradient at `x = 3.0` can
be computed as:

```python
x = tf.constant(3.)
with tfe.GradientTape() as g:
  g.watch(x)
  y = x * x
grad = g.gradient(y, [x])[0] # Will compute to 6.0
```

GradientTapes can be nested to compute higher-order derivatives. For example,

```python
x = tf.constant(3.0)
with tfe.GradientTape() as g:
  with tfe.GradientTape() as gg:
    gg.watch(x)
    y = x * x
  dy_dx = gg.gradient(y, [x])[0]     # Will compute to 6.0
d2y_dx2 = g.gradient(dy_dx, [x])[0]  # Will compute to 2.0
```

By default, the resources held by a GradientTape are released as soon as
GradientTape.gradient() method is called. To compute multiple gradients over
the same computation, create a persistent gradient tape. This allows multiple
calls to the gradient() method as resources are released when the tape object
is garbage collected. For example:

```python
x = tf.constant(3.0)
with tfe.GradientTape(persistent=True) as g:
  g.watch(x)
  y = x * x
  z = y * y
dy_dx = g.gradient(z, [x])[0]  # 6.0
dz_dx = g.gradient(y, [x])[0]  # 108.0 (4*x^3 at x = 3)
del g  # Drop the reference to the tape

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(persistent=False)
```

Creates a new GradientTape.

#### Args:

* <b>`persistent`</b>: Boolean controlling whether a persistent gradient tape
    is created. False by default, which means at most one call can
    be made to the gradient() method on this object.

<h3 id="__enter__"><code>__enter__</code></h3>

``` python
__enter__()
```



<h3 id="__exit__"><code>__exit__</code></h3>

``` python
__exit__(
    typ,
    value,
    traceback
)
```



<h3 id="gradient"><code>gradient</code></h3>

``` python
gradient(
    target,
    sources,
    output_gradients=None
)
```

Computes the gradient using operations recorded in context of this tape.

#### Args:

* <b>`target`</b>: Tensor to be differentiated.
* <b>`sources`</b>: a list or nested structure of Tensors or Variables. `target`
    will be differentiated against elements in `sources`.
* <b>`output_gradients`</b>: a list of gradients, one for each element of
    target. Defaults to None.


#### Returns:

a list or nested structure of Tensors (or IndexedSlices, or None),
one for each element in `sources`. Returned structure is the same as
the structure of `sources`.


#### Raises:

* <b>`RuntimeError`</b>: if called inside the context of the tape, or if called more
   than once on a non-persistent tape.

<h3 id="watch"><code>watch</code></h3>

``` python
watch(tensor)
```

Ensures that `tensor` is being traced by this tape.

#### Args:

* <b>`tensor`</b>: a Tensor or list of Tensors.

<h3 id="watched_variables"><code>watched_variables</code></h3>

``` python
watched_variables()
```





