page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.call_logit_fn

Calls logit_fn.

``` python
tf.contrib.estimator.call_logit_fn(
    logit_fn,
    features,
    mode,
    params,
    config
)
```



Defined in [`contrib/estimator/python/estimator/logit_fns.py`](https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/contrib/estimator/python/estimator/logit_fns.py).

<!-- Placeholder for "Used in" -->

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