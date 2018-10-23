

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.replicate_model_fn

``` python
replicate_model_fn(
    model_fn,
    optimizer_fn,
    devices=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/replicate_model_fn.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/estimator/python/estimator/replicate_model_fn.py).

Replicate `Estimator.model_fn` over GPUs within a single host.

The given `model_fn` specifies a single forward pass of a model.  To replicate
such a model over GPUs, each GPU gets its own instance of the forward pass
(a.k.a. a tower).  The input features and labels get sharded into the chunks
that correspond to the number of GPUs.  Each tower computes its own loss based
on its input.  For each such loss, gradients are computed.  After that, the
available losses are summed to form aggregated loss.  The available
gradients are summed too.  Then, they update weights using the specified
optimizer.

If `devices` are `None`, then all available GPUs are going to be used for
replication.  If no GPUs are available, then the model is going to be
placed on the CPU.

Two modes of local replication over available GPUs are supported:
  1)  If exactly 1 GPU is detected, then variables and operations are placed
      onto GPU.
  2)  If more than 1 GPU is detected, then variables are going to be placed on
      the CPU.  Replicas of operations are placed on each individual GPU.

Here is an example of how one might use their `model_fn` to run over GPUs:
>        def optimizer_fn():
>          return tf.train.GradientDescentOptimizer(learning_rate=0.001)
>        ...
>        def model_fn(...):  # See `model_fn` in `Estimator`.
>          loss = ...
>          if mode == tf.estimator.ModeKeys.TRAIN:
>            #  See the section below on `EstimatorSpec.train_op`.
>            return EstimatorSpec(mode=mode, loss=loss, train_op=tf.noop())
>     
>          #  No change for `ModeKeys.EVAL` or `ModeKeys.PREDICT`.
>          return EstimatorSpec(...)
>        ...
>        classifier = tf.estimator.Estimator(
>          model_fn=replicate_model_fn.replicate_model_fn(model_fn, optimizer_fn))

On `EstimatorSpec.train_op`:
`model_fn` returns `EstimatorSpec.train_op` for
`tf.estimator.GraphKeys.TRAIN`. It is typically derived using an optimizer.
`replicate_model_fn` ignores the returned `EstimatorSpec.train_op`, so there
is no need to use an optimizer inside the user's `model_fn`.  The
`EstimatorSpec.loss` subgraph is going to be executed, while
`EstimatorSpec.train_op` isn't going to be executed. One could pass
`train_op=tf.noop()` to `EstimatorSpec`.

On sharding input features and labels:
Input features and labels are split for consumption by each tower. They are
split across the dimension 0.  Features and labels need to be batch major.

On reduction algorithms:
Certain algorithms were chosen for aggregating results of computations on
multiple towers:
  - Losses from all towers are reduced using sum.
  - Gradients are reduced using sum for each trainable variable.
  - `eval_metrics_ops` are reduced per metric using `reduce_mean`.
  - `EstimatorSpec.predictions` and `EstimatorSpec.export_outputs` are
    reduced using concatenation.
  - For all other fields of `EstimatorSpec` the values of the first tower
    are taken.

On distribution of variables:
Variables are not duplicated between towers.  Instead, they are placed on a
single device as defined above and shared across towers.

Other current limitations:
  - `predictions` are not supported for `ModeKeys.EVAL`.  That is required for
    `tf.contrib.estimator.add_metrics`.

#### Args:

* <b>`model_fn`</b>: `model_fn` as defined in `Estimator`.  See the section above about
    the train_op argument of `EstimatorSpec`.
* <b>`optimizer_fn`</b>: a function that returns an optimizer instance.  The function
    may accept one `params` argument.  This is the `params` argument as
    defined by `Estimator`.  See  the `Estimator` documentation for details.
* <b>`devices`</b>: Optional list of devices to replicate the model across.  This
    argument can be used to replice only on the subset of available GPUs.
    If `None`, then all available GPUs are going to be used for replication.
    If no GPUs are available, then the model is going to be placed on the CPU.


#### Returns:

A replicated version of the supplied `model_fn`. Returned function that
  conforms to the requirements of `Estimator`'s `model_fn` and can be used
  instead of the supplied `model_fn`.