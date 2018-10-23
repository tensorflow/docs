

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.errors.NotFoundError

## Class `NotFoundError`

Inherits From: [`OpError`](../../tf/OpError)



Defined in [`tensorflow/python/framework/errors_impl.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/framework/errors_impl.py).

See the guide: [Running Graphs > Error classes and convenience functions](../../../../api_guides/python/client#Error_classes_and_convenience_functions)

Raised when a requested entity (e.g., a file or directory) was not found.

For example, running the
[`tf.WholeFileReader.read`](../../tf/WholeFileReader#read)
operation could raise `NotFoundError` if it receives the name of a file that
does not exist.


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

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    node_def,
    op,
    message
)
```

Creates a `NotFoundError`.



