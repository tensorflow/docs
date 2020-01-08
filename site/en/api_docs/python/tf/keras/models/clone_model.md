page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.clone_model

``` python
tf.keras.models.clone_model(
    model,
    input_tensors=None
)
```



Defined in [`tensorflow/python/keras/models.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/keras/models.py).

Clone any `Model` instance.

Model cloning is similar to calling a model on new inputs,
except that it creates new layers (and thus new weights) instead
of sharing the weights of the existing layers.

#### Arguments:

* <b>`model`</b>: Instance of `Model`
        (could be a functional model or a Sequential model).
* <b>`input_tensors`</b>: optional list of input tensors
        to build the model upon. If not provided,
        placeholders will be created.


#### Returns:

An instance of `Model` reproducing the behavior
of the original model, on top of new inputs tensors,
using newly instantiated weights.


#### Raises:

* <b>`ValueError`</b>: in case of invalid `model` argument value.