page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.ScheduledEmbeddingTrainingHelper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L315-L413">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ScheduledEmbeddingTrainingHelper`

A training helper that adds scheduled sampling.

Inherits From: [`TrainingHelper`](../../../tf/contrib/seq2seq/TrainingHelper)

<!-- Placeholder for "Used in" -->

Returns -1s for sample_ids where no sampling took place; valid sample id
values elsewhere.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L322-L362">View source</a>

``` python
__init__(
    inputs,
    sequence_length,
    embedding,
    sampling_probability,
    time_major=False,
    seed=None,
    scheduling_seed=None,
    name=None
)
```

Initializer.


#### Args:


* <b>`inputs`</b>: A (structure of) input tensors.
* <b>`sequence_length`</b>: An int32 vector tensor.
* <b>`embedding`</b>: A callable that takes a vector tensor of `ids` (argmax ids),
  or the `params` argument for `embedding_lookup`.
* <b>`sampling_probability`</b>: A 0D `float32` tensor: the probability of sampling
  categorically from the output ids instead of reading directly from the
  inputs.
* <b>`time_major`</b>: Python bool.  Whether the tensors in `inputs` are time major.
  If `False` (default), they are assumed to be batch major.
* <b>`seed`</b>: The sampling seed.
* <b>`scheduling_seed`</b>: The schedule decision rule sampling seed.
* <b>`name`</b>: Name scope for any created operations.


#### Raises:


* <b>`ValueError`</b>: if `sampling_probability` is not a scalar or vector.



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L364-L365">View source</a>

``` python
initialize(name=None)
```

Returns `(initial_finished, initial_inputs)`.


<h3 id="next_inputs"><code>next_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L381-L413">View source</a>

``` python
next_inputs(
    time,
    outputs,
    state,
    sample_ids,
    name=None
)
```

next_inputs_fn for TrainingHelper.


<h3 id="sample"><code>sample</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L367-L379">View source</a>

``` python
sample(
    time,
    outputs,
    state,
    name=None
)
```

Returns `sample_ids`.
