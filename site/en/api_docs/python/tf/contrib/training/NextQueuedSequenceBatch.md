

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.NextQueuedSequenceBatch

## Class `NextQueuedSequenceBatch`





Defined in [`tensorflow/contrib/training/python/training/sequence_queueing_state_saver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/training/python/training/sequence_queueing_state_saver.py).

See the guide: [Training (contrib) > Splitting sequence inputs into minibatches with state saving](../../../../../api_guides/python/contrib.training#Splitting_sequence_inputs_into_minibatches_with_state_saving)

NextQueuedSequenceBatch stores deferred SequenceQueueingStateSaver data.

This class is instantiated by `SequenceQueueingStateSaver` and is accessible
via its `next_batch` property.

## Properties

<h3 id="batch_size"><code>batch_size</code></h3>

The batch_size of the given batch.

Usually, this is the batch_size requested when initializing the SQSS, but
if allow_small_batch=True this will become smaller when inputs are
exhausted.

#### Returns:

A scalar integer tensor, the batch_size

<h3 id="context"><code>context</code></h3>

A dict mapping keys of `input_context` to batched context.

#### Returns:

A dict mapping keys of `input_context` to tensors.
If we had at input:

```python
context["name"].get_shape() == [d1, d2, ...]
```

then for this property:

```python
context["name"].get_shape() == [batch_size, d1, d2, ...]
```

<h3 id="insertion_index"><code>insertion_index</code></h3>

The insertion indices of the examples (when they were first added).

These indices start with the value -2**63 and increase with every
call to the prefetch op.  Each whole example gets its own insertion
index, and this is used to prioritize the example so that its truncated
segments appear in adjacent iterations, even if new examples are inserted
by the prefetch op between iterations.

#### Returns:

An int64 vector of length `batch_size`, the insertion indices.

<h3 id="key"><code>key</code></h3>

The key names of the given truncated unrolled examples.

The format of the key is:

```python
"%05d_of_%05d:%s" % (sequence, sequence_count, original_key)
```

where `original_key` is the unique key read in by the prefetcher.

#### Returns:

A string vector of length `batch_size`, the keys.

<h3 id="length"><code>length</code></h3>

The lengths of the given truncated unrolled examples.

For initial iterations, for which `sequence * num_unroll < length`,
this number is `num_unroll`.  For the remainder,
this number is between `0` and `num_unroll`.

#### Returns:

An integer vector of length `batch_size`, the lengths.

<h3 id="next_key"><code>next_key</code></h3>

The key names of the next (in iteration) truncated unrolled examples.

The format of the key is:

```python
"%05d_of_%05d:%s" % (sequence + 1, sequence_count, original_key)
```

if `sequence + 1 < sequence_count`, otherwise:

```python
"STOP:%s" % original_key
```

where `original_key` is the unique key read in by the prefetcher.

#### Returns:

A string vector of length `batch_size`, the keys.

<h3 id="sequence"><code>sequence</code></h3>

An int32 vector, length `batch_size`: the sequence index of each entry.

When an input is split up, the sequence values

```
0, 1, ..., sequence_count - 1
```
are assigned to each split.

#### Returns:

An int32 vector `Tensor`.

<h3 id="sequence_count"><code>sequence_count</code></h3>

An int32 vector, length `batch_size`: the sequence count of each entry.

When an input is split up, the number of splits is equal to:
`padded_length / num_unroll`.  This is the sequence_count.

#### Returns:

An int32 vector `Tensor`.

<h3 id="sequences"><code>sequences</code></h3>

A dict mapping keys of `input_sequences` to split and rebatched data.

#### Returns:

A dict mapping keys of `input_sequences` to tensors.
If we had at input:

```python
sequences["name"].get_shape() == [None, d1, d2, ...]
```

where `None` meant the sequence time was dynamic, then for this property:

```python
sequences["name"].get_shape() == [batch_size, num_unroll, d1, d2, ...].
```

<h3 id="total_length"><code>total_length</code></h3>

The lengths of the original (non-truncated) unrolled examples.

#### Returns:

An integer vector of length `batch_size`, the total lengths.



## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(state_saver)
```



<h3 id="save_state"><code>save_state</code></h3>

``` python
save_state(
    state_name,
    value,
    name=None
)
```

Returns an op to save the current batch of state `state_name`.

#### Args:

* <b>`state_name`</b>: string, matches a key provided in `initial_states`.
* <b>`value`</b>: A `Tensor`.
    Its type must match that of `initial_states[state_name].dtype`.
    If we had at input:

    ```python
    initial_states[state_name].get_shape() == [d1, d2, ...]
    ```

    then the shape of `value` must match:

    ```python
    tf.shape(value) == [batch_size, d1, d2, ...]
    ```

* <b>`name`</b>: string (optional).  The name scope for newly created ops.


#### Returns:

A control flow op that stores the new state of each entry into
the state saver.  This op must be run for every iteration that
accesses data from the state saver (otherwise the state saver
will never progress through its states and run out of capacity).


#### Raises:

* <b>`KeyError`</b>: if `state_name` does not match any of the initial states
    declared in `initial_states`.

<h3 id="state"><code>state</code></h3>

``` python
state(state_name)
```

Returns batched state tensors.

#### Args:

* <b>`state_name`</b>: string, matches a key provided in `initial_states`.


#### Returns:

A `Tensor`: a batched set of states, either initial states (if this is
the first run of the given example), or a value as stored during
a previous iteration via `save_state` control flow.
Its type is the same as `initial_states["state_name"].dtype`.
If we had at input:

```python
initial_states[state_name].get_shape() == [d1, d2, ...],
```

then

```python
state(state_name).get_shape() == [batch_size, d1, d2, ...]
```


#### Raises:

* <b>`KeyError`</b>: if `state_name` does not match any of the initial states
    declared in `initial_states`.



