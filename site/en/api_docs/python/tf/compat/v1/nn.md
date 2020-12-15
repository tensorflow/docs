description: Wrappers for primitive Neural Net (NN) Operations.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.nn" />
<meta itemprop="path" content="Stable" />
</div>

# Module: tf.compat.v1.nn

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Wrappers for primitive Neural Net (NN) Operations.



## Modules

[`rnn_cell`](../../../tf/compat/v1/nn/rnn_cell.md) module: Module for constructing RNN Cells.

## Functions

[`all_candidate_sampler(...)`](../../../tf/random/all_candidate_sampler.md): Generate the set of all classes.

[`atrous_conv2d(...)`](../../../tf/nn/atrous_conv2d.md): Atrous convolution (a.k.a. convolution with holes or dilated convolution).

[`atrous_conv2d_transpose(...)`](../../../tf/nn/atrous_conv2d_transpose.md): The transpose of `atrous_conv2d`.

[`avg_pool(...)`](../../../tf/compat/v1/nn/avg_pool.md): Performs the average pooling on the input.

[`avg_pool1d(...)`](../../../tf/nn/avg_pool1d.md): Performs the average pooling on the input.

[`avg_pool2d(...)`](../../../tf/compat/v1/nn/avg_pool.md): Performs the average pooling on the input.

[`avg_pool3d(...)`](../../../tf/nn/avg_pool3d.md): Performs the average pooling on the input.

[`avg_pool_v2(...)`](../../../tf/nn/avg_pool.md): Performs the avg pooling on the input.

[`batch_norm_with_global_normalization(...)`](../../../tf/compat/v1/nn/batch_norm_with_global_normalization.md): Batch normalization.

[`batch_normalization(...)`](../../../tf/nn/batch_normalization.md): Batch normalization.

[`bias_add(...)`](../../../tf/nn/bias_add.md): Adds `bias` to `value`.

[`bidirectional_dynamic_rnn(...)`](../../../tf/compat/v1/nn/bidirectional_dynamic_rnn.md): Creates a dynamic version of bidirectional recurrent neural network. (deprecated)

[`collapse_repeated(...)`](../../../tf/nn/collapse_repeated.md): Merge repeated labels into single labels.

[`compute_accidental_hits(...)`](../../../tf/nn/compute_accidental_hits.md): Compute the position ids in `sampled_candidates` matching `true_classes`.

[`compute_average_loss(...)`](../../../tf/nn/compute_average_loss.md): Scales per-example losses with sample_weights and computes their average.

[`conv1d(...)`](../../../tf/compat/v1/nn/conv1d.md): Computes a 1-D convolution of input with rank `>=3` and a `3-D` filter. (deprecated argument values) (deprecated argument values)

[`conv1d_transpose(...)`](../../../tf/nn/conv1d_transpose.md): The transpose of `conv1d`.

[`conv2d(...)`](../../../tf/compat/v1/nn/conv2d.md): Computes a 2-D convolution given 4-D `input` and `filter` tensors.

[`conv2d_backprop_filter(...)`](../../../tf/compat/v1/nn/conv2d_backprop_filter.md): Computes the gradients of convolution with respect to the filter.

[`conv2d_backprop_input(...)`](../../../tf/compat/v1/nn/conv2d_backprop_input.md): Computes the gradients of convolution with respect to the input.

[`conv2d_transpose(...)`](../../../tf/compat/v1/nn/conv2d_transpose.md): The transpose of `conv2d`.

[`conv3d(...)`](../../../tf/compat/v1/nn/conv3d.md): Computes a 3-D convolution given 5-D `input` and `filter` tensors.

[`conv3d_backprop_filter(...)`](../../../tf/compat/v1/nn/conv3d_backprop_filter.md): Computes the gradients of 3-D convolution with respect to the filter.

[`conv3d_backprop_filter_v2(...)`](../../../tf/compat/v1/nn/conv3d_backprop_filter.md): Computes the gradients of 3-D convolution with respect to the filter.

[`conv3d_transpose(...)`](../../../tf/compat/v1/nn/conv3d_transpose.md): The transpose of `conv3d`.

