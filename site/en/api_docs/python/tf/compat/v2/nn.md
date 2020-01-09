page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.compat.v2.nn


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Wrappers for primitive Neural Net (NN) Operations.

<!-- Placeholder for "Used in" -->


## Classes

[`class RNNCellDeviceWrapper`](../../../tf/nn/RNNCellDeviceWrapper): Operator that ensures an RNNCell runs on a particular device.

[`class RNNCellDropoutWrapper`](../../../tf/nn/RNNCellDropoutWrapper): Operator adding dropout to inputs and outputs of the given cell.

[`class RNNCellResidualWrapper`](../../../tf/nn/RNNCellResidualWrapper): RNNCell wrapper that ensures cell inputs are added to the outputs.

## Functions

[`all_candidate_sampler(...)`](../../../tf/random/all_candidate_sampler): Generate the set of all classes.

[`atrous_conv2d(...)`](../../../tf/nn/atrous_conv2d): Atrous convolution (a.k.a. convolution with holes or dilated convolution).

[`atrous_conv2d_transpose(...)`](../../../tf/nn/atrous_conv2d_transpose): The transpose of `atrous_conv2d`.

[`avg_pool(...)`](../../../tf/nn/avg_pool): Performs the avg pooling on the input.

[`avg_pool1d(...)`](../../../tf/nn/avg_pool1d): Performs the average pooling on the input.

[`avg_pool2d(...)`](../../../tf/nn/avg_pool2d): Performs the average pooling on the input.

[`avg_pool3d(...)`](../../../tf/nn/avg_pool3d): Performs the average pooling on the input.

[`batch_norm_with_global_normalization(...)`](../../../tf/nn/batch_norm_with_global_normalization): Batch normalization.

[`batch_normalization(...)`](../../../tf/nn/batch_normalization): Batch normalization.

[`bias_add(...)`](../../../tf/nn/bias_add): Adds `bias` to `value`.

[`collapse_repeated(...)`](../../../tf/nn/collapse_repeated): Merge repeated labels into single labels.

[`compute_accidental_hits(...)`](../../../tf/nn/compute_accidental_hits): Compute the position ids in `sampled_candidates` matching `true_classes`.

[`compute_average_loss(...)`](../../../tf/nn/compute_average_loss): Scales per-example losses with sample_weights and computes their average.

[`conv1d(...)`](../../../tf/nn/conv1d): Computes a 1-D convolution given 3-D input and filter tensors.

[`conv1d_transpose(...)`](../../../tf/nn/conv1d_transpose): The transpose of `conv1d`.

[`conv2d(...)`](../../../tf/nn/conv2d): Computes a 2-D convolution given 4-D `input` and `filters` tensors.

[`conv2d_transpose(...)`](../../../tf/nn/conv2d_transpose): The transpose of `conv2d`.

[`conv3d(...)`](../../../tf/nn/conv3d): Computes a 3-D convolution given 5-D `input` and `filters` tensors.

[`conv3d_transpose(...)`](../../../tf/nn/conv3d_transpose): The transpose of `conv3d`.

[`conv_transpose(...)`](../../../tf/nn/conv_transpose): The transpose of `convolution`.

[`convolution(...)`](../../../tf/nn/convolution): Computes sums of N-D convolutions (actually cross-correlation).

[`crelu(...)`](../../../tf/nn/crelu): Computes Concatenated ReLU.

[`ctc_beam_search_decoder(...)`](../../../tf/nn/ctc_beam_search_decoder): Performs beam search decoding on the logits given in input.

[`ctc_greedy_decoder(...)`](../../../tf/nn/ctc_greedy_decoder): Performs greedy decoding on the logits given in input (best path).

[`ctc_loss(...)`](../../../tf/nn/ctc_loss): Computes CTC (Connectionist Temporal Classification) loss.

[`ctc_unique_labels(...)`](../../../tf/nn/ctc_unique_labels): Get unique labels and indices for batched labels for <a href="../../../tf/nn/ctc_loss"><code>tf.nn.ctc_loss</code></a>.

[`depth_to_space(...)`](../../../tf/nn/depth_to_space): DepthToSpace for tensors of type T.

[`depthwise_conv2d(...)`](../../../tf/nn/depthwise_conv2d): Depthwise 2-D convolution.

[`depthwise_conv2d_backprop_filter(...)`](../../../tf/nn/depthwise_conv2d_backprop_filter): Computes the gradients of depthwise convolution with respect to the filter.

[`depthwise_conv2d_backprop_input(...)`](../../../tf/nn/depthwise_conv2d_backprop_input): Computes the gradients of depthwise convolution with respect to the input.

[`dilation2d(...)`](../../../tf/nn/dilation2d): Computes the grayscale dilation of 4-D `input` and 3-D `filters` tensors.

[`dropout(...)`](../../../tf/nn/dropout): Computes dropout.

[`elu(...)`](../../../tf/nn/elu): Computes exponential linear: `exp(features) - 1` if < 0, `features` otherwise.

[`embedding_lookup(...)`](../../../tf/nn/embedding_lookup): Looks up `ids` in a list of embedding tensors.

[`embedding_lookup_sparse(...)`](../../../tf/nn/embedding_lookup_sparse): Computes embeddings for the given ids and weights.

[`erosion2d(...)`](../../../tf/nn/erosion2d): Computes the grayscale erosion of 4-D `value` and 3-D `filters` tensors.

