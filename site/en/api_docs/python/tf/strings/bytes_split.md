page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.bytes_split


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/ops/ragged/ragged_string_ops.py#L34-L79">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Split string elements of `input` into bytes.

### Aliases:

* `tf.compat.v1.strings.bytes_split`
* `tf.compat.v2.strings.bytes_split`


``` python
tf.strings.bytes_split(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### Examples:

<pre class="devsite-click-to-copy prettyprint lang-py">
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}tf.strings.bytes_split('hello'){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}['h', 'e', 'l', 'l', 'o']{% endhtmlescape %}</code>
<code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">{% htmlescape %}tf.strings.bytes_split(['hello', '123']){% endhtmlescape %}</code>
<code class="no-select nocode">{% htmlescape %}<RaggedTensor [['h', 'e', 'l', 'l', 'o'], ['1', '2', '3']]>{% endhtmlescape %}</code>
</pre>

Note that this op splits strings into bytes, not unicode characters.  To
split strings into unicode characters, use <a href="../../tf/strings/unicode_split"><code>tf.strings.unicode_split</code></a>.

See also: <a href="../../tf/io/decode_raw"><code>tf.io.decode_raw</code></a>, <a href="../../tf/strings/split"><code>tf.strings.split</code></a>, <a href="../../tf/strings/unicode_split"><code>tf.strings.unicode_split</code></a>.

#### Args:


* <b>`input`</b>: A string `Tensor` or `RaggedTensor`: the strings to split.  Must
  have a statically known rank (`N`).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `RaggedTensor` of rank `N+1`: the bytes that make up the source strings.
