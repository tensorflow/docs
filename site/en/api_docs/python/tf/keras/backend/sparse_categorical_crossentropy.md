page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.sparse_categorical_crossentropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/sparse_categorical_crossentropy">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4376-L4451">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Categorical crossentropy with integer targets.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/sparse_categorical_crossentropy"><code>tf.compat.v1.keras.backend.sparse_categorical_crossentropy</code></a>
* <a href="/api_docs/python/tf/keras/backend/sparse_categorical_crossentropy"><code>tf.compat.v2.keras.backend.sparse_categorical_crossentropy</code></a>


``` python
tf.keras.backend.sparse_categorical_crossentropy(
    target,
    output,
    from_logits=False,
    axis=-1
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`target`</b>: An integer tensor.
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
