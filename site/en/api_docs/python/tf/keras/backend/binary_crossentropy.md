page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.binary_crossentropy


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/backend.py#L4558-L4588">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Binary crossentropy between an output tensor and a target tensor.

### Aliases:

* `tf.compat.v1.keras.backend.binary_crossentropy`
* `tf.compat.v2.keras.backend.binary_crossentropy`


``` python
tf.keras.backend.binary_crossentropy(
    target,
    output,
    from_logits=False
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`target`</b>: A tensor with the same shape as `output`.
* <b>`output`</b>: A tensor.
* <b>`from_logits`</b>: Whether `output` is expected to be a logits tensor.
    By default, we consider that `output`
    encodes a probability distribution.


#### Returns:

A tensor.
