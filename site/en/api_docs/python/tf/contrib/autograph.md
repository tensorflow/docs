page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.autograph

This is the legacy module for AutoGraph, kept for backward compatibility.



Defined in [`contrib/autograph/__init__.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/autograph/__init__.py).

<!-- Placeholder for "Used in" -->

New users should instead use `tensorflow.python.autograph`.

## Classes

[`class AutoGraphError`](../../tf/contrib/autograph/AutoGraphError): Base class for all AutoGraph exceptions.

[`class ConversionOptions`](../../tf/contrib/autograph/ConversionOptions): Immutable container for global conversion flags.

[`class Feature`](../../tf/autograph/experimental/Feature): Represents conversion options that can be toggled on or off.

[`class RunMode`](../../tf/contrib/autograph/RunMode): Specifies the way a converted function or method should be executed in TF.

## Functions

[`convert(...)`](../../tf/contrib/autograph/convert): Decorator that compiles a function to use TensorFlow ops.

[`converted_call(...)`](../../tf/contrib/autograph/converted_call): Compiles a function call inline. For internal use only.

[`do_not_convert(...)`](../../tf/contrib/autograph/do_not_convert): Decorator that suppresses the conversion of a function.

[`set_element_type(...)`](../../tf/contrib/autograph/set_element_type): Indicates that the entity is expected hold items of specified type/shape.

[`set_loop_options(...)`](../../tf/autograph/experimental/set_loop_options): Specifies additional arguments to be passed to the enclosing while_loop.

[`stack(...)`](../../tf/contrib/autograph/stack): Stacks the input, if it admits the notion of stacking.

[`to_code(...)`](../../tf/compat/v2/autograph/to_code): Similar to `to_graph`, but returns Python source code as a string.

[`to_graph(...)`](../../tf/compat/v2/autograph/to_graph): Converts a Python entity into a TensorFlow graph.

