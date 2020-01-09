page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.one_hot


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L3215-L3231">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the one-hot representation of an integer tensor.

### Aliases:

* `tf.compat.v1.keras.backend.one_hot`
* `tf.compat.v2.keras.backend.one_hot`


``` python
tf.keras.backend.one_hot(
    indices,
    num_classes
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`indices`</b>: nD integer tensor of shape
    `(batch_size, dim1, dim2, ... dim(n-1))`
* <b>`num_classes`</b>: Integer, number of classes to consider.


#### Returns:

(n + 1)D one hot representation of the input
with shape `(batch_size, dim1, dim2, ... dim(n-1), num_classes)`



#### Returns:

The one-hot tensor.
