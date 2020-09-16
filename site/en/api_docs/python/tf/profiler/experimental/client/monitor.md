description: Sends grpc requests to profiler server to perform on-demand monitoring.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.profiler.experimental.client.monitor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.profiler.experimental.client.monitor

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/profiler/profiler_client.py#L94-L121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Sends grpc requests to profiler server to perform on-demand monitoring.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.profiler.experimental.client.monitor(
    service_addr, duration_ms, level=1
)
</code></pre>



<!-- Placeholder for "Used in" -->

The monitoring result is a light weight performance summary of your model
execution. This method will block the caller thread until it receives the
monitoring result. This method currently supports Cloud TPU only.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`service_addr`
</td>
<td>
gRPC address of profiler service e.g. grpc://10.0.0.2:8466.
</td>
</tr><tr>
<td>
`duration_ms`
</td>
<td>
Duration of monitoring in ms.
</td>
</tr><tr>
<td>
`level`
</td>
<td>
Choose a monitoring level between 1 and 2 to monitor your job. Level
2 is more verbose than level 1 and shows more metrics.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A string of monitoring output.
</td>
</tr>

</table>



#### Example usage:


# Continuously send gRPC requests to the Cloud TPU to monitor the model
# execution.
```python
for query in range(0, 100):
  print(tf.profiler.experimental.client.monitor('grpc://10.0.0.2:8466', 1000))