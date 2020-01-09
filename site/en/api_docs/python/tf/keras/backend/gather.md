page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.gather


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/gather">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L1829-L1840">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Retrieves the elements of indices `indices` in the tensor `reference`.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/gather"><code>tf.compat.v1.keras.backend.gather</code></a>
* <a href="/api_docs/python/tf/keras/backend/gather"><code>tf.compat.v2.keras.backend.gather</code></a>


``` python
tf.keras.backend.gather(
    reference,
    indices
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`reference`</b>: A tensor.
* <b>`indices`</b>: An integer tensor of indices.


#### Returns:

A tensor of same type as `reference`.
