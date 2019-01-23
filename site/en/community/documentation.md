# Writing TensorFlow Documentation

We welcome contributions to the TensorFlow documentation from the community.
This document explains how you can contribute to that documentation. In
particular, this document explains the following:

* Where the documentation is located.
* How to make conformant edits.

You can view TensorFlow documentation at [tensorflow.org](https://www.tensorflow.org), and you
can view and edit the raw files at the corresponding paths in
[the `site/en` directory](https://github.com/tensorflow/docs/tree/master/site/en).

We're publishing our docs on GitHub so everybody can contribute. Whatever gets
checked in to `tensorflow/docs/site/en` will be published soon after on
[tensorflow.org](https://www.tensorflow.org).

Republishing TensorFlow documentation in different forms is absolutely allowed,
but we are unlikely to accept other documentation formats (or the tooling to
generate them) into our repository. If you do choose to republish our
documentation in another form, please be sure to include:

* The version of the API this represents (for example, r1.0, master, etc.)
* The commit or version from which the documentation was generated
* Where to get the latest documentation (that is, https://www.tensorflow.org)
* The Apache 2.0 license.

## Versions and branches

[tensorflow.org](https://www.tensorflow.org), at root, shows documentation for the latest stable binary.  This
is the documentation you should be reading if you are using `pip install tensorflow`.

The default TensorFlow pip package is built from the stable branch `rX.X` in the [main TensorFlow repository](https://github.com/tensorflow/tensorflow/). 

In contrast, to quickly publish fixes, the docs on the site are built from the [`docs/master` branch](https://github.com/tensorflow/docs/blob/master/site/en/). 

Old versions of the documentation are available in the `rX.X` branches. An "old-version" branch will only be created when the next version is released: When `r1.11` is released, we will create the `r1.10` branch.

In the rare case that a there is a major update for a new feature that we do not wish to publish to the site in the mean time, the docs will be developed in a feature-branch, and merged to master when ready.

## API documentation

The following reference documentation is automatically generated from comments
in the code:

- C++ API reference docs
- Java API reference docs
- Python API reference docs

To modify the reference documentation, you edit the appropriate code comments and doc strings. These are only updated with new releases, as they reflect the contents of the default installation.

The Python API documentation is generated from the main TensorFlow repository using the `//tensorflow/tools/docs:generate` bazel build target:

```sh
bazel run //tensorflow/tools/docs:generate -- --output_dir=/tmp/master_out
```

The C++ API documentation is generated from XML files generated via doxygen;
however, those tools are not available in open source at this time.


## Markdown and Notebooks

TensorFlow documentation is written in Markdown (`.md`) or Notebooks (`.ipynb`). With a few exceptions,
TensorFlow uses the [standard Markdown rules](https://daringfireball.net/projects/markdown/).

Use
[this template](https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb)
for TensorFlow notebooks.

This section explains the primary differences between standard Markdown rules
and the Markdown rules that TensorFlow documentation uses.

### Math in Markdown

You may use MathJax within TensorFlow when editing Markdown files, but note the
following:

- MathJax renders properly on [tensorflow.org](https://www.tensorflow.org)
- MathJax does not render properly on [GitHub](https://github.com/tensorflow/tensorflow).

When writing MathJax, you can use <code>&#36;&#36;</code> and `\\(` and `\\)` to
surround your math.  <code>&#36;&#36;</code> guards will cause line breaks, so
within text, use `\\(` `\\)` instead.

### Links in Markdown

#### Links between files in this repository

For links between files in this repository, use relative links and include the
file extension.

<code>&#91;Eager Basics&#93;(../tutorials/eager/eager_basics.ipynb)</code>

> [Eager Basics](../tutorials/eager/eager_basics.ipynb)

These links will work on GitHub (linking to the source file), and tensorflow.org
(linking to the rendered page).

#### Links to TensorFlow API documentation

Links to the TensorFlow API documentation are converted when the site is
published.

For the Python API, enclose the full symbol path in backticks:

<code>
\`tf.data.Dataset\`
</code>

> `tf.data.Dataset`

For the C++ API, use the namespace path in backticks:

```
`tensorflow::Tensor`
```

> `tensorflow::Tensor`

#### Links to TensorFlow source code

To link to source code, use a link starting with:
`https://github.com/tensorflow/tensorflow/blob/master`, followed by the file
path starting *from* the GitHub project root. (That is, don't repeat the name of
the GitHub repository a second time).

```
[Example link to tensorflow/python/__init__.py,
in the TensorFlow repo](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/__init__.py)
```

> [Example link to tensorflow/python/__init__.py, in the TensorFlow repo](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/__init__.py)

Do not include any additional parameters or query strings in the Markdown URL.

#### External Links

Use regular Markdown links for:

-   external pages
-   pages on tensorflow.org that are not sourced in the
    [tensorflow/docs](https://github.com/tensorflow/docs) repository
-   pages on tensorflow.org that are sourced from the
    [tensorflow/docs](https://github.com/tensorflow/docs) repository, but from a
    non-Markdown file (for example, a `.yaml` file).

In these cases, follow the standard Markdown link syntax, and include the full
URL.

## Op documentation style guide

Long, descriptive module-level documentation for modules should go in the [API
Guides](../api_guides/python/).

For classes and ops, ideally, you should provide the following information, in
order of presentation:

* A short sentence that describes what the op does.
* A short description of what happens when you pass arguments to the op.
* An example showing how the op works (pseudocode is best).
* Requirements, caveats, important notes (if there are any).
* Descriptions of inputs, outputs, and Attrs or other parameters of the op
  constructor.

Each of these is described in more
detail [below](#description-of-the-docstring-sections).

Write your text in Markdown format. A basic syntax reference
is [here](https://daringfireball.net/projects/markdown/). You are allowed to
use [MathJax](https://www.mathjax.org) notation for equations (see above for
restrictions).

### Writing about code

Put backticks around these things when they're used in text:

* Argument names (for example, `input`, `x`, `tensor`)
* Returned tensor names (for example, `output`, `idx`, `out`)
* Data types (for example, `int32`, `float`, `uint8`)
* Other op names referenced in text (for example, `list_diff()`, `shuffle()`)
* Class names (for example, `Tensor` when you actually mean a `Tensor` object;
  don't capitalize or use backticks if you're just explaining what an op does to
  a tensor, or a graph, or an operation in general)
* File names (for example, `image_ops.py`, or
  `/path-to-your-data/xml/example-name`)
* Math expressions or conditions (for example, `-1-input.dims() <= dim <=
  input.dims()`)

Put three backticks around sample code and pseudocode examples. And use `# ==>`
instead of a single equal sign when you want to show what an op returns. For
example:

    ```
    # 'input' is a tensor of shape [2, 3, 5]
    (tf.expand_dims(input, 0))  # ==> [1, 2, 3, 5]
    ```

If you're providing a Python code sample, add the python style label to ensure
proper syntax highlighting:

    ``` python
    # some Python code
    ```

Two notes about backticks for code samples in Markdown:

1. You can use backticks for pretty printing languages other than Python, if
   necessary. A full list of languages is available
   [here](https://github.com/google/code-prettify#how-do-i-specify-the-language-of-my-code).
2. Markdown also allows you to indent four spaces to specify a code sample.
   However, do NOT indent four spaces and use backticks simultaneously. Use one
   or the other.

### Tensor dimensions

When you're talking about a tensor in general, don't capitalize the word tensor.
When you're talking about the specific object that's provided to an op as an
argument or returned by an op, then you should capitalize the word Tensor and
add backticks around it because you're talking about a `Tensor` object.

Don't use the word `Tensors` to describe multiple Tensor objects unless you
really are talking about a `Tensors` object. Better to say "a list of `Tensor`
objects."

Use the term "dimensions" to refer to the shape of a tensor. If you need to be
specific about the size, use these conventions:

- Refer to a scalar as a "0-D tensor"
- Refer to a vector as a "1-D tensor"
- Refer to a matrix as a "2-D tensor"
- Refer to tensors with 3 or more dimensions as 3-D tensors or n-D tensors. Use
  the word "rank" only if it's unambiguous in that context. Never use the word "order"
  to describe the size of a tensor.

Use the word "shape" to detail the dimensions of a tensor, and show the shape in
square brackets with backticks. For example:

<pre>
If `input` is a 3-D tensor with shape `[3, 4, 3]`, this operation
returns a 3-D tensor with shape `[6, 8, 6]`.
</pre>

### Ops defined in C++

All Ops defined in C++ (and accessible from other languages) must be documented
with a `REGISTER_OP` declaration. The docstring in the C++ file is processed to
automatically add some information for the input types, output types, and Attr
types and default values.

For example:

```c++
REGISTER_OP("PngDecode")
  .Input("contents: string")
  .Attr("channels: int = 0")
  .Output("image: uint8")
  .Doc(R"doc(
Decodes the contents of a PNG file into a uint8 tensor.

contents: PNG file contents.
channels: Number of color channels, or 0 to autodetect based on the input.
  Must be 0 for autodetect, 1 for grayscale, 3 for RGB, or 4 for RGBA.
  If the input has a different number of channels, it will be transformed
  accordingly.
image:= A 3-D uint8 tensor of shape `[height, width, channels]`.
  If `channels` is 0, the last dimension is determined
  from the png contents.
)doc");
```

Results in this piece of Markdown:

    ### tf.image.png_decode(contents, channels=None, name=None) {#png_decode}

    Decodes the contents of a PNG file into a uint8 tensor.

    #### Args:

    *  **contents**: A string Tensor. PNG file contents.
    *  **channels**: An optional int. Defaults to 0.
       Number of color channels, or 0 to autodetect based on the input.
       Must be 0 for autodetect, 1 for grayscale, 3 for RGB, or 4 for RGBA.  If the
       input has a different number of channels, it will be transformed accordingly.
    *  **name**: A name for the operation (optional).

    #### Returns:
    A 3-D uint8 tensor of shape `[height, width, channels]`.  If `channels` is
    0, the last dimension is determined from the png contents.

Much of the argument description is added automatically. In particular, the doc
generator automatically adds the name and type of all inputs, attrs, and
outputs. In the above example, `contents: A string Tensor.` was added
automatically. You should write your additional text to flow naturally after
that description.

For inputs and output, you can prefix your additional text with an equal sign to
prevent the automatically added name and type. In the above example, the
description for the output named `image` starts with `=` to prevent the addition
of `A uint8 Tensor.` before our text `A 3-D uint8 Tensor...`. You cannot prevent
the addition of the name, type, and default value of attrs this way, so write
your text carefully.

### Ops defined in Python

If your op is defined in a `python/ops/*.py` file, then you need to provide text
for all of the arguments and output (returned) tensors. The doc generator does
not auto-generate any text for ops that are defined in Python, so what you write
is what you get.

You should conform to the usual Python docstring conventions, except that you
should use Markdown in the docstring.

Here's a simple example:

    def foo(x, y, name="bar"):
      """Computes foo.

      Given two 1-D tensors `x` and `y`, this operation computes the foo.

      Example:

      ```
      # x is [1, 1]
      # y is [2, 2]
      tf.foo(x, y) ==> [3, 3]
      ```
      Args:
        x: A `Tensor` of type `int32`.
        y: A `Tensor` of type `int32`.
        name: A name for the operation (optional).

      Returns:
        A `Tensor` of type `int32` that is the foo of `x` and `y`.

      Raises:
        ValueError: If `x` or `y` are not of type `int32`.
      """

## Description of the docstring sections

This section details each of the elements in docstrings.

### Short sentence describing what the op does

Examples:

<pre>
Concatenates tensors.
</pre>

<pre>
Flips an image horizontally from left to right.
</pre>

<pre>
Computes the Levenshtein distance between two sequences.
</pre>

<pre>
Saves a list of tensors to a file.
</pre>

<pre>
Extracts a slice from a tensor.
</pre>

### Short description of what happens when you pass arguments to the op

Examples:

<pre>
Given a tensor input of numerical type, this operation returns a tensor of
the same type and size with values reversed along dimension `seq_dim`. A
vector `seq_lengths` determines which elements are reversed for each index
within dimension 0 (usually the batch dimension).


This operation returns a tensor of type `dtype` and dimensions `shape`, with
all elements set to zero.
</pre>

### Example demonstrating the op

Good code samples are short and easy to understand, typically containing a brief
snippet of code to clarify what the example is demonstrating. When an op
manipulates the shape of a Tensor it is often useful to include an example of
the before and after, as well.

The `squeeze()` op has a nice pseudocode example:

<pre>
# 't' is a tensor of shape [1, 2, 1, 3, 1, 1]
shape(squeeze(t)) ==> [2, 3]
</pre>

The `tile()` op provides a good example in descriptive text:

<pre>
For example, tiling `[a, b, c, d]` by `[2]` produces `[a b c d a b c d]`.
</pre>

It is often helpful to show code samples in Python. Never put them in the C++
Ops file, and avoid putting them in the Python Ops doc. We recommend, if
possible, putting code samples in the
[API guides](https://github.com/tensorflow/docs/tree/master/site/en/api_guides).
Otherwise, add them to the module or class docstring where the Ops constructors
are called out.

Here's an example from the module docstring in `api_guides/python/math_ops.md`:

<pre>
## Segmentation

TensorFlow provides several operations that you can use to perform common
math computations on tensor segments.
...
In particular, a segmentation of a matrix tensor is a mapping of rows to
segments.

For example:

```python
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
tf.segment_sum(c, tf.constant([0, 0, 1]))
  ==>  [[0 0 0 0]
        [5 6 7 8]]
```
</pre>

### Requirements, caveats, important notes

Examples:

<pre>
This operation requires that: `-1-input.dims() <= dim <= input.dims()`
</pre>

<pre>
Note: This tensor will produce an error if evaluated. Its value must
be fed using the `feed_dict` optional argument to `Session.run()`,
`Tensor.eval()`, or `Operation.run()`.
</pre>

### Descriptions of arguments and output (returned) tensors.

Keep the descriptions brief and to the point. You should not have to explain how
the operation works in the argument sections.

Mention if the Op has strong constraints on the dimensions of the input or
output tensors. Remember that for C++ Ops, the type of the tensor is
automatically added as either as "A ..type.. Tensor" or "A Tensor with type in
{...list of types...}". In such cases, if the Op has a constraint on the
dimensions either add text such as "Must be 4-D" or start the description with
`=` (to prevent the tensor type to be added) and write something like "A 4-D
float tensor".

For example, here are two ways to document an image argument of a C++ op (note
the "=" sign):

<pre>
image: Must be 4-D. The image to resize.
</pre>

<pre>
image:= A 4-D `float` tensor. The image to resize.
</pre>

In the documentation, these will be rendered to Markdown as

<pre>
image: A `float` Tensor. Must be 4-D. The image to resize.
</pre>

<pre>
image: A 4-D `float` Tensor. The image to resize.
</pre>

### Optional arguments descriptions ("attrs")

The doc generator always describes the type for each attr and their default
value, if any. You cannot override that with an equal sign because the
description is very different in the C++ and Python generated docs.

Phrase any additional attr description so that it flows well after the type
and default value. The type and defaults are displayed first, and additional
descriptions follow afterwards. Therefore, complete sentences are best.

Here's an example from `image_ops.cc`:

<pre>
REGISTER_OP("DecodePng")
    .Input("contents: string")
    .Attr("channels: int = 0")
    .Attr("dtype: {uint8, uint16} = DT_UINT8")
    .Output("image: dtype")
    .SetShapeFn(DecodeImageShapeFn)
    .Doc(R"doc(
Decode a PNG-encoded image to a uint8 or uint16 tensor.

The attr `channels` indicates the desired number of color channels for the
decoded image.

Accepted values are:

*   0: Use the number of channels in the PNG-encoded image.
*   1: output a grayscale image.
*   3: output an RGB image.
*   4: output an RGBA image.

If needed, the PNG-encoded image is transformed to match the requested
number of color channels.

contents: 0-D.  The PNG-encoded image.
channels: Number of color channels for the decoded image.
image: 3-D with shape `[height, width, channels]`.
)doc");
</pre>

This generates the following Args section in
`api_docs/python/tf/image/decode_png.md`:

<pre>
#### Args:

* **`contents`**: A `Tensor` of type `string`. 0-D.  The PNG-encoded
  image.
* **`channels`**: An optional `int`. Defaults to `0`. Number of color
  channels for the decoded image.
* **`dtype`**: An optional `tf.DType` from: `tf.uint8,
  tf.uint16`. Defaults to `tf.uint 8`.
* **`name`**: A name for the operation (optional).
</pre>