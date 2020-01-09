page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.optimizers.get


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/optimizers/get">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/optimizers.py#L818-L848">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retrieves a Keras Optimizer instance.

### Aliases:

* <a href="/api_docs/python/tf/keras/optimizers/get"><code>tf.compat.v1.keras.optimizers.get</code></a>
* <a href="/api_docs/python/tf/keras/optimizers/get"><code>tf.compat.v2.keras.optimizers.get</code></a>
* <a href="/api_docs/python/tf/keras/optimizers/get"><code>tf.compat.v2.optimizers.get</code></a>


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
