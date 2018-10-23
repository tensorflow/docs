

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.seq2seq.sequence_loss

``` python
sequence_loss(
    logits,
    targets,
    weights,
    average_across_timesteps=True,
    average_across_batch=True,
    softmax_loss_function=None,
    name=None
)
```



Defined in [`tensorflow/contrib/seq2seq/python/ops/loss.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/seq2seq/python/ops/loss.py).

Weighted cross-entropy loss for a sequence of logits.

Depending on the values of `average_across_timesteps` and
`average_across_batch`, the return Tensor will have rank 0, 1, or 2 as these
arguments reduce the cross-entropy at each target, which has shape
`[batch_size, sequence_length]`, over their respective dimensions. For
example, if `average_across_timesteps` is `True` and `average_across_batch`
is `False`, then the return Tensor will have shape `[batch_size]`.

#### Args:

* <b>`logits`</b>: A Tensor of shape
    `[batch_size, sequence_length, num_decoder_symbols]` and dtype float.
    The logits correspond to the prediction across all classes at each
    timestep.
* <b>`targets`</b>: A Tensor of shape `[batch_size, sequence_length]` and dtype
    int. The target represents the true class at each timestep.
* <b>`weights`</b>: A Tensor of shape `[batch_size, sequence_length]` and dtype
    float. `weights` constitutes the weighting of each prediction in the
    sequence. When using `weights` as masking, set all valid timesteps to 1
    and all padded timesteps to 0, e.g. a mask returned by `tf.sequence_mask`.
* <b>`average_across_timesteps`</b>: If set, sum the cost across the sequence
    dimension and divide the cost by the total label weight across timesteps.
* <b>`average_across_batch`</b>: If set, sum the cost across the batch dimension and
    divide the returned cost by the batch size.
* <b>`softmax_loss_function`</b>: Function (labels, logits) -> loss-batch
    to be used instead of the standard softmax (the default if this is None).
    **Note that to avoid confusion, it is required for the function to accept
    named arguments.**
* <b>`name`</b>: Optional name for this operation, defaults to "sequence_loss".


#### Returns:

A float Tensor of rank 0, 1, or 2 depending on the
`average_across_timesteps` and `average_across_batch` arguments. By default,
it has rank 0 (scalar) and is the weighted average cross-entropy
(log-perplexity) per symbol.


#### Raises:

* <b>`ValueError`</b>: logits does not have 3 dimensions or targets does not have 2
              dimensions or weights does not have 2 dimensions.