description: An error is raised for unsupported operator in Graph execution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.errors.OperatorNotAllowedInGraphError" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
</div>

# tf.errors.OperatorNotAllowedInGraphError

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/framework/errors_impl.py#L52-L58">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An error is raised for unsupported operator in Graph execution.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.errors.OperatorNotAllowedInGraphError(
    *args, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->

For example, using a <a href="../../tf/Tensor.md"><code>tf.Tensor</code></a> as a Python `bool` in Graph execution
is not allowed.

