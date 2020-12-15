description: Options for loading a SavedModel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.saved_model.LoadOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="experimental_io_device"/>
</div>

# tf.saved_model.LoadOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/saved_model/load_options.py#L25-L57">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Options for loading a SavedModel.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.saved_model.LoadOptions(
    experimental_io_device=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function may be used in the `options` argument in functions that
load a SavedModel (<a href="../../tf/saved_model/load.md"><code>tf.saved_model.load</code></a>, <a href="../../tf/keras/models/load_model.md"><code>tf.keras.models.load_model</code></a>).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`experimental_io_device`
</td>
<td>
string. Applies in a distributed setting.
Tensorflow device to use to access the filesystem. If `None` (default)
then for each variable the filesystem is accessed from the CPU:0 device
of the host where that variable is assigned. If specified, the
filesystem is instead accessed from that device for all variables.
This is for example useful if you want to load from a local directory,
such as "/tmp" when running in a distributed setting. In that case
pass a device for the host where the "/tmp" directory is accessible.
</td>
</tr>
</table>



## Class Variables

* `experimental_io_device` <a id="experimental_io_device"></a>
