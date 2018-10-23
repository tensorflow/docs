

page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>


<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.estimator.forward_features

``` python
tf.contrib.estimator.forward_features(
    estimator,
    keys=None
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/extenders.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/estimator/python/estimator/extenders.py).

Forward features to predictions dictionary.

In some cases, user wants to see some of the features in estimators prediction
output. As an example, consider a batch prediction service: The service simply
runs inference on the users graph and returns the results. Keys are essential
because there is no order guarantee on the outputs so they need to be rejoined
to the inputs via keys or transclusion of the inputs in the outputs.

Example:

```python
  def input_fn():
    features, labels = ...
    features['unique_example_id'] = ...
    features, labels

  estimator = tf.estimator.LinearClassifier(...)
  estimator = tf.contrib.estimator.forward_features(
      estimator, 'unique_example_id')
  estimator.train(...)
  assert 'unique_example_id' in estimator.predict(...)
```

#### Args:

* <b>`estimator`</b>: A <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> object.
* <b>`keys`</b>: a `string` or a `list` of `string`. If it is `None`, all of the
    `features` in `dict` is forwarded to the `predictions`. If it is a
    `string`, only given key is forwarded. If it is a `list` of strings, all
    the given `keys` are forwarded.


#### Returns:

A new <a href="../../../tf/estimator/Estimator"><code>tf.estimator.Estimator</code></a> which forwards features to predictions.


#### Raises:

* <b>`ValueError`</b>:     * if `keys` is already part of `predictions`. We don't allow
      override.
    * if 'keys' does not exist in `features`.
    * if feature key refers to a `SparseTensor`, since we don't support
      `SparseTensor` in `predictions`. `SparseTensor` is common in `features`.
* <b>`TypeError`</b>: if `keys` type is not one of `string` or list/tuple of `string`.