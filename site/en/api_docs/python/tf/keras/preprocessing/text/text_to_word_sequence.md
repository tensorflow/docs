description: Converts a text to a sequence of words (or tokens).

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.text.text_to_word_sequence" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.text.text_to_word_sequence

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/keras/preprocessing/text.py#L31-L57">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a text to a sequence of words (or tokens).

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.text.text_to_word_sequence`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.text.text_to_word_sequence(
    input_text, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=(True),
    split=' '
)
</code></pre>



<!-- Placeholder for "Used in" -->

This function transforms a string of text into a list of words
while ignoring `filters` which include punctuations by default.

```
>>> sample_text = 'This is a sample sentence.'
>>> tf.keras.preprocessing.text.text_to_word_sequence(sample_text)
['this', 'is', 'a', 'sample', 'sentence']
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`input_text`
</td>
<td>
Input text (string).
</td>
</tr><tr>
<td>
`filters`
</td>
<td>
list (or concatenation) of characters to filter out, such as
punctuation. Default: `'!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n'`,
includes basic punctuation, tabs, and newlines.
</td>
</tr><tr>
<td>
`lower`
</td>
<td>
boolean. Whether to convert the input to lowercase.
</td>
</tr><tr>
<td>
`split`
</td>
<td>
str. Separator for word splitting.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A list of words (or tokens).
</td>
</tr>

</table>

