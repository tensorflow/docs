page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/__init__.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Contrib module containing volatile or experimental code.

<!-- Placeholder for "Used in" -->

Warning: The <a href="../tf/contrib"><code>tf.contrib</code></a> module will not be included in TensorFlow 2.0. Many
of its submodules have been integrated into TensorFlow core, or spun-off into
other projects like [`tensorflow_io`](https://github.com/tensorflow/io), or
[`tensorflow_addons`](https://github.com/tensorflow/addons). For instructions
on how to upgrade see the
[Migration guide](https://www.tensorflow.org/beta/guide/migration_guide).

## Modules

[`autograph`](../tf/contrib/autograph) module: This is the legacy module for AutoGraph, kept for backward compatibility.

[`batching`](../tf/contrib/batching) module: Ops and modules related to batch.

[`bayesflow`](../tf/contrib/bayesflow) module: Ops for representing Bayesian computation.

[`checkpoint`](../tf/contrib/checkpoint) module: Tools for working with object-based checkpoints.

[`cloud`](../tf/contrib/cloud) module: Module for cloud ops.

[`cluster_resolver`](../tf/contrib/cluster_resolver) module: Standard imports for Cluster Resolvers.

[`compiler`](../tf/contrib/compiler) module: A module for controlling the Tensorflow/XLA JIT compiler.

[`constrained_optimization`](../tf/contrib/constrained_optimization) module: A library for performing constrained optimization in TensorFlow.

[`copy_graph`](../tf/contrib/copy_graph) module: Functions to copy elements between graphs.

[`crf`](../tf/contrib/crf) module: Linear-chain CRF layer.

[`cudnn_rnn`](../tf/contrib/cudnn_rnn) module: Ops for fused Cudnn RNN models.

[`data`](../tf/contrib/data) module: Experimental API for building input pipelines.

[`deprecated`](../tf/contrib/deprecated) module: Non-core alias for the deprecated tf.X_summary ops.

[`distribute`](../tf/contrib/distribute) module: A distributed computation library for TF.

[`distributions`](../tf/contrib/distributions) module: Classes representing statistical distributions and ops for working with them.

[`eager`](../tf/contrib/eager) module: TensorFlow Eager execution prototype.

[`estimator`](../tf/contrib/estimator) module: estimator python module.

[`factorization`](../tf/contrib/factorization) module: Ops and modules related to factorization.

[`feature_column`](../tf/contrib/feature_column) module: Experimental utilities for tf.feature_column.

[`ffmpeg`](../tf/contrib/ffmpeg) module: Working with audio using FFmpeg.

[`framework`](../tf/contrib/framework) module: Framework utilities.

[`graph_editor`](../tf/contrib/graph_editor) module: TensorFlow Graph Editor.

[`grid_rnn`](../tf/contrib/grid_rnn) module: GridRNN cells

[`image`](../tf/contrib/image) module: Ops for image manipulation.

[`input_pipeline`](../tf/contrib/input_pipeline) module: Ops and modules related to input_pipeline.

[`integrate`](../tf/contrib/integrate) module: Integration and ODE solvers.

[`keras`](../tf/contrib/keras) module: Implementation of the Keras API meant to be a high-level API for TensorFlow.

[`kernel_methods`](../tf/contrib/kernel_methods) module: Ops and estimators that enable explicit kernel methods in TensorFlow.

[`labeled_tensor`](../tf/contrib/labeled_tensor) module: Labels for TensorFlow.

[`layers`](../tf/contrib/layers) module: Ops for building neural network layers, regularizers, summaries, etc.

[`learn`](../tf/contrib/learn) module: High level API for learning (DEPRECATED).

[`legacy_seq2seq`](../tf/contrib/legacy_seq2seq) module: Deprecated library for creating sequence-to-sequence models in TensorFlow.

[`linear_optimizer`](../tf/contrib/linear_optimizer) module: Ops for training linear models.

[`lookup`](../tf/contrib/lookup) module: Ops for lookup operations.

[`losses`](../tf/contrib/losses) module: Ops for building neural network losses.

[`memory_stats`](../tf/contrib/memory_stats) module: Ops for memory statistics.

[`metrics`](../tf/contrib/metrics) module: Ops for evaluation metrics and summary statistics.

[`mixed_precision`](../tf/contrib/mixed_precision) module: Library for mixed precision training.

[`model_pruning`](../tf/contrib/model_pruning) module: Model pruning implementation in tensorflow.

[`nn`](../tf/contrib/nn) module: Module for variants of ops in tf.nn.

[`opt`](../tf/contrib/opt) module: A module containing optimization routines.

[`optimizer_v2`](../tf/contrib/optimizer_v2) module: Distribution-aware version of Optimizer.

[`periodic_resample`](../tf/contrib/periodic_resample) module: Custom op used by periodic_resample.

[`predictor`](../tf/contrib/predictor) module: Modules for `Predictor`s.

[`proto`](../tf/contrib/proto) module: Ops and modules related to proto.

[`quantization`](../tf/contrib/quantization) module: Ops for building quantized models.

[`quantize`](../tf/contrib/quantize) module: Functions for rewriting graphs for quantized training.

[`receptive_field`](../tf/contrib/receptive_field) module: Module that declares the functions in tf.contrib.receptive_field's API.

[`recurrent`](../tf/contrib/recurrent) module: Recurrent computations library.

[`reduce_slice_ops`](../tf/contrib/reduce_slice_ops) module: reduce by slice

[`remote_fused_graph`](../tf/contrib/remote_fused_graph) module: Remote fused graph ops python library.

[`resampler`](../tf/contrib/resampler) module: Ops and modules related to resampler.

[`rnn`](../tf/contrib/rnn) module: RNN Cells and additional RNN operations.

[`rpc`](../tf/contrib/rpc) module: Ops and modules related to RPC.

[`saved_model`](../tf/contrib/saved_model) module: SavedModel contrib support.

[`seq2seq`](../tf/contrib/seq2seq) module: Ops for building neural network seq2seq decoders and losses.

[`signal`](../tf/contrib/signal) module: Signal processing operations.

[`slim`](../tf/contrib/slim) module: Slim is an interface to contrib functions, examples and models.

[`solvers`](../tf/contrib/solvers) module: Ops for representing Bayesian computation.

[`sparsemax`](../tf/contrib/sparsemax) module: Module that implements sparsemax and sparsemax loss, see [1].

[`specs`](../tf/contrib/specs) module: Init file, giving convenient access to all specs ops.

[`staging`](../tf/contrib/staging) module: contrib module containing StagingArea.

[`stat_summarizer`](../tf/contrib/stat_summarizer) module: Exposes the Python wrapper for StatSummarizer utility class.

[`stateless`](../tf/contrib/stateless) module: Stateless random ops which take seed as a tensor input.

[`summary`](../tf/contrib/summary) module: TensorFlow Summary API v2.

[`tensor_forest`](../tf/contrib/tensor_forest) module: Random forest implementation in tensorflow.

[`tensorboard`](../tf/contrib/tensorboard) module: tensorboard module containing volatile or experimental code.

[`testing`](../tf/contrib/testing) module: Testing utilities.

[`tfprof`](../tf/contrib/tfprof) module: tfprof is a tool that profile various aspect of TensorFlow model.

[`timeseries`](../tf/contrib/timeseries) module: A time series library in TensorFlow (TFTS).

[`tpu`](../tf/contrib/tpu) module: Ops related to Tensor Processing Units.

[`training`](../tf/contrib/training) module: Training and input utilities.

[`util`](../tf/contrib/util) module: Utilities for dealing with Tensors.
