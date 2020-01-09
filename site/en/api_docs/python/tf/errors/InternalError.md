page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.errors.InternalError


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/errors/InternalError">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/errors_impl.py#L445-L456">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `InternalError`

Raised when the system experiences an internal error.

Inherits From: [`OpError`](../../tf/errors/OpError)

### Aliases:

* Class <a href="/api_docs/python/tf/errors/InternalError"><code>tf.compat.v1.errors.InternalError</code></a>
* Class <a href="/api_docs/python/tf/errors/InternalError"><code>tf.compat.v2.errors.InternalError</code></a>


<!-- Placeholder for "Used in" -->

This exception is raised when some invariant expected by the runtime
has been broken. Catching this exception is not recommended.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/errors_impl.py#L454-L456">View source</a>

``` python
__init__(
    node_def,
    op,
    message
)
```

Creates an `InternalError`.




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
