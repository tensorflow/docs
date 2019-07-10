page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v2.lite.TFLiteConverter

## Class `TFLiteConverter`

Converts a TensorFlow model into TensorFlow Lite model.





Defined in [`lite/python/lite.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/lite/python/lite.py).

<!-- Placeholder for "Used in" -->


#### Attributes:


* <b>`allow_custom_ops`</b>: Boolean indicating whether to allow custom operations.
  When false any unknown operation is an error. When true, custom ops are
  created for any op that is unknown. The developer will need to provide
  these to the TensorFlow Lite runtime with a custom resolver.
  (default False)
* <b>`target_spec`</b>: Experimental flag, subject to change. Specification of target
  device.
* <b>`optimizations`</b>: Experimental flag, subject to change. A list of optimizations
  to apply when converting the model. E.g. `[Optimize.DEFAULT]
* <b>`representative_dataset`</b>: A representative dataset that can be used to
  generate input and output samples for the model. The converter can use the
  dataset to evaluate different optimizations.


#### Example usage:


```python
# Converting a SavedModel to a TensorFlow Lite model.
converter = lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

# Converting a tf.Keras model to a TensorFlow Lite model.
converter = lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Converting ConcreteFunctions to a TensorFlow Lite model.
converter = lite.TFLiteConverter.from_concrete_functions([func])
tflite_model = converter.convert()
```


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    funcs,
    trackable_obj=None
)
```

Constructor for TFLiteConverter.


#### Args:


* <b>`funcs`</b>: List of TensorFlow ConcreteFunctions. The list should not contain
  duplicate elements.
* <b>`trackable_obj`</b>: tf.AutoTrackable object associated with `funcs`. A
  reference to this object needs to be maintained so that Variables do not
  get garbage collected since functions have a weak reference to
  Variables. This is only required when the tf.AutoTrackable object is not
  maintained by the user (e.g. `from_saved_model`).



## Methods

<h3 id="convert"><code>convert</code></h3>

``` python
convert()
```

Converts a TensorFlow GraphDef based on instance variables.


#### Returns:

The converted data in serialized format.



#### Raises:


* <b>`ValueError`</b>:   Multiple concrete functions are specified.
  Input shape is not specified.
  Invalid quantization parameters.

<h3 id="from_concrete_functions"><code>from_concrete_functions</code></h3>

``` python
@classmethod
from_concrete_functions(
    cls,
    funcs
)
```

Creates a TFLiteConverter object from ConcreteFunctions.


#### Args:


* <b>`funcs`</b>: List of TensorFlow ConcreteFunctions. The list should not contain
  duplicate elements.


#### Returns:

TFLiteConverter object.



#### Raises:

Invalid input type.


<h3 id="from_keras_model"><code>from_keras_model</code></h3>

``` python
@classmethod
from_keras_model(
    cls,
    model
)
```

Creates a TFLiteConverter object from a Keras model.


#### Args:


* <b>`model`</b>: tf.Keras.Model


#### Returns:

TFLiteConverter object.


<h3 id="from_saved_model"><code>from_saved_model</code></h3>

``` python
@classmethod
from_saved_model(
    cls,
    saved_model_dir,
    signature_keys=None,
    tags=None
)
```

Creates a TFLiteConverter object from a SavedModel directory.


#### Args:


* <b>`saved_model_dir`</b>: SavedModel directory to convert.
* <b>`signature_keys`</b>: List of keys identifying SignatureDef containing inputs
  and outputs. Elements should not be duplicated. By default the
  `signatures` attribute of the MetaGraphdef is used. (default
  saved_model.signatures)
* <b>`tags`</b>: Set of tags identifying the MetaGraphDef within the SavedModel to
  analyze. All tags in the tag set must be present. (default set(SERVING))


#### Returns:

TFLiteConverter object.



#### Raises:

Invalid signature keys.




