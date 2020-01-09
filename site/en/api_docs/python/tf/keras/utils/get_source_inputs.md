page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.get_source_inputs


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/get_source_inputs">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/layer_utils.py#L31-L67">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Returns the list of input tensors necessary to compute `tensor`.

### Aliases:

* <a href="/api_docs/python/tf/keras/utils/get_source_inputs"><code>tf.compat.v1.keras.utils.get_source_inputs</code></a>
* <a href="/api_docs/python/tf/keras/utils/get_source_inputs"><code>tf.compat.v2.keras.utils.get_source_inputs</code></a>


``` python
tf.keras.utils.get_source_inputs(
    tensor,
    layer=None,
    node_index=None
)
```



<!-- Placeholder for "Used in" -->

Output will always be a list of tensors
(potentially with 1 element).

#### Arguments:


* <b>`tensor`</b>: The tensor to start from.
* <b>`layer`</b>: Origin layer of the tensor. Will be
    determined via tensor._keras_history if not provided.
* <b>`node_index`</b>: Origin node index of the tensor.


#### Returns:

List of input tensors.
