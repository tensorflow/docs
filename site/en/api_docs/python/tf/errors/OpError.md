page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.errors.OpError


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/errors/OpError">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/errors_impl.py#L59-L167">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `OpError`

A generic error that is raised when TensorFlow execution fails.



### Aliases:

* Class <a href="/api_docs/python/tf/errors/OpError"><code>tf.OpError</code></a>
* Class <a href="/api_docs/python/tf/errors/OpError"><code>tf.compat.v1.OpError</code></a>
* Class <a href="/api_docs/python/tf/errors/OpError"><code>tf.compat.v1.errors.OpError</code></a>
* Class <a href="/api_docs/python/tf/errors/OpError"><code>tf.compat.v2.errors.OpError</code></a>


<!-- Placeholder for "Used in" -->

Whenever possible, the session will raise a more specific subclass
of `OpError` from the <a href="../../tf/errors"><code>tf.errors</code></a> module.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/errors_impl.py#L66-L80">View source</a>

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
