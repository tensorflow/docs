page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.models.model_from_yaml


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/saving/model_config.py#L58-L78">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Parses a yaml model configuration file and returns a model instance.

### Aliases:

* `tf.compat.v1.keras.models.model_from_yaml`
* `tf.compat.v2.keras.models.model_from_yaml`


``` python
tf.keras.models.model_from_yaml(
    yaml_string,
    custom_objects=None
)
```



### Used in the guide:

* [Keras overview](https://www.tensorflow.org/guide/keras/overview)




#### Arguments:


* <b>`yaml_string`</b>: YAML string encoding a model configuration.
* <b>`custom_objects`</b>: Optional dictionary mapping names
    (strings) to custom classes or functions to be
    considered during deserialization.


#### Returns:

A Keras model instance (uncompiled).



#### Raises:


* <b>`ImportError`</b>: if yaml module is not found.
