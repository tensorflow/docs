page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.split_dependency

``` python
tf.contrib.checkpoint.split_dependency(
    component_names,
    component_dtypes,
    fill_save_buffer_fn,
    consume_restore_buffer_fn
)
```



Defined in [`tensorflow/contrib/checkpoint/python/split_dependency.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/checkpoint/python/split_dependency.py).

Creates multiple dependencies with a synchronized save/restore.

Useful when a single op produces `Tensor`s which should each be saved under
different objects, or when `Tensor`s saved with many different objects need to
be restored together as inputs to a single op (i.e. an object which uses a
single fused op may be swapped out for a subgraph of objects, and these two
programs are checkpoint compatible).

#### Args:

* <b>`component_names`</b>: A sequence of names for the split
    dependencies. `fill_save_buffer_fn` must add these keys to the dictionary
    it is passed, and `consume_restore_buffer_fn` will receive a dictionary
    with these keys.
* <b>`component_dtypes`</b>: Data types for the `Tensor`s being saved and restored, a
    sequence corresponding to `component_names`.
* <b>`fill_save_buffer_fn`</b>: A function which takes an empty dictionary as an
    argument and adds `Tensor`s with `component_names` as keys. These
    `Tensor`s will be saved as if they were individual variables.
* <b>`consume_restore_buffer_fn`</b>: A function which takes a dictionary with
    `component_names` as keys mapping to restored individual `Tensor`s and
    returns a restore op (or if executing eagerly, runs the restoration and
    may return `None`).


#### Returns:

A dictionary mapping from names to Checkpointable objects. If one is
reachable from an object as a dependency, the others should be too; adding
dependencies on some but not all of the objects will result in errors.