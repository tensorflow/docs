description: Replication mode for input function.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.InputReplicationMode" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="PER_REPLICA"/>
<meta itemprop="property" content="PER_WORKER"/>
</div>

# tf.distribute.InputReplicationMode

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/distribute_lib.py#L437-L450">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Replication mode for input function.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.InputReplicationMode`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

* `PER_WORKER`: The input function will be called on each worker
  independently, creating as many input pipelines as number of workers.
  Replicas will dequeue from the local Dataset on their worker.
  <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> doesn't manage any state sharing between such
  separate input pipelines.
* `PER_REPLICA`: The input function will be called on each replica seperately.
  <a href="../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> doesn't manage any state sharing between such
  separate input pipelines.

## Class Variables

* `PER_REPLICA` <a id="PER_REPLICA"></a>
* `PER_WORKER` <a id="PER_WORKER"></a>
