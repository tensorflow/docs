page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.train



Defined in [`tensorflow/train/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/train/__init__.py).

Support for training models.

See the <a href="../../../api_guides/python/train">Training</a> guide.

## Modules

[`queue_runner`](../tf/train/queue_runner) module: Create threads to run multiple enqueue ops.

## Classes

[`class AdadeltaOptimizer`](../tf/train/AdadeltaOptimizer): Optimizer that implements the Adadelta algorithm.

[`class AdagradDAOptimizer`](../tf/train/AdagradDAOptimizer): Adagrad Dual Averaging algorithm for sparse linear models.

[`class AdagradOptimizer`](../tf/train/AdagradOptimizer): Optimizer that implements the Adagrad algorithm.

[`class AdamOptimizer`](../tf/train/AdamOptimizer): Optimizer that implements the Adam algorithm.

[`class BytesList`](../tf/train/BytesList)

[`class Checkpoint`](../tf/train/Checkpoint): Groups checkpointable objects, saving and restoring them.

[`class CheckpointSaverHook`](../tf/train/CheckpointSaverHook): Saves checkpoints every N steps or seconds.

[`class CheckpointSaverListener`](../tf/train/CheckpointSaverListener): Interface for listeners that take action before or after checkpoint save.

[`class ChiefSessionCreator`](../tf/train/ChiefSessionCreator): Creates a tf.Session for a chief.

[`class ClusterDef`](../tf/train/ClusterDef)

[`class ClusterSpec`](../tf/train/ClusterSpec): Represents a cluster as a set of "tasks", organized into "jobs".

[`class Coordinator`](../tf/train/Coordinator): A coordinator for threads.

[`class Example`](../tf/train/Example)

[`class ExponentialMovingAverage`](../tf/train/ExponentialMovingAverage): Maintains moving averages of variables by employing an exponential decay.

[`class Feature`](../tf/train/Feature)

[`class FeatureList`](../tf/train/FeatureList)

[`class FeatureLists`](../tf/train/FeatureLists)

[`class Features`](../tf/train/Features)

[`class FeedFnHook`](../tf/train/FeedFnHook): Runs `feed_fn` and sets the `feed_dict` accordingly.

[`class FinalOpsHook`](../tf/train/FinalOpsHook): A hook which evaluates `Tensors` at the end of a session.

[`class FloatList`](../tf/train/FloatList)

[`class FtrlOptimizer`](../tf/train/FtrlOptimizer): Optimizer that implements the FTRL algorithm.

[`class GlobalStepWaiterHook`](../tf/train/GlobalStepWaiterHook): Delays execution until global step reaches `wait_until_step`.

[`class GradientDescentOptimizer`](../tf/train/GradientDescentOptimizer): Optimizer that implements the gradient descent algorithm.

[`class Int64List`](../tf/train/Int64List)

[`class JobDef`](../tf/train/JobDef)

[`class LoggingTensorHook`](../tf/train/LoggingTensorHook): Prints the given tensors every N local steps, every N seconds, or at end.

[`class LooperThread`](../tf/train/LooperThread): A thread that runs code repeatedly, optionally on a timer.

[`class MomentumOptimizer`](../tf/train/MomentumOptimizer): Optimizer that implements the Momentum algorithm.

[`class MonitoredSession`](../tf/train/MonitoredSession): Session-like object that handles initialization, recovery and hooks.

[`class NanLossDuringTrainingError`](../tf/train/NanLossDuringTrainingError)

[`class NanTensorHook`](../tf/train/NanTensorHook): Monitors the loss tensor and stops training if loss is NaN.

[`class Optimizer`](../tf/train/Optimizer): Base class for optimizers.

[`class ProfilerHook`](../tf/train/ProfilerHook): Captures CPU/GPU profiling information every N steps or seconds.

[`class ProximalAdagradOptimizer`](../tf/train/ProximalAdagradOptimizer): Optimizer that implements the Proximal Adagrad algorithm.

[`class ProximalGradientDescentOptimizer`](../tf/train/ProximalGradientDescentOptimizer): Optimizer that implements the proximal gradient descent algorithm.

[`class QueueRunner`](../tf/train/QueueRunner): Holds a list of enqueue operations for a queue, each to be run in a thread.

[`class RMSPropOptimizer`](../tf/train/RMSPropOptimizer): Optimizer that implements the RMSProp algorithm.

[`class Saver`](../tf/train/Saver): Saves and restores variables.

[`class SaverDef`](../tf/train/SaverDef)

[`class Scaffold`](../tf/train/Scaffold): Structure to create or gather pieces commonly needed to train a model.

[`class SecondOrStepTimer`](../tf/train/SecondOrStepTimer): Timer that triggers at most once every N seconds or once every N steps.

[`class SequenceExample`](../tf/train/SequenceExample)

[`class Server`](../tf/train/Server): An in-process TensorFlow server, for use in distributed training.

[`class ServerDef`](../tf/train/ServerDef)

[`class SessionCreator`](../tf/train/SessionCreator): A factory for tf.Session.

[`class SessionManager`](../tf/train/SessionManager): Training helper that restores from checkpoint and creates session.

[`class SessionRunArgs`](../tf/train/SessionRunArgs): Represents arguments to be added to a `Session.run()` call.

[`class SessionRunContext`](../tf/train/SessionRunContext): Provides information about the `session.run()` call being made.

[`class SessionRunHook`](../tf/train/SessionRunHook): Hook to extend calls to MonitoredSession.run().

[`class SessionRunValues`](../tf/train/SessionRunValues): Contains the results of `Session.run()`.

[`class SingularMonitoredSession`](../tf/train/SingularMonitoredSession): Session-like object that handles initialization, restoring, and hooks.

[`class StepCounterHook`](../tf/train/StepCounterHook): Hook that counts steps per second.

[`class StopAtStepHook`](../tf/train/StopAtStepHook): Hook that requests stop at a specified step.

[`class SummarySaverHook`](../tf/train/SummarySaverHook): Saves summaries every N steps.

[`class Supervisor`](../tf/train/Supervisor): A training helper that checkpoints models and computes summaries.

[`class SyncReplicasOptimizer`](../tf/train/SyncReplicasOptimizer): Class to synchronize, aggregate gradients and pass them to the optimizer.

[`class VocabInfo`](../tf/estimator/VocabInfo): Vocabulary information for warm-starting.

[`class WorkerSessionCreator`](../tf/train/WorkerSessionCreator): Creates a tf.Session for a worker.

## Functions

[`MonitoredTrainingSession(...)`](../tf/train/MonitoredTrainingSession): Creates a `MonitoredSession` for training.

[`NewCheckpointReader(...)`](../tf/train/NewCheckpointReader)

[`add_queue_runner(...)`](../tf/train/add_queue_runner): Adds a `QueueRunner` to a collection in the graph.

[`assert_global_step(...)`](../tf/train/assert_global_step): Asserts `global_step_tensor` is a scalar int `Variable` or `Tensor`.

[`basic_train_loop(...)`](../tf/train/basic_train_loop): Basic loop to train a model.

[`batch(...)`](../tf/train/batch): Creates batches of tensors in `tensors`.

[`batch_join(...)`](../tf/train/batch_join): Runs a list of tensors to fill a queue to create batches of examples.

[`checkpoint_exists(...)`](../tf/train/checkpoint_exists): Checks whether a V1 or V2 checkpoint exists with the specified prefix.

[`cosine_decay(...)`](../tf/train/cosine_decay): Applies cosine decay to the learning rate.

[`cosine_decay_restarts(...)`](../tf/train/cosine_decay_restarts): Applies cosine decay with restarts to the learning rate.

[`create_global_step(...)`](../tf/train/create_global_step): Create global step tensor in graph.

[`do_quantize_training_on_graphdef(...)`](../tf/train/do_quantize_training_on_graphdef): A general quantization scheme is being developed in <a href="../tf/contrib/quantize"><code>tf.contrib.quantize</code></a>.

[`exponential_decay(...)`](../tf/train/exponential_decay): Applies exponential decay to the learning rate.

[`export_meta_graph(...)`](../tf/train/export_meta_graph): Returns `MetaGraphDef` proto. Optionally writes it to filename.

[`generate_checkpoint_state_proto(...)`](../tf/train/generate_checkpoint_state_proto): Generates a checkpoint state proto.

[`get_checkpoint_mtimes(...)`](../tf/train/get_checkpoint_mtimes): Returns the mtimes (modification timestamps) of the checkpoints.

[`get_checkpoint_state(...)`](../tf/train/get_checkpoint_state): Returns CheckpointState proto from the "checkpoint" file.

[`get_global_step(...)`](../tf/train/get_global_step): Get the global step tensor.

[`get_or_create_global_step(...)`](../tf/train/get_or_create_global_step): Returns and create (if necessary) the global step tensor.

[`global_step(...)`](../tf/train/global_step): Small helper to get the global step.

[`import_meta_graph(...)`](../tf/train/import_meta_graph): Recreates a Graph saved in a `MetaGraphDef` proto.

[`init_from_checkpoint(...)`](../tf/train/init_from_checkpoint): Initializes current variables with tensors loaded from given checkpoint.

[`input_producer(...)`](../tf/train/input_producer): Output the rows of `input_tensor` to a queue for an input pipeline.

[`inverse_time_decay(...)`](../tf/train/inverse_time_decay): Applies inverse time decay to the initial learning rate.

[`latest_checkpoint(...)`](../tf/train/latest_checkpoint): Finds the filename of latest saved checkpoint file.

[`limit_epochs(...)`](../tf/train/limit_epochs): Returns tensor `num_epochs` times and then raises an `OutOfRange` error.

[`linear_cosine_decay(...)`](../tf/train/linear_cosine_decay): Applies linear cosine decay to the learning rate.

[`list_variables(...)`](../tf/train/list_variables): Returns list of all variables in the checkpoint.

[`load_checkpoint(...)`](../tf/train/load_checkpoint): Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

[`load_variable(...)`](../tf/train/load_variable): Returns the tensor value of the given variable in the checkpoint.

[`match_filenames_once(...)`](../tf/train/match_filenames_once): Save the list of files matching pattern, so it is only computed once.

[`maybe_batch(...)`](../tf/train/maybe_batch): Conditionally creates batches of tensors based on `keep_input`.

[`maybe_batch_join(...)`](../tf/train/maybe_batch_join): Runs a list of tensors to conditionally fill a queue to create batches.

[`maybe_shuffle_batch(...)`](../tf/train/maybe_shuffle_batch): Creates batches by randomly shuffling conditionally-enqueued tensors.

[`maybe_shuffle_batch_join(...)`](../tf/train/maybe_shuffle_batch_join): Create batches by randomly shuffling conditionally-enqueued tensors.

[`natural_exp_decay(...)`](../tf/train/natural_exp_decay): Applies natural exponential decay to the initial learning rate.

[`noisy_linear_cosine_decay(...)`](../tf/train/noisy_linear_cosine_decay): Applies noisy linear cosine decay to the learning rate.

[`piecewise_constant(...)`](../tf/train/piecewise_constant): Piecewise constant from boundaries and interval values.

[`polynomial_decay(...)`](../tf/train/polynomial_decay): Applies a polynomial decay to the learning rate.

[`range_input_producer(...)`](../tf/train/range_input_producer): Produces the integers from 0 to limit-1 in a queue.

[`remove_checkpoint(...)`](../tf/train/remove_checkpoint): Removes a checkpoint given by `checkpoint_prefix`.

[`replica_device_setter(...)`](../tf/train/replica_device_setter): Return a `device function` to use when building a Graph for replicas.

[`sdca_fprint(...)`](../tf/train/sdca_fprint): Computes fingerprints of the input strings.

[`sdca_optimizer(...)`](../tf/train/sdca_optimizer): Distributed version of Stochastic Dual Coordinate Ascent (SDCA) optimizer for

[`sdca_shrink_l1(...)`](../tf/train/sdca_shrink_l1): Applies L1 regularization shrink step on the parameters.

[`shuffle_batch(...)`](../tf/train/shuffle_batch): Creates batches by randomly shuffling tensors.

[`shuffle_batch_join(...)`](../tf/train/shuffle_batch_join): Create batches by randomly shuffling tensors.

[`slice_input_producer(...)`](../tf/train/slice_input_producer): Produces a slice of each `Tensor` in `tensor_list`.

[`start_queue_runners(...)`](../tf/train/start_queue_runners): Starts all queue runners collected in the graph.

[`string_input_producer(...)`](../tf/train/string_input_producer): Output strings (e.g. filenames) to a queue for an input pipeline.

[`summary_iterator(...)`](../tf/train/summary_iterator): An iterator for reading `Event` protocol buffers from an event file.

[`update_checkpoint_state(...)`](../tf/train/update_checkpoint_state): Updates the content of the 'checkpoint' file.

[`warm_start(...)`](../tf/train/warm_start): Warm-starts a model using the given settings.

[`write_graph(...)`](../tf/train/write_graph): Writes a graph proto to a file.

