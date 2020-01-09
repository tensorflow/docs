page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.categorical_crossentropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/categorical_crossentropy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4321-L4373">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Categorical crossentropy between an output tensor and a target tensor.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/categorical_crossentropy"><code>tf.compat.v1.keras.backend.categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/backend/categorical_crossentropy"><code>tf.compat.v2.keras.backend.categorical_crossentropy</code></a>


``` python
tf.keras.backend.categorical_crossentropy(
    target,
    output,
    from_logits=False,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`target`</b>: A tensor of the same shape as `output`.
* <b>`output`</b>: A tensor resulting from a softmax
    (unless `from_logits` is True, in which
    case `output` is expected to be the logits).
* <b>`from_logits`</b>: Boolean, whether `output` is the
    result of a softmax, or is a tensor of logits.
* <b>`axis`</b>: Int specifying the channels axis. `axis=-1` corresponds to data
    format `channels_last', and `axis=1` corresponds to data format
    `channels_first`.


#### Returns:

Output tensor.



#### Raises:


* <b>`ValueError`</b>: if `axis` is neither -1 nor one of the axes of `output`.


#### Example:


```python:
import tensorflow as tf
from tensorflow.keras import backend as K
a = tf.constant([1., 0., 0., 0., 1., 0., 0., 0., 1.], shape=[3,3])
print("a: ", a)
b = tf.constant([.9, .05, .05, .5, .89, .6, .05, .01, .94], shape=[3,3])
print("b: ", b)
loss = K.categorical_crossentropy(a, b)
print('Loss: ', loss) #Loss: tf.Tensor([0.10536055 0.8046684  0.06187541], shape=(3,), dtype=float32)
loss = K.categorical_crossentropy(a, a)
print('Loss: ', loss) #Loss:  tf.Tensor([1.1920929e-07 1.1920929e-07 1.1920929e-07], shape=(3,), dtype=float32)
```
