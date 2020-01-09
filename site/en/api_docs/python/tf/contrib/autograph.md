page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.autograph



Defined in [`tensorflow/contrib/autograph/__init__.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/autograph/__init__.py).

This is the legacy module for AutoGraph, kept for backward compatibility.

New users should instead use `tensorflow.python.autograph`.

## Classes

[`class AutographParseError`](../../tf/contrib/autograph/AutographParseError)

[`class ConversionOptions`](../../tf/contrib/autograph/ConversionOptions): Container for conversion flags.

[`class GraphConstructionError`](../../tf/contrib/autograph/GraphConstructionError): Error for graph construction errors from AutoGraph generated code.

[`class RunMode`](../../tf/contrib/autograph/RunMode): Specifies the way a converted function or method should be executed in TF.

[`class TfRuntimeError`](../../tf/contrib/autograph/TfRuntimeError): Error wrapper for runtime errors raised by AutoGraph generated code.

## Functions

[`convert(...)`](../../tf/contrib/autograph/convert): Decorator that compiles a function to use TensorFlow ops.

[`converted_call(...)`](../../tf/contrib/autograph/converted_call): Compiles a function call inline. For internal use only.

[`do_not_convert(...)`](../../tf/contrib/autograph/do_not_convert): Decorator that suppresses the conversion of a function.

[`improved_errors(...)`](../../tf/contrib/autograph/improved_errors): Context manager that rewrites runtime errors.

[`set_element_type(...)`](../../tf/contrib/autograph/set_element_type): Indicates that the entity is expected hold items of specified type/shape.

[`set_loop_options(...)`](../../tf/contrib/autograph/set_loop_options): Specifies additional arguments to be passed to the enclosing while_loop.

[`stack(...)`](../../tf/contrib/autograph/stack): Stacks the input, if it admits the notion of stacking.

[`tensor_list(...)`](../../tf/contrib/autograph/tensor_list): Creates an tensor list and populates it with the given elements.

[`to_code(...)`](../../tf/contrib/autograph/to_code): Returns the equivalent code that uses TensorFlow ops.

[`to_graph(...)`](../../tf/contrib/autograph/to_graph): Converts a Python entity into equivalent code that uses TensorFlow ops.

## Other Members

<h3 id="absolute_import"><code>absolute_import</code></h3>

<h3 id="division"><code>division</code></h3>

<h3 id="print_function"><code>print_function</code></h3>

