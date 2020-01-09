page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.compat.v1.train.maybe_batch


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/training/input.py#L1023-L1077">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Conditionally creates batches of tensors based on `keep_input`. (deprecated)

``` python
tf.compat.v1.train.maybe_batch(
    tensors,
    keep_input,
    batch_size,
    num_threads=1,
    capacity=32,
    enqueue_many=False,
    shapes=None,
    dynamic_pad=False,
    allow_smaller_final_batch=False,
    shared_name=None,
    name=None
)
```



<!-- Placeholder for "Used in" -->

Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
Instructions for updating:
Queue-based input pipelines have been replaced by <a href="../../../../tf/data"><code>tf.data</code></a>. Use `tf.data.Dataset.filter(...).batch(batch_size)` (or `padded_batch(...)` if `dynamic_pad=True`).

See docstring in `batch` for more details.

#### Args:


* <b>`tensors`</b>: The list or dictionary of tensors to enqueue.
* <b>`keep_input`</b>: A `bool` Tensor.  This tensor controls whether the input is
  added to the queue or not.  If it is a scalar and evaluates `True`, then
  `tensors` are all added to the queue. If it is a vector and `enqueue_many`
  is `True`, then each example is added to the queue only if the
  corresponding value in `keep_input` is `True`. This tensor essentially
  acts as a filtering mechanism.
* <b>`batch_size`</b>: The new batch size pulled from the queue.
* <b>`num_threads`</b>: The number of threads enqueuing `tensors`.  The batching will
  be nondeterministic if `num_threads > 1`.
* <b>`capacity`</b>: An integer. The maximum number of elements in the queue.
* <b>`enqueue_many`</b>: Whether each tensor in `tensors` is a single example.
* <b>`shapes`</b>: (Optional) The shapes for each example.  Defaults to the
  inferred shapes for `tensors`.
* <b>`dynamic_pad`</b>: Boolean.  Allow variable dimensions in input shapes.
  The given dimensions are padded upon dequeue so that tensors within a
  batch have the same shapes.
* <b>`allow_smaller_final_batch`</b>: (Optional) Boolean. If `True`, allow the final
  batch to be smaller if there are insufficient items left in the queue.
* <b>`shared_name`</b>: (Optional). If set, this queue will be shared under the given
  name across multiple sessions.
* <b>`name`</b>: (Optional) A name for the operations.


#### Returns:

A list or dictionary of tensors with the same types as `tensors`.



#### Raises:


* <b>`ValueError`</b>: If the `shapes` are not specified, and cannot be
  inferred from the elements of `tensors`.
