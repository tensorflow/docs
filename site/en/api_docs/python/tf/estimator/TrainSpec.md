page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.TrainSpec


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/training.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TrainSpec`

Configuration for the "train" part for the `train_and_evaluate` call.



### Aliases:

* Class `tf.compat.v1.estimator.TrainSpec`
* Class `tf.compat.v2.estimator.TrainSpec`


### Used in the guide:

* [Migrate your TensorFlow 1 code to TensorFlow 2](https://www.tensorflow.org/guide/migrate)

### Used in the tutorials:

* [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)



`TrainSpec` determines the input data for the training, as well as the
duration. Optional hooks run at various stages of training.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/training.py">View source</a>

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
  See [Premade Estimators](
  https://tensorflow.org/guide/premade_estimators#create_input_functions)
  for more information. The function should construct and return one of
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
* <b>`hooks`</b>: Iterable of `tf.train.SessionRunHook` objects to run
  on all workers (including chief) during training.


#### Returns:

A validated `TrainSpec` object.



#### Raises:


* <b>`ValueError`</b>: If any of the input arguments is invalid.
* <b>`TypeError`</b>: If any of the arguments is not of the expected type.



## Properties

<h3 id="input_fn"><code>input_fn</code></h3>




<h3 id="max_steps"><code>max_steps</code></h3>




<h3 id="hooks"><code>hooks</code></h3>
