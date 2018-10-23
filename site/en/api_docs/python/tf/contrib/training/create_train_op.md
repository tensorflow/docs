

page_type: reference
<style> table img { max-width: 100%; } </style>


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.training.create_train_op

``` python
tf.contrib.training.create_train_op(
    total_loss,
    optimizer,
    global_step=_USE_GLOBAL_STEP,
    update_ops=None,
    variables_to_train=None,
    transform_grads_fn=None,
    summarize_gradients=False,
    gate_gradients=tf_optimizer.Optimizer.GATE_OP,
    aggregation_method=None,
    colocate_gradients_with_ops=False,
    check_numerics=True
)
```



Defined in [`tensorflow/contrib/training/python/training/training.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.7/tensorflow/contrib/training/python/training/training.py).

Creates an `Operation` that evaluates the gradients and returns the loss.

#### Args:

* <b>`total_loss`</b>: A `Tensor` representing the total loss.
* <b>`optimizer`</b>: A tf.Optimizer to use for computing the gradients.
* <b>`global_step`</b>: A `Tensor` representing the global step variable. If left as
    `_USE_GLOBAL_STEP`, then tf.contrib.framework.global_step() is used.
* <b>`update_ops`</b>: An optional list of updates to execute. If `update_ops` is
    `None`, then the update ops are set to the contents of the
    `tf.GraphKeys.UPDATE_OPS` collection. If `update_ops` is not `None`, but
    it doesn't contain all of the update ops in `tf.GraphKeys.UPDATE_OPS`,
    a warning will be displayed.
* <b>`variables_to_train`</b>: an optional list of variables to train. If None, it will
    default to all tf.trainable_variables().
* <b>`transform_grads_fn`</b>: A function which takes a single argument, a list of
    gradient to variable pairs (tuples), performs any requested gradient
    updates, such as gradient clipping or multipliers, and returns the updated
    list.
* <b>`summarize_gradients`</b>: Whether or not add summaries for each gradient.
* <b>`gate_gradients`</b>: How to gate the computation of gradients. See tf.Optimizer.
* <b>`aggregation_method`</b>: Specifies the method used to combine gradient terms.
    Valid values are defined in the class `AggregationMethod`.
* <b>`colocate_gradients_with_ops`</b>: Whether or not to try colocating the gradients
    with the ops that generated them.
* <b>`check_numerics`</b>: Whether or not we apply check_numerics.


#### Returns:

A `Tensor` that when evaluated, computes the gradients and returns the total
  loss value.