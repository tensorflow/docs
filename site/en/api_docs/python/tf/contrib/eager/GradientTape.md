

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.eager.GradientTape

## Class `GradientTape`





Defined in [`tensorflow/python/eager/backprop.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/eager/backprop.py).

Records operations to use to compute gradients.

Operations are recorded if:
  - they happen in code marked by this context manager
  - at least one of their inputs is being watched

Outputs of recorded operations are watched. Variables are automatically
watched and tensors can be manually watched by calling the watch method on the
context manager.

Example usage:

```python
with tfe.GradientTape() as g:
  x = tf.constant(3.0)
  g.watch(x)
  y = x * x
grad = g.gradient(y, [x])[0]
assert grad.numpy() == 6.0
```

It is possible to use GradientTapes to compute higher-order derivatives as
follows:

```python
with tfe.GradientTape() as g:
  x = tf.constant(3.0)
  g.watch(x)
  y = x * x
  with tfe.GradientTape() as gg:
    gg.watch(y)
    z = 2 * y
  inner_grad = gg.gradient(z, [y])[0]
  assert inner_grad.numpy() == 2
  y = y + inner_grad
grad = g.gradient(y, [x])[0]
assert grad.numpy() == 6.0
```

By default, the resources held by a GradientTape are released as soon as
GradientTape.gradient() method is called. However, if one need to compute
multiple gradients over the same computation, she can create a persistent
GradientTape. Persistent tapes allow multiple calls to the gradient() method
and release resources when the tape object is destructed.

Example usage:

```python
with tfe.GradientTape(persistent=True) as g:
  x = tf.constant(3.0)
  g.watch(x)
  y = x * x
  z = y * y
dz_dx = g.gradient(z, [x])[0]
assert dz_dx.numpy() == 108.0   # 4*x^3 at x = 3
dy_dx = g.gradient(y, [x])[0]
assert dy_dx.numpy() == 6.0
del g  # Drop the reference to the tape

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(persistent=False)
```

Creates a new GradientTape.

#### Args:

* <b>`persistent`</b>: Boolean controlling whether a persistent gradient tape
    is created. Must be True or False.

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
    sources
)
```

Computes the gradient using information traced by the tape.

#### Args:

* <b>`target`</b>: the tensor to be differentiated.
* <b>`sources`</b>: a list of Tensors or Variables, the target will be
   differentiated with respect to the sources.


#### Returns:

a list of Tensors (or IndexedSlices, or None), one for each element in
`sources`.


#### Raises:

* <b>`RuntimeError`</b>: if called inside the context of the tape, or if called more
   than once.

<h3 id="watch"><code>watch</code></h3>

``` python
watch(tensor)
```

Ensures that `tensor` is being traced by this tape.

#### Args:

* <b>`tensor`</b>: a Tensor or Variable a list of Tensors or Variables.



