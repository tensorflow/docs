description: Returns the TF session to be used by the backend.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.backend.get_session" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.keras.backend.get_session

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/keras/backend.py#L618-L645">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns the TF session to be used by the backend.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.keras.backend.get_session(
    op_input_list=()
)
</code></pre>



<!-- Placeholder for "Used in" -->

If a default TensorFlow session is available, we will return it.

Else, we will return the global Keras session assuming it matches
the current graph.

If no global Keras session exists at this point:
we will create a new global session.

Note that you can manually set the global session
via `K.set_session(sess)`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`op_input_list`
</td>
<td>
An option sequence of tensors or ops, which will be used
to determine the current graph. Otherwise the default graph will be
used.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A TensorFlow session.
</td>
</tr>

</table>

