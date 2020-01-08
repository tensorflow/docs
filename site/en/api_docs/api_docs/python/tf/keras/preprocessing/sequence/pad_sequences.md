

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.sequence.pad_sequences

``` python
tf.keras.preprocessing.sequence.pad_sequences(
    sequences,
    maxlen=None,
    dtype='int32',
    padding='pre',
    truncating='pre',
    value=0.0
)
```



Defined in [`tensorflow/python/keras/preprocessing/sequence.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/sequence.py).

Pads sequences to the same length.

This function transforms a list of
`num_samples` sequences (lists of integers)
into a 2D Numpy array of shape `(num_samples, num_timesteps)`.
`num_timesteps` is either the `maxlen` argument if provided,
or the length of the longest sequence otherwise.

Sequences that are shorter than `num_timesteps`
are padded with `value` at the end.

Sequences longer than `num_timesteps` are truncated
so that they fit the desired length.
The position where padding or truncation happens is determined by
the arguments `padding` and `truncating`, respectively.

Pre-padding is the default.

#### Arguments:

* <b>`sequences`</b>: List of lists, where each element is a sequence.
* <b>`maxlen`</b>: Int, maximum length of all sequences.
* <b>`dtype`</b>: Type of the output sequences.
* <b>`padding`</b>: String, 'pre' or 'post':
        pad either before or after each sequence.
* <b>`truncating`</b>: String, 'pre' or 'post':
        remove values from sequences larger than
        `maxlen`, either at the beginning or at the end of the sequences.
* <b>`value`</b>: Float, padding value.


#### Returns:

* <b>`x`</b>: Numpy array with shape `(len(sequences), maxlen)`


#### Raises:

* <b>`ValueError`</b>: In case of invalid values for `truncating` or `padding`,
        or in case of invalid shape for a `sequences` entry.