# TensorFlow Documentation Style Guide

## Best practices {#best-practices}

*   Focus on user intent and audience.
*   Use every-day words, and keep sentences short.
*   Use consistent sentence construction, wording, and capitalization.
*   Make your article easy to scan.
*   Show empathy.

We aspire to follow these principles when we write technical content for
TensorFlow docs. We might not always get there, but we keep trying.

## Markdown syntax

With a few exceptions, TensorFlow uses the standard Markdown rules. This section
explains the primary differences between standard Markdown rules and the
Markdown rules that TensorFlow documentation uses.

### Math in Markdown {#math-in-markdown}

You may use MathJax within TensorFlow when editing Markdown files, but note the
following:

*   MathJax renders properly on http://tensorflow.org.
*   MathJax does not render properly on GitHub.

When writing MathJax, you can use $$ and \\( and \\) to surround your math. $$
guards will cause line breaks, so within text use $$ $$ instead.

### Writing about code {#writing-about-code}

#### Inline mentions of code

Put <code>`backticks`</code> around these things when they're used in text:

*   Argument names: <code>`input`</code>, <code>`x`</code>,
    <code>`tensor`</code>)
*   Returned tensor names: <code>`output`</code>, <code>`idx`</code>,
    <code>`out`</code>
*   Data types: <code>`int32`</code>, <code>`float`</code>, <code>`uint8`</code>
*   Other op names reference in text: <code>`list_diff()`</code>,
    <code>`shuffle()`</code>
*   Class names: <code>`Tensor`</code>, <code>`Strategy`</code>
*   File name: <code>`image_ops.py`</code>,
    <code>`/path-to-your-data/xml/example-name`</code>
*   Math expressions or conditions: <code>`-1-input.dims() &lt;= dim &lt;=
    input.dims()`</code>

#### Code blocks

Use three backticks before and after code block. In the opening backtick line,
specify the language.

<pre><code>
```python
# some python code here
```
</code></pre>



### Links in Markdown {#links-in-markdown}

#### Links between files in this repository

For links between files in this repository, use relative links: `[Eager
Basics](../tutorials/eager/eager_basics)` produces
[Eager Basics](https://www.tensorflow.org/tutorials/eager/eager_basics). These
links will work on both GitHub and http://tensorflow.org.

#### Links to API documentation

API links are converted when the site is published.

To link to the Python API, enclose the full symbol path in backticks:

*   `tf.data.Dataset` to produce
    [tf.data.Dataset](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)

For the C++ API, use the namespace path:

*   `tensorflow::Tensor` to produce
    [tensorflow::Tensor](https://www.tensorflow.org/api_docs/cc/class/tensorflow/tensor)

#### External links

For external links, including files on http://tensorflow.org that are not in the
`tensorflow/docs` repository, just use regular Markdown links with the full URI.

To link to source code, use a link starting with
https://www.github.com/tensorflow/tensorflow/blob/master/, followed by the file
name starting at the GitHub root.

This URI naming scheme ensures that http://tensorflow.org can forward the link
to the branch of the code corresponding to the version of the documentation
you're viewing.

Do not include URI query parameters in the link.

## Prose style

If you are going to write or edit substantial portions of the narrative
documentation, please read the
[Google style guide](https://developers.google.com/style).

### Principles of good style

*   **Check the spelling and grammar in your contributions.** Most editors
    include a spell checker or have an available spell-checking plugin. You can
    also paste your text into a Google Doc or other document software for a more
    robust spelling and grammar check.

*   **Use a casual and friendly voice.** Write TensorFlow documentation like a
    conversation — as if you're talking to another person one-on-one. Use a
    supportive tone in the article.

    **Note:** Being less formal does not mean being less technical. Simplify
    your prose, not the technical content.

*   **Avoid disclaimers, opinions, and value judgements.** Words like "easily",
    "just", and "simple" are loaded with assumptions. Something might seem easy
    to you, but be difficult for another person. Try to avoid these whenever
    possible.

*   **Use simple, to the point sentences without complicated jargon.** Compound
    sentences, chains of clauses, and location-specific idioms can make text
    hard to understand and translate. If a sentence can be split in two, it
    probably should. Avoid semicolons. Use bullet lists when appropriate.

*   **Provide context.** Don't use abbreviations without explaining them. Don't
    mention non-TensorFlow projects without linking to them. Explain why the
    code is written the way it is.

### Usage guide

#### Ops

Use `# ⇒` instead of a single equal sign when you want to show what an op
returns.

```python
# 'input' is a tensor of shape [2, 3, 5]
(tf.expand_dims(input, 0))  # ⇒ [1, 2, 3, 5]
```

#### Tensors

When you're talking about a tensor in general, don't capitalize the word
*tensor*. When you're talking about the specific object that's provided to or
returned from an op, then you should capitalize the word *Tensor* and add
backticks around it because you're talking about a `Tensor` object.

Don't use the word *Tensors* (plural) to describe multiple `Tensor` objects
unless you really are talking about a `Tensors` object. Instead, say "a list (or
collection) of `Tensor` objects".

Use the term *dimensions* to refer to the shape of a tensor. If you need to be
specific about the size, use these conventions:

*   Refer to a scalar as a *0-D tensor*.
*   Refer to a vector as a *1-D tensor*.
*   Refer to a matrix as a *2-D tensor*.
*   Refer to a tensor with 3 or more dimensions as a 3-D tensor or n-D tensor.
    Use the word *rank* only if it's unambiguous in that context. Never use the
    word *order* to describe the size of a tensor.

Use the word *shape* to detail the dimensions of a tensor, and show the shape in
square brackets with backticks. For example:

```markdown
If `input` is a 3-D tensor with shape `[3, 4, 3]`,
this operation returns a 3-D tensor with shape `[6, 8, 6]`.
```
