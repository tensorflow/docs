

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.EvalSpec

## Class `EvalSpec`





Defined in [`tensorflow/python/estimator/training.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/estimator/training.py).

Configuration for the "eval" part for the `train_and_evaluate` call.

`EvalSpec` combines details of evaluation of the trained model as well as its
export. Evaluation consists of computing metrics to judge the performance of
the trained model.  Export writes out the trained model on to external
storage.

## Properties

<h3 id="exporters"><code>exporters</code></h3>

Alias for field number 4

<h3 id="hooks"><code>hooks</code></h3>

Alias for field number 3

<h3 id="input_fn"><code>input_fn</code></h3>

Alias for field number 0

<h3 id="name"><code>name</code></h3>

Alias for field number 2

<h3 id="start_delay_secs"><code>start_delay_secs</code></h3>

Alias for field number 5

<h3 id="steps"><code>steps</code></h3>

Alias for field number 1

<h3 id="throttle_secs"><code>throttle_secs</code></h3>

Alias for field number 6



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    input_fn,
    steps=100,
    name=None,
    hooks=None,
    exporters=None,
    start_delay_secs=120,
    throttle_secs=600
)
```

Creates a validated `EvalSpec` instance.

#### Args:

* <b>`input_fn`</b>: Evaluation input function returning a tuple of:
      features - `Tensor` or dictionary of string feature name to `Tensor`.
      labels - `Tensor` or dictionary of `Tensor` with labels.
* <b>`steps`</b>: Int. Positive number of steps for which to evaluate model. If
    `None`, evaluates until `input_fn` raises an end-of-input exception.
    See `Estimator.evaluate` for details.
* <b>`name`</b>: String. Name of the evaluation if user needs to run multiple
    evaluations on different data sets. Metrics for different evaluations
    are saved in separate folders, and appear separately in tensorboard.
* <b>`hooks`</b>: Iterable of `tf.train.SessionRunHook` objects to run
    on all workers (including chief) during training.
* <b>`exporters`</b>: Iterable of `Exporter`s, or a single one, or `None`.
    `exporters` will be invoked after each evaluation.
* <b>`start_delay_secs`</b>: Int. Start evaluating after waiting for this many
    seconds.
* <b>`throttle_secs`</b>: Int. Do not re-evaluate unless the last evaluation was
    started at least this many seconds ago. Of course, evaluation does not
    occur if no new checkpoints are available, hence, this is the minimum.


#### Returns:

A validated `EvalSpec` object.


#### Raises:

* <b>`ValueError`</b>: If any of the input arguments is invalid.
* <b>`TypeError`</b>: If any of the arguments is not of the expected type.



