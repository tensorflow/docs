

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


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



Defined in [`tensorflow/python/keras/_impl/keras/preprocessing/text.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/keras/_impl/keras/preprocessing/text.py).

One-hot encodes a text into a list of word indexes of size n.

This is a wrapper to the `hashing_trick` function using `hash` as the
hashing function; unicity of word to index mapping non-guaranteed.

#### Arguments:

* <b>`text`</b>: Input text (string).
* <b>`n`</b>: Dimension of the hashing space.
* <b>`filters`</b>: Sequence of characters to filter out.
* <b>`lower`</b>: Whether to convert the input to lowercase.
* <b>`split`</b>: Sentence split marker (string).


#### Returns:

A list of integer word indices (unicity non-guaranteed).