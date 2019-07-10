page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.ctc_label_dense_to_sparse

Converts CTC labels from dense to sparse.

### Aliases:

* `tf.compat.v1.keras.backend.ctc_label_dense_to_sparse`
* `tf.compat.v2.keras.backend.ctc_label_dense_to_sparse`
* `tf.keras.backend.ctc_label_dense_to_sparse`

``` python
tf.keras.backend.ctc_label_dense_to_sparse(
    labels,
    label_lengths
)
```



Defined in [`python/keras/backend.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/keras/backend.py).

<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`labels`</b>: dense CTC labels.
* <b>`label_lengths`</b>: length of the labels.


#### Returns:

A sparse tensor representation of the labels.
