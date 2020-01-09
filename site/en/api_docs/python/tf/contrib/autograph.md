page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.autograph


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/autograph/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



This is the legacy module for AutoGraph, kept for backward compatibility.

<!-- Placeholder for "Used in" -->

New users should instead use `tensorflow.python.autograph`.

## Classes

[`class AutoGraphError`](../../tf/contrib/autograph/AutoGraphError): Base class for all AutoGraph exceptions.

[`class ConversionOptions`](../../tf/contrib/autograph/ConversionOptions): Immutable container for global conversion flags.

[`class Feature`](../../tf/autograph/experimental/Feature): This enumeration represents optional conversion options.

[`class StackTraceMapper`](../../tf/contrib/autograph/StackTraceMapper): Remaps generated code to code it originated from.

## Functions

[`convert(...)`](../../tf/contrib/autograph/convert): Decorator that compiles a function to use TensorFlow ops.

[`converted_call(...)`](../../tf/contrib/autograph/converted_call): Compiles a function call inline.

[`do_not_convert(...)`](../../tf/autograph/experimental/do_not_convert): Decorator that suppresses the conversion of a function.

[`set_element_type(...)`](../../tf/contrib/autograph/set_element_type): Indicates that the entity is expected hold items of specified type/shape.

[`stack(...)`](../../tf/contrib/autograph/stack): Stacks the input, if it admits the notion of stacking.

[`to_code(...)`](../../tf/compat/v2/autograph/to_code): Similar to `to_graph`, but returns Python source code as a string.

[`to_graph(...)`](../../tf/compat/v2/autograph/to_graph): Converts a Python entity into a TensorFlow graph.
