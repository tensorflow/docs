page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.one_hot

One-hot encodes a text into a list of word indexes of size n.

### Aliases:

* `tf.compat.v1.keras.preprocessing.text.one_hot`
* `tf.compat.v2.keras.preprocessing.text.one_hot`
* `tf.keras.preprocessing.text.one_hot`

``` python
tf.keras.preprocessing.text.one_hot(
    text,
    n,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```

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