page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.keras_to_tpu_model

``` python
tf.contrib.tpu.keras_to_tpu_model(
    *args,
    **kwargs
)
```



Defined in [`tensorflow/contrib/framework/python/framework/experimental.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/contrib/framework/python/framework/experimental.py).

Copy `model` along with weights to the TPU. (experimental)

Warning: THIS FUNCTION IS EXPERIMENTAL. It may change or be removed at any time, and without warning.

Returns a TPU model.

Usage:

```
a = Input(shape=(32,))
b = Dense(32)(a)
model = Model(inputs=a, outputs=b)

# If `num_cores_per_host` is greater than one, batch parallelism will be used
# to run on multiple TPU cores.
strategy = keras_support.TPUDistributionStrategy(tpu_cluster_resolver)
model = keras_support.tpu_model(model, strategy)
model.compile(
    optimizer=tf.train.GradientDescentOptimizer(learning_rate=1.0),
    ...)
```

#### Args:

* <b>`model`</b>: A <a href="../../../tf/keras/models/Model"><code>tf.keras.Model</code></a> instance.
* <b>`strategy`</b>: `TPUDistributionStrategy`.  The strategy to use for replicating
    model across multiple TPU cores.


#### Returns:

A new `KerasTPUModel` instance.