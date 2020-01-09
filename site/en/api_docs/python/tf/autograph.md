page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.autograph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/autograph">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Conversion of plain Python into TensorFlow graph code.

<!-- Placeholder for "Used in" -->

NOTE: In TensorFlow 2.0, AutoGraph is automatically applied when using
<a href="../tf/function"><code>tf.function</code></a>. This module contains lower-level APIs for advanced use.

For more information, see the
[AutoGraph guide](https://www.tensorflow.org/guide/autograph).

By equivalent graph code we mean code that generates a TensorFlow graph when
run. The generated graph has the same effects as the original code when executed
(for example with <a href="../tf/function"><code>tf.function</code></a> or <a href="../tf/Session#run"><code>tf.compat.v1.Session.run</code></a>). In other words,
using AutoGraph can be thought of as running Python in TensorFlow.

## Modules

[`experimental`](../tf/autograph/experimental) module: Public API for tf.autograph.experimental namespace.

## Functions

[`set_verbosity(...)`](../tf/autograph/set_verbosity): Sets the AutoGraph verbosity level.

[`to_code(...)`](../tf/autograph/to_code): Similar to `to_graph`, but returns Python source code as a string.

[`to_graph(...)`](../tf/autograph/to_graph): Converts a Python entity into a TensorFlow graph.

[`trace(...)`](../tf/autograph/trace): Traces argument information at compilation time.
