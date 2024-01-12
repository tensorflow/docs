
# TensorFlow Hub Library Overview

The [`tensorflow_hub`](https://github.com/tensorflow/hub) library lets you
download and reuse trained models in your TensorFlow program with a minimum
amount of code. The main way to load a trained model is using the
`hub.KerasLayer` API.

```python
import tensorflow_hub as hub

embed = hub.KerasLayer("https://tfhub.dev/google/nnlm-en-dim128/2")
embeddings = embed(["A long sentence.", "single-word", "http://example.com"])
print(embeddings.shape, embeddings.dtype)
```
**Note:** This documentation uses TFhub.dev URL handles in examples. See more
information regarding other valid handle types [here](tf2_saved_model.md#model_handles).

## Setting the cache location for downloads.

By default, `tensorflow_hub` uses a system-wide, temporary directory to cache
downloaded and uncompressed models. See [Caching](caching.md) for options to use
other, possibly more persistent locations.

## API stability

Although we hope to prevent breaking changes, this project is still under active
development and is not yet guaranteed to have a stable API or model format.

## Fairness

As in all of machine learning, [fairness](http://ml-fairness.com) is an
[important](https://research.googleblog.com/2016/10/equality-of-opportunity-in-machine.html)
consideration. Many pre-trained models are trained on large datasets. When
reusing any model, it’s important to be mindful of what data the model was
trained on (and whether there are any existing biases there), and how these
might impact your use of it.

## Security

Since they contain arbitrary TensorFlow graphs, models can be thought of as
programs.
[Using TensorFlow Securely](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md)
describes the security implications of referencing a model from an untrusted
source.

## Next Steps

-   [Use the library](tf2_saved_model.md)
-   [Reusable SavedModels](reusable_saved_models.md)
