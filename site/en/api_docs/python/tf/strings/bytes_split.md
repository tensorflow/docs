page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.strings.bytes_split

Split string elements of `input` into bytes.

### Aliases:

* `tf.compat.v1.strings.bytes_split`
* `tf.compat.v2.strings.bytes_split`
* `tf.strings.bytes_split`

``` python
tf.strings.bytes_split(
    input,
    name=None
)
```



Defined in [`python/ops/ragged/ragged_string_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ragged/ragged_string_ops.py).

<!-- Placeholder for "Used in" -->


#### Examples:



```python
>>> tf.strings.to_bytes('hello')
['h', 'e', 'l', 'l', 'o']
>>> tf.strings.to_bytes(['hello', '123'])
<RaggedTensor [['h', 'e', 'l', 'l', 'o'], ['1', '2', '3']]>
```

Note that this op splits strings into bytes, not unicode characters.  To
split strings into unicode characters, use <a href="../../tf/strings/unicode_split"><code>tf.strings.unicode_split</code></a>.

See also: <a href="../../tf/decode_raw"><code>tf.io.decode_raw</code></a>, <a href="../../tf/strings/split"><code>tf.strings.split</code></a>, <a href="../../tf/strings/unicode_split"><code>tf.strings.unicode_split</code></a>.

#### Args:


* <b>`input`</b>: A string `Tensor` or `RaggedTensor`: the strings to split.  Must
  have a statically known rank (`N`).
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `RaggedTensor` of rank `N+1`: the bytes that make up the soruce strings.
