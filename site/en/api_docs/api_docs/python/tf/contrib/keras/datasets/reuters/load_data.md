

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.datasets.reuters.load_data

``` python
load_data(
    path='reuters.npz',
    num_words=None,
    skip_top=0,
    maxlen=None,
    test_split=0.2,
    seed=113,
    start_char=1,
    oov_char=2,
    index_from=3
)
```



Defined in [`tensorflow/contrib/keras/python/keras/datasets/reuters.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/datasets/reuters.py).

Loads the Reuters newswire classification dataset.

#### Arguments:

    path: where to cache the data (relative to `~/.keras/dataset`).
    num_words: max number of words to include. Words are ranked
        by how often they occur (in the training set) and only
        the most frequent words are kept
    skip_top: skip the top N most frequently occurring words
        (which may not be informative).
    maxlen: truncate sequences after this length.
    test_split: Fraction of the dataset to be used as test data.
    seed: random seed for sample shuffling.
    start_char: The start of a sequence will be marked with this character.
        Set to 1 because 0 is usually the padding character.
    oov_char: words that were cut out because of the `num_words`
        or `skip_top` limit will be replaced with this character.
    index_from: index actual words with this index and higher.


#### Returns:

    Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.

Note that the 'out of vocabulary' character is only used for
words that were present in the training set but are not included
because they're not making the `num_words` cut here.
Words that were not seen in the training set but are in the test set
have simply been skipped.