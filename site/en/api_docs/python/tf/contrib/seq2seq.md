

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# Module: tf.contrib.seq2seq



Defined in [`tensorflow/contrib/seq2seq/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/seq2seq/__init__.py).

Ops for building neural network seq2seq decoders and losses.

See the <a href="../../../../api_guides/python/contrib.seq2seq">Seq2seq Library (contrib)</a> guide.

## Classes

[`class AttentionMechanism`](../../tf/contrib/seq2seq/AttentionMechanism)

[`class AttentionWrapper`](../../tf/contrib/seq2seq/AttentionWrapper): Wraps another `RNNCell` with attention.

[`class AttentionWrapperState`](../../tf/contrib/seq2seq/AttentionWrapperState): `namedtuple` storing the state of a `AttentionWrapper`.

[`class BahdanauAttention`](../../tf/contrib/seq2seq/BahdanauAttention): Implements Bahdanau-style (additive) attention.

[`class BahdanauMonotonicAttention`](../../tf/contrib/seq2seq/BahdanauMonotonicAttention): Monotonic attention mechanism with Bahadanau-style energy function.

[`class BasicDecoder`](../../tf/contrib/seq2seq/BasicDecoder): Basic sampling decoder.

[`class BasicDecoderOutput`](../../tf/contrib/seq2seq/BasicDecoderOutput)

[`class BeamSearchDecoder`](../../tf/contrib/seq2seq/BeamSearchDecoder): BeamSearch sampling decoder.

[`class BeamSearchDecoderOutput`](../../tf/contrib/seq2seq/BeamSearchDecoderOutput)

[`class BeamSearchDecoderState`](../../tf/contrib/seq2seq/BeamSearchDecoderState)

[`class CustomHelper`](../../tf/contrib/seq2seq/CustomHelper): Base abstract class that allows the user to customize sampling.

[`class Decoder`](../../tf/contrib/seq2seq/Decoder): An RNN Decoder abstract interface object.

[`class FinalBeamSearchDecoderOutput`](../../tf/contrib/seq2seq/FinalBeamSearchDecoderOutput): Final outputs returned by the beam search after all decoding is finished.

[`class GreedyEmbeddingHelper`](../../tf/contrib/seq2seq/GreedyEmbeddingHelper): A helper for use during inference.

[`class Helper`](../../tf/contrib/seq2seq/Helper): Interface for implementing sampling in seq2seq decoders.

[`class InferenceHelper`](../../tf/contrib/seq2seq/InferenceHelper): A helper to use during inference with a custom sampling function.

[`class LuongAttention`](../../tf/contrib/seq2seq/LuongAttention): Implements Luong-style (multiplicative) attention scoring.

[`class LuongMonotonicAttention`](../../tf/contrib/seq2seq/LuongMonotonicAttention): Monotonic attention mechanism with Luong-style energy function.

[`class SampleEmbeddingHelper`](../../tf/contrib/seq2seq/SampleEmbeddingHelper): A helper for use during inference.

[`class ScheduledEmbeddingTrainingHelper`](../../tf/contrib/seq2seq/ScheduledEmbeddingTrainingHelper): A training helper that adds scheduled sampling.

[`class ScheduledOutputTrainingHelper`](../../tf/contrib/seq2seq/ScheduledOutputTrainingHelper): A training helper that adds scheduled sampling directly to outputs.

[`class TrainingHelper`](../../tf/contrib/seq2seq/TrainingHelper): A helper for use during training.  Only reads inputs.

## Functions

[`dynamic_decode(...)`](../../tf/contrib/seq2seq/dynamic_decode): Perform dynamic decoding with `decoder`.

[`gather_tree(...)`](../../tf/contrib/seq2seq/gather_tree): Calculates the full beams from the per-step ids and parent beam ids.

[`hardmax(...)`](../../tf/contrib/seq2seq/hardmax): Returns batched one-hot vectors.

[`monotonic_attention(...)`](../../tf/contrib/seq2seq/monotonic_attention): Compute monotonic attention distribution from choosing probabilities.

[`safe_cumprod(...)`](../../tf/contrib/seq2seq/safe_cumprod): Computes cumprod of x in logspace using cumsum to avoid underflow.

[`sequence_loss(...)`](../../tf/contrib/seq2seq/sequence_loss): Weighted cross-entropy loss for a sequence of logits.

[`tile_batch(...)`](../../tf/contrib/seq2seq/tile_batch): Tile the batch dimension of a (possibly nested structure of) tensor(s) t.

