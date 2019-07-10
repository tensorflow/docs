page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.clone_model

Clone any `Model` instance.

### Aliases:

* `tf.compat.v1.keras.models.clone_model`
* `tf.compat.v2.keras.models.clone_model`
* `tf.keras.models.clone_model`

``` python
tf.keras.models.clone_model(
    model,
    input_tensors=None,
    clone_function=None
)
```



Defined in [`python/keras/models.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/models.py).

<!-- Placeholder for "Used in" -->

Model cloning is similar to calling a model on new inputs,
except that it creates new layers (and thus new weights) instead
of sharing the weights of the existing layers.

#### Arguments:


* <b>`model`</b>: Instance of `Model`
    (could be a functional model or a Sequential model).
* <b>`input_tensors`</b>: optional list of input tensors or InputLayer objects
    to build the model upon. If not provided,
    placeholders will be created.
* <b>`clone_function`</b>: Callable to be used to clone each layer in the target
    model (except `InputLayer` instances). It takes as argument the layer
    instance to be cloned, and returns the corresponding layer instance to
    be used in the model copy. If unspecified, this callable defaults to
    the following serialization/deserialization function:
    `lambda layer: layer.__class__.from_config(layer.get_config())`.
    By passing a custom callable, you can customize your copy of the
    model, e.g. by wrapping certain layers of interest (you might want to
    replace all `LSTM` instances with equivalent
    `Bidirectional(LSTM(...))` instances, for example).


#### Returns:

An instance of `Model` reproducing the behavior
of the original model, on top of new inputs tensors,
using newly instantiated weights. The cloned model might behave
differently from the original model if a custom clone_function
modifies the layer.



#### Raises:


* <b>`ValueError`</b>: in case of invalid `model` argument value.