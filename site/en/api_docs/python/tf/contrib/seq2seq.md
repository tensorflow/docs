

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# Module: tf.contrib.seq2seq

### Module `tf.contrib.seq2seq`



Defined in [`tensorflow/contrib/seq2seq/__init__.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/__init__.py).

Ops for building neural network seq2seq decoders and losses.

See the [Seq2seq Library (contrib)](../../../../api_guides/python/contrib.seq2seq) guide.







## Classes

[`class BahdanauAttention`](../../tf/contrib/seq2seq/BahdanauAttention): Implements Bhadanau-style (additive) attention.

[`class BasicDecoder`](../../tf/contrib/seq2seq/BasicDecoder): Basic sampling decoder.

[`class BasicDecoderOutput`](../../tf/contrib/seq2seq/BasicDecoderOutput)

[`class CustomHelper`](../../tf/contrib/seq2seq/CustomHelper): Base abstract class that allows the user to customize sampling.

[`class Decoder`](../../tf/contrib/seq2seq/Decoder): An RNN Decoder abstract interface object.

[`class DynamicAttentionWrapper`](../../tf/contrib/seq2seq/DynamicAttentionWrapper): Wraps another `RNNCell` with attention.

[`class DynamicAttentionWrapperState`](../../tf/contrib/seq2seq/DynamicAttentionWrapperState): `namedtuple` storing the state of a `DynamicAttentionWrapper`.

[`class GreedyEmbeddingHelper`](../../tf/contrib/seq2seq/GreedyEmbeddingHelper): A helper for use during inference.

[`class Helper`](../../tf/contrib/seq2seq/Helper): Helper interface.  Helper instances are used by SamplingDecoder.

[`class LuongAttention`](../../tf/contrib/seq2seq/LuongAttention): Implements Luong-style (multiplicative) attention scoring.

[`class ScheduledEmbeddingTrainingHelper`](../../tf/contrib/seq2seq/ScheduledEmbeddingTrainingHelper): A training helper that adds scheduled sampling.

[`class ScheduledOutputTrainingHelper`](../../tf/contrib/seq2seq/ScheduledOutputTrainingHelper): A training helper that adds scheduled sampling directly to outputs.

[`class TrainingHelper`](../../tf/contrib/seq2seq/TrainingHelper): A helper for use during training.  Only reads inputs.

## Functions

[`dynamic_decode(...)`](../../tf/contrib/seq2seq/dynamic_decode): Perform dynamic decoding with `decoder`.

[`hardmax(...)`](../../tf/contrib/seq2seq/hardmax): Returns batched one-hot vectors.

[`sequence_loss(...)`](../../tf/contrib/seq2seq/sequence_loss): Weighted cross-entropy loss for a sequence of logits (per example).

