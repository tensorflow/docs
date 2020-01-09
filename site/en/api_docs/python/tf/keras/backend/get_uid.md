page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.get_uid


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L189-L213">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Associates a string prefix with an integer counter in a TensorFlow graph.

### Aliases:

* `tf.compat.v1.keras.backend.get_uid`
* `tf.compat.v2.keras.backend.get_uid`


``` python
tf.keras.backend.get_uid(prefix='')
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`prefix`</b>: String prefix to index.


#### Returns:

Unique integer ID.



#### Example:



```
  >>> get_uid('dense')
  1
  >>> get_uid('dense')
  2
```
