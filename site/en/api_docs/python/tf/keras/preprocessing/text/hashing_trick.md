description: Converts a text to a sequence of indexes in a fixed-size hashing space.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.preprocessing.text.hashing_trick" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.preprocessing.text.hashing_trick

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/keras-team/keras-preprocessing/tree/master/keras_preprocessing/text.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Converts a text to a sequence of indexes in a fixed-size hashing space.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.keras.preprocessing.text.hashing_trick`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.keras.preprocessing.text.hashing_trick(
    text, n, hash_function=None, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=(True), split=' '
)
</code></pre>



<!-- Placeholder for "Used in" -->

# Arguments
    text: Input text (string).
    n: Dimension of the hashing space.
    hash_function: defaults to python `hash` function, can be 'md5' or
        any function that takes in input a string and returns a int.
        Note that 'hash' is not a stable hashing function, so
        it is not consistent across different runs, while 'md5'
        is a stable hashing function.
    filters: list (or concatenation) of characters to filter out, such as
        punctuation. Default: ``!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n``,
        includes basic punctuation, tabs, and newlines.
    lower: boolean. Whether to set the text to lowercase.
    split: str. Separator for word splitting.

# Returns
    A list of integer word indices (unicity non-guaranteed).

`0` is a reserved index that won't be assigned to any word.

Two or more words may be assigned to the same index, due to possible
collisions by the hashing function.
The [probability](
    https://en.wikipedia.org/wiki/Birthday_problem#Probability_table)
of a collision is in relation to the dimension of the hashing space and
the number of distinct objects.