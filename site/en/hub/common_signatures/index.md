
# Common Signatures for TF Hub Modules

## Introduction

[TensorFlow Hub](https://tfhub.dev) hosts models for a variety of tasks. Models
for the same task are encouraged to implement a common API so that model
consumers can easily exchange them without modifying the code that uses them,
even if they come from different publishers.

The goal is to make exchanging different models for the same task as simple as
switching a string-valued hyperparameter. With that, model consumers can easily
find the best one for their problem.

This directory collects specifications of common signatures for modules in the
[TF1 Hub format](../tf1_hub_module.md).

Note that the TF1 Hub format has been **deprecated** in favor of the
[TF2 SavedModel format](../tf2_saved_model.md) and its
[Common SavedModel APIs](../common_saved_model_apis/index.md).

## Signatures

*   [Image Signatures](images.md)
*   [Text Signatures](text.md)
