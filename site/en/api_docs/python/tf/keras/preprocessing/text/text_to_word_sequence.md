page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.text_to_word_sequence


<table class="tfo-notebook-buttons tfo-api" align="left">
</table>



Converts a text to a sequence of words (or tokens).

### Aliases:

* `tf.compat.v1.keras.preprocessing.text.text_to_word_sequence`
* `tf.compat.v2.keras.preprocessing.text.text_to_word_sequence`


``` python
tf.keras.preprocessing.text.text_to_word_sequence(
    text,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' '
)
```



<!-- Placeholder for "Used in" -->

# Arguments
    text: Input text (string).
    filters: list (or concatenation) of characters to filter out, such as
        punctuation. Default: ``!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n``,
        includes basic punctuation, tabs, and newlines.
    lower: boolean. Whether to convert the input to lowercase.
    split: str. Separator for word splitting.

# Returns
    A list of words (or tokens).
