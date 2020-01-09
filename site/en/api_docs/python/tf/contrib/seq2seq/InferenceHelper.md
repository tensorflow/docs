page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.seq2seq.InferenceHelper


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L681-L736">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `InferenceHelper`

A helper to use during inference with a custom sampling function.

Inherits From: [`Helper`](../../../tf/contrib/seq2seq/Helper)

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L684-L707">View source</a>

``` python
__init__(
    sample_fn,
    sample_shape,
    sample_dtype,
    start_inputs,
    end_fn,
    next_inputs_fn=None
)
```

Initializer.


#### Args:


* <b>`sample_fn`</b>: A callable that takes `outputs` and emits tensor `sample_ids`.
* <b>`sample_shape`</b>: Either a list of integers, or a 1-D Tensor of type `int32`,
  the shape of the each sample in the batch returned by `sample_fn`.
* <b>`sample_dtype`</b>: the dtype of the sample returned by `sample_fn`.
* <b>`start_inputs`</b>: The initial batch of inputs.
* <b>`end_fn`</b>: A callable that takes `sample_ids` and emits a `bool` vector
  shaped `[batch_size]` indicating whether each sample is an end token.
* <b>`next_inputs_fn`</b>: (Optional) A callable that takes `sample_ids` and returns
  the next batch of inputs. If not provided, `sample_ids` is used as the
  next batch of inputs.



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L721-L723">View source</a>

``` python
initialize(name=None)
```

Returns `(initial_finished, initial_inputs)`.


<h3 id="next_inputs"><code>next_inputs</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L729-L736">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/contrib/seq2seq/python/ops/helper.py#L725-L727">View source</a>

``` python
sample(
    time,
    outputs,
    state,
    name=None
)
```

Returns `sample_ids`.
