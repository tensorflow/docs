
# Common Signatures for Text

This page describes common signatures that should be implemented by modules in
the [TF1 Hub format](../tf1_hub_module.md) for tasks that accept text inputs.
(For the [TF2 SavedModel format](../tf2_saved_model.md), see the analogous
[SavedModel API](../common_saved_model_apis/text.md).)

## Text feature vector

A **text feature vector** module creates a dense vector representation
from text features.
It accepts a batch of strings of shape `[batch_size]` and maps them to
a `float32` tensor of shape `[batch_size, N]`. This is often called
**text embedding** in dimension `N`.

### Basic usage

```python
  embed = hub.Module("path/to/module")
  representations = embed([
      "A long sentence.",
      "single-word",
      "http://example.com"])
```

### Feature column usage

```python
    feature_columns = [
      hub.text_embedding_column("comment", "path/to/module", trainable=False),
    ]
    input_fn = tf.estimator.inputs.numpy_input_fn(features, labels, shuffle=True)
    estimator = tf.estimator.DNNClassifier(hidden_units, feature_columns)
    estimator.train(input_fn, max_steps=100)
```

## Notes

Modules have been pre-trained on different domains and/or tasks,
and therefore not every text feature vector module would be suitable for
your problem. E.g.: some modules could have been trained on a single language.

This interface does not allow fine-tuning of the text representation on TPUs,
because it requires the module to instantiate both string processing and the
trainable variables at the same time.
