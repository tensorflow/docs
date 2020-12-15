description: Base class for all TensorFlow decorators.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.tf_decorator.TFDecorator" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.flags.tf_decorator.TFDecorator

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/util/tf_decorator.py#L229-L280">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Base class for all TensorFlow decorators.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.app.flags.tf_decorator.TFDecorator`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.flags.tf_decorator.TFDecorator(
    decorator_name, target, decorator_doc='', decorator_argspec=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

TFDecorator captures and exposes the wrapped target, and provides details
about the current decorator.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`decorated_target`
</td>
<td>

</td>
</tr><tr>
<td>
`decorator_argspec`
</td>
<td>

</td>
</tr><tr>
<td>
`decorator_doc`
</td>
<td>

</td>
</tr><tr>
<td>
`decorator_name`
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/util/tf_decorator.py#L259-L260">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__call__(
    *args, **kwargs
)
</code></pre>

Call self as a function.




