description: Support for training models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.train

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Support for training models.


See the [Training](https://tensorflow.org/api_guides/python/train) guide.

## Modules

[`experimental`](../tf/train/experimental.md) module: Public API for tf.train.experimental namespace.

## Classes

[`class BytesList`](../tf/train/BytesList.md): A ProtocolMessage

[`class Checkpoint`](../tf/train/Checkpoint.md): Groups trackable objects, saving and restoring them.

[`class CheckpointManager`](../tf/train/CheckpointManager.md): Manages multiple checkpoints by keeping some and deleting unneeded ones.

[`class CheckpointOptions`](../tf/train/CheckpointOptions.md): Options for constructing a Checkpoint.

[`class ClusterDef`](../tf/train/ClusterDef.md): A ProtocolMessage

[`class ClusterSpec`](../tf/train/ClusterSpec.md): Represents a cluster as a set of "tasks", organized into "jobs".

[`class Coordinator`](../tf/train/Coordinator.md): A coordinator for threads.

[`class Example`](../tf/train/Example.md): A ProtocolMessage

[`class ExponentialMovingAverage`](../tf/train/ExponentialMovingAverage.md): Maintains moving averages of variables by employing an exponential decay.

[`class Feature`](../tf/train/Feature.md): A ProtocolMessage

[`class FeatureList`](../tf/train/FeatureList.md): A ProtocolMessage

[`class FeatureLists`](../tf/train/FeatureLists.md): A ProtocolMessage

[`class Features`](../tf/train/Features.md): A ProtocolMessage

[`class FloatList`](../tf/train/FloatList.md): A ProtocolMessage

[`class Int64List`](../tf/train/Int64List.md): A ProtocolMessage

[`class JobDef`](../tf/train/JobDef.md): A ProtocolMessage

[`class SequenceExample`](../tf/train/SequenceExample.md): A ProtocolMessage

[`class ServerDef`](../tf/train/ServerDef.md): A ProtocolMessage

## Functions

[`checkpoints_iterator(...)`](../tf/train/checkpoints_iterator.md): Continuously yield new checkpoint files as they appear.

[`get_checkpoint_state(...)`](../tf/train/get_checkpoint_state.md): Returns CheckpointState proto from the "checkpoint" file.

[`latest_checkpoint(...)`](../tf/train/latest_checkpoint.md): Finds the filename of latest saved checkpoint file.

[`list_variables(...)`](../tf/train/list_variables.md): Returns list of all variables in the checkpoint.

[`load_checkpoint(...)`](../tf/train/load_checkpoint.md): Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

[`load_variable(...)`](../tf/train/load_variable.md): Returns the tensor value of the given variable in the checkpoint.

