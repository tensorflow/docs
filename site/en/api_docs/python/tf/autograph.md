page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.autograph





Conversion of plain Python into TensorFlow graph code.

NOTE: In TensorFlow 2.0, AutoGraph is automatically applied when using
`tf.function`. This module contains lower-level APIs for advanced use.

For more information, see the
[AutoGraph guide](https://www.tensorflow.org/guide/autograph).

By equivalent graph code we mean code that generates a TensorFlow graph when
run. The generated graph has the same effects as the original code when executed
(for example with `tf.function` or `tf.compat.v1.Session.run`). In other words,
using AutoGraph can be thought of as running Python in TensorFlow.

## Modules

[`experimental`](../tf/autograph/experimental) module: Public API for tf.autograph.experimental namespace.

## Functions

[`to_code(...)`](../tf/autograph/to_code): Similar to `to_graph`, but returns Python source code as a string.

[`to_graph(...)`](../tf/autograph/to_graph): Converts a Python entity into a TensorFlow graph.

