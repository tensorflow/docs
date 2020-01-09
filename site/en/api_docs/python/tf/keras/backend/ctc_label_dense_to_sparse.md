page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ctc_label_dense_to_sparse


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L5661-L5704">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts CTC labels from dense to sparse.

### Aliases:

* `tf.compat.v1.keras.backend.ctc_label_dense_to_sparse`
* `tf.compat.v2.keras.backend.ctc_label_dense_to_sparse`


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
