page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.TrainingHelper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L227-L312">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TrainingHelper`

A helper for use during training.  Only reads inputs.

Inherits From: [`Helper`](../../../tf/contrib/seq2seq/Helper)

<!-- Placeholder for "Used in" -->

Returned sample_ids are the argmax of the RNN output logits.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L233-L263">View source</a>

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



## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

Batch size of tensor returned by `sample`.

Returns a scalar int32 tensor.

<h3 id="inputs"><code>inputs</code></h3>




<h3 id="sample_ids_dtype"><code>sample_ids_dtype</code></h3>

DType of tensor returned by `sample`.

Returns a DType.

<h3 id="sample_ids_shape"><code>sample_ids_shape</code></h3>

Shape of tensor returned by `sample`, excluding the batch dimension.

Returns a `TensorShape`.

<h3 id="sequence_length"><code>sequence_length</code></h3>






## Methods

<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L285-L292">View source</a>

``` python
initialize(name=None)
```

Returns `(initial_finished, initial_inputs)`.


<h3 id="next_inputs"><code>next_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L300-L312">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L294-L298">View source</a>

``` python
sample(
    time,
    outputs,
    name=None,
    **unused_kwargs
)
```

Returns `sample_ids`.
