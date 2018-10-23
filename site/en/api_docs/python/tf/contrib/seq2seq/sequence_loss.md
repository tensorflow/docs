

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.sequence_loss

### `tf.contrib.seq2seq.sequence_loss`

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



Defined in [`tensorflow/contrib/seq2seq/python/ops/loss.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/python/ops/loss.py).

Weighted cross-entropy loss for a sequence of logits (per example).

#### Args:

* <b>`logits`</b>: A 3D Tensor of shape
    [batch_size x sequence_length x num_decoder_symbols] and dtype float.
    The logits correspond to the prediction across all classes at each
    timestep.
* <b>`targets`</b>: A 2D Tensor of shape [batch_size x sequence_length] and dtype
    int. The target represents the true class at each timestep.
* <b>`weights`</b>: A 2D Tensor of shape [batch_size x sequence_length] and dtype
    float. Weights constitutes the weighting of each prediction in the
    sequence. When using weights as masking set all valid timesteps to 1 and
    all padded timesteps to 0.
* <b>`average_across_timesteps`</b>: If set, sum the cost across the sequence
    dimension and divide the cost by the total label weight across timesteps.
* <b>`average_across_batch`</b>: If set, sum the cost across the batch dimension and
    divide the returned cost by the batch size.
* <b>`softmax_loss_function`</b>: Function (labels-batch, inputs-batch) -> loss-batch
    to be used instead of the standard softmax (the default if this is None).
* <b>`name`</b>: Optional name for this operation, defaults to "sequence_loss".


#### Returns:

  A scalar float Tensor: The average log-perplexity per symbol (weighted).


#### Raises:

* <b>`ValueError`</b>: logits does not have 3 dimensions or targets does not have 2
              dimensions or weights does not have 2 dimensions.