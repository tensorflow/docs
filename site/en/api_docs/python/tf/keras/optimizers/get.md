page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.get


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/optimizers.py#L820-L850">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retrieves a Keras Optimizer instance.

### Aliases:

* `tf.compat.v1.keras.optimizers.get`
* `tf.compat.v2.keras.optimizers.get`
* `tf.compat.v2.optimizers.get`
* `tf.optimizers.get`


``` python
tf.keras.optimizers.get(identifier)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`identifier`</b>: Optimizer identifier, one of
    - String: name of an optimizer
    - Dictionary: configuration dictionary. - Keras Optimizer instance (it
      will be returned unchanged). - TensorFlow Optimizer instance (it
      will be wrapped as a Keras Optimizer).


#### Returns:

A Keras Optimizer instance.



#### Raises:


* <b>`ValueError`</b>: If `identifier` cannot be interpreted.
