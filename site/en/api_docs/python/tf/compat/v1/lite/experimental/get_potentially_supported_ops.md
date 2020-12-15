description: Returns operations potentially supported by TensorFlow Lite.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.lite.experimental.get_potentially_supported_ops" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.lite.experimental.get_potentially_supported_ops

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/experimental/tensorboard/ops_util.py#L34-L50">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Returns operations potentially supported by TensorFlow Lite.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.lite.experimental.get_potentially_supported_ops()
</code></pre>



<!-- Placeholder for "Used in" -->

The potentially support list contains a list of ops that are partially or
fully supported, which is derived by simply scanning op names to check whether
they can be handled without real conversion and specific parameters.

Given that some ops may be partially supported, the optimal way to determine
if a model's operations are supported is by converting using the TensorFlow
Lite converter.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of SupportedOp.
</td>
</tr>

</table>

