page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.one_hot

``` python
tf.keras.preprocessing.text.one_hot(
    text,
    n,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```



Defined in [`tensorflow/python/keras/preprocessing/text.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/python/keras/preprocessing/text.py).

One-hot encodes a text into a list of word indexes of size n.

This is a wrapper to the `hashing_trick` function using `hash` as the
hashing function; unicity of word to index mapping non-guaranteed.

#### Arguments:

* <b>`text`</b>: Input text (string).
* <b>`n`</b>: int, size of vocabulary.
* <b>`filters`</b>: list (or concatenation) of characters to filter out, such as
        punctuation. Default: '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
        includes basic punctuation, tabs, and newlines.
* <b>`lower`</b>: boolean, whether to set the text to lowercase.
* <b>`split`</b>: string, separator for word splitting.


#### Returns:

List of integers in [1, n].
Each integer encodes a word (unicity non-guaranteed).