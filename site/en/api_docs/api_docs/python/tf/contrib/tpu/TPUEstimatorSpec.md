

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.TPUEstimatorSpec

## Class `TPUEstimatorSpec`





Defined in [`tensorflow/contrib/tpu/python/tpu/tpu_estimator.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/tpu/python/tpu/tpu_estimator.py).

Ops and objects returned from a `model_fn` and passed to `TPUEstimator`.

See `EstimatorSpec` for `mode`, 'predictions, 'loss', 'train_op', and
'export_outputs`.

TPU evaluation expects a slightly different signature from the
${tf.estimator.Estimator}. While `EstimatorSpec.eval_metric_ops` expects a
dict, `TPUEstimatorSpec.eval_metrics` is a tuple of `metric_fn` and `tensors`.
The `tensors` could be a list of `Tensor`s or dict of names to `Tensor`s. The
`tensors` usually specify the model logits, which are transferred back from
TPU system to CPU host. All tensors must have be batch-major, i.e., the batch
size is the first dimension. Once all tensors are available at CPU host from
all shards, they are concatenated (on CPU) and passed as positional arguments
to the `metric_fn` if `tensors` is list or keyword arguments if `tensors` is
dict. `metric_fn` takes the `tensors` and returns a dict from metric string
name to the result of calling a metric function, namely a `(metric_tensor,
update_op)` tuple.

See `TPUEstimator` for MNIST example how to specify the `eval_metrics`.

## Properties

<h3 id="eval_metrics"><code>eval_metrics</code></h3>

Alias for field number 4

<h3 id="export_outputs"><code>export_outputs</code></h3>

Alias for field number 5

<h3 id="loss"><code>loss</code></h3>

Alias for field number 2

<h3 id="mode"><code>mode</code></h3>

Alias for field number 0

<h3 id="predictions"><code>predictions</code></h3>

Alias for field number 1

<h3 id="train_op"><code>train_op</code></h3>

Alias for field number 3



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    mode,
    predictions=None,
    loss=None,
    train_op=None,
    eval_metrics=None,
    export_outputs=None
)
```

Creates a validated `TPUEstimatorSpec` instance.

<h3 id="as_estimator_spec"><code>as_estimator_spec</code></h3>

``` python
as_estimator_spec()
```

Creates an equivalent `EstimatorSpec` used by CPU train/eval.



