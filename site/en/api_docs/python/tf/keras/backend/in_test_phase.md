page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.in_test_phase


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/in_test_phase">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4185-L4203">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Selects `x` in test phase, and `alt` otherwise.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/in_test_phase"><code>tf.compat.v1.keras.backend.in_test_phase</code></a>
* <a href="/api_docs/python/tf/keras/backend/in_test_phase"><code>tf.compat.v2.keras.backend.in_test_phase</code></a>


``` python
tf.keras.backend.in_test_phase(
    x,
    alt,
    training=None
)
```



<!-- Placeholder for "Used in" -->

Note that `alt` should have the *same shape* as `x`.

#### Arguments:


* <b>`x`</b>: What to return in test phase
    (tensor or callable that returns a tensor).
* <b>`alt`</b>: What to return otherwise
    (tensor or callable that returns a tensor).
* <b>`training`</b>: Optional scalar tensor
    (or Python boolean, or Python integer)
    specifying the learning phase.


#### Returns:

Either `x` or `alt` based on `K.learning_phase`.
