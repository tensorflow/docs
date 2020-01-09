page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.model_to_dot


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="/api_docs/python/tf/keras/utils/model_to_dot">
  <img src="https://www.tensorflow.org/images/tf_logo_32px.png" />
  TensorFlow 2 version</a>
</td>

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/keras/utils/vis_utils.py#L68-L249">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Convert a Keras model to dot format.

### Aliases:

* <a href="/api_docs/python/tf/keras/utils/model_to_dot"><code>tf.compat.v1.keras.utils.model_to_dot</code></a>
* <a href="/api_docs/python/tf/keras/utils/model_to_dot"><code>tf.compat.v2.keras.utils.model_to_dot</code></a>


``` python
tf.keras.utils.model_to_dot(
    model,
    show_shapes=False,
    show_layer_names=True,
    rankdir='TB',
    expand_nested=False,
    dpi=96,
    subgraph=False
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`model`</b>: A Keras model instance.
* <b>`show_shapes`</b>: whether to display shape information.
* <b>`show_layer_names`</b>: whether to display layer names.
* <b>`rankdir`</b>: `rankdir` argument passed to PyDot,
    a string specifying the format of the plot:
    'TB' creates a vertical plot;
    'LR' creates a horizontal plot.
* <b>`expand_nested`</b>: whether to expand nested models into clusters.
* <b>`dpi`</b>: Dots per inch.
* <b>`subgraph`</b>: whether to return a `pydot.Cluster` instance.


#### Returns:

A `pydot.Dot` instance representing the Keras model or
a `pydot.Cluster` instance representing nested model if
`subgraph=True`.



#### Raises:


* <b>`ImportError`</b>: if graphviz or pydot are not available.