[`conv_transpose(...)`](../../../tf/nn/conv_transpose.md): The transpose of `convolution`.

[`convolution(...)`](../../../tf/compat/v1/nn/convolution.md): Computes sums of N-D convolutions (actually cross-correlation).

[`crelu(...)`](../../../tf/compat/v1/nn/crelu.md): Computes Concatenated ReLU.

[`ctc_beam_search_decoder(...)`](../../../tf/compat/v1/nn/ctc_beam_search_decoder.md): Performs beam search decoding on the logits given in input.

[`ctc_beam_search_decoder_v2(...)`](../../../tf/nn/ctc_beam_search_decoder.md): Performs beam search decoding on the logits given in input.

[`ctc_greedy_decoder(...)`](../../../tf/nn/ctc_greedy_decoder.md): Performs greedy decoding on the logits given in input (best path).

[`ctc_loss(...)`](../../../tf/compat/v1/nn/ctc_loss.md): Computes the CTC (Connectionist Temporal Classification) Loss.

[`ctc_loss_v2(...)`](../../../tf/compat/v1/nn/ctc_loss_v2.md): Computes CTC (Connectionist Temporal Classification) loss.

[`ctc_unique_labels(...)`](../../../tf/nn/ctc_unique_labels.md): Get unique labels and indices for batched labels for <a href="../../../tf/nn/ctc_loss.md"><code>tf.nn.ctc_loss</code></a>.

[`depth_to_space(...)`](../../../tf/compat/v1/depth_to_space.md): DepthToSpace for tensors of type T.

[`depthwise_conv2d(...)`](../../../tf/compat/v1/nn/depthwise_conv2d.md): Depthwise 2-D convolution.

[`depthwise_conv2d_backprop_filter(...)`](../../../tf/nn/depthwise_conv2d_backprop_filter.md): Computes the gradients of depthwise convolution with respect to the filter.

[`depthwise_conv2d_backprop_input(...)`](../../../tf/nn/depthwise_conv2d_backprop_input.md): Computes the gradients of depthwise convolution with respect to the input.

[`depthwise_conv2d_native(...)`](../../../tf/compat/v1/nn/depthwise_conv2d_native.md): Computes a 2-D depthwise convolution.

[`depthwise_conv2d_native_backprop_filter(...)`](../../../tf/nn/depthwise_conv2d_backprop_filter.md): Computes the gradients of depthwise convolution with respect to the filter.

[`depthwise_conv2d_native_backprop_input(...)`](../../../tf/nn/depthwise_conv2d_backprop_input.md): Computes the gradients of depthwise convolution with respect to the input.

[`dilation2d(...)`](../../../tf/compat/v1/nn/dilation2d.md): Computes the grayscale dilation of 4-D `input` and 3-D `filter` tensors.

[`dropout(...)`](../../../tf/compat/v1/nn/dropout.md): Computes dropout. (deprecated arguments)

[`dynamic_rnn(...)`](../../../tf/compat/v1/nn/dynamic_rnn.md): Creates a recurrent neural network specified by RNNCell `cell`. (deprecated)

[`elu(...)`](../../../tf/nn/elu.md): Computes exponential linear: `exp(features) - 1` if < 0, `features` otherwise.

[`embedding_lookup(...)`](../../../tf/compat/v1/nn/embedding_lookup.md): Looks up embeddings for the given `ids` from a list of tensors.

[`embedding_lookup_sparse(...)`](../../../tf/compat/v1/nn/embedding_lookup_sparse.md): Looks up embeddings for the given ids and weights from a list of tensors.

[`erosion2d(...)`](../../../tf/compat/v1/nn/erosion2d.md): Computes the grayscale erosion of 4-D `value` and 3-D `kernel` tensors.

[`fixed_unigram_candidate_sampler(...)`](../../../tf/random/fixed_unigram_candidate_sampler.md): Samples a set of classes using the provided (fixed) base distribution.

[`fractional_avg_pool(...)`](../../../tf/compat/v1/nn/fractional_avg_pool.md): Performs fractional average pooling on the input. (deprecated)

[`fractional_max_pool(...)`](../../../tf/compat/v1/nn/fractional_max_pool.md): Performs fractional max pooling on the input. (deprecated)

