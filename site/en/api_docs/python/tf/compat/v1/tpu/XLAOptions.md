description: XLA compilation options.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.XLAOptions" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="use_spmd_for_xla_partitioning"/>
</div>

# tf.compat.v1.tpu.XLAOptions

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/tpu/tpu.py#L848-L861">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



XLA compilation options.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.XLAOptions(
    use_spmd_for_xla_partitioning=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`use_spmd_for_xla_partitioning`
</td>
<td>
Boolean. Whether to use XLA's SPMD
partitioner instead of MPMD partitioner when compiler partitioning is
requested.
</td>
</tr>
</table>



## Class Variables

* `use_spmd_for_xla_partitioning` <a id="use_spmd_for_xla_partitioning"></a>
