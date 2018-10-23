


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.layers.batch_normalization, gamma_initializer=tf.ones_initializer(), moving_mean_initializer=tf.zeros_initializer(), moving_variance_initializer=tf.ones_initializer(), beta_regularizer=None, gamma_regularizer=None, training=False, trainable=True, name=None, reuse=None)

### `tf.layers.batch_normalization`

```
tf.layers.batch_normalization(inputs, axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer=tf.zeros_initializer(), gamma_initializer=tf.ones_initializer(), moving_mean_initializer=tf.zeros_initializer(), moving_variance_initializer=tf.ones_initializer(), beta_regularizer=None, gamma_regularizer=None, training=False, trainable=True, name=None, reuse=None)
```


Functional interface for the batch normalization layer.

Reference: http://arxiv.org/abs/1502.03167

"Batch Normalization: Accelerating Deep Network Training by Reducing
Internal Covariate Shift"

Sergey Ioffe, Christian Szegedy

#### Arguments:

* <b>`inputs`</b>: Tensor input.
* <b>`axis`</b>: Integer, the axis that should be normalized (typically the features
    axis). For instance, after a `Convolution2D` layer with
    `data_format="channels_first"`, set `axis=1` in `BatchNormalization`.
* <b>`momentum`</b>: Momentum for the moving average.
* <b>`epsilon`</b>: Small float added to variance to avoid dividing by zero.
* <b>`center`</b>: If True, add offset of `beta` to normalized tensor. If False, `beta`
    is ignored.
* <b>`scale`</b>: If True, multiply by `gamma`. If False, `gamma` is
    not used. When the next layer is linear (also e.g. `nn.relu`), this can be
    disabled since the scaling can be done by the next layer.
* <b>`beta_initializer`</b>: Initializer for the beta weight.
* <b>`gamma_initializer`</b>: Initializer for the gamma weight.
* <b>`moving_mean_initializer`</b>: Initializer for the moving mean.
* <b>`moving_variance_initializer`</b>: Initializer for the moving variance.
* <b>`beta_regularizer`</b>: Optional regularizer for the beta weight.
* <b>`gamma_regularizer`</b>: Optional regularizer for the gamma weight.
* <b>`training`</b>: Either a Python boolean, or a TensorFlow boolean scalar tensor
    (e.g. a placeholder). Whether to return the output in training mode
    (normalized with statistics of the current batch) or in inference mode
    (normalized with moving statistics).
* <b>`trainable`</b>: Boolean, if `True` also add variables to the graph collection
    `GraphKeys.TRAINABLE_VARIABLES` (see tf.Variable).
* <b>`name`</b>: String, the name of the layer.
* <b>`reuse`</b>: Boolean, whether to reuse the weights of a previous layer
    by the same name.


#### Returns:

  Output tensor.

Defined in [`tensorflow/python/layers/normalization.py`](https://www.tensorflow.org/code/tensorflow/python/layers/normalization.py).