[`fused_batch_norm(...)`](../../../tf/compat/v1/nn/fused_batch_norm.md): Batch normalization.

[`in_top_k(...)`](../../../tf/compat/v1/math/in_top_k.md): Says whether the targets are in the top `K` predictions.

[`l2_loss(...)`](../../../tf/nn/l2_loss.md): L2 Loss.

[`l2_normalize(...)`](../../../tf/compat/v1/linalg/l2_normalize.md): Normalizes along dimension `axis` using an L2 norm. (deprecated arguments)

[`leaky_relu(...)`](../../../tf/nn/leaky_relu.md): Compute the Leaky ReLU activation function.

[`learned_unigram_candidate_sampler(...)`](../../../tf/random/learned_unigram_candidate_sampler.md): Samples a set of classes from a distribution learned during training.

[`local_response_normalization(...)`](../../../tf/nn/local_response_normalization.md): Local Response Normalization.

[`log_poisson_loss(...)`](../../../tf/nn/log_poisson_loss.md): Computes log Poisson loss given `log_input`.

[`log_softmax(...)`](../../../tf/compat/v1/math/log_softmax.md): Computes log softmax activations. (deprecated arguments)

[`log_uniform_candidate_sampler(...)`](../../../tf/random/log_uniform_candidate_sampler.md): Samples a set of classes using a log-uniform (Zipfian) base distribution.

[`lrn(...)`](../../../tf/nn/local_response_normalization.md): Local Response Normalization.

[`max_pool(...)`](../../../tf/compat/v1/nn/max_pool.md): Performs the max pooling on the input.

[`max_pool1d(...)`](../../../tf/nn/max_pool1d.md): Performs the max pooling on the input.

[`max_pool2d(...)`](../../../tf/nn/max_pool2d.md): Performs the max pooling on the input.

[`max_pool3d(...)`](../../../tf/nn/max_pool3d.md): Performs the max pooling on the input.

[`max_pool_v2(...)`](../../../tf/nn/max_pool.md): Performs the max pooling on the input.

[`max_pool_with_argmax(...)`](../../../tf/compat/v1/nn/max_pool_with_argmax.md): Performs max pooling on the input and outputs both max values and indices.

[`moments(...)`](../../../tf/compat/v1/nn/moments.md): Calculate the mean and variance of `x`.

[`nce_loss(...)`](../../../tf/compat/v1/nn/nce_loss.md): Computes and returns the noise-contrastive estimation training loss.

[`normalize_moments(...)`](../../../tf/nn/normalize_moments.md): Calculate the mean and variance of based on the sufficient statistics.

[`pool(...)`](../../../tf/compat/v1/nn/pool.md): Performs an N-D pooling operation.

[`quantized_avg_pool(...)`](../../../tf/compat/v1/nn/quantized_avg_pool.md): Produces the average pool of the input tensor for quantized types.

[`quantized_conv2d(...)`](../../../tf/compat/v1/nn/quantized_conv2d.md): Computes a 2D convolution given quantized 4D input and filter tensors.

[`quantized_max_pool(...)`](../../../tf/compat/v1/nn/quantized_max_pool.md): Produces the max pool of the input tensor for quantized types.

[`quantized_relu_x(...)`](../../../tf/compat/v1/nn/quantized_relu_x.md): Computes Quantized Rectified Linear X: `min(max(features, 0), max_value)`

[`raw_rnn(...)`](../../../tf/compat/v1/nn/raw_rnn.md): Creates an `RNN` specified by RNNCell `cell` and loop function `loop_fn`.

[`relu(...)`](../../../tf/nn/relu.md): Computes rectified linear: `max(features, 0)`.

[`relu6(...)`](../../../tf/nn/relu6.md): Computes Rectified Linear 6: `min(max(features, 0), 6)`.

[`relu_layer(...)`](../../../tf/compat/v1/nn/relu_layer.md): Computes Relu(x * weight + biases).

[`safe_embedding_lookup_sparse(...)`](../../../tf/compat/v1/nn/safe_embedding_lookup_sparse.md): Lookup embedding results, accounting for invalid IDs and empty features.

