page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.CustomHelper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L168-L224">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `CustomHelper`

Base abstract class that allows the user to customize sampling.

Inherits From: [`Helper`](../../../tf/contrib/seq2seq/Helper)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L171-L192">View source</a>

``` python
__init__(
    initialize_fn,
    sample_fn,
    next_inputs_fn,
    sample_ids_shape=None,
    sample_ids_dtype=None
)
```

Initializer.


#### Args:


* <b>`initialize_fn`</b>: callable that returns `(finished, next_inputs)`
  for the first iteration.
* <b>`sample_fn`</b>: callable that takes `(time, outputs, state)`
  and emits tensor `sample_ids`.
* <b>`next_inputs_fn`</b>: callable that takes `(time, outputs, state, sample_ids)`
  and emits `(finished, next_inputs, next_state)`.
* <b>`sample_ids_shape`</b>: Either a list of integers, or a 1-D Tensor of type
  `int32`, the shape of each value in the `sample_ids` batch. Defaults to
  a scalar.
* <b>`sample_ids_dtype`</b>: The dtype of the `sample_ids` tensor. Defaults to int32.



## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

Batch size of tensor returned by `sample`.

Returns a scalar int32 tensor.

<h3 id="sample_ids_dtype"><code>sample_ids_dtype</code></h3>

DType of tensor returned by `sample`.

Returns a DType.

<h3 id="sample_ids_shape"><code>sample_ids_shape</code></h3>

Shape of tensor returned by `sample`, excluding the batch dimension.

Returns a `TensorShape`.



## Methods

<h3 id="initialize"><code>initialize</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L208-L213">View source</a>

``` python
initialize(name=None)
```

Returns `(initial_finished, initial_inputs)`.


<h3 id="next_inputs"><code>next_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L220-L224">View source</a>

``` python
next_inputs(
    time,
    outputs,
    state,
    sample_ids,
    name=None
)
```

Returns `(finished, next_inputs, next_state)`.


<h3 id="sample"><code>sample</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L215-L218">View source</a>

``` python
sample(
    time,
    outputs,
    state,
    name=None
)
```

Returns `sample_ids`.
