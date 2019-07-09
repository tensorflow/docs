page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.checkpoint.CheckpointableBase

## Class `CheckpointableBase`





Defined in [`tensorflow/python/training/checkpointable/base.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/training/checkpointable/base.py).

Base class for `Checkpointable` objects without automatic dependencies.

This class has no __setattr__ override for performance reasons. Dependencies
must be added explicitly. Unless attribute assignment is performance-critical,
use `Checkpointable` instead. Use `CheckpointableBase` for `isinstance`
checks.

