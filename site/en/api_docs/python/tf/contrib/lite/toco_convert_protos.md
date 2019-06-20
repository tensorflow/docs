page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.lite.toco_convert_protos

``` python
tf.contrib.lite.toco_convert_protos(
    model_flags_str,
    toco_flags_str,
    input_data_str
)
```



Defined in [`tensorflow/contrib/lite/python/convert.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/lite/python/convert.py).

Convert `input_data_str` according to model and toco parameters.

Unless you know what you are doing consider using
the more friendly <a href="../../../tf/contrib/lite/toco_convert"><code>tf.contrib.lite.toco_convert</code></a>}.

#### Args:

* <b>`model_flags_str`</b>: Serialized proto describing model properties, see
    `toco/model_flags.proto`.
* <b>`toco_flags_str`</b>: Serialized proto describing conversion properties, see
    `toco/toco_flags.proto`.
* <b>`input_data_str`</b>: Input data in serialized form (e.g. a graphdef is common)

#### Returns:

Converted model in serialized form (e.g. a TFLITE model is common).

#### Raises:

* <b>`RuntimeError`</b>: When conversion fails, an exception is raised with the error
    message embedded.