page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.unicode_decode_with_offsets


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L225-L283">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Decodes each string into a sequence of code points with start offsets.

### Aliases:

* `tf.compat.v1.strings.unicode_decode_with_offsets`
* `tf.compat.v2.strings.unicode_decode_with_offsets`


``` python
tf.strings.unicode_decode_with_offsets(
    input,
    input_encoding,
    errors='replace',
    replacement_char=65533,
    replace_control_characters=False,
    name=None
)
```



### Used in the tutorials:

* [Unicode strings](https://www.tensorflow.org/tutorials/load_data/unicode)



This op is similar to `tf.strings.decode(...)`, but it also returns the
start offset for each character in its respective string.  This information
can be used to align the characters with the original byte sequence.

Returns a tuple `(codepoints, start_offsets)` where:

* `codepoints[i1...iN, j]` is the Unicode codepoint for the `j`th character
  in `input[i1...iN]`, when decoded using `input_encoding`.
* `start_offsets[i1...iN, j]` is the start byte offset for the `j`th
  character in `input[i1...iN]`, when decoded using `input_encoding`.

#### Args:


* <b>`input`</b>: An `N` dimensional potentially ragged `string` tensor with shape
  `[D1...DN]`.  `N` must be statically known.
* <b>`input_encoding`</b>: String name for the unicode encoding that should be used to
  decode each string.
* <b>`errors`</b>: Specifies the response when an input string can't be converted
  using the indicated encoding. One of:
  * `'strict'`: Raise an exception for any illegal substrings.
  * `'replace'`: Replace illegal substrings with `replacement_char`.
  * `'ignore'`: Skip illegal substrings.
* <b>`replacement_char`</b>: The replacement codepoint to be used in place of invalid
  substrings in `input` when `errors='replace'`; and in place of C0 control
  characters in `input` when `replace_control_characters=True`.
* <b>`replace_control_characters`</b>: Whether to replace the C0 control characters
  `(U+0000 - U+001F)` with the `replacement_char`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A tuple of `N+1` dimensional tensors `(codepoints, start_offsets)`.

* `codepoints` is an `int32` tensor with shape `[D1...DN, (num_chars)]`.
* `offsets` is an `int64` tensor with shape `[D1...DN, (num_chars)]`.

The returned tensors are <a href="../../tf/Tensor"><code>tf.Tensor</code></a>s if `input` is a scalar, or
<a href="../../tf/RaggedTensor"><code>tf.RaggedTensor</code></a>s otherwise.


#### Example:

>      >>> input = [s.encode('utf8') for s in (u'G\xf6\xf6dnight', u'\U0001f60a')]
>      >>> result = tf.strings.unicode_decode_with_offsets(input, 'UTF-8')
>      >>> result[0].tolist()  # codepoints
>      [[71, 246, 246, 100, 110, 105, 103, 104, 116], [128522]]
>      >>> result[1].tolist()  # offsets
>     [[0, 1, 3, 5, 6, 7, 8, 9, 10], [0]]
