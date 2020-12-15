description: Adds a QueueRunner to a collection in the graph. (deprecated)

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.add_queue_runner" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.add_queue_runner

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/queue_runner_impl.py#L394-L411">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Adds a `QueueRunner` to a collection in the graph. (deprecated)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.queue_runner.add_queue_runner`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.train.add_queue_runner(
    qr, collection=tf.GraphKeys.QUEUE_RUNNERS
)
</code></pre>



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
To construct input pipelines, use the <a href="../../../../tf/data.md"><code>tf.data</code></a> module.

When building a complex model that uses many queues it is often difficult to
gather all the queue runners that need to be run.  This convenience function
allows you to add a queue runner to a well known collection in the graph.

The companion method `start_queue_runners()` can be used to start threads for
all the collected queue runners.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`qr`
</td>
<td>
A `QueueRunner`.
</td>
</tr><tr>
<td>
`collection`
</td>
<td>
A `GraphKey` specifying the graph collection to add
the queue runner to.  Defaults to `GraphKeys.QUEUE_RUNNERS`.
</td>
</tr>
</table>

