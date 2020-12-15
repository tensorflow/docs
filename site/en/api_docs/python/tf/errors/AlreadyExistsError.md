description: Raised when an entity that we attempted to create already exists.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.errors.AlreadyExistsError" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.errors.AlreadyExistsError

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/errors_impl.py#L309-L323">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Raised when an entity that we attempted to create already exists.

Inherits From: [`OpError`](../../tf/errors/OpError.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.errors.AlreadyExistsError`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.errors.AlreadyExistsError(
    node_def, op, message
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, running an operation that saves a file
(e.g. `tf.train.Saver.save`)
could potentially raise this exception if an explicit filename for an
existing file was passed.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`error_code`
</td>
<td>
The integer error code that describes the error.
</td>
</tr><tr>
<td>
`message`
</td>
<td>
The error message that describes the error.
</td>
</tr><tr>
<td>
`node_def`
</td>
<td>
The `NodeDef` proto representing the op that failed.
</td>
</tr><tr>
<td>
`op`
</td>
<td>
The operation that failed, if known.

*N.B.* If the failed op was synthesized at runtime, e.g. a `Send`
or `Recv` op, there will be no corresponding
<a href="../../tf/Operation.md"><code>tf.Operation</code></a>
object.  In that case, this will return `None`, and you should
instead use the <a href="../../tf/errors/OpError.md#node_def"><code>tf.errors.OpError.node_def</code></a> to
discover information about the op.
</td>
</tr>
</table>



