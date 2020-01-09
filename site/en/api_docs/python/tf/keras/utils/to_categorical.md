page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.to_categorical


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/to_categorical">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/np_utils.py#L24-L52">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a class vector (integers) to binary class matrix.

### Aliases:

* <a href="/api_docs/python/tf/keras/utils/to_categorical"><code>tf.compat.v1.keras.utils.to_categorical</code></a>
* <a href="/api_docs/python/tf/keras/utils/to_categorical"><code>tf.compat.v2.keras.utils.to_categorical</code></a>


``` python
tf.keras.utils.to_categorical(
    y,
    num_classes=None,
    dtype='float32'
)
```



<!-- Placeholder for "Used in" -->

E.g. for use with categorical_crossentropy.

#### Arguments:


* <b>`y`</b>: class vector to be converted into a matrix
    (integers from 0 to num_classes).
* <b>`num_classes`</b>: total number of classes.
* <b>`dtype`</b>: The data type expected by the input. Default: `'float32'`.


#### Returns:

A binary matrix representation of the input. The classes axis is placed
last.
