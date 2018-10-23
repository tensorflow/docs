

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.keras.preprocessing.sequence.skipgrams

``` python
skipgrams(
    sequence,
    vocabulary_size,
    window_size=4,
    negative_samples=1.0,
    shuffle=True,
    categorical=False,
    sampling_table=None
)
```



Defined in [`tensorflow/contrib/keras/python/keras/preprocessing/sequence.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/contrib/keras/python/keras/preprocessing/sequence.py).

Generates skipgram word pairs.

Takes a sequence (list of indexes of words),
returns couples of [word_index, other_word index] and labels (1s or 0s),
where label = 1 if 'other_word' belongs to the context of 'word',
and label=0 if 'other_word' is randomly sampled

#### Arguments:

    sequence: a word sequence (sentence), encoded as a list
        of word indices (integers). If using a `sampling_table`,
        word indices are expected to match the rank
        of the words in a reference dataset (e.g. 10 would encode
        the 10-th most frequently occurring token).
        Note that index 0 is expected to be a non-word and will be skipped.
    vocabulary_size: int. maximum possible word index + 1
    window_size: int. actually half-window.
        The window of a word wi will be [i-window_size, i+window_size+1]
    negative_samples: float >= 0. 0 for no negative (=random) samples.
        1 for same number as positive samples. etc.
    shuffle: whether to shuffle the word couples before returning them.
    categorical: bool. if False, labels will be
        integers (eg. [0, 1, 1 .. ]),
        if True labels will be categorical eg. [[1,0],[0,1],[0,1] .. ]
    sampling_table: 1D array of size `vocabulary_size` where the entry i
        encodes the probabibily to sample a word of rank i.


#### Returns:

    couples, labels: where `couples` are int pairs and
        `labels` are either 0 or 1.

# Note
    By convention, index 0 in the vocabulary is
    a non-word and will be skipped.