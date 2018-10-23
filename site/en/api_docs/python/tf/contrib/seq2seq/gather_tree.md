

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.seq2seq.gather_tree

### `tf.contrib.seq2seq.gather_tree`

``` python
gather_tree(
    step_ids,
    parent_ids,
    sequence_length,
    name=None
)
```



Defined in `tensorflow/contrib/seq2seq/ops/gen_beam_search_ops.py`.

Calculates the full beams from the per-step ids and parent beam ids.

This op implements the following mathematical equations:

```python
TODO(ebrevdo): fill in
```

#### Args:

* <b>`step_ids`</b>: A `Tensor`. Must be one of the following types: `int32`.
    `[max_time, batch_size, beam_width]`.
* <b>`parent_ids`</b>: A `Tensor`. Must have the same type as `step_ids`.
    `[max_time, batch_size, beam_width]`.
* <b>`sequence_length`</b>: A `Tensor`. Must have the same type as `step_ids`.
    `[batch_size, beam_width]`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

  A `Tensor`. Has the same type as `step_ids`.
  `[max_time, batch_size, beam_width]`.