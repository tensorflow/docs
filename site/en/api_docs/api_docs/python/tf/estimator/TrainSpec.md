

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.TrainSpec

## Class `TrainSpec`





Defined in [`tensorflow/python/estimator/training.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/python/estimator/training.py).

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

* <b>`input_fn`</b>: A function that provides input data for training as minibatches.
    See <a href="../../../../guide/premade_estimators#create_input_functions">Premade Estimators</a> for more
    information. The function should construct and return one of
    the following:
      * A 'tf.data.Dataset' object: Outputs of `Dataset` object must be a
        tuple (features, labels) with same constraints as below.
      * A tuple (features, labels): Where features is a `Tensor` or a
        dictionary of string feature name to `Tensor` and labels is a
        `Tensor` or a dictionary of string label name to `Tensor`.

* <b>`max_steps`</b>: Int. Positive number of total steps for which to train model.
    If `None`, train forever. The training `input_fn` is not expected to
    generate `OutOfRangeError` or `StopIteration` exceptions. See the
    `train_and_evaluate` stop condition section for details.
* <b>`hooks`</b>: Iterable of <a href="../../tf/train/SessionRunHook"><code>tf.train.SessionRunHook</code></a> objects to run
    on all workers (including chief) during training.


#### Returns:

A validated `TrainSpec` object.


#### Raises:

* <b>`ValueError`</b>: If any of the input arguments is invalid.
* <b>`TypeError`</b>: If any of the arguments is not of the expected type.



