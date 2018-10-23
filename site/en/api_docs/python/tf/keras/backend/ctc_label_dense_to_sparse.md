

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.backend.ctc_label_dense_to_sparse

``` python
ctc_label_dense_to_sparse(
    labels,
    label_lengths
)
```



Defined in [`tensorflow/python/keras/_impl/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/python/keras/_impl/keras/backend.py).

Converts CTC labels from dense to sparse.

#### Arguments:

* <b>`labels`</b>: dense CTC labels.
* <b>`label_lengths`</b>: length of the labels.


#### Returns:

A sparse tensor representation of the labels.