page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.hashing_trick

``` python
tf.keras.preprocessing.text.hashing_trick(
    text,
    n,
    hash_function=None,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```



Defined in [`tensorflow/python/keras/preprocessing/text.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/keras/preprocessing/text.py).

Converts a text to a sequence of indexes in a fixed-size hashing space.

#### Arguments:

* <b>`text`</b>: Input text (string).
* <b>`n`</b>: Dimension of the hashing space.
* <b>`hash_function`</b>: defaults to python `hash` function, can be 'md5' or
        any function that takes in input a string and returns a int.
        Note that 'hash' is not a stable hashing function, so
        it is not consistent across different runs, while 'md5'
        is a stable hashing function.
* <b>`filters`</b>: list (or concatenation) of characters to filter out, such as
        punctuation. Default: '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
        includes basic punctuation, tabs, and newlines.
* <b>`lower`</b>: boolean, whether to set the text to lowercase.
* <b>`split`</b>: string, separator for word splitting.


#### Returns:

    A list of integer word indices (unicity non-guaranteed).

`0` is a reserved index that won't be assigned to any word.

Two or more words may be assigned to the same index, due to possible
collisions by the hashing function.
The
probability
of a collision is in relation to the dimension of the hashing space and
the number of distinct objects.