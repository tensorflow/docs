page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.sequence.make_sampling_table


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Generates a word rank-based probabilistic sampling table.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table"><code>tf.compat.v1.keras.preprocessing.sequence.make_sampling_table</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/sequence/make_sampling_table"><code>tf.compat.v2.keras.preprocessing.sequence.make_sampling_table</code></a>


``` python
tf.keras.preprocessing.sequence.make_sampling_table(
    size,
    sampling_factor=1e-05
)
```



<!-- Placeholder for "Used in" -->

Used for generating the `sampling_table` argument for `skipgrams`.
`sampling_table[i]` is the probability of sampling
the word i-th most common word in a dataset
(more common words should be sampled less frequently, for balance).

The sampling probabilities are generated according
to the sampling distribution used in word2vec:

```
p(word) = (min(1, sqrt(word_frequency / sampling_factor) /
    (word_frequency / sampling_factor)))
```

We assume that the word frequencies follow Zipf's law (s=1) to derive
a numerical approximation of frequency(rank):

`frequency(rank) ~ 1/(rank * (log(rank) + gamma) + 1/2 - 1/(12*rank))`
where `gamma` is the Euler-Mascheroni constant.

# Arguments
    size: Int, number of possible words to sample.
    sampling_factor: The sampling factor in the word2vec formula.

# Returns
    A 1D Numpy array of length `size` where the ith entry
    is the probability that a word of rank i should be sampled.
