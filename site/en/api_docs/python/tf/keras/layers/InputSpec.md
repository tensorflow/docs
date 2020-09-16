description: Specifies the rank, dtype and shape of every input to a layer.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.InputSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.layers.InputSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/input_spec.py#L34-L106">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Specifies the rank, dtype and shape of every input to a layer.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.layers.InputSpec`, `tf.compat.v1.layers.InputSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.layers.InputSpec(
    dtype=None, shape=None, ndim=None, max_ndim=None, min_ndim=None, axes=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Layers can expose (if appropriate) an `input_spec` attribute:
an instance of `InputSpec`, or a nested structure of `InputSpec` instances
(one per input tensor). These objects enable the layer to run input
compatibility checks for input structure, input rank, input shape, and
input dtype.

A None entry in a shape is compatible with any dimension,
a None shape is compatible with any shape.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`dtype`
</td>
<td>
Expected DataType of the input.
</td>
</tr><tr>
<td>
`shape`
</td>
<td>
Shape tuple, expected shape of the input
(may include None for unchecked axes).
</td>
</tr><tr>
<td>
`ndim`
</td>
<td>
Integer, expected rank of the input.
</td>
</tr><tr>
<td>
`max_ndim`
</td>
<td>
Integer, maximum rank of the input.
</td>
</tr><tr>
<td>
`min_ndim`
</td>
<td>
Integer, minimum rank of the input.
</td>
</tr><tr>
<td>
`axes`
</td>
<td>
Dictionary mapping integer axes to
a specific dimension value.
</td>
</tr>
</table>



## Methods

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/input_spec.py#L104-L106">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_config(
    config
)
</code></pre>




<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/engine/input_spec.py#L95-L102">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_config()
</code></pre>






