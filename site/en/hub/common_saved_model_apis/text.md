
# Common SavedModel APIs for Text Tasks

This page describes how [TF2 SavedModels](../tf2_saved_model.md) for
text-related tasks should implement the
[Reusable SavedModel API](../reusable_saved_models.md). (This replaces and
extends the [Common Signatures for Text](../common_signatures/text.md) for the
now-deprecated [TF1 Hub format](../tf1_hub_module).)

## Overview

There are several APIs to compute **text embeddings** (also known as dense
representations of text, or text feature vectors).

*   The API for *text embeddings from text inputs* is implemented by a
    SavedModel that maps a batch of strings to a batch of embedding vectors.
    This is very easy to use, and many models on TF Hub have implemented it.
    However, this does not allow fine-tuning the model on TPU.

*   The API for *text embeddings with preprocessed inputs* solves the same task,
    but is implemented by two separate SavedModels:

    *   a *preprocessor* that can run inside a tf.data input pipeline and
        converts strings and other variable-length data into numeric Tensors,
    *   an *encoder* that accepts the results of the preprocessor and performs
        the trainable part of the embedding computation.

    This split allows inputs to be preprocessed asynchronously before being fed
    into the training loop. In particular, it allows building encoders that can
    be run and fine-tuned on [TPU](https://www.tensorflow.org/guide/tpu).

*   The API for *text embeddings with Transformer encoders* extends the API for
    text embeddings from preprocessed inputs to the particular case of BERT and
    other Transformer encoders.

    *   The *preprocessor* is extended to build encoder inputs from more than
        one segment of input text.
    *   The *Transformer encoder* exposes the context-aware embeddings of
        individual tokens.

In each case, the text inputs are UTF-8 encoded strings, typically of plain
text, unless the model documentation provides otherwise.

Regardless of API, different models have been pre-trained on text from different
languages and domains, and with different tasks in mind. Therefore, not every
text embedding model is suitable for every problem.

<a name="feature-vector"></a>
<a name="text-embeddings-from-text"></a>

## Text Embedding from Text Inputs

A SavedModel for **text embeddings from text inputs** accepts a batch of inputs
in a string Tensor of shape `[batch_size]` and maps them to a float32 Tensor of
shape `[batch_size, dim]` with dense representations (feature vectors) of the
inputs.

### Usage synopsis

```python
obj = hub.load("path/to/model")
text_input = ["A long sentence.",
              "single-word",
              "http://example.com"]
embeddings = obj(text_input)
```

Recall from the [Reusable SavedModel API](../reusable_saved_models.md) that
running the model in training mode (e.g., for dropout) may require a keyword
argument `obj(..., training=True)`, and that `obj` provides attributes
`.variables`, `.trainable_variables` and `.regularization_losses` as applicable.

In Keras, all this is taken care of by

```python
embeddings = hub.KerasLayer("path/to/model", trainable=...)(text_input)
```

### Distributed training

If the text embedding is used as part of a model that gets trained with a
distribution strategy, the call to `hub.load("path/to/model")` or
`hub.KerasLayer("path/to/model", ...)`, resp., must happen inside the
DistributionStrategy scope in order to create the model's variables in the
distributed way. For example

```python
  with strategy.scope():
    ...
    model = hub.load("path/to/model")
    ...
```

### Examples

*   Colab tutorial
    [Text Classification with Movie Reviews](https://colab.research.google.com/github/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/tf2_text_classification.ipynb).

<a name="text-embeddings-preprocessed"></a>

## Text Embeddings with Preprocessed Inputs

A **text embedding with preprocessed inputs** is implemented by two separate
SavedModels:

*   a **preprocessor** that maps a string Tensor of shape `[batch_size]` to a
    dict of numeric Tensors,
*   an **encoder** that accepts a dict of Tensors as returned by the
    preprocessor, performs the trainable part of the embedding computation, and
    returns a dict of outputs. The output under key `"default"` is a float32
    Tensor of shape `[batch_size, dim]`.

This allows to run the preprocessor in an input pipeline but fine-tune the
embeddings computed by the encoder as part of a larger model. In particular, it
allows to build encoders that can be run and fine-tuned on
[TPU](https://www.tensorflow.org/guide/tpu).

It is an implementation detail which Tensors are contained in the preprocessor's
output, and which (if any) additional Tensors besides `"default"` are contained
in the encoder's output.

The documentation of the encoder must specify which preprocessor to use with it.
Typically, there is exactly one correct choice.

### Usage synopsis

```python
text_input = tf.constant(["A long sentence.",
                          "single-word",
                          "http://example.com"])
preprocessor = hub.load("path/to/preprocessor")  # Must match `encoder`.
encoder_inputs = preprocessor(text_input)

encoder = hub.load("path/to/encoder")
enocder_outputs = encoder(encoder_inputs)
embeddings = enocder_outputs["default"]
```

Recall from the [Reusable SavedModel API](../reusable_saved_models.md) that
running the encoder in training mode (e.g., for dropout) may require a keyword
argument `encoder(..., training=True)`, and that `encoder` provides attributes
`.variables`, `.trainable_variables` and `.regularization_losses` as applicable.

The `preprocessor` model may have `.variables` but is not meant to be trained
further. Preprocessing is not mode-dependent: if `preprocessor()` has a
`training=...` argument at all, it has no effect.

In Keras, all this is taken care of by

```python
encoder_inputs = hub.KerasLayer("path/to/preprocessor")(text_input)
encoder_outputs = hub.KerasLayer("path/to/encoder", trainable=True)(encoder_inputs)
embeddings = encoder_outputs["default"]
```

### Distributed training

If the encoder is used as part of a model that gets trained with a distribution
strategy, the call to `hub.load("path/to/encoder")` or
`hub.KerasLayer("path/to/encoder", ...)`, resp., must happen inside

```python
  with strategy.scope():
    ...
```

in order to re-create the encoder variables in the distributed way.

Likewise, if the preprocessor is part of the trained model (as in the simple
example above), it also needs to be loaded under the distribution strategy
scope. If, however, the preprocessor is used in an input pipeline (e.g., in a
callable passed to `tf.data.Dataset.map()`), its loading must happen *outside*
the distribution strategy scope, in order to place its variables (if any) on the
host CPU.

### Examples

*   Colab tutorial
    [Classify text with BERT](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/text/classify_text_with_bert.ipynb).

<a name="transformer-encoders"></a>

## Text embeddings with Transformer Encoders

Transformer encoders for text operate on a batch of input sequences, each
sequence comprising *n* ≥ 1 segments of tokenized text, within some
model-specific bound on *n*. For BERT and many of its extensions, that bound is
2, so they accept single segments and segment pairs.

The API for **text embeddings with Transformer encoders** extends the API for
text embeddings with preprocessed inputs to this setting.

### Preprocessor

A preprocessor SavedModel for text embeddings with Transformer encoders
implements the API of a preprocessor SavedModel for text embeddings with
preprocessed inputs (see above), which provides a way to map single-segment text
inputs directly to encoder inputs.

In addition, the preprocessor SavedModel provides callable subobjects `tokenize`
for tokenization (separately per segment) and `bert_pack_inputs` for packing *n*
tokenized segments into one input sequence for the encoder. Each subobject
follows the [Reusable SavedModel API](../reusable_saved_models.md).

#### Usage synopsis

As a concrete example for two segments of text, let us look at a sentence
entailment task that asks whether a premise (first segment) does or does not
imply a hypothesis (second segment).

```python
preprocessor = hub.load("path/to/preprocessor")

# Tokenize batches of both text inputs.
text_premises = tf.constant(["The quick brown fox jumped over the lazy dog.",
                             "Good day."])
tokenized_premises = preprocessor.tokenize(text_premises)
text_hypotheses = tf.constant(["The dog was lazy.",  # Implied.
                               "Axe handle!"])       # Not implied.
tokenized_hypotheses = preprocessor.tokenize(text_hypotheses)

# Pack input sequences for the Transformer encoder.
seq_length = 128
encoder_inputs = preprocessor.bert_pack_inputs(
    [tokenized_premises, tokenized_hypotheses],
    seq_length=seq_length)  # Optional argument.
```

In Keras, this computation can be expressed as

```python
tokenize = hub.KerasLayer(preprocessor.tokenize)
tokenized_hypotheses = tokenize(text_hypotheses)
tokenized_premises = tokenize(text_premises)

bert_pack_inputs = hub.KerasLayer(
    preprocessor.bert_pack_inputs,
    arguments=dict(seq_length=seq_length))  # Optional argument.
encoder_inputs = bert_pack_inputs([tokenized_premises, tokenized_hypotheses])
```

#### Details of `tokenize`

A call to `preprocessor.tokenize()` accepts a string Tensor of shape
`[batch_size]` and returns a
[RaggedTensor](https://www.tensorflow.org/guide/ragged_tensor) of shape
`[batch_size, ...]` whose values are int32 token ids representing the input
strings. There can be *r* ≥ 1 ragged dimensions after `batch_size` but no other
uniform dimension.

*   If *r*=1, the shape is `[batch_size, (tokens)]`, and each input is simply
    tokenized into a flat sequence of tokens.
*   If *r*>1, there are *r*-1 additional levels of grouping. For example,
    [tensorflow_text.BertTokenizer](https://github.com/tensorflow/text/blob/v2.3.0/tensorflow_text/python/ops/bert_tokenizer.py#L138)
    uses *r*=2 to group tokens by words and yields shape `[batch_size, (words),
    (tokens_per_word)]`. It is up to the model at hand how many of these extra
    level(s) exist, if any, and what groupings they represent.

The user can (but need not) modify tokenized inputs, e.g., to accommodate the
seq_length limit that will be enforced in packing encoder inputs. Extra
dimensions in the tokenizer output can help here (e.g., to respect word
boundaries) but become meaningless in the next step.

In terms of the [Reusable SavedModel API](../reusable_saved_models.md), the
`preprocessor.tokenize` object may have `.variables` but is not meant to be
trained further. Tokenization is not mode-dependent: if
`preprocessor.tokenize()` has a `training=...` argument at all, it has no
effect.

#### Details of `bert_pack_inputs`

A call to `preprocessor.bert_pack_inputs()` accepts a Python list of tokenized
inputs (batched separately for each input segment) and returns a dict of Tensors
representing a batch of fixed-length input sequences for the Transformer encoder
model.

Each tokenized input is an int32 RaggedTensor of shape `[batch_size, ...]`,
where the number *r* of ragged dimensions after batch_size is either 1 or the
same as in the output of `preprocessor.tokenize().` (The latter is for
convenience only; the extra dimensions are flattened out before packing.)

Packing adds special tokens around the input segments as expected by the
encoder. The `bert_pack_inputs()` call implements exactly the packing scheme
used by the original BERT models and many of their extensions: the packed
sequence starts with one start-of-sequence token, followed by the tokenized
segments, each terminated by one end-of-segment token. Remaining positions up to
seq_length, if any, are filled up with padding tokens.

If a packed sequence would exceed seq_length, `bert_pack_inputs()` truncates its
segments to prefixes of approximately equal sizes so that the packed sequence
fits exactly within seq_length.

Packing is not mode-dependent: if `preprocessor.bert_pack_inputs()` has a
`training=...` argument at all, it has no effect. Also,
`preprocessor.bert_pack_inputs` is not expected to have variables, or support
fine-tuning.

### Encoder

The encoder is called on the dict of `encoder_inputs` in the same way as in the
API for text embeddings with preprocessed inputs (see above), including the
provisions from the [Reusable SavedModel API](../reusable_saved_models.md).

#### Usage synopsis

```python
enocder = hub.load("path/to/encoder")
enocder_outputs = encoder(encoder_inputs)
```

or equivalently in Keras:

```python
encoder = hub.KerasLayer("path/to/encoder", trainable=True)
encoder_outputs = encoder(encoder_inputs)
```

#### Details

The `encoder_outputs` are a dict of Tensors with the following keys.
<!-- TODO(b/172561269): More guidance for models trained without poolers. -->

*   `"sequence_output"`: a float32 Tensor of shape `[batch_size, seq_length,
    dim]` with the context-aware embedding of each token of every packed input
    sequence.
*   `"pooled_output"`: a float32 Tensor of shape `[batch_size, dim]` with the
    embedding of each input sequence as a whole, derived from sequence_output in
    some trainable manner.
*   `"default"`, as required by the API for text embeddings with preprocessed
    inputs: a float32 Tensor of shape `[batch_size, dim]` with the embedding of
    each input sequence. (This might be just an alias of pooled_output.)

The contents of the `encoder_inputs` are not strictly required by this API
definition. However, for encoders that use BERT-style inputs, it is recommended
to use the following names (from the
[NLP Modeling Toolkit of TensorFlow Model Garden](https://github.com/tensorflow/models/tree/master/official/nlp))
to minimize friction in interchanging encoders and reusing preprocessor models:

*   `"input_word_ids"`: an int32 Tensor of shape `[batch_size, seq_length]` with
    the token ids of the packed input sequence (that is, including a
    start-of-sequence token, end-of-segment tokens, and padding).
*   `"input_mask"`: an int32 Tensor of shape `[batch_size, seq_length]` with
    value 1 at the position of all input tokens present before padding and value
    0 for the padding tokens.
*   `"input_type_ids"`: an int32 Tensor of shape `[batch_size, seq_length]` with
    the index of the input segment that gave rise to the input token at the
    respective position. The first input segment (index 0) includes the
    start-of-sequence token and its end-of-segment token. The second and later
    segments (if present) include their respective end-of-segment token. Padding
    tokens get index 0 again.

### Distributed training

For loading the preprocessor and encoder objects inside or outside a
distribution strategy scope, the same rules apply as in the API for text
embeddings with preprocessed inputs (see above).

### Examples

*   Colab tutorial
    [Solve GLUE tasks using BERT on TPU](https://colab.research.google.com/github/tensorflow/text/blob/master/docs/tutorials/bert_glue.ipynb).
