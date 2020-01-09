page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.errors.ResourceExhaustedError


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/errors/ResourceExhaustedError">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/errors_impl.py#L356-L368">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ResourceExhaustedError`

Some resource has been exhausted.

Inherits From: [`OpError`](../../tf/errors/OpError)

### Aliases:

* Class <a href="/api_docs/python/tf/errors/ResourceExhaustedError"><code>tf.compat.v1.errors.ResourceExhaustedError</code></a>
* Class <a href="/api_docs/python/tf/errors/ResourceExhaustedError"><code>tf.compat.v2.errors.ResourceExhaustedError</code></a>


<!-- Placeholder for "Used in" -->

For example, this error might be raised if a per-user quota is
exhausted, or perhaps the entire file system is out of space.


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/framework/errors_impl.py#L365-L368">View source</a>

``` python
__init__(
    node_def,
    op,
    message
)
```

Creates a `ResourceExhaustedError`.




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
