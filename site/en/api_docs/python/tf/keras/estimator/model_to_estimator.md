

page_type: reference


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



Defined in [`tensorflow/python/keras/_impl/keras/estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/keras/_impl/keras/estimator.py).

Constructs an `Estimator` instance from given keras model.

For usage example, please see
<a href="../../../../../programmers_guide/estimators">creating_estimators_from_keras_models</a>.

#### Args:

* <b>`keras_model`</b>: Keras model in memory.
* <b>`keras_model_path`</b>: Directory to a keras model on disk.
* <b>`custom_objects`</b>: Dictionary for custom objects.
* <b>`model_dir`</b>: Directory to save Estimator model parameters, graph and etc.
* <b>`config`</b>: Configuration object.


#### Returns:

An Estimator from given keras model.


#### Raises:

* <b>`ValueError`</b>: if neither keras_model nor keras_model_path was given.
* <b>`ValueError`</b>: if both keras_model and keras_model_path was given.
* <b>`ValueError`</b>: if the keras_model_path is a GCS URI.
* <b>`ValueError`</b>: if keras_model has not been compiled.