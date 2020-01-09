page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.utils.plot_model


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/keras/utils/vis_utils.py#L252-L300">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



Converts a Keras model to dot format and save to a file.

### Aliases:

* `tf.compat.v1.keras.utils.plot_model`
* `tf.compat.v2.keras.utils.plot_model`


``` python
tf.keras.utils.plot_model(
    model,
    to_file='model.png',
    show_shapes=False,
    show_layer_names=True,
    rankdir='TB',
    expand_nested=False,
    dpi=96
)
```



### Used in the guide:

* [The Keras functional API in TensorFlow](https://www.tensorflow.org/guide/keras/functional)
* [Train and evaluate with Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate)




#### Arguments:


* <b>`model`</b>: A Keras model instance
* <b>`to_file`</b>: File name of the plot image.
* <b>`show_shapes`</b>: whether to display shape information.
* <b>`show_layer_names`</b>: whether to display layer names.
* <b>`rankdir`</b>: `rankdir` argument passed to PyDot,
    a string specifying the format of the plot:
    'TB' creates a vertical plot;
    'LR' creates a horizontal plot.
* <b>`expand_nested`</b>: Whether to expand nested models into clusters.
* <b>`dpi`</b>: Dots per inch.


#### Returns:

A Jupyter notebook Image object if Jupyter is installed.
This enables in-line display of the model plots in notebooks.
