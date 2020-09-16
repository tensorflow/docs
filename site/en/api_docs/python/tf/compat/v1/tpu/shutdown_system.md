description: Shuts down a running a distributed TPU system.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.tpu.shutdown_system" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.tpu.shutdown_system

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/tpu/tpu.py#L163-L175">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Shuts down a running a distributed TPU system.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.tpu.shutdown_system(
    job=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`job`
</td>
<td>
The job (the XXX in TensorFlow device specification /job:XXX) that
contains the TPU devices that will be shutdown. If job=None it is
assumed there is only one job in the TensorFlow flock, and an error will
be returned if this assumption does not hold.
</td>
</tr>
</table>

