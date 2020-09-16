description: Specification of target device.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.TargetSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.lite.TargetSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/lite/python/lite.py#L157-L178">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Specification of target device.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lite.TargetSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lite.TargetSpec(
    supported_ops=None, supported_types=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Details about target device. Converter optimizes the generated model for
specific device.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`supported_ops`
</td>
<td>
Experimental flag, subject to change. Set of OpsSet options
supported by the device. (default set([OpsSet.TFLITE_BUILTINS]))
</td>
</tr><tr>
<td>
`supported_types`
</td>
<td>
List of types for constant values on the target device.
Supported values are types exported by lite.constants. Frequently, an
optimization choice is driven by the most compact (i.e. smallest) type in
this list (default [constants.FLOAT])
</td>
</tr>
</table>



