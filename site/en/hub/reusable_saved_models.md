
# Reusable SavedModels

## Introduction

TensorFlow Hub hosts SavedModels for TensorFlow 2, among other assets.
They can be loaded back into a Python program with `obj = hub.load(url)`
[[learn more](tf2_saved_model)]. The returned `obj` is the result
of `tf.saved_model.load()` (see TensorFlow's
[SavedModel guide](https://www.tensorflow.org/guide/saved_model)).
This object can have arbitrary attributes that are tf.functions,
tf.Variables (initialized from their pre-trained values), other resources
and, recursively, more such objects.

This page describes an interface to be implemented by the loaded `obj`
in order to be *reused* in a TensorFlow Python program.
SavedModels conforming to this interface are called *Reusable SavedModels*.

Reusing means building a larger model around `obj`, including the ability
to fine-tune it. Fine-tuning means further training of the weights in the loaded
`obj` as part of the surrounding model. The loss function and the
optimizer are determined by the surrounding model; `obj` only defines
the mapping of input to output activations (the "forward pass"), possibly
including techniques such as dropout or batch normalization.

**The TensorFlow Hub team recommends implementing the Reusable SavedModel
interface** in all SavedModels that are meant to be reused in the above sense.
Many utilities from the `tensorflow_hub` library, notably `hub.KerasLayer`,
require SavedModels to implement it.

### Relation to SignatureDefs

This interface in terms of tf.functions and other TF2 features
is separate from the SavedModel's signatures, which have been
available since TF1 and continue to be used in TF2 for inference
(such as deploying SavedModels to TF Serving or TF Lite).
Signatures for inference are not expressive enough to support fine-tuning,
and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
provides a more natural and expressive
[Python API](https://www.tensorflow.org/tutorials/customization/performance)
for the reused model.

### Relation to model-building libraries

A Reusable SavedModel uses only TensorFlow 2 primitives, independent of any
particular model-building library like Keras or Sonnet. This facilitates reuse
across model-building libraries, free from dependencies on the original
model-building code.

Some amount of adaptation will be needed load Reusable SavedModels into or save
them from any given model-building library. For Keras,
[hub.KerasLayer](https://www.tensorflow.org/hub/api_docs/python/hub/KerasLayer)
provides the loading, and Keras's built-in saving in the SavedModel format has
been redesigned for TF2 with the goal of providing a superset of this interface
(see the
[RFC](https://github.com/tensorflow/community/blob/master/rfcs/20190509-keras-saved-model.md)
from May 2019).

### Relation to task-specific "Common SavedModel APIs"

The interface definition on this page allows for any number and type of inputs
and outputs. The
[Common SavedModel APIs for TF Hub](common_saved_model_apis/index.md) refine
this general interface with usage conventions for specific tasks to make models
easily interchangeable.

## Interface definition

### Attributes

A Reusable SavedModel is a TensorFlow 2 SavedModel such that
`obj = tf.saved_model.load(...)` returns an object that has the following
attributes

  * `__call__`. Required. A tf.function implementing the model's computation
    (the "forward pass") subject to the specification below.

  * `variables`: A list of tf.Variable objects, listing all the variables
    used by any possible invocation of `__call__`, including both
    trainable and non-trainable ones.

    This list can be omitted if empty.

    Note: Conveniently, this name coincides with the attribute synthesized by
    `tf.saved_model.load(...)` when loading a TF1 SavedModel to represent
    its `GLOBAL_VARIABLES` collection.

  * `trainable_variables`: A list of tf.Variable objects such that
    `v.trainable` is true for all elements.
    These variables must be a subset of `variables`.
    These are the variables to be trained when fine-tuning the object.
    The SavedModel creator may choose to omit some variables here that were
    originally trainable to indicate that these should not be modified during
    fine-tuning.

    This list can be omitted if empty, in particular, if the SavedModel does not
    support fine-tuning.

  * `regularization_losses`: A list of tf.functions, each taking zero inputs
    and returning a single scalar float tensor. For fine-tuning, the
    SavedModel user is advised to include these as additional regularization
    terms into the loss (in the simplest case without further scaling).
    Typically, these are used to represent weight regularizers.
    (For lack of inputs, these tf.functions cannot express
    activity regularizers.)

    This list can be omitted if empty, in particular, if the SavedModel does not
    support fine-tuning or does not wish to prescribe weight regularization.

### The `__call__` function

A Restored SavedModel `obj` has an `obj.__call__` attribute that is
a restored tf.function and allows `obj` to be called as follows.

Synopsis (pseudo-code):

```python
outputs = obj(inputs, trainable=..., **kwargs)
```

#### Arguments

The arguments are as follows.

  * There is one positional, required argument with a batch of input activations
    of the SavedModel. Its type is one of

      * a single Tensor for a single input,
      * a list of Tensors for an ordered sequence of unnamed inputs,
      * a dict of Tensors keyed by a particular set of input names.

    (Future revisions of this interface may allow more general nests.)
    The SavedModel creator chooses one of those and the tensor shapes
    and dtypes. Where useful, some dimensions of the shape should be
    undefined (notably batch size).

  * There may be an optional keyword argument `training` that accepts a Python
    boolean, `True` or `False`. The default is `False`.
    If the model supports fine-tuning, and if its computation differs between
    the two (e.g., as in dropout and batch normalization), that distinction
    is implemented with this argument. Otherwise, this argument may be absent.

    It is not required that `__call__` accept a Tensor-valued `training`
    argument. It falls on the caller to use `tf.cond()` if necessary
    to dispatch between them.

  * The SavedModel creator may choose to accept more optional `kwargs`
    of particular names.

      * For Tensor-valued arguments, the SavedModel creator defines their
        permissible dtypes and shapes. `tf.function` accepts a Python default
        value on an argument that is traced with a tf.TensorSpec input.
        Such arguments can be used to allow customization of numeric
        hyperparameters involved in `__call__` (e.g., dropout rate).

      * For Python-valued arguments, the SavedModel creator defines their
        permissible values. Such arguments can be used as flags to make
        discrete choices in the traced function (but mind the combinatorial
        explosion of traces).

The restored `__call__` function must provide traces for all permissible
combinations of arguments. Flipping `training` between `True` and `False`
must not change the permissibility of arguments.

#### Result

The `outputs` from calling `obj` can be

  * a single Tensor for a single output,
  * a list of Tensors for an ordered sequence of unnamed outputs,
  * a dict of Tensors keyed by a particular set of output names.

(Future revisions of this interface may allow more general nests.)
The return type may vary depending on the Python-valued kwargs.
This allows for flags producing extra outputs.
The SavedModel creator defines the output dtypes and shapes and their
dependency on inputs.


### Named callables

A Reusable SavedModel can provide multiple model pieces in the way
described above by putting them into named subobjects, for example,
`obj.foo`, `obj.bar` and so on.
Each subobject provides a `__call__` method and supporting attributes
about the variables etc. specific to that model piece.
For the example above, there would be `obj.foo.__call__`,
`obj.foo.variables` and so on.

Note that this interface does *not* cover the approach of adding
a bare tf.function directly as `tf.foo`.

Users of Reusable SavedModels are only expected to handle one level of nesting
(`obj.bar` but not `obj.bar.baz`). (Future revisions of this interface may allow
deeper nesting, and may waive the requirement that the top-level object be
callable itself.)

## Closing remarks

### Relation to in-process APIs

This document describes an interface of a Python class which consists
of primitives like tf.function and tf.Variable that survive a
round-trip through serialization via `tf.saved_model.save()`
and `tf.saved_model.load()`. However, the interface was already present
on the original object that was passed to `tf.saved_model.save()`.
Adaptation to that interface enables the exchange of model pieces
across model-building APIs within a single TensorFlow program.
