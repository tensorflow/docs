description: Tests if a variable has been initialized.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.is_variable_initialized" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.is_variable_initialized

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/ops/variables.py#L3328-L3340">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tests if a variable has been initialized.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.is_variable_initialized(
    variable
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`variable`
</td>
<td>
A `Variable`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Returns a scalar boolean Tensor, `True` if the variable has been
initialized, `False` otherwise.
</td>
</tr>

</table>


Note: The output of this function should be used. If it is not, a warning will be logged or an error may be raised. To mark the output as used, call its .mark_used() method.