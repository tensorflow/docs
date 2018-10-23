

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.keras.preprocessing.text.text_to_word_sequence

### `tf.contrib.keras.preprocessing.text.text_to_word_sequence`

``` python
text_to_word_sequence(
    text,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/text.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/keras/python/keras/preprocessing/text.py).

Converts a text to a sequence of word indices.

#### Arguments:

    text: Input text (string).
    filters: Sequence of characters to filter out.
    lower: Whether to convert the input to lowercase.
    split: Sentence split marker (string).


#### Returns:

    A list of integer word indices.