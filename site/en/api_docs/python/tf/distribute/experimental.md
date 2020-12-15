description: Public API for tf.distribute.experimental namespace.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.distribute.experimental

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Public API for tf.distribute.experimental namespace.



## Modules

[`coordinator`](../../tf/distribute/experimental/coordinator.md) module: Public API for tf.distribute.experimental.coordinator namespace.

[`partitioners`](../../tf/distribute/experimental/partitioners.md) module: Public API for tf.distribute.experimental.partitioners namespace.

## Classes

[`class CentralStorageStrategy`](../../tf/distribute/experimental/CentralStorageStrategy.md): A one-machine strategy that puts all variables on a single device.

[`class CollectiveCommunication`](../../tf/distribute/experimental/CommunicationImplementation.md): Cross device communication implementation.

[`class CollectiveHints`](../../tf/distribute/experimental/CollectiveHints.md): Hints for collective operations like AllReduce.

[`class CommunicationImplementation`](../../tf/distribute/experimental/CommunicationImplementation.md): Cross device communication implementation.

[`class CommunicationOptions`](../../tf/distribute/experimental/CommunicationOptions.md): Options for cross device communications like All-reduce.

[`class MultiWorkerMirroredStrategy`](../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md): A distribution strategy for synchronous training on multiple workers.

[`class ParameterServerStrategy`](../../tf/distribute/experimental/ParameterServerStrategy.md): An multi-worker tf.distribute strategy with parameter servers.

[`class TPUStrategy`](../../tf/distribute/experimental/TPUStrategy.md): Synchronous training on TPUs and TPU Pods.

[`class ValueContext`](../../tf/distribute/experimental/ValueContext.md): A class wrapping information needed by a distribute function.

