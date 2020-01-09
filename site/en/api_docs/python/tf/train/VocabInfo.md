page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.train.VocabInfo

## Class `VocabInfo`





Defined in [`tensorflow/python/training/warm_starting_util.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/python/training/warm_starting_util.py).

Vocabulary information for warm-starting.

See `tf.estimator.WarmStartSettings` for examples of using
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
* <b>`axis`</b>: [Optional] Denotes what axis the vocabulary corresponds to.  The
    default, 0, corresponds to the most common use case (embeddings or
    linear weights for binary classification / regression).  An axis of 1
    could be used for warm-starting output layers with class vocabularies.

    For example:

    embeddings_vocab_info = tf.VocabInfo(
        new_vocab='embeddings_vocab',
        new_vocab_size=100,
        num_oov_buckets=1,
        old_vocab='pretrained_embeddings_vocab',
        old_vocab_size=10000,
        backup_initializer=tf.truncated_normal_initializer(
            mean=0.0, stddev=(1 / math.sqrt(embedding_dim))),
        axis=0)

    softmax_output_layer_kernel_vocab_info = tf.VocabInfo(
        new_vocab='class_vocab',
        new_vocab_size=5,
        num_oov_buckets=0,  # No OOV for classes.
        old_vocab='old_class_vocab',
        old_vocab_size=8,
        backup_initializer=tf.glorot_uniform_initializer(),
        axis=1)

    softmax_output_layer_bias_vocab_info = tf.VocabInfo(
        new_vocab='class_vocab',
        new_vocab_size=5,
        num_oov_buckets=0,  # No OOV for classes.
        old_vocab='old_class_vocab',
        old_vocab_size=8,
        backup_initializer=tf.zeros_initializer(),
        axis=0)

    Currently, only axis=0 and axis=1 are supported.

<h2 id="__new__"><code>__new__</code></h2>

``` python
@staticmethod
__new__(
    cls,
    new_vocab,
    new_vocab_size,
    num_oov_buckets,
    old_vocab,
    old_vocab_size=-1,
    backup_initializer=None,
    axis=0
)
```





## Properties

<h3 id="new_vocab"><code>new_vocab</code></h3>



<h3 id="new_vocab_size"><code>new_vocab_size</code></h3>



<h3 id="num_oov_buckets"><code>num_oov_buckets</code></h3>



<h3 id="old_vocab"><code>old_vocab</code></h3>



<h3 id="old_vocab_size"><code>old_vocab_size</code></h3>



<h3 id="backup_initializer"><code>backup_initializer</code></h3>



<h3 id="axis"><code>axis</code></h3>