[`sampled_softmax_loss(...)`](../../../tf/compat/v1/nn/sampled_softmax_loss.md): Computes and returns the sampled softmax training loss.

[`scale_regularization_loss(...)`](../../../tf/nn/scale_regularization_loss.md): Scales the sum of the given regularization losses by number of replicas.

[`selu(...)`](../../../tf/nn/selu.md): Computes scaled exponential linear: `scale * alpha * (exp(features) - 1)`

[`separable_conv2d(...)`](../../../tf/compat/v1/nn/separable_conv2d.md): 2-D convolution with separable filters.

[`sigmoid(...)`](../../../tf/math/sigmoid.md): Computes sigmoid of `x` element-wise.

[`sigmoid_cross_entropy_with_logits(...)`](../../../tf/compat/v1/nn/sigmoid_cross_entropy_with_logits.md): Computes sigmoid cross entropy given `logits`.

[`softmax(...)`](../../../tf/compat/v1/math/softmax.md): Computes softmax activations. (deprecated arguments)

[`softmax_cross_entropy_with_logits(...)`](../../../tf/compat/v1/nn/softmax_cross_entropy_with_logits.md): Computes softmax cross entropy between `logits` and `labels`. (deprecated)

[`softmax_cross_entropy_with_logits_v2(...)`](../../../tf/compat/v1/nn/softmax_cross_entropy_with_logits_v2.md): Computes softmax cross entropy between `logits` and `labels`. (deprecated arguments)

[`softplus(...)`](../../../tf/math/softplus.md): Computes softplus: `log(exp(features) + 1)`.

[`softsign(...)`](../../../tf/nn/softsign.md): Computes softsign: `features / (abs(features) + 1)`.

[`space_to_batch(...)`](../../../tf/compat/v1/space_to_batch.md): SpaceToBatch for 4-D tensors of type T.

[`space_to_depth(...)`](../../../tf/compat/v1/space_to_depth.md): SpaceToDepth for tensors of type T.

[`sparse_softmax_cross_entropy_with_logits(...)`](../../../tf/compat/v1/nn/sparse_softmax_cross_entropy_with_logits.md): Computes sparse softmax cross entropy between `logits` and `labels`.

[`static_bidirectional_rnn(...)`](../../../tf/compat/v1/nn/static_bidirectional_rnn.md): Creates a bidirectional recurrent neural network. (deprecated)

[`static_rnn(...)`](../../../tf/compat/v1/nn/static_rnn.md): Creates a recurrent neural network specified by RNNCell `cell`. (deprecated)

[`static_state_saving_rnn(...)`](../../../tf/compat/v1/nn/static_state_saving_rnn.md): RNN that accepts a state saver for time-truncated RNN calculation. (deprecated)

[`sufficient_statistics(...)`](../../../tf/compat/v1/nn/sufficient_statistics.md): Calculate the sufficient statistics for the mean and variance of `x`.

[`swish(...)`](../../../tf/nn/swish.md): Computes the Swish activation function: `x * sigmoid(x)`.

[`tanh(...)`](../../../tf/math/tanh.md): Computes hyperbolic tangent of `x` element-wise.

[`top_k(...)`](../../../tf/math/top_k.md): Finds values and indices of the `k` largest entries for the last dimension.

[`uniform_candidate_sampler(...)`](../../../tf/random/uniform_candidate_sampler.md): Samples a set of classes using a uniform base distribution.

[`weighted_cross_entropy_with_logits(...)`](../../../tf/compat/v1/nn/weighted_cross_entropy_with_logits.md): Computes a weighted cross entropy. (deprecated arguments)

[`weighted_moments(...)`](../../../tf/compat/v1/nn/weighted_moments.md): Returns the frequency-weighted mean and variance of `x`.

[`with_space_to_batch(...)`](../../../tf/nn/with_space_to_batch.md): Performs `op` on the space-to-batch representation of `input`.

[`xw_plus_b(...)`](../../../tf/compat/v1/nn/xw_plus_b.md): Computes matmul(x, weights) + biases.

[`zero_fraction(...)`](../../../tf/math/zero_fraction.md): Returns the fraction of zeros in `value`.

