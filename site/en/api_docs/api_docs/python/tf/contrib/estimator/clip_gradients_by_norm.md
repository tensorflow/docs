

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.estimator.clip_gradients_by_norm

``` python
clip_gradients_by_norm(
    optimizer,
    clip_norm
)
```



Defined in [`tensorflow/contrib/estimator/python/estimator/extenders.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/estimator/python/estimator/extenders.py).

Returns an optimizer which clips gradients before appliying them.

Example:

```python
optimizer = tf.train.ProximalAdagradOptimizer(
    learning_rate=0.1,
    l1_regularization_strength=0.001)
optimizer = tf.contrib.estimator.clip_gradients_by_norm(
    optimizer, clip_norm)
estimator = tf.estimator.DNNClassifier(
    feature_columns=[...],
    hidden_units=[1024, 512, 256],
    optimizer=optimizer)
```

#### Args:

* <b>`optimizer`</b>: An `tf.Optimizer` object to apply gradients.
* <b>`clip_norm`</b>: A 0-D (scalar) `Tensor` > 0. The clipping ratio.


#### Returns:

A `tf.Optimizer`.