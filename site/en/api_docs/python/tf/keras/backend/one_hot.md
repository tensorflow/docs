page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.one_hot


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/one_hot">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L3101-L3117">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Computes the one-hot representation of an integer tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/one_hot"><code>tf.compat.v1.keras.backend.one_hot</code></a>
* <a href="/api_docs/python/tf/keras/backend/one_hot"><code>tf.compat.v2.keras.backend.one_hot</code></a>


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
