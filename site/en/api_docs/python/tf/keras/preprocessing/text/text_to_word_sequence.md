

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.text_to_word_sequence

``` python
tf.keras.preprocessing.text.text_to_word_sequence(
    text,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```



Defined in [`tensorflow/python/keras/preprocessing/text.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/preprocessing/text.py).

Converts a text to a sequence of words (or tokens).

#### Arguments:

* <b>`text`</b>: Input text (string).
* <b>`filters`</b>: list (or concatenation) of characters to filter out, such as
        punctuation. Default: '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
        includes basic punctuation, tabs, and newlines.
* <b>`lower`</b>: boolean, whether to convert the input to lowercase.
* <b>`split`</b>: string, separator for word splitting.


#### Returns:

A list of words (or tokens).