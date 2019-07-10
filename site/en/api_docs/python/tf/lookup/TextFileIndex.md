page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.lookup.TextFileIndex

## Class `TextFileIndex`

The key and value content to get from each line.



### Aliases:

* Class `tf.compat.v1.lookup.TextFileIndex`
* Class `tf.compat.v2.lookup.TextFileIndex`
* Class `tf.contrib.lookup.TextFileIndex`
* Class `tf.lookup.TextFileIndex`



Defined in [`python/ops/lookup_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/lookup_ops.py).

<!-- Placeholder for "Used in" -->

This class defines the key and value used for tf.lookup.TextFileInitializer.

The key and value content to get from each line is specified either
by the following, or a value `>=0`.
* <a href="../../tf/lookup/TextFileIndex#LINE_NUMBER"><code>TextFileIndex.LINE_NUMBER</code></a> means use the line number starting from zero,
  expects data type int64.
* <a href="../../tf/lookup/TextFileIndex#WHOLE_LINE"><code>TextFileIndex.WHOLE_LINE</code></a> means use the whole line content, expects data
  type string.

A value `>=0` means use the index (starting at zero) of the split line based
    on `delimiter`.

## Class Members

* `LINE_NUMBER = -1` <a id="LINE_NUMBER"></a>
* `WHOLE_LINE = -2` <a id="WHOLE_LINE"></a>
