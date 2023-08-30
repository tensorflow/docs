# Text Cookbook

This page lists a set of known guides and tools solving problems in the text
domain with TensorFlow Hub. It is a starting place for anybody who wants to
solve typical ML problems using pre-trained ML components rather than starting
from scratch.

## Classification

When we want to predict a class for a given example, for example **sentiment**,
**toxicity**, **article category**, or any other characteristic.

![Text Classification Graphic](https://www.gstatic.com/aihub/tfhub/universal-sentence-encoder/example-classification.png)

The tutorials below are solving the same task from different perspectives and
using different tools.

### Keras

[Text classification with Keras](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub) -
example for building an IMDB sentiment classifier with Keras and TensorFlow
Datasets.

### Estimator

[Text classification](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/text_classification_with_tf_hub.ipynb) -
example for building an IMDB sentiment classifier with Estimator. Contains
multiple tips for improvement and a module comparison section.

### BERT
[Predicting Movie Review Sentiment with BERT on TF Hub](https://github.com/google-research/bert/blob/master/predicting_movie_reviews_with_bert_on_tf_hub.ipynb) -
shows how to use a BERT module for classification. Includes use of `bert`
library for tokenization and preprocessing.

### Kaggle

[IMDB classification on Kaggle](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/text_classification_with_tf_hub_on_kaggle.ipynb) -
shows how to easily interact with a Kaggle competition from a Colab, including
downloading the data and submitting the results.

                                                                                                                                                                                         | Estimator                                                                                         | Keras                                                                                             | TF2                                                                                               | TF Datasets                                                                                       | BERT                                                                                              | Kaggle APIs
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -----------
[Text classification](https://www.tensorflow.org/hub/tutorials/text_classification_with_tf_hub)                                                                                          | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) |                                                                                                   |                                                                                                   |                                                                                                   |                                                                                                   |
[Text classification with Keras](https://www.tensorflow.org/tutorials/keras/text_classification_with_hub)                                                                                |                                                                                                   | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) |                                                                                                   |
[Predicting Movie Review Sentiment with BERT on TF Hub](https://github.com/google-research/bert/blob/master/predicting_movie_reviews_with_bert_on_tf_hub.ipynb)                          | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) |                                                                                                   |                                                                                                   |                                                                                                   | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) |
[IMDB classification on Kaggle](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/text_classification_with_tf_hub_on_kaggle.ipynb) | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png) |                                                                                                   |                                                                                                   |                                                                                                   |                                                                                                   | ![done](https://www.gstatic.com/images/icons/material/system_gm/1x/bigtop_done_googblue_18dp.png)

### Bangla task with FastText embeddings
TensorFlow Hub does not currently offer a module in every language. The
following tutorial shows how to leverage TensorFlow Hub for fast experimentation
and modular ML development.

[Bangla Article Classifier](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/bangla_article_classifier.ipynb) -
demonstrates how to create a reusable TensorFlow Hub text embedding, and use it
to train a Keras classifier for
[BARD Bangla Article dataset](https://github.com/tanvirfahim15/BARD-Bangla-Article-Classifier).

## Semantic similarity

When we want to find out which sentences correlate with each other in zero-shot
setup (no training examples).

![Semantic Similarity Graphic](https://www.gstatic.com/aihub/tfhub/universal-sentence-encoder/example-similarity.png)

### Basic

[Semantic similarity](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder.ipynb) -
shows how to use the sentence encoder module to compute sentence similarity.

### Cross-lingual

[Cross-lingual semantic similarity](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/cross_lingual_similarity_with_tf_hub_multilingual_universal_encoder.ipynb) -
shows how to use one of the cross-lingual sentence encoders to compute sentence
similarity across languages.

### Semantic retrieval

[Semantic retrieval](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa.ipynb) -
shows how to use Q/A sentence encoder to index a collection of documents for
retrieval based on semantic similarity.

### SentencePiece input

[Semantic similarity with universal encoder lite](https://github.com/tensorflow/docs/blob/master/g3doc/en/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite.ipynb) -
shows how to use sentence encoder modules that accept
[SentencePiece](https://github.com/google/sentencepiece) ids on input instead of
text.

## Module creation
Instead of using only modules on [tfhub.dev](https://tfhub.dev), there are ways
to create own modules. This can be a useful tool for better ML codebase
modularity and for further sharing.

### Wrapping existing pre-trained embeddings
[Text embedding module exporter](https://github.com/tensorflow/hub/blob/master/examples/text_embeddings/export.py) -
a tool to wrap an existing pre-trained embedding into a module. Shows how to
include text pre-processing ops into the module. This allows to create a
sentence embedding module from token embeddings.

[Text embedding module exporter v2](https://github.com/tensorflow/hub/blob/master/examples/text_embeddings_v2/export_v2.py) -
same as above, but compatible with TensorFlow 2 and eager execution.
