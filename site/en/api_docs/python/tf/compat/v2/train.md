page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.train

Support for training models.

<!-- Placeholder for "Used in" -->

See the [Training](https://tensorflow.org/api_guides/python/train) guide.

## Modules

[`experimental`](../../../tf/compat/v2/train/experimental) module: Public API for tf.train.experimental namespace.

## Classes

[`class BytesList`](../../../tf/train/BytesList)

[`class Checkpoint`](../../../tf/compat/v2/train/Checkpoint): Groups trackable objects, saving and restoring them.

[`class CheckpointManager`](../../../tf/train/CheckpointManager): Deletes old checkpoints.

[`class ClusterDef`](../../../tf/train/ClusterDef)

[`class ClusterSpec`](../../../tf/train/ClusterSpec): Represents a cluster as a set of "tasks", organized into "jobs".

[`class Coordinator`](../../../tf/train/Coordinator): A coordinator for threads.

[`class Example`](../../../tf/train/Example)

[`class ExponentialMovingAverage`](../../../tf/train/ExponentialMovingAverage): Maintains moving averages of variables by employing an exponential decay.

[`class Feature`](../../../tf/train/Feature)

[`class FeatureList`](../../../tf/train/FeatureList)

[`class FeatureLists`](../../../tf/train/FeatureLists)

[`class Features`](../../../tf/train/Features)

[`class FloatList`](../../../tf/train/FloatList)

[`class Int64List`](../../../tf/train/Int64List)

[`class JobDef`](../../../tf/train/JobDef)

[`class SequenceExample`](../../../tf/train/SequenceExample)

[`class ServerDef`](../../../tf/train/ServerDef)

## Functions

[`checkpoints_iterator(...)`](../../../tf/train/checkpoints_iterator): Continuously yield new checkpoint files as they appear.

[`get_checkpoint_state(...)`](../../../tf/train/get_checkpoint_state): Returns CheckpointState proto from the "checkpoint" file.

[`latest_checkpoint(...)`](../../../tf/train/latest_checkpoint): Finds the filename of latest saved checkpoint file.

[`list_variables(...)`](../../../tf/train/list_variables): Returns list of all variables in the checkpoint.

[`load_checkpoint(...)`](../../../tf/train/load_checkpoint): Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

[`load_variable(...)`](../../../tf/train/load_variable): Returns the tensor value of the given variable in the checkpoint.

