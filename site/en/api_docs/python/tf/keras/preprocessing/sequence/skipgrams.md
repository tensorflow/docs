description: Generates skipgram word pairs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.sequence.skipgrams" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.sequence.skipgrams

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



Generates skipgram word pairs.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.sequence.skipgrams`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.sequence.skipgrams(
    sequence, vocabulary_size, window_size=4, negative_samples=1.0, shuffle=(True),
    categorical=(False), sampling_table=None, seed=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function transforms a sequence of word indexes (list of integers)
into tuples of words of the form:

- (word, word in the same window), with label 1 (positive samples).
- (word, random word from the vocabulary), with label 0 (negative samples).

Read more about Skipgram in this gnomic paper by Mikolov et al.:
[Efficient Estimation of Word Representations in
Vector Space](http://arxiv.org/pdf/1301.3781v3.pdf)

# Arguments
    sequence: A word sequence (sentence), encoded as a list
        of word indices (integers). If using a `sampling_table`,
        word indices are expected to match the rank
        of the words in a reference dataset (e.g. 10 would encode
        the 10-th most frequently occurring token).
        Note that index 0 is expected to be a non-word and will be skipped.
    vocabulary_size: Int, maximum possible word index + 1
    window_size: Int, size of sampling windows (technically half-window).
        The window of a word `w_i` will be
        `[i - window_size, i + window_size+1]`.
    negative_samples: Float >= 0. 0 for no negative (i.e. random) samples.
        1 for same number as positive samples.
    shuffle: Whether to shuffle the word couples before returning them.
    categorical: bool. if False, labels will be
        integers (eg. `[0, 1, 1 .. ]`),
        if `True`, labels will be categorical, e.g.
        `[[1,0],[0,1],[0,1] .. ]`.
    sampling_table: 1D array of size `vocabulary_size` where the entry i
        encodes the probability to sample a word of rank i.
    seed: Random seed.

# Returns
    couples, labels: where `couples` are int pairs and
        `labels` are either 0 or 1.

# Note
    By convention, index 0 in the vocabulary is
    a non-word and will be skipped.