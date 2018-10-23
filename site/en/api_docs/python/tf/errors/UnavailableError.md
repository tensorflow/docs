


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.errors.UnavailableError

### `class tf.errors.UnavailableError`

See the guide: [Running Graphs > Error classes and convenience functions](../../../../api_guides/python/client#Error_classes_and_convenience_functions)

Raised when the runtime is currently unavailable.

This exception is not currently used.


## Properties

<h3 id="error_code"><code>error_code</code></h3>

The integer error code that describes the error.

<h3 id="message"><code>message</code></h3>

The error message that describes the error.

<h3 id="node_def"><code>node_def</code></h3>

The `NodeDef` proto representing the op that failed.

<h3 id="op"><code>op</code></h3>

The operation that failed, if known.

*N.B.* If the failed op was synthesized at runtime, e.g. a `Send`
or `Recv` op, there will be no corresponding
[`tf.Operation`](../../tf/Operation)
object.  In that case, this will return `None`, and you should
instead use the [`tf.OpError.node_def`](../../tf/OpError#node_def) to
discover information about the op.

#### Returns:

  The `Operation` that failed, or None.



## Methods

<h3 id="__init__"><code>__init__(node_def, op, message)</code></h3>

Creates an `UnavailableError`.



## Class Members

<h3 id="args"><code>args</code></h3>



Defined in [`tensorflow/python/framework/errors_impl.py`](https://www.tensorflow.org/code/tensorflow/python/framework/errors_impl.py).

