

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.estimator.TrainSpec

## Class `TrainSpec`





Defined in [`tensorflow/python/estimator/training.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/estimator/training.py).

Configuration for the "train" part for the `train_and_evaluate` call.

`TrainSpec` determines the input data for the training, as well as the
duration. Optional hooks run at various stages of training.

## Properties

<h3 id="hooks"><code>hooks</code></h3>

Alias for field number 2

<h3 id="input_fn"><code>input_fn</code></h3>

Alias for field number 0

<h3 id="max_steps"><code>max_steps</code></h3>

Alias for field number 1



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    input_fn,
    max_steps=None,
    hooks=None
)
```

Creates a validated `TrainSpec` instance.

#### Args:

* <b>`input_fn`</b>: Training input function returning a tuple of:
      features - `Tensor` or dictionary of string feature name to `Tensor`.
      labels - `Tensor` or dictionary of `Tensor` with labels.
* <b>`max_steps`</b>: Int. Positive number of total steps for which to train model.
    If `None`, train forever. The training `input_fn` is not expected to
    generate `OutOfRangeError` or `StopIteration` exceptions. See the
    `train_and_evaluate` stop condition section for details.
* <b>`hooks`</b>: Iterable of `tf.train.SessionRunHook` objects to run
    on all workers (including chief) during training.


#### Returns:

A validated `TrainSpec` object.


#### Raises:

* <b>`ValueError`</b>: If any of the input arguments is invalid.
* <b>`TypeError`</b>: If any of the arguments is not of the expected type.



