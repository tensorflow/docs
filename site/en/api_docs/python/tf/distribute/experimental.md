description: Experimental Distribution Strategy library.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.experimental" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.distribute.experimental

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Experimental Distribution Strategy library.



## Classes

[`class CentralStorageStrategy`](../../tf/distribute/experimental/CentralStorageStrategy.md): A one-machine strategy that puts all variables on a single device.

[`class CollectiveCommunication`](../../tf/distribute/experimental/CollectiveCommunication.md): Communication choices for CollectiveOps.

[`class CollectiveHints`](../../tf/distribute/experimental/CollectiveHints.md): Hints for collective operations like AllReduce.

[`class MultiWorkerMirroredStrategy`](../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md): A distribution strategy for synchronous training on multiple workers.

[`class ParameterServerStrategy`](../../tf/distribute/experimental/ParameterServerStrategy.md): An asynchronous multi-worker parameter server tf.distribute strategy.

[`class TPUStrategy`](../../tf/distribute/experimental/TPUStrategy.md): Synchronous training on TPUs and TPU Pods.

[`class ValueContext`](../../tf/distribute/experimental/ValueContext.md): A class wrapping information needed by a distribute function.

