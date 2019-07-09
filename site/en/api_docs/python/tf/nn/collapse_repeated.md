page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.collapse_repeated

``` python
tf.nn.collapse_repeated(
    labels,
    seq_length,
    name=None
)
```



Defined in [`tensorflow/python/ops/ctc_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/ctc_ops.py).

Merge repeated labels into single labels.

#### Args:

* <b>`labels`</b>: Tensor of shape (batch, max value in seq_length)
* <b>`seq_length`</b>: Tensor of shape (batch), sequence length of each batch element.
* <b>`name`</b>: A name for this `Op`. Defaults to "collapse_repeated_labels".


#### Returns:

tuple of Tensor of shape (batch, max_seq_length) with repeated labels
collapsed and padded to max_seq_length, eg:
    [[A, A, B, B, A],
     [A, B, C, D, E]] => [[A, B, A, 0, 0],
                          [A, B, C, D, E]]
and int tensor of shape [batch] with new sequence lengths.