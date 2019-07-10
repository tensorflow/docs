page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.collapse_repeated

Merge repeated labels into single labels.

### Aliases:

* `tf.compat.v1.nn.collapse_repeated`
* `tf.compat.v2.nn.collapse_repeated`
* `tf.nn.collapse_repeated`

``` python
tf.nn.collapse_repeated(
    labels,
    seq_length,
    name=None
)
```



Defined in [`python/ops/ctc_ops.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/ops/ctc_ops.py).

<!-- Placeholder for "Used in" -->


#### Args:


* <b>`labels`</b>: Tensor of shape [batch, max value in seq_length]
* <b>`seq_length`</b>: Tensor of shape [batch], sequence length of each batch element.
* <b>`name`</b>: A name for this `Op`. Defaults to "collapse_repeated_labels".


#### Returns:

A tuple `(collapsed_labels, new_seq_length)` where


* <b>`collapsed_labels`</b>: Tensor of shape [batch, max_seq_length] with repeated
labels collapsed and padded to max_seq_length, eg:
`[[A, A, B, B, A], [A, B, C, D, E]] => [[A, B, A, 0, 0], [A, B, C, D, E]]`

* <b>`new_seq_length`</b>: int tensor of shape [batch] with new sequence lengths.