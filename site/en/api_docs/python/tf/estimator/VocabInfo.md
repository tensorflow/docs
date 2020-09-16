description: Vocabulary information for warm-starting.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.VocabInfo" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="axis"/>
<meta itemprop="property" content="backup_initializer"/>
<meta itemprop="property" content="new_vocab"/>
<meta itemprop="property" content="new_vocab_size"/>
<meta itemprop="property" content="num_oov_buckets"/>
<meta itemprop="property" content="old_vocab"/>
<meta itemprop="property" content="old_vocab_size"/>
</div>

# tf.estimator.VocabInfo

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/training/warm_starting_util.py#L39-L135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Vocabulary information for warm-starting.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.estimator.VocabInfo`, `tf.compat.v1.train.VocabInfo`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.estimator.VocabInfo(
    new_vocab, new_vocab_size, num_oov_buckets, old_vocab, old_vocab_size=-1,
    backup_initializer=None, axis=0
)
</code></pre>



<!-- Placeholder for "Used in" -->

  See <a href="../../tf/estimator/WarmStartSettings.md"><code>tf.estimator.WarmStartSettings</code></a> for examples of using
  VocabInfo to warm-start.

  Args:
    new_vocab: [Required] A path to the new vocabulary file (used with the model
      to be trained).
    new_vocab_size: [Required] An integer indicating how many entries of the new
      vocabulary will used in training.
    num_oov_buckets: [Required] An integer indicating how many OOV buckets are
      associated with the vocabulary.
    old_vocab: [Required] A path to the old vocabulary file (used with the
      checkpoint to be warm-started from).
    old_vocab_size: [Optional] An integer indicating how many entries of the old
      vocabulary were used in the creation of the checkpoint. If not provided,
      the entire old vocabulary will be used.
    backup_initializer: [Optional] A variable initializer used for variables
      corresponding to new vocabulary entries and OOV. If not provided, these
      entries will be zero-initialized.
    axis: [Optional] Denotes what axis the vocabulary corresponds to.  The
      default, 0, corresponds to the most common use case (embeddings or
      linear weights for binary classification / regression).  An axis of 1
      could be used for warm-starting output layers with class vocabularies.

  Returns:
    A `VocabInfo` which represents the vocabulary information for warm-starting.

  Raises:
    ValueError: `axis` is neither 0 or 1.

      Example Usage:
```python
      embeddings_vocab_info = tf.VocabInfo(
          new_vocab='embeddings_vocab',
          new_vocab_size=100,
          num_oov_buckets=1,
          old_vocab='pretrained_embeddings_vocab',
          old_vocab_size=10000,
          backup_initializer=tf.compat.v1.truncated_normal_initializer(
              mean=0.0, stddev=(1 / math.sqrt(embedding_dim))),
          axis=0)

      softmax_output_layer_kernel_vocab_info = tf.VocabInfo(
          new_vocab='class_vocab',
          new_vocab_size=5,
          num_oov_buckets=0,  # No OOV for classes.
          old_vocab='old_class_vocab',
          old_vocab_size=8,
          backup_initializer=tf.compat.v1.glorot_uniform_initializer(),
          axis=1)

      softmax_output_layer_bias_vocab_info = tf.VocabInfo(
          new_vocab='class_vocab',
          new_vocab_size=5,
          num_oov_buckets=0,  # No OOV for classes.
          old_vocab='old_class_vocab',
          old_vocab_size=8,
          backup_initializer=tf.compat.v1.zeros_initializer(),
          axis=0)

      #Currently, only axis=0 and axis=1 are supported.
  ```
  



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`new_vocab`
</td>
<td>

</td>
</tr><tr>
<td>
`new_vocab_size`
</td>
<td>

</td>
</tr><tr>
<td>
`num_oov_buckets`
</td>
<td>

</td>
</tr><tr>
<td>
`old_vocab`
</td>
<td>

</td>
</tr><tr>
<td>
`old_vocab_size`
</td>
<td>

</td>
</tr><tr>
<td>
`backup_initializer`
</td>
<td>

</td>
</tr><tr>
<td>
`axis`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `axis` <a id="axis"></a>
* `backup_initializer` <a id="backup_initializer"></a>
* `new_vocab` <a id="new_vocab"></a>
* `new_vocab_size` <a id="new_vocab_size"></a>
* `num_oov_buckets` <a id="num_oov_buckets"></a>
* `old_vocab` <a id="old_vocab"></a>
* `old_vocab_size` <a id="old_vocab_size"></a>
