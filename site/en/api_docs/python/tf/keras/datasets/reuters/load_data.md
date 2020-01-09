page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.datasets.reuters.load_data


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/datasets/reuters.py#L31-L116">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Loads the Reuters newswire classification dataset.

### Aliases:

* `tf.compat.v1.keras.datasets.reuters.load_data`
* `tf.compat.v2.keras.datasets.reuters.load_data`


``` python
tf.keras.datasets.reuters.load_data(
    path='reuters.npz',
    num_words=None,
    skip_top=0,
    maxlen=None,
    test_split=0.2,
    seed=113,
    start_char=1,
    oov_char=2,
    index_from=3,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`path`</b>: where to cache the data (relative to `~/.keras/dataset`).
* <b>`num_words`</b>: max number of words to include. Words are ranked
    by how often they occur (in the training set) and only
    the most frequent words are kept
* <b>`skip_top`</b>: skip the top N most frequently occurring words
    (which may not be informative).
* <b>`maxlen`</b>: truncate sequences after this length.
* <b>`test_split`</b>: Fraction of the dataset to be used as test data.
* <b>`seed`</b>: random seed for sample shuffling.
* <b>`start_char`</b>: The start of a sequence will be marked with this character.
    Set to 1 because 0 is usually the padding character.
* <b>`oov_char`</b>: words that were cut out because of the `num_words`
    or `skip_top` limit will be replaced with this character.
* <b>`index_from`</b>: index actual words with this index and higher.
* <b>`**kwargs`</b>: Used for backwards compatibility.


#### Returns:

Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.


Note that the 'out of vocabulary' character is only used for
words that were present in the training set but are not included
because they're not making the `num_words` cut here.
Words that were not seen in the training set but are in the test set
have simply been skipped.
