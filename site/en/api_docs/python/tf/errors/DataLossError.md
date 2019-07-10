page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.errors.DataLossError

## Class `DataLossError`

Raised when unrecoverable data loss or corruption is encountered.

Inherits From: [`OpError`](../../tf/errors/OpError)

### Aliases:

* Class `tf.compat.v1.errors.DataLossError`
* Class `tf.compat.v2.errors.DataLossError`
* Class `tf.errors.DataLossError`



Defined in [`python/framework/errors_impl.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/framework/errors_impl.py).

<!-- Placeholder for "Used in" -->

For example, this may be raised by running a
<a href="../../tf/WholeFileReader#read"><code>tf.WholeFileReader.read</code></a>
operation, if the file is truncated while it is being read.


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    node_def,
    op,
    message
)
```

Creates a `DataLossError`.




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
<a href="../../tf/Operation"><code>tf.Operation</code></a>
object.  In that case, this will return `None`, and you should
instead use the <a href="../../tf/errors/OpError#node_def"><code>tf.errors.OpError.node_def</code></a> to
discover information about the op.

#### Returns:

The `Operation` that failed, or None.




