

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.call_logit_fn

``` python
call_logit_fn(
    logit_fn,
    features,
    mode,
    params,
    config
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/logit_fns.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.5/tensorflow/contrib/estimator/python/estimator/logit_fns.py).

Calls logit_fn.

A utility function that calls the provided logit_fn with the relevant subset
of provided arguments.  Similar to tf.estimator._call_model_fn().

#### Args:

* <b>`logit_fn`</b>: A logit_fn as defined above.
* <b>`features`</b>: The features dict.
* <b>`mode`</b>: TRAIN / EVAL / PREDICT ModeKeys.
* <b>`params`</b>: The hyperparameter dict.
* <b>`config`</b>: The configuration object.


#### Returns:

A logit Tensor, the output of logit_fn.


#### Raises:

* <b>`ValueError`</b>: if logit_fn does not return a Tensor or a dictionary mapping
    strings to Tensors.