

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.keras.preprocessing.sequence.pad_sequences

``` python
pad_sequences(
    sequences,
    maxlen=None,
    dtype='int32',
    padding='pre',
    truncating='pre',
    value=0.0
)
```



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/sequence.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/keras/_impl/keras/preprocessing/sequence.py).

Pads each sequence to the same length (length of the longest sequence).

If maxlen is provided, any sequence longer
than maxlen is truncated to maxlen.
Truncation happens off either the beginning (default) or
the end of the sequence.

Supports post-padding and pre-padding (default).

#### Arguments:

* <b>`sequences`</b>: list of lists where each element is a sequence
* <b>`maxlen`</b>: int, maximum length
* <b>`dtype`</b>: type to cast the resulting sequence.
* <b>`padding`</b>: 'pre' or 'post', pad either before or after each sequence.
* <b>`truncating`</b>: 'pre' or 'post', remove values from sequences larger than
        maxlen either in the beginning or in the end of the sequence
* <b>`value`</b>: float, value to pad the sequences to the desired value.


#### Returns:

* <b>`x`</b>: numpy array with dimensions (number_of_sequences, maxlen)


#### Raises:

* <b>`ValueError`</b>: in case of invalid values for `truncating` or `padding`,
        or in case of invalid shape for a `sequences` entry.