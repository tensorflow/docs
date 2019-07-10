page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>
<script src="/_static/js/managed/mathjax/MathJax.js?config=TeX-AMS-MML_SVG"></script>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.preprocessing.text.Tokenizer

## Class `Tokenizer`

Text tokenization utility class.



### Aliases:

* Class `tf.compat.v1.keras.preprocessing.text.Tokenizer`
* Class `tf.compat.v2.keras.preprocessing.text.Tokenizer`
* Class `tf.keras.preprocessing.text.Tokenizer`

<!-- Placeholder for "Used in" -->

This class allows to vectorize a text corpus, by turning each
text into either a sequence of integers (each integer being the index
of a token in a dictionary) or into a vector where the coefficient
for each token could be binary, based on word count, based on tf-idf...

# Arguments
    num_words: the maximum number of words to keep, based
        on word frequency. Only the most common `num_words-1` words will
        be kept.
    filters: a string where each element is a character that will be
        filtered from the texts. The default is all punctuation, plus
        tabs and line breaks, minus the `'` character.
    lower: boolean. Whether to convert the texts to lowercase.
    split: str. Separator for word splitting.
    char_level: if True, every character will be treated as a token.
    oov_token: if given, it will be added to word_index and used to
        replace out-of-vocabulary words during text_to_sequence calls

By default, all punctuation is removed, turning the texts into
space-separated sequences of words
(words maybe include the `'` character). These sequences are then
split into lists of tokens. They will then be indexed or vectorized.

`0` is a reserved index that won't be assigned to any word.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    num_words=None,
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',
    lower=True,
    split=' ',
    char_level=False,
    oov_token=None,
    document_count=0,
    **kwargs
)
```






## Methods

<h3 id="fit_on_sequences"><code>fit_on_sequences</code></h3>

``` python
fit_on_sequences(sequences)
```

Updates internal vocabulary based on a list of sequences.

Required before using `sequences_to_matrix`
(if `fit_on_texts` was never called).

# Arguments
    sequences: A list of sequence.
        A "sequence" is a list of integer word indices.

<h3 id="fit_on_texts"><code>fit_on_texts</code></h3>

``` python
fit_on_texts(texts)
```

Updates internal vocabulary based on a list of texts.

In the case where texts contains lists,
we assume each entry of the lists to be a token.

Required before using `texts_to_sequences` or `texts_to_matrix`.

# Arguments
    texts: can be a list of strings,
        a generator of strings (for memory-efficiency),
        or a list of list of strings.

<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```

Returns the tokenizer configuration as Python dictionary.
The word count dictionaries used by the tokenizer get serialized
into plain JSON, so that the configuration can be read by other
projects.

# Returns
    A Python dictionary with the tokenizer configuration.

<h3 id="sequences_to_matrix"><code>sequences_to_matrix</code></h3>

``` python
sequences_to_matrix(
    sequences,
    mode='binary'
)
```

Converts a list of sequences into a Numpy matrix.

# Arguments
    sequences: list of sequences
        (a sequence is a list of integer word indices).
    mode: one of "binary", "count", "tfidf", "freq"

# Returns
    A Numpy matrix.

# Raises
    ValueError: In case of invalid `mode` argument,
        or if the Tokenizer requires to be fit to sample data.

<h3 id="sequences_to_texts"><code>sequences_to_texts</code></h3>

``` python
sequences_to_texts(sequences)
```

Transforms each sequence into a list of text.

Only top `num_words-1` most frequent words will be taken into account.
Only words known by the tokenizer will be taken into account.

# Arguments
    sequences: A list of sequences (list of integers).

# Returns
    A list of texts (strings)

<h3 id="sequences_to_texts_generator"><code>sequences_to_texts_generator</code></h3>

``` python
sequences_to_texts_generator(sequences)
```

Transforms each sequence in `sequences` to a list of texts(strings).

Each sequence has to a list of integers.
In other words, sequences should be a list of sequences

Only top `num_words-1` most frequent words will be taken into account.
Only words known by the tokenizer will be taken into account.

# Arguments
    sequences: A list of sequences.

# Yields
    Yields individual texts.

<h3 id="texts_to_matrix"><code>texts_to_matrix</code></h3>

``` python
texts_to_matrix(
    texts,
    mode='binary'
)
```

Convert a list of texts to a Numpy matrix.

# Arguments
    texts: list of strings.
    mode: one of "binary", "count", "tfidf", "freq".

# Returns
    A Numpy matrix.

<h3 id="texts_to_sequences"><code>texts_to_sequences</code></h3>

``` python
texts_to_sequences(texts)
```

Transforms each text in texts to a sequence of integers.

Only top `num_words-1` most frequent words will be taken into account.
Only words known by the tokenizer will be taken into account.

# Arguments
    texts: A list of texts (strings).

# Returns
    A list of sequences.

<h3 id="texts_to_sequences_generator"><code>texts_to_sequences_generator</code></h3>

``` python
texts_to_sequences_generator(texts)
```

Transforms each text in `texts` to a sequence of integers.

Each item in texts can also be a list,
in which case we assume each item of that list to be a token.

Only top `num_words-1` most frequent words will be taken into account.
Only words known by the tokenizer will be taken into account.

# Arguments
    texts: A list of texts (strings).

# Yields
    Yields individual sequences.

<h3 id="to_json"><code>to_json</code></h3>

``` python
to_json(**kwargs)
```

Returns a JSON string containing the tokenizer configuration.
To load a tokenizer from a JSON string, use
`keras.preprocessing.text.tokenizer_from_json(json_string)`.

# Arguments
    **kwargs: Additional keyword arguments
        to be passed to `json.dumps()`.

# Returns
    A JSON string containing the tokenizer configuration.



