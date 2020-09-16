description: One-hot encodes a text into a list of word indexes of size n.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.text.one_hot" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.text.one_hot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>



One-hot encodes a text into a list of word indexes of size n.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.text.one_hot`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.text.one_hot(
    text, n, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=(True), split=' '
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is a wrapper to the `hashing_trick` function using `hash` as the
hashing function; unicity of word to index mapping non-guaranteed.

# Arguments
    text: Input text (string).
    n: int. Size of vocabulary.
    filters: list (or concatenation) of characters to filter out, such as
        punctuation. Default: ``!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n``,
        includes basic punctuation, tabs, and newlines.
    lower: boolean. Whether to set the text to lowercase.
    split: str. Separator for word splitting.

# Returns
    List of integers in [1, n]. Each integer encodes a word
    (unicity non-guaranteed).