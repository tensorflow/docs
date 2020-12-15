description: A container that holds a list of values, one value per worker.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental.coordinator.PerWorkerValues" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.distribute.experimental.coordinator.PerWorkerValues

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/coordinator/cluster_coordinator.py#L290-L308">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A container that holds a list of values, one value per worker.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.experimental.coordinator.PerWorkerValues(
    values
)
</code></pre>



<!-- Placeholder for "Used in" -->

<a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a> contains a collection
of values, where each of the value is located one worker respectively, and
upon being used as one of the `args` or `kwargs` of
<a href="../../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md#schedule"><code>tf.distribute.experimental.coordinator.ClusterCoordinator.schedule()</code></a>, the
value specific to a worker will be passed into the function being executed at
that particular worker.

Currently, the only supported path to create an object of
<a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a> is through calling
`iter` on a <a href="../../../../tf/distribute/experimental/coordinator/ClusterCoordinator.md#create_per_worker_dataset"><code>ClusterCoordinator.create_per_worker_dataset</code></a>-returned
distributed dataset instance. The mechanism to create a custom
<a href="../../../../tf/distribute/experimental/coordinator/PerWorkerValues.md"><code>tf.distribute.experimental.coordinator.PerWorkerValues</code></a> is not yet supported.

