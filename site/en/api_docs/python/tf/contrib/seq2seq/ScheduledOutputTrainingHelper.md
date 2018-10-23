

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.contrib.seq2seq.ScheduledOutputTrainingHelper

### `class tf.contrib.seq2seq.ScheduledOutputTrainingHelper`



Defined in [`tensorflow/contrib/seq2seq/python/ops/helper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/contrib/seq2seq/python/ops/helper.py).

See the guide: [Seq2seq Library (contrib) > Dynamic Decoding](../../../../../api_guides/python/contrib.seq2seq#Dynamic_Decoding)

A training helper that adds scheduled sampling directly to outputs.

Returns False for sample_ids where no sampling took place; True elsewhere.

## Properties

<h3 id="batch_size"><code>batch_size</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    inputs,
    sequence_length,
    sampling_probability,
    time_major=False,
    seed=None,
    next_input_layer=None,
    auxiliary_inputs=None,
    name=None
)
```

Initializer.

#### Args:

* <b>`inputs`</b>: A (structure) of input tensors.
* <b>`sequence_length`</b>: An int32 vector tensor.
* <b>`sampling_probability`</b>: A 0D `float32` tensor: the probability of sampling
    from the outputs instead of reading directly from the inputs.
* <b>`time_major`</b>: Python bool.  Whether the tensors in `inputs` are time major.
    If `False` (default), they are assumed to be batch major.
* <b>`seed`</b>: The sampling seed.
* <b>`next_input_layer`</b>: (Optional) An instance of `tf.layers.Layer`, i.e.,
    `tf.layers.Dense`.  Optional layer to apply to the RNN output to create
    the next input.
* <b>`auxiliary_inputs`</b>: An optional (structure of) auxiliary input tensors with
    a shape that matches `inputs` in all but (potentially) the final
    dimension. These tensors will be concatenated to the sampled output or
    the `inputs` when not sampling for use as the next input.
* <b>`name`</b>: Name scope for any created operations.


#### Raises:

* <b>`ValueError`</b>: if `sampling_probability` is not a scalar or vector.

<h3 id="initialize"><code>initialize</code></h3>

``` python
initialize(name=None)
```



<h3 id="next_inputs"><code>next_inputs</code></h3>

``` python
next_inputs(
    time,
    outputs,
    state,
    sample_ids,
    name=None
)
```



<h3 id="sample"><code>sample</code></h3>

``` python
sample(
    time,
    outputs,
    state,
    name=None
)
```





