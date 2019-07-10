page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.experimental.export_saved_model

Exports a <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a> as a Tensorflow SavedModel.

### Aliases:

* `tf.compat.v1.keras.experimental.export_saved_model`
* `tf.compat.v2.keras.experimental.export_saved_model`
* `tf.contrib.saved_model.save_keras_model`
* `tf.keras.experimental.export_saved_model`

``` python
tf.keras.experimental.export_saved_model(
    model,
    saved_model_path,
    custom_objects=None,
    as_text=False,
    input_signature=None,
    serving_only=False
)
```



Defined in [`python/keras/saving/saved_model.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/saving/saved_model.py).

<!-- Placeholder for "Used in" -->

Note that at this time, subclassed models can only be saved using
`serving_only=True`.

The exported `SavedModel` is a standalone serialization of Tensorflow objects,
and is supported by TF language APIs and the Tensorflow Serving system.
To load the model, use the function
<a href="../../../tf/keras/experimental/load_from_saved_model"><code>tf.keras.experimental.load_from_saved_model</code></a>.

The `SavedModel` contains:

1. a checkpoint containing the model weights.
2. a `SavedModel` proto containing the Tensorflow backend graph. Separate
   graphs are saved for prediction (serving), train, and evaluation. If
   the model has not been compiled, then only the graph computing predictions
   will be exported.
3. the model's json config. If the model is subclassed, this will only be
   included if the model's `get_config()` method is overwritten.

#### Example:



```python
import tensorflow as tf

# Create a tf.keras model.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=[10]))
model.summary()

# Save the tf.keras model in the SavedModel format.
path = '/tmp/simple_keras_model'
tf.keras.experimental.export_saved_model(model, path)

# Load the saved keras model back.
new_model = tf.keras.experimental.load_from_saved_model(path)
new_model.summary()
```

#### Args:


* <b>`model`</b>: A <a href="../../../tf/keras/Model"><code>tf.keras.Model</code></a> to be saved. If the model is subclassed, the flag
  `serving_only` must be set to True.
* <b>`saved_model_path`</b>: a string specifying the path to the SavedModel directory.
* <b>`custom_objects`</b>: Optional dictionary mapping string names to custom classes
  or functions (e.g. custom loss functions).
* <b>`as_text`</b>: bool, `False` by default. Whether to write the `SavedModel` proto
  in text format. Currently unavailable in serving-only mode.
* <b>`input_signature`</b>: A possibly nested sequence of <a href="../../../tf/TensorSpec"><code>tf.TensorSpec</code></a> objects, used
  to specify the expected model inputs. See <a href="../../../tf/function"><code>tf.function</code></a> for more details.
* <b>`serving_only`</b>: bool, `False` by default. When this is true, only the
  prediction graph is saved.


#### Raises:


* <b>`NotImplementedError`</b>: If the model is a subclassed model, and serving_only is
  False.
* <b>`ValueError`</b>: If the input signature cannot be inferred from the model.
* <b>`AssertionError`</b>: If the SavedModel directory already exists and isn't empty.