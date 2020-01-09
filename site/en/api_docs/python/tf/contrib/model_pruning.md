page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.model_pruning



Defined in [`tensorflow/contrib/model_pruning/__init__.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/model_pruning/__init__.py).

Model pruning implementation in tensorflow.

## Classes

[`class MaskedBasicLSTMCell`](../../tf/contrib/model_pruning/MaskedBasicLSTMCell): Basic LSTM recurrent network cell with pruning.

[`class MaskedLSTMCell`](../../tf/contrib/model_pruning/MaskedLSTMCell): LSTMCell with pruning.

[`class Pruning`](../../tf/contrib/model_pruning/Pruning)

## Functions

[`apply_mask(...)`](../../tf/contrib/model_pruning/apply_mask): Apply mask to a given weight tensor.

[`get_masked_weights(...)`](../../tf/contrib/model_pruning/get_masked_weights)

[`get_masks(...)`](../../tf/contrib/model_pruning/get_masks)

[`get_pruning_hparams(...)`](../../tf/contrib/model_pruning/get_pruning_hparams): Get a tf.HParams object with the default values for the hyperparameters.

[`get_thresholds(...)`](../../tf/contrib/model_pruning/get_thresholds)

[`get_weight_sparsity(...)`](../../tf/contrib/model_pruning/get_weight_sparsity): Get sparsity of the weights.

[`get_weights(...)`](../../tf/contrib/model_pruning/get_weights)

[`graph_def_from_checkpoint(...)`](../../tf/contrib/model_pruning/graph_def_from_checkpoint): Converts checkpoint data to GraphDef.

[`masked_conv2d(...)`](../../tf/contrib/model_pruning/masked_conv2d): Adds an 2D convolution followed by an optional batch_norm layer.

[`masked_convolution(...)`](../../tf/contrib/model_pruning/masked_conv2d): Adds an 2D convolution followed by an optional batch_norm layer.

[`masked_fully_connected(...)`](../../tf/contrib/model_pruning/masked_fully_connected): Adds a sparse fully connected layer. The weight matrix is masked.

[`strip_pruning_vars_fn(...)`](../../tf/contrib/model_pruning/strip_pruning_vars_fn): Removes mask variable from the graph.

[`train(...)`](../../tf/contrib/model_pruning/train): Wrapper around tf-slim's train function.

