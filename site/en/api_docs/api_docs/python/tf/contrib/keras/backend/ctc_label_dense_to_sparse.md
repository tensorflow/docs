

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.backend.ctc_label_dense_to_sparse

``` python
ctc_label_dense_to_sparse(
    labels,
    label_lengths
)
```



Defined in [`tensorflow/contrib/keras/python/keras/backend.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/backend.py).

Converts CTC labels from dense to sparse.

#### Arguments:

    labels: dense CTC labels.
    label_lengths: length of the labels.


#### Returns:

    A sparse tensor representation of the lablels.