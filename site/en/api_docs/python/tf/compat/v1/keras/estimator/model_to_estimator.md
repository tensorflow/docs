page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.keras.estimator.model_to_estimator


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/estimator/__init__.py#L29-L107">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Constructs an `Estimator` instance from given keras model.

``` python
tf.compat.v1.keras.estimator.model_to_estimator(
    keras_model=None,
    keras_model_path=None,
    custom_objects=None,
    model_dir=None,
    config=None,
    checkpoint_format='saver'
)
```



<!-- Placeholder for "Used in" -->

For usage example, please see:
[Creating estimators from Keras
Models](https://tensorflow.org/guide/estimators#model_to_estimator).

__Sample Weights__
Estimators returned by `model_to_estimator` are configured to handle sample
weights (similar to `keras_model.fit(x, y, sample_weights)`). To pass sample
weights when training or evaluating the Estimator, the first item returned by
the input function should be a dictionary with keys `features` and
`sample_weights`. Example below:

```
keras_model = tf.keras.Model(...)
keras_model.compile(...)

estimator = tf.keras.estimator.model_to_estimator(keras_model)

def input_fn():
  return dataset_ops.Dataset.from_tensors(
      ({'features': features, 'sample_weights': sample_weights},
       targets))

estimator.train(input_fn, steps=1)
```

#### Args:


* <b>`keras_model`</b>: A compiled Keras model object. This argument is mutually
  exclusive with `keras_model_path`.
* <b>`keras_model_path`</b>: Path to a compiled Keras model saved on disk, in HDF5
  format, which can be generated with the `save()` method of a Keras model.
  This argument is mutually exclusive with `keras_model`.
* <b>`custom_objects`</b>: Dictionary for custom objects.
* <b>`model_dir`</b>: Directory to save `Estimator` model parameters, graph, summary
  files for TensorBoard, etc.
* <b>`config`</b>: `RunConfig` to config `Estimator`.
* <b>`checkpoint_format`</b>: Sets the format of the checkpoint saved by the estimator
  when training. May be `saver` or `checkpoint`, depending on whether to
  save checkpoints from `tf.train.Saver` or <a href="../../../../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>. This
  argument currently defaults to `saver`. When 2.0 is released, the default
  will be `checkpoint`. Estimators use name-based `tf.train.Saver`
  checkpoints, while Keras models use object-based checkpoints from
  <a href="../../../../../tf/train/Checkpoint"><code>tf.train.Checkpoint</code></a>. Currently, saving object-based checkpoints from
  `model_to_estimator` is only supported by Functional and Sequential
  models.


#### Returns:

An Estimator from given keras model.



#### Raises:


* <b>`ValueError`</b>: if neither keras_model nor keras_model_path was given.
* <b>`ValueError`</b>: if both keras_model and keras_model_path was given.
* <b>`ValueError`</b>: if the keras_model_path is a GCS URI.
* <b>`ValueError`</b>: if keras_model has not been compiled.
* <b>`ValueError`</b>: if an invalid checkpoint_format was given.
