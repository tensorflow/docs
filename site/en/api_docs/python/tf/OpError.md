

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.OpError

## Class `OpError`



### Aliases:

* Class `tf.OpError`
* Class `tf.errors.OpError`



Defined in [`tensorflow/python/framework/errors_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/framework/errors_impl.py).

See the guide: [Running Graphs > Error classes and convenience functions](../../../api_guides/python/client#Error_classes_and_convenience_functions)

A generic error that is raised when TensorFlow execution fails.

Whenever possible, the session will raise a more specific subclass
of `OpError` from the `tf.errors` module.

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
<a href="../tf/Operation"><code>tf.Operation</code></a>
object.  In that case, this will return `None`, and you should
instead use the <a href="../tf/OpError#node_def"><code>tf.OpError.node_def</code></a> to
discover information about the op.

#### Returns:

The `Operation` that failed, or None.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    node_def,
    op,
    message,
    error_code
)
```

Creates a new `OpError` indicating that a particular op failed.

#### Args:

* <b>`node_def`</b>: The `node_def_pb2.NodeDef` proto representing the op that
    failed, if known; otherwise None.
* <b>`op`</b>: The `ops.Operation` that failed, if known; otherwise None.
* <b>`message`</b>: The message string describing the failure.
* <b>`error_code`</b>: The `error_codes_pb2.Code` describing the error.



