

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.TrainingHelper

## Class `TrainingHelper`

Inherits From: [`Helper`](../../../tf/contrib/seq2seq/Helper)



Defined in [`tensorflow/contrib/seq2seq/python/ops/helper.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/seq2seq/python/ops/helper.py).

See the guide: [Seq2seq Library (contrib) > Dynamic Decoding](../../../../../api_guides/python/contrib.seq2seq#Dynamic_Decoding)

A helper for use during training.  Only reads inputs.

Returned sample_ids are the argmax of the RNN output logits.

## Properties

<h3 id="batch_size"><code>batch_size</code></h3>



<h3 id="inputs"><code>inputs</code></h3>



<h3 id="sample_ids_dtype"><code>sample_ids_dtype</code></h3>



<h3 id="sample_ids_shape"><code>sample_ids_shape</code></h3>



<h3 id="sequence_length"><code>sequence_length</code></h3>





## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    inputs,
    sequence_length,
    time_major=False,
    name=None
)
```

Initializer.

#### Args:

* <b>`inputs`</b>: A (structure of) input tensors.
* <b>`sequence_length`</b>: An int32 vector tensor.
* <b>`time_major`</b>: Python bool.  Whether the tensors in `inputs` are time major.
    If `False` (default), they are assumed to be batch major.
* <b>`name`</b>: Name scope for any created operations.


#### Raises:

* <b>`ValueError`</b>: if `sequence_length` is not a 1D tensor.

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
    name=None,
    **unused_kwargs
)
```

next_inputs_fn for TrainingHelper.

<h3 id="sample"><code>sample</code></h3>

``` python
sample(
    time,
    outputs,
    name=None,
    **unused_kwargs
)
```





