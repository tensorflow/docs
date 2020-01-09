page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ctc_label_dense_to_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/ctc_label_dense_to_sparse">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L5557-L5600">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts CTC labels from dense to sparse.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/ctc_label_dense_to_sparse"><code>tf.compat.v1.keras.backend.ctc_label_dense_to_sparse</code></a>
* <a href="/api_docs/python/tf/keras/backend/ctc_label_dense_to_sparse"><code>tf.compat.v2.keras.backend.ctc_label_dense_to_sparse</code></a>


``` python
tf.keras.backend.ctc_label_dense_to_sparse(
    labels,
    label_lengths
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`labels`</b>: dense CTC labels.
* <b>`label_lengths`</b>: length of the labels.


#### Returns:

A sparse tensor representation of the labels.
