

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.VocabInfo

## Class `VocabInfo`





Defined in [`tensorflow/python/estimator/warm_starting_util.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/python/estimator/warm_starting_util.py).

Vocabulary information for WarmStartSettings.

See <a href="../../tf/estimator/WarmStartSettings">WarmStartSettings</a> for examples of using
VocabInfo to warm-start.

#### Attributes:

* <b>`new_vocab`</b>: [Required] A path to the new vocabulary file (used with the
    model to be trained).
* <b>`new_vocab_size`</b>: [Required] An integer indicating how many entries of the new
    vocabulary will used in training.
* <b>`num_oov_buckets`</b>: [Required] An integer indicating how many OOV buckets are
    associated with the vocabulary.
* <b>`old_vocab`</b>: [Required] A path to the old vocabulary file (used with the
    checkpoint to be warm-started from).
* <b>`old_vocab_size`</b>: [Optional] An integer indicating how many entries of the old
    vocabulary were used in the creation of the checkpoint. If not provided,
    the entire old vocabulary will be used.
* <b>`backup_initializer`</b>: [Optional] A variable initializer used for variables
    corresponding to new vocabulary entries and OOV. If not provided, these
    entries will be zero-initialized.

## Properties

<h3 id="backup_initializer"><code>backup_initializer</code></h3>

Alias for field number 5

<h3 id="new_vocab"><code>new_vocab</code></h3>

Alias for field number 0

<h3 id="new_vocab_size"><code>new_vocab_size</code></h3>

Alias for field number 1

<h3 id="num_oov_buckets"><code>num_oov_buckets</code></h3>

Alias for field number 2

<h3 id="old_vocab"><code>old_vocab</code></h3>

Alias for field number 3

<h3 id="old_vocab_size"><code>old_vocab_size</code></h3>

Alias for field number 4



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    new_vocab,
    new_vocab_size,
    num_oov_buckets,
    old_vocab,
    old_vocab_size=-1,
    backup_initializer=None
)
```





