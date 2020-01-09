page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.backend.switch


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/backend/switch">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/backend.py#L4080-L4141">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Switches between two operations depending on a scalar value.

### Aliases:

* <a href="/api_docs/python/tf/keras/backend/switch"><code>tf.compat.v1.keras.backend.switch</code></a>
* <a href="/api_docs/python/tf/keras/backend/switch"><code>tf.compat.v2.keras.backend.switch</code></a>


``` python
tf.keras.backend.switch(
    condition,
    then_expression,
    else_expression
)
```



<!-- Placeholder for "Used in" -->

Note that both `then_expression` and `else_expression`
should be symbolic tensors of the *same shape*.

#### Arguments:


* <b>`condition`</b>: tensor (`int` or `bool`).
* <b>`then_expression`</b>: either a tensor, or a callable that returns a tensor.
* <b>`else_expression`</b>: either a tensor, or a callable that returns a tensor.


#### Returns:

The selected tensor.



#### Raises:


* <b>`ValueError`</b>: If rank of `condition` is greater than rank of expressions.
