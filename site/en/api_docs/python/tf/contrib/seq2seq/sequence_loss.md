page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.sequence_loss

Weighted cross-entropy loss for a sequence of logits.

``` python
tf.contrib.seq2seq.sequence_loss(
    logits,
    targets,
    weights,
    average_across_timesteps=True,
    average_across_batch=True,
    sum_over_timesteps=False,
    sum_over_batch=False,
    softmax_loss_function=None,
    name=None
)
```



Defined in [`contrib/seq2seq/python/ops/loss.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/contrib/seq2seq/python/ops/loss.py).

<!-- Placeholder for "Used in" -->

Depending on the values of `average_across_timesteps` / `sum_over_timesteps`
and `average_across_batch` / `sum_over_batch`, the return Tensor will have
rank 0, 1, or 2 as these arguments reduce the cross-entropy at each target,
which has shape `[batch_size, sequence_length]`, over their respective
dimensions. For example, if `average_across_timesteps` is `True` and
`average_across_batch` is `False`, then the return Tensor will have shape
`[batch_size]`.

Note that `average_across_timesteps` and `sum_over_timesteps` cannot be True
at same time. Same for `average_across_batch` and `sum_over_batch`.

The recommended loss reduction in tf 2.0 has been changed to sum_over, instead
of weighted average. User are recommend to use `sum_over_timesteps` and
`sum_over_batch` for reduction.

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
  and all padded timesteps to 0, e.g. a mask returned by <a href="../../../tf/sequence_mask"><code>tf.sequence_mask</code></a>.
* <b>`average_across_timesteps`</b>: If set, sum the cost across the sequence
  dimension and divide the cost by the total label weight across timesteps.
* <b>`average_across_batch`</b>: If set, sum the cost across the batch dimension and
  divide the returned cost by the batch size.
* <b>`sum_over_timesteps`</b>: If set, sum the cost across the sequence dimension and
  divide the size of the sequence. Note that any element with 0 weights will
  be excluded from size calculation.
* <b>`sum_over_batch`</b>: if set, sum the cost across the batch dimension and divide
  the total cost by the batch size. Not that any element with 0 weights will
  be excluded from size calculation.
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