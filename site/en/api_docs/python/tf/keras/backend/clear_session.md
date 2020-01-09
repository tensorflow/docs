page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.clear_session


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L224-L249">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Destroys the current TF graph and creates a new one.

### Aliases:

* `tf.compat.v1.keras.backend.clear_session`
* `tf.compat.v2.keras.backend.clear_session`


``` python
tf.keras.backend.clear_session()
```



### Used in the guide:

* [Save and serialize models with Keras](https://www.tensorflow.org/guide/keras/save_and_serialize)
* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)
* [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)
* [Writing custom layers and models with Keras](https://www.tensorflow.org/guide/keras/custom_layers_and_models)



Useful to avoid clutter from old models / layers.
