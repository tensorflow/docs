page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.hashing_trick


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/text/hashing_trick">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Converts a text to a sequence of indexes in a fixed-size hashing space.

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/text/hashing_trick"><code>tf.compat.v1.keras.preprocessing.text.hashing_trick</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/text/hashing_trick"><code>tf.compat.v2.keras.preprocessing.text.hashing_trick</code></a>


``` python
tf.keras.preprocessing.text.hashing_trick(
    text,
    n,
    hash_function=None,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```



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
