page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.NumpyState

## Class `NumpyState`

Inherits From: [`CheckpointableBase`](../../../tf/contrib/checkpoint/CheckpointableBase)



Defined in [`tensorflow/contrib/checkpoint/python/python_state.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/checkpoint/python/python_state.py).

A checkpointable object whose NumPy array attributes are saved/restored.

Example usage:

```python
arrays = tf.contrib.checkpoint.NumpyState()
checkpoint = tf.train.Checkpoint(numpy_arrays=arrays)
arrays.x = numpy.zeros([3, 4])
save_path = checkpoint.save("/tmp/ckpt")
arrays.x[1, 1] = 4.
checkpoint.restore(save_path)
assert (arrays.x == numpy.zeros([3, 4])).all()

second_checkpoint = tf.train.Checkpoint(
    numpy_arrays=tf.contrib.checkpoint.NumpyState())
# Attributes of NumpyState objects are created automatically by restore()
second_checkpoint.restore(save_path)
assert (second_checkpoint.numpy_arrays.x == numpy.zeros([3, 4])).all()
```

Note that `NumpyState` objects re-create the attributes of the previously
saved object on `restore()`. This is in contrast to TensorFlow variables, for
which a `Variable` object must be created and assigned to an attribute.

This snippet works both when graph building and when executing eagerly. On
save, the NumPy array(s) are fed as strings to be saved in the checkpoint (via
a placeholder when graph building, or as a string constant when executing
eagerly). When restoring they skip the TensorFlow graph entirely, and so no
restore ops need be run. This means that restoration always happens eagerly,
rather than waiting for `checkpoint.restore(...).run_restore_ops()` like
TensorFlow variables when graph building.

## Methods

<h3 id="__getattribute__"><code>__getattribute__</code></h3>

``` python
__getattribute__(name)
```

Un-wrap `_NumpyWrapper` objects when accessing attributes.

<h3 id="__setattr__"><code>__setattr__</code></h3>

``` python
__setattr__(
    name,
    value
)
```

Automatically wrap NumPy arrays assigned to attributes.



