page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.sparse_categorical_crossentropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L4480-L4555">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Categorical crossentropy with integer targets.

### Aliases:

* `tf.compat.v1.keras.backend.sparse_categorical_crossentropy`
* `tf.compat.v2.keras.backend.sparse_categorical_crossentropy`


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
