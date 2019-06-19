page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.estimator.model_to_estimator

``` python
tf.keras.estimator.model_to_estimator(
    keras_model=None,
    keras_model_path=None,
    custom_objects=None,
    model_dir=None,
    config=None
)
```



Defined in [`tensorflow/python/estimator/keras.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/estimator/keras.py).

Constructs an `Estimator` instance from given keras model.

For usage example, please see
<a href="../../../../../guide/estimators">creating_estimators_from_keras_models</a>.

#### Args:

* <b>`keras_model`</b>: A compiled Keras model object. This argument is mutually
    exclusive with `keras_model_path`.
* <b>`keras_model_path`</b>: Path to a compiled Keras model saved on disk, in HDF5
    format, which can be generated with the `save()` method of a Keras model.
    This argument is mutually exclusive with `keras_model`.
* <b>`custom_objects`</b>: Dictionary for custom objects.
* <b>`model_dir`</b>: Directory to save Estimator model parameters, graph, summary
    files for TensorBoard, etc.
* <b>`config`</b>: Configuration object.


#### Returns:

An Estimator from given keras model.


#### Raises:

* <b>`ValueError`</b>: if neither keras_model nor keras_model_path was given.
* <b>`ValueError`</b>: if both keras_model and keras_model_path was given.
* <b>`ValueError`</b>: if the keras_model_path is a GCS URI.
* <b>`ValueError`</b>: if keras_model has not been compiled.