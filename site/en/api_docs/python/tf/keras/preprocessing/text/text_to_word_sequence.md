page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.text_to_word_sequence


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/preprocessing/text/text_to_word_sequence">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>
</table>



Converts a text to a sequence of words (or tokens).

### Aliases:

* <a href="/api_docs/python/tf/keras/preprocessing/text/text_to_word_sequence"><code>tf.compat.v1.keras.preprocessing.text.text_to_word_sequence</code></a>
* <a href="/api_docs/python/tf/keras/preprocessing/text/text_to_word_sequence"><code>tf.compat.v2.keras.preprocessing.text.text_to_word_sequence</code></a>


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
