

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.nn.ctc_greedy_decoder

``` python
tf.nn.ctc_greedy_decoder(
    inputs,
    sequence_length,
    merge_repeated=True
)
```



Defined in [`tensorflow/python/ops/ctc_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/python/ops/ctc_ops.py).

See the guide: [Neural Network > Connectionist Temporal Classification (CTC)](../../../../api_guides/python/nn#Connectionist_Temporal_Classification_CTC_)

Performs greedy decoding on the logits given in input (best path).

Note: Regardless of the value of merge_repeated, if the maximum index of a
given time and batch corresponds to the blank index `(num_classes - 1)`, no
new element is emitted.

If `merge_repeated` is `True`, merge repeated classes in output.
This means that if consecutive logits' maximum indices are the same,
only the first of these is emitted.  The sequence `A B B * B * B` (where '*'
is the blank label) becomes

  * `A B B B` if `merge_repeated=True`.
  * `A B B B B` if `merge_repeated=False`.

#### Args:

* <b>`inputs`</b>: 3-D `float` `Tensor` sized
    `[max_time, batch_size, num_classes]`.  The logits.
* <b>`sequence_length`</b>: 1-D `int32` vector containing sequence lengths,
    having size `[batch_size]`.
* <b>`merge_repeated`</b>: Boolean.  Default: True.


#### Returns:

A tuple `(decoded, neg_sum_logits)` where
* <b>`decoded`</b>: A single-element list. `decoded[0]`
    is an `SparseTensor` containing the decoded outputs s.t.:
    `decoded.indices`: Indices matrix `(total_decoded_outputs, 2)`.
      The rows store: `[batch, time]`.
    `decoded.values`: Values vector, size `(total_decoded_outputs)`.
      The vector stores the decoded classes.
    `decoded.dense_shape`: Shape vector, size `(2)`.
      The shape values are: `[batch_size, max_decoded_length]`
* <b>`neg_sum_logits`</b>: A `float` matrix `(batch_size x 1)` containing, for the
      sequence found, the negative of the sum of the greatest logit at each
      timeframe.