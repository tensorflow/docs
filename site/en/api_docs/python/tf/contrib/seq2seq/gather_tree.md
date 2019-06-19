page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.gather_tree

``` python
tf.contrib.seq2seq.gather_tree(
    step_ids,
    parent_ids,
    max_sequence_lengths,
    end_token,
    name=None
)
```



Defined in generated file: `tensorflow/contrib/seq2seq/ops/gen_beam_search_ops.py`.

Calculates the full beams from the per-step ids and parent beam ids.

On CPU, if an out of bound parent id is found, an error is returned.
On GPU, if an out of bound parent id is found, a -1 is stored in the
corresponding output value and the execution for that beam returns early.

For a given beam, past the time step containing the first decoded `end_token`
all values are filled in with `end_token`.

TODO(ebrevdo): fill in the remainder of this docstring.

#### Args:

* <b>`step_ids`</b>: A `Tensor`. Must be one of the following types: `int32`.
    `[max_time, batch_size, beam_width]`.
* <b>`parent_ids`</b>: A `Tensor`. Must have the same type as `step_ids`.
    `[max_time, batch_size, beam_width]`.
* <b>`max_sequence_lengths`</b>: A `Tensor` of type `int32`. `[batch_size]`.
* <b>`end_token`</b>: A `Tensor`. Must have the same type as `step_ids`. `[]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `step_ids`.
`[max_time, batch_size, beam_width]`.