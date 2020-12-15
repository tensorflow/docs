description: Representative dataset to evaluate optimizations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.lite.RepresentativeDataset" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.lite.RepresentativeDataset

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/lite/python/lite.py#L134-L152">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Representative dataset to evaluate optimizations.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.lite.RepresentativeDataset`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.lite.RepresentativeDataset(
    input_gen
)
</code></pre>



<!-- Placeholder for "Used in" -->

A representative dataset that can be used to evaluate optimizations by the
converter. E.g. converter can use these examples to estimate (min, max) ranges
by calibrating the model on inputs. This can allow converter to quantize a
converted floating point model.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`input_gen`
</td>
<td>
an input generator that can be used to generate input samples
for the model. This must be a callable object that returns an object
that supports the `iter()` protocol (e.g. a generator function). The
elements generated must have same type and shape as inputs to the model.
</td>
</tr>
</table>



