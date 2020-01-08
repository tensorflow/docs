page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.predictor.from_contrib_estimator

``` python
tf.contrib.predictor.from_contrib_estimator(
    estimator,
    prediction_input_fn,
    input_alternative_key=None,
    output_alternative_key=None,
    graph=None,
    config=None
)
```



Defined in [`tensorflow/contrib/predictor/predictor_factories.py`](https://github.com/tensorflow/tensorflow/blob/r1.12/tensorflow/contrib/predictor/predictor_factories.py).

Constructs a `Predictor` from a <a href="../../../tf/contrib/learn/Estimator"><code>tf.contrib.learn.Estimator</code></a>.

#### Args:

* <b>`estimator`</b>: an instance of <a href="../../../tf/contrib/learn/Estimator"><code>tf.contrib.learn.Estimator</code></a>.
* <b>`prediction_input_fn`</b>: a function that takes no arguments and returns an
    instance of `InputFnOps`.
* <b>`input_alternative_key`</b>: Optional. Specify the input alternative used for
    prediction.
* <b>`output_alternative_key`</b>: Specify the output alternative used for
    prediction. Not needed for single-headed models but required for
    multi-headed models.
* <b>`graph`</b>: Optional. The Tensorflow `graph` in which prediction should be
    done.
* <b>`config`</b>: `ConfigProto` proto used to configure the session.


#### Returns:

An initialized `Predictor`.


#### Raises:

* <b>`TypeError`</b>: if `estimator` is a core `Estimator` instead of a contrib
    `Estimator`.