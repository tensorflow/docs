description: Pads sequences to the same length.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.sequence.pad_sequences" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.sequence.pad_sequences

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/keras/preprocessing/sequence.py#L92-L158">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Pads sequences to the same length.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.sequence.pad_sequences`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.sequence.pad_sequences(
    sequences, maxlen=None, dtype='int32', padding='pre', truncating='pre',
    value=0.0
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function transforms a list (of length `num_samples`)
of sequences (lists of integers)
into a 2D Numpy array of shape `(num_samples, num_timesteps)`.
`num_timesteps` is either the `maxlen` argument if provided,
or the length of the longest sequence in the list.

Sequences that are shorter than `num_timesteps`
are padded with `value` until they are `num_timesteps` long.

Sequences longer than `num_timesteps` are truncated
so that they fit the desired length.

The position where padding or truncation happens is determined by
the arguments `padding` and `truncating`, respectively.
Pre-padding or removing values from the beginning of the sequence is the
default.

```
>>> sequence = [[1], [2, 3], [4, 5, 6]]
>>> tf.keras.preprocessing.sequence.pad_sequences(sequence)
array([[0, 0, 1],
       [0, 2, 3],
       [4, 5, 6]], dtype=int32)
```

```
>>> tf.keras.preprocessing.sequence.pad_sequences(sequence, value=-1)
array([[-1, -1,  1],
       [-1,  2,  3],
       [ 4,  5,  6]], dtype=int32)
```

```
>>> tf.keras.preprocessing.sequence.pad_sequences(sequence, padding='post')
array([[1, 0, 0],
       [2, 3, 0],
       [4, 5, 6]], dtype=int32)
```

```
>>> tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=2)
array([[0, 1],
       [2, 3],
       [5, 6]], dtype=int32)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`sequences`
</td>
<td>
List of sequences (each sequence is a list of integers).
</td>
</tr><tr>
<td>
`maxlen`
</td>
<td>
Optional Int, maximum length of all sequences. If not provided,
sequences will be padded to the length of the longest individual
sequence.
</td>
</tr><tr>
<td>
`dtype`
</td>
<td>
(Optional, defaults to int32). Type of the output sequences.
To pad sequences with variable length strings, you can use `object`.
</td>
</tr><tr>
<td>
`padding`
</td>
<td>
String, 'pre' or 'post' (optional, defaults to 'pre'):
pad either before or after each sequence.
</td>
</tr><tr>
<td>
`truncating`
</td>
<td>
String, 'pre' or 'post' (optional, defaults to 'pre'):
remove values from sequences larger than
`maxlen`, either at the beginning or at the end of the sequences.
</td>
</tr><tr>
<td>
`value`
</td>
<td>
Float or String, padding value. (Optional, defaults to 0.)
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
Numpy array with shape `(len(sequences), maxlen)`
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
In case of invalid values for `truncating` or `padding`,
or in case of invalid shape for a `sequences` entry.
</td>
</tr>
</table>

