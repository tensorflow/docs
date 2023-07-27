# Text and natural language processing with TensorFlow

Before you can train a model on text data, you'll typically need to process
(or preprocess) the text. In many cases, text needs to be tokenized and
vectorized before it can be fed to a model, and in some cases the text requires
additional preprocessing steps such as normalization and feature selection.

After text is processed into a suitable format, you can use it in natural
language processing (NLP) workflows such as text classification, text
generation, summarization, and translation.

TensorFlow provides two libraries for text and natural language processing:
KerasNLP ([GitHub](https://github.com/keras-team/keras-nlp)) and
TensorFlow Text ([GitHub](https://github.com/tensorflow/text)).

KerasNLP is a high-level NLP modeling library that includes all the latest
transformer-based models as well as lower-level tokenization utilities. It's the
recommended solution for most NLP use cases. Built on TensorFlow Text, KerasNLP
abstracts low-level text processing operations into an API that's designed for
ease of use. But if you prefer not to work with the Keras API, or you need
access to the lower-level text processing ops, you can use TensorFlow Text
directly.

## KerasNLP

The easiest way to get started processing text in TensorFlow is to use
[KerasNLP](https://keras.io/keras_nlp/). KerasNLP is a natural language
processing library that supports workflows built from modular components that
have state-of-the-art preset weights and architectures. You can use KerasNLP
components with their out-of-the-box configuration. If you need more control,
you can easily customize components. KerasNLP provides in-graph computation for
all workflows so you can expect easy productionization using the TensorFlow
ecosystem.

KerasNLP contains end-to-end implementations of popular
[model architectures](https://keras.io/api/keras_nlp/models/) like
[BERT](https://keras.io/api/keras_nlp/models/bert/) and
[FNet](https://keras.io/api/keras_nlp/models/f_net/). Using KerasNLP models,
layers, and tokenizers, you can complete many state-of-the-art NLP workflows,
including
[machine translation](https://keras.io/examples/nlp/neural_machine_translation_with_keras_nlp/),
[text generation](https://keras.io/examples/generative/text_generation_gpt/),
[text classification](https://keras.io/examples/nlp/fnet_classification_with_keras_nlp/),
and
[transformer model training](https://keras.io/guides/keras_nlp/transformer_pretraining/).

KerasNLP is an extension of the core Keras API, and every high-level KerasNLP
module is a `Layer` or `Model`. If you're familiar with Keras, you already
understand most of KerasNLP.

## TensorFlow Text

KerasNLP provides high-level text processing modules that are available as
layers or models. If you need access to lower-level tools, you can use
[TensorFlow Text](https://www.tensorflow.org/text/guide/tf_text_intro).
TensorFlow Text provides operations and libraries to help you work with raw text
strings and documents. TensorFlow Text can perform the preprocessing regularly
required by text-based models, and it also includes other features useful for
sequence modeling.

Using TensorFlow Text, you can do the following:

* Apply feature-rich tokenizers that can split strings on whitespace, separate
  words and punctuation, and return byte offsets with tokens, so that you know
  where a string can be found in the source text.
* Check if a token matches a specified string pattern. You can check for
  capitalization, punctuation, numerical data, and other token features.
* Combine tokens into n-grams.
* Process text within the TensorFlow graph, so that tokenization during training
  matches tokenization at inference.

## Where to start

The following resources will help you get started with TensorFlow text
processing:

* [TensorFlow Text](https://www.tensorflow.org/text): Tutorials, guides, and
  other resources to help you process text using TensorFlow Text and KerasNLP.
* [KerasNLP](https://keras.io/keras_nlp/): Documentation and resources for
  KerasNLP.
  * [Getting Started with KerasNLP](https://keras.io/guides/keras_nlp/getting_started/)
  * [Pretraining a Transformer from scratch with KerasNLP](https://keras.io/guides/keras_nlp/transformer_pretraining/)
* [TensorFlow tutorials](https://www.tensorflow.org/tutorials): The core
  TensorFlow documentation (this guide) includes several text processing
  tutorials.
  * [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification)
  * [Text classification with TensorFlow Hub: Movie reviews](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)
  * [Load text](https://www.tensorflow.org/tutorials/load_data/text)
* [Google Machine Learning: Text Classification guide](https://developers.google.com/machine-learning/guides/text-classification):
  A step-by-step introduction to text classification. This is a good place to
  start if you're new to machine learning.