[`fixed_unigram_candidate_sampler(...)`](../../../tf/random/fixed_unigram_candidate_sampler): Samples a set of classes using the provided (fixed) base distribution.

[`fractional_avg_pool(...)`](../../../tf/nn/fractional_avg_pool): Performs fractional average pooling on the input.

[`fractional_max_pool(...)`](../../../tf/nn/fractional_max_pool): Performs fractional max pooling on the input.

[`in_top_k(...)`](../../../tf/math/in_top_k): Says whether the targets are in the top `K` predictions.

[`l2_loss(...)`](../../../tf/nn/l2_loss): L2 Loss.

[`l2_normalize(...)`](../../../tf/math/l2_normalize): Normalizes along dimension `axis` using an L2 norm.

[`leaky_relu(...)`](../../../tf/nn/leaky_relu): Compute the Leaky ReLU activation function.

[`learned_unigram_candidate_sampler(...)`](../../../tf/random/learned_unigram_candidate_sampler): Samples a set of classes from a distribution learned during training.

[`local_response_normalization(...)`](../../../tf/nn/local_response_normalization): Local Response Normalization.

[`log_poisson_loss(...)`](../../../tf/nn/log_poisson_loss): Computes log Poisson loss given `log_input`.

[`log_softmax(...)`](../../../tf/nn/log_softmax): Computes log softmax activations.

[`lrn(...)`](../../../tf/nn/local_response_normalization): Local Response Normalization.

[`max_pool(...)`](../../../tf/nn/max_pool): Performs the max pooling on the input.

[`max_pool1d(...)`](../../../tf/nn/max_pool1d): Performs the max pooling on the input.

[`max_pool2d(...)`](../../../tf/nn/max_pool2d): Performs the max pooling on the input.

[`max_pool3d(...)`](../../../tf/nn/max_pool3d): Performs the max pooling on the input.

[`max_pool_with_argmax(...)`](../../../tf/nn/max_pool_with_argmax): Performs max pooling on the input and outputs both max values and indices.

[`moments(...)`](../../../tf/nn/moments): Calculates the mean and variance of `x`.

[`nce_loss(...)`](../../../tf/nn/nce_loss): Computes and returns the noise-contrastive estimation training loss.

[`normalize_moments(...)`](../../../tf/nn/normalize_moments): Calculate the mean and variance of based on the sufficient statistics.

[`pool(...)`](../../../tf/nn/pool): Performs an N-D pooling operation.

[`relu(...)`](../../../tf/nn/relu): Computes rectified linear: `max(features, 0)`.

[`relu6(...)`](../../../tf/nn/relu6): Computes Rectified Linear 6: `min(max(features, 0), 6)`.

[`safe_embedding_lookup_sparse(...)`](../../../tf/nn/safe_embedding_lookup_sparse): Lookup embedding results, accounting for invalid IDs and empty features.

[`sampled_softmax_loss(...)`](../../../tf/nn/sampled_softmax_loss): Computes and returns the sampled softmax training loss.

[`scale_regularization_loss(...)`](../../../tf/nn/scale_regularization_loss): Scales the sum of the given regularization losses by number of replicas.

[`selu(...)`](../../../tf/nn/selu): Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

[`separable_conv2d(...)`](../../../tf/nn/separable_conv2d): 2-D convolution with separable filters.

[`sigmoid(...)`](../../../tf/math/sigmoid): Computes sigmoid of `x` element-wise.

[`sigmoid_cross_entropy_with_logits(...)`](../../../tf/nn/sigmoid_cross_entropy_with_logits): Computes sigmoid cross entropy given `logits`.

[`softmax(...)`](../../../tf/nn/softmax): Computes softmax activations.

[`softmax_cross_entropy_with_logits(...)`](../../../tf/nn/softmax_cross_entropy_with_logits): Computes softmax cross entropy between `logits` and `labels`.

[`softplus(...)`](../../../tf/math/softplus): Computes softplus: `log(exp(features) + 1)`.

[`softsign(...)`](../../../tf/nn/softsign): Computes softsign: `features / (abs(features) + 1)`.

[`space_to_batch(...)`](../../../tf/space_to_batch): SpaceToBatch for N-D tensors of type T.

[`space_to_depth(...)`](../../../tf/nn/space_to_depth): SpaceToDepth for tensors of type T.

[`sparse_softmax_cross_entropy_with_logits(...)`](../../../tf/nn/sparse_softmax_cross_entropy_with_logits): Computes sparse softmax cross entropy between `logits` and `labels`.

[`sufficient_statistics(...)`](../../../tf/nn/sufficient_statistics): Calculate the sufficient statistics for the mean and variance of `x`.

[`tanh(...)`](../../../tf/math/tanh): Computes hyperbolic tangent of `x` element-wise.

[`top_k(...)`](../../../tf/math/top_k): Finds values and indices of the `k` largest entries for the last dimension.

[`weighted_cross_entropy_with_logits(...)`](../../../tf/nn/weighted_cross_entropy_with_logits): Computes a weighted cross entropy.

[`weighted_moments(...)`](../../../tf/nn/weighted_moments): Returns the frequency-weighted mean and variance of `x`.

[`with_space_to_batch(...)`](../../../tf/nn/with_space_to_batch): Performs `op` on the space-to-batch representation of `input`.

[`zero_fraction(...)`](../../../tf/math/zero_fraction): Returns the fraction of zeros in `value`.

## Other Members

* `swish` <a id="swish"></a>
