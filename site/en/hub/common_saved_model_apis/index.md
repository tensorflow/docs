
# Common SavedModel APIs for TF Hub

## Introduction

[TensorFlow Hub](https://tfhub.dev) hosts models for a variety of tasks. Models
for the same task are encouraged to implement a common API so that model
consumers can easily exchange them without modifying the code that uses them,
even if they come from different publishers.

The goal is to make exchanging different models for the same task as simple as
switching a string-valued hyperparameter. With that, model consumers can easily
find the best one for their problem.

This directory collects specifications of common APIs for models in the
[TF2 SavedModel format](../tf2_saved_model.md). (It replaces the
[Common Signatures](../common_signatures/index.md) for the now-deprecated
[TF1 Hub format](../tf1_hub_module.md).)

## Reusable SavedModel: the common foundation

The [Reusable SavedModel API](../reusable_saved_models.md) defines general
conventions how to load a SavedModel back into a Python program and reuse it as
part of a bigger TensorFlow model.

Basic usage:

```python
obj = hub.load("path/to/model")  # That's tf.saved_model.load() after download.
outputs = obj(inputs, training=False)  # Invokes the tf.function obj.__call__.
```

Key point: This uses the object-based interface to restored SavedModels that was
added in TensorFlow 2, not the SavedModel signatures for serving.

For Keras users, the `hub.KerasLayer` class relies on this API to wrap the
Reusable SavedModel as a Keras Layer (shielding Keras users from its details),
with inputs and outputs according to the task-specific APIs listed below.

## Task-specific APIs

These refine the [Reusable SavedModel API](../reusable_saved_models.md) with
conventions for particular ML tasks and types of data.

*   [Image tasks](images.md)
*   [Text tasks](text.md)